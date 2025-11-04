# Agentic AI for Verilog & Testbench Generation

## 🚀 Project Overview
**Agentic AI for Verilog & Testbench Generation** is an automation tool that leverages an AI agent to generate SystemVerilog modules and corresponding testbenches. The agent is designed to accelerate verification workflows by producing synthesizable Verilog (or SystemVerilog) code, generating testbenches with stimulus, and helping automate simulation runs. This project is ideal for hardware designers and verification engineers who want to prototype RTL quickly or bootstrap verification environments.

---

## 📁 Repository Structure

```yaml
agentic_ai_Verilog_TB_generation/
├── ai_verilog_agent.py     # Core agent implementation: prompts, code generation, scaffolding
├── main.py                 # Example CLI / entrypoint to call the agent and generate files
└── README.md               # This file
```
## 🧠 Features
```yaml
-AI-driven generation of Verilog/SystemVerilog modules
-Automatic creation of simple testbenches (stimulus + basic checks)
-CLI entrypoint to request a design and output generated files
-Modular codebase for integrating different LLM backends or prompt templates
```
## 🛠️ Requirements
```yaml
-Python 3.8+
-An LLM API or local model endpoint compatible with the project's prompt format (set environment variables or modify ai_verilog_agent.py to configure)
Optional: Icarus Verilog and GTKWave for local simulation and waveform viewing
```
## ⚙️ How to Use (Example)
```yaml
-Install Python dependencies (if any). Example:
   pip install -r requirements.txt
(If your project does not have a requirements.txt, install the libraries your environment uses for LLM calls — e.g., openai, requests, or the client for your local model.)
Configure your LLM credentials or endpoint inside ai_verilog_agent.py or via environment variables (follow comments in the file).

-Run the agent (example CLI):
   python main.py

The script will prompt for a design description and output generated Verilog/SystemVerilog files and a testbench in the working directory.

-(Optional) Simulate the generated files using Icarus Verilog:

iverilog -o simv generated_module.sv generated_tb.sv
vvp simv
gtkwave dump.vcd
```

## 🔧 Implementation Notes

The project contains a simple agent implementation (ai_verilog_agent.py) that constructs prompts, calls a model endpoint, and writes returned code to disk. It is intentionally modular so you can plug in a different model client or add prompt engineering improvements.
Generated testbenches include basic stimulus and checks. For production-grade verification, expand the template to include assertions, functional coverage, constrained-random stimulus, or UVM environments.
Always review generated RTL and testbench code manually before synthesis or integration.
