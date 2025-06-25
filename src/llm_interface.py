from transformers import pipeline
from typing import Literal
import yaml

# --- Load config from config.yaml ---
def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

CONFIG = load_config()

# --- Simple wrapper around HuggingFace LLMs ---
class HuggingFaceLLM:
    def __init__(self, model_name: str, max_tokens: int, temperature: float):
        print(f"🔧 Loading HuggingFace model: {model_name}")
        self.generator = pipeline("text-generation", model=model_name, device_map="auto")
        self.max_tokens = max_tokens
        self.temperature = temperature

    def generate_response(self, prompt: str, max_tokens: int = None, temperature: float = None):
        outputs = self.generator(
            prompt,
            max_new_tokens=max_tokens or self.max_tokens,
            do_sample=True,
            temperature=temperature or self.temperature,
            pad_token_id=self.generator.tokenizer.eos_token_id
        )
        return outputs[0]['generated_text']

# --- Unified interface (expandable to support other backends later) ---
class LLMInterface:
    def __init__(self, backend: Literal['huggingface'] = None, model_name: str = None):
        backend = backend or CONFIG['llm_backend']
        self.backend_name = backend

        if backend == 'huggingface':
            hf_cfg = CONFIG['huggingface']
            self.backend = HuggingFaceLLM(
                model_name=model_name or hf_cfg['model_name'],
                max_tokens=hf_cfg.get('max_tokens', 256),
                temperature=hf_cfg.get('temperature', 0.7)
            )
        else:
            raise NotImplementedError(f"Backend '{backend}' is not implemented yet.")

    def query(self, prompt: str, **kwargs) -> str:
        return self.backend.generate_response(prompt, **kwargs)

# --- Sample usage ---
if __name__ == "__main__":
    llm = LLMInterface()
    prompt = "You are a climate scientist. What are the three most impactful renewable technologies for the next decade?"
    print(llm.query(prompt))
