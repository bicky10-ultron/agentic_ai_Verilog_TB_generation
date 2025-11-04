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
🧠 Features

AI-driven generation of Verilog/SystemVerilog modules

Automatic creation of simple testbenches (stimulus + basic checks)

CLI entrypoint to request a design and output generated files

Modular codebase for integrating different LLM backends or prompt templates

🛠️ Requirements

Python 3.8+

An LLM API or local model endpoint compatible with the project's prompt format (set environment variables or modify ai_verilog_agent.py to configure)

Optional: Icarus Verilog and GTKWave for local simulation and waveform viewing
