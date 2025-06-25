import json
from pathlib import Path
from src.llm_interface import LLMInterface
import yaml

# --- Load config ---
def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

CONFIG = load_config()

# --- Expert personas (can be moved to JSON later) ---
personas = [
    {
        "name": "Energy Economist",
        "description": "An expert in global energy policy and markets with 20 years of experience."
    },
    {
        "name": "Climate Scientist",
        "description": "A senior climate researcher specializing in renewable technologies and climate modeling."
    }
]

# --- Sample problem statement ---
problem_statement = "What are the most critical technologies to invest in for renewable energy in the next 5 years?"

# --- Initialize LLM ---
llm = LLMInterface()

# --- Simulate LLM response ---
def simulate_response(persona, question):
    prompt = f"You are {persona['name']}, {persona['description']}\nQuestion: {question}\nAnswer:"
    return llm.query(prompt)

# --- Run simulation for each persona ---
def run_simulation_round(personas, question):
    responses = []
    for persona in personas:
        response = simulate_response(persona, question)
        responses.append({
            "persona": persona['name'],
            "response": response
        })
    return responses

# --- Save responses ---
def save_responses_to_json(responses, filename="data/round1.json"):
    Path("data").mkdir(parents=True, exist_ok=True)
    with open(filename, "w") as f:
        json.dump(responses, f, indent=4)

# --- Main execution ---
if __name__ == "__main__":
    responses = run_simulation_round(personas, problem_statement)
    save_responses_to_json(responses)
    print("Round 1 expert responses saved to data/round1.json")
