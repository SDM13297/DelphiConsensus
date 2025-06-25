# DelphiConsensus 🧠  
**Simulating Expert Feedback Loops Using LLMs**

DelphiConsensus is an open-source project that simulates the Delphi Method using Large Language Models (LLMs). It orchestrates multi-round expert feedback from multiple simulated SMEs (Subject Matter Experts), enabling consensus-building through AI. Originally designed for adaptive learning and decision support, the system supports plug-and-play LLMs, customizable personas, and a modular pipeline.

---

## 🔍 Core Idea

> *“What if you could ask a panel of experts — from psychology, policy, economics, or tech — and watch them evolve their opinions through structured dialogue?”*

This project builds exactly that. DelphiConsensus enables:

- SME simulation across multiple subjects
- Multi-round opinion generation and summarization
- Consensus exploration through disagreement and revision
- Optional document-grounded reasoning via RAG (planned)

---

## 🧱 Project Structure

```bash
DelphiConsensus/
├── src/
│   ├── llm_interface.py        # Connects to LLM backend (HuggingFace / OpenAI)
│   ├── simulate_experts.py     # Simulates expert responses for a round
│   ├── summarize_round.py      # Generates a summary from round responses
│   ├── run_delphi.py           # Orchestrates the Delphi simulation process
│   └── os_utils.py             # [Placeholder] OS/file system utilities (TBD)
├── data/
│   ├── round1.json             # Responses from first round
│   ├── summary1.txt            # LLM-generated summary
│   ├── round2.json             # Responses post-summary
├── config/
│   ├── config.yaml             # LLM + runtime configuration
│   └── personas.json           # Defines SME persona behaviors and styles
├── notebooks/
│   └── prompt_experiments.ipynb # Exploratory prompt tuning and testing
├── requirements.txt            # Python dependencies
└── README.md                   # You're here

---

## 🧠 How It Works

1. **User provides**:  
   - A question  
   - One or more subjects  
   - (Optional) Knowledge base files for RAG use

2. **System generates SMEs**  
   - Each SME tied to a subject  
   - Prompted via persona and configuration settings

3. **Simulation Loop**  
   - **Round 1**: SMEs provide initial responses  
   - **Summarization**: LLM generates cross-expert synthesis  
   - **Round 2**: SMEs revise opinions based on the summary  
   - Repeatable if desired

4. **Outputs**  
   - Individual responses  
   - Summary  
   - Delta/consensus visualization (planned)