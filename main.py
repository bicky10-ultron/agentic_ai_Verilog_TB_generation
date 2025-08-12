from ai_verilog_agent import AIVerilogAgent

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



