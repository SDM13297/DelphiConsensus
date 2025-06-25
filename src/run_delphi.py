import json
from src.simulate_experts import run_simulation_round, personas, problem_statement

# --- Round 1 ---
print("\n🔁 Running Round 1")
round1_responses = run_simulation_round(personas, problem_statement)
with open("data/round1.json", "w") as f:
    json.dump(round1_responses, f, indent=4)

# --- Summary ---
def summarize_responses(responses):
    # Placeholder: just return a static summary for now
    return "Most experts agree on solar, battery storage, and smart grid tech. Some mention offshore wind and green hydrogen."

print("\n🧠 Summarizing Round 1 responses")
summary1 = summarize_responses(round1_responses)
with open("data/summary1.txt", "w") as f:
    f.write(summary1)

# --- Round 2 (experts revise after seeing summary) ---
def run_round2_with_context(personas, question, context):
    revised_responses = []
    for persona in personas:
        # Simulated context injection (can be replaced by real prompt tuning)
        response = f"Considering the group summary: '{context}', as a {persona['name']}, I now believe key investments should also include green hydrogen and offshore wind."
        revised_responses.append({
            "persona": persona['name'],
            "response": response
        })
    return revised_responses

print("\n🔁 Running Round 2 (with context from summary)")
round2_responses = run_round2_with_context(personas, problem_statement, summary1)
with open("data/round2.json", "w") as f:
    json.dump(round2_responses, f, indent=4)

print("\n✅ Delphi simulation complete. Responses saved in 'data/' folder.")
