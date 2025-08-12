import os
import subprocess
from langchain_community.chat_models import ChatOllama
from langchain.schema import HumanMessage
from langchain_core.output_parsers import BaseOutputParser


class CodeOutputParser(BaseOutputParser):
    """Extract clean code from LLM output supporting multiple delimiters."""
    def parse(self, text: str) -> str:
        delimiters = ["```", "***", "~~~"]
        for delim in delimiters:
            if delim in text:
                parts = text.split(delim)
                for p in parts:
                    if "module" in p and "endmodule" in p:
                        return p.strip()
        # fallback: return the whole text if no delimiters found
        return text.strip()


class AIVerilogAgent:
    def __init__(self, model_name="llama3"):
        self.llm = ChatOllama(model=model_name)
        self.parser = CodeOutputParser()
        self.output_dir = "generated_verilog"
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_module(self, spec: str):
        """Generate synthesizable Verilog code for a given specification."""
        prompt = (
    f"Write synthesizable Verilog code for: {spec}.\n"
    "Your output must be a complete Verilog module with a meaningful module name.\n"
    "Declare all inputs and outputs properly using 'input wire' and 'output wire' as needed.\n"
    "If outputs are driven by continuous assignment, declare them as 'output wire'.\n"
    "If outputs require registers, declare them as 'output reg' and drive inside always blocks.\n"
    "Do NOT include testbench code, comments, or explanations—only the Verilog module code.\n"
    "Output ONLY the Verilog code without any markdown, backticks, or language tags."
)
        
        raw_output = self.llm.invoke([HumanMessage(content=prompt)]).content
        verilog_code = self.parser.parse(raw_output)

        verilog_path = os.path.join(self.output_dir, "module_under_test.v")
        with open(verilog_path, "w") as f:
            f.write(verilog_code)

        print(f"✅ Verilog module saved to {verilog_path}")
        return verilog_code, verilog_path

    def generate_testbench(self, verilog_code: str):
        """Generate a complete Verilog testbench for the given module."""
        prompt = (
        "Write a complete runnable Verilog testbench for the following module.\n"
        "The testbench must:\n"
        "- Declare inputs as reg and outputs as wire\n"
        "- Instantiate the module\n"
        "- Apply a variety of test vectors\n"
        "- Use $display to show inputs and outputs\n"
        "- Include $dumpfile(\"dump.vcd\") and $dumpvars(0, <testbench_module_name>) for waveform dumping\n"
        "- End with $finish\n\n"
        "Here is the module code:\n"
        f"{verilog_code}\n\n"
        "Output ONLY the testbench code without any markdown formatting, triple backticks, or language tags.")
        raw_output = self.llm.invoke([HumanMessage(content=prompt)]).content
        tb_code = self.parser.parse(raw_output).strip()
        tb_code = tb_code.replace("`", "")
        if not tb_code.startswith("timescale"):
            tb_code = "`timescale 1ns/1ps\n" + tb_code
        else:
            tb_code = "`" + tb_code  
        tb_path = os.path.join(self.output_dir, "tb.v")
        with open(tb_path, "w") as f:
            f.write(tb_code)
        print(f"✅ Testbench saved to {tb_path}")
        return tb_code, tb_path
    
    def run_simulation(self, verilog_path: str, tb_path: str):
        """Compile and simulate the generated Verilog module and testbench."""
        print("🔄 Compiling Verilog code...")
        compile_result = subprocess.run(
            ["iverilog", "-o", "sim.out", verilog_path, tb_path],
            capture_output=True, text=True
        )

        if compile_result.returncode != 0:
            print("❌ Compilation failed:")
            print(compile_result.stderr)
            return

        print("▶️ Running simulation...")
        run_result = subprocess.run(["vvp", "sim.out"], capture_output=True, text=True)

        print("📜 Simulation Output:")
        print(run_result.stdout)


if __name__ == "__main__":
    print("💡 Welcome to the VLSI Verilog Agent!")
    print("I can turn your plain English hardware ideas into Verilog modules + testbenches and run them.")
    print("-" * 60)

    agent = AIVerilogAgent()
    spec = input("🛠 Enter Verilog module specification: ")

    verilog_code, verilog_path = agent.generate_module(spec)
    tb_code, tb_path = agent.generate_testbench(verilog_code)

    choice = input("▶️ Do you want to compile & simulate now? (y/n): ").strip().lower()
    if choice == "y":
        agent.run_simulation(verilog_path, tb_path)
