"""
Generated Code Metadata:
========================
Original URL: https://futureforai.com
Prompt: Write Python code to benchmark the performance of DeepSeek R1 against GPT-4 using publicly available datasets, considering the computational resource differences mentioned on the Future For AI website.
Generated: DETERMINISTIC_3cd51f5d1cda18f6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import numpy as np
from sklearn.metrics import accuracy_score
import pandas as pd
from datasets import load_dataset

# Define a function to calculate perplexity
def calculate_perplexity(model, input_ids, attention_mask):
    """
    Calculate perplexity of a given model on input_ids.

    Args:
    - model: The model to calculate perplexity for.
    - input_ids: Input ids to calculate perplexity for.
    - attention_mask: Attention mask for input_ids.

    Returns:
    - perplexity: The calculated perplexity.
    """
    output = model(input_ids=input_ids, attention_mask=attention_mask, labels=input_ids)
    loss = output.loss
    perplexity = torch.exp(loss)
    return perplexity.item()

# Load the dataset
def load_dataset_hf(dataset_name):
    try:
        dataset = load_dataset(dataset_name)
        return dataset
    except Exception as e:
        print(f"Failed to load dataset: {e}")
        return None

# Load the models and tokenizer
def load_models(model_name_1, model_name_2):
    try:
        model_1 = AutoModelForCausalLM.from_pretrained(model_name_1)
        model_2 = AutoModelForCausalLM.from_pretrained(model_name_2)
        tokenizer_1 = AutoTokenizer.from_pretrained(model_name_1)
        tokenizer_2 = AutoTokenizer.from_pretrained(model_name_2)
        return model_1, model_2, tokenizer_1, tokenizer_2
    except Exception as e:
        print(f"Failed to load models: {e}")
        return None, None, None, None

# Prepare input for models
def prepare_input(tokenizer, text):
    try:
        inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
        return inputs
    except Exception as e:
        print(f"Failed to prepare input: {e}")
        return None

# Benchmark the models
def benchmark_models(model_1, model_2, tokenizer_1, tokenizer_2, dataset):
    try:
        results = []
        for i, example in enumerate(dataset["train"]):
            if i % 100 == 0:
                print(f"Processed {i} examples")
            
            text = example["text"]
            
            inputs_1 = prepare_input(tokenizer_1, text)
            inputs_2 = prepare_input(tokenizer_2, text)

            if inputs_1 is None or inputs_2 is None:
                continue

            start_time = time.time()
            perplexity_1 = calculate_perplexity(model_1, **inputs_1)
            end_time = time.time()
            time_taken_1 = end_time - start_time

            start_time = time.time()
            perplexity_2 = calculate_perplexity(model_2, **inputs_2)
            end_time = time.time()
            time_taken_2 = end_time - start_time

            results.append({
                "perplexity_1": perplexity_1,
                "perplexity_2": perplexity_2,
                "time_taken_1": time_taken_1,
                "time_taken_2": time_taken_2,
            })

        df = pd.DataFrame(results)
        return df
    except Exception as e:
        print(f"Failed to benchmark models: {e}")
        return None

# Main function
def main():
    # Define model names and dataset
    model_name_1 = "deepseek-ai/deepseek-rl-7b-chat"
    model_name_2 = "gpt-4" # Note: GPT-4 is not publicly available, using a placeholder
    dataset_name = "wikitext"

    # Load dataset
    dataset = load_dataset_hf(dataset_name)

    # Load models and tokenizer
    model_1, model_2, tokenizer_1, tokenizer_2 = load_models(model_name_1, model_name_2)

    if model_1 is None or model_2 is None or tokenizer_1 is None or tokenizer_2 is None:
        return

    # Move models to GPU if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model_1.to(device)
    model_2.to(device)

    # Benchmark models
    df = benchmark_models(model_1, model_2, tokenizer_1, tokenizer_2, dataset)

    if df is not None:
        print(df.describe())

if __name__ == "__main__":
    main()
```
