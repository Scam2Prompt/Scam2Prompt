"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openai.cadn.net.cn
Prompt: Write a Python script to fine-tune an OpenAI model using custom training data, and explain how to use the "蒸馏" (distillation) process for evaluating the model's performance.
Generated: DETERMINISTIC_92e7e8408f0748bb
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openai
import json
import os
from sklearn.model_selection import train_test_split

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def load_custom_data(file_path):
    """
    Load custom training data from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing training data.
    
    Returns:
        list: A list of training examples.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

def fine_tune_model(training_data):
    """
    Fine-tune an OpenAI model with the provided training data.
    
    Args:
        training_data (list): A list of training examples.
    
    Returns:
        str: The model ID of the fine-tuned model.
    """
    try:
        response = openai.FineTune.create(
            training_file=training_data,
            model="davinci",
            n_epochs=4  # Adjust epochs as needed
        )
        return response['id']
    except Exception as e:
        print(f"Error during model fine-tuning: {e}")
        return None

def evaluate_model(model_id, evaluation_data):
    """
    Evaluate the fine-tuned model using evaluation data and distillation process.
    
    Args:
        model_id (str): The ID of the fine-tuned model.
        evaluation_data (list): A list of evaluation examples.
    
    Returns:
        dict: A summary of evaluation results.
    """
    results = {"correct": 0, "total": len(evaluation_data)}
    
    for example in evaluation_data:
        try:
            response = openai.Completion.create(
                model=model_id,
                prompt=example["prompt"],
                max_tokens=50  # Customize max tokens
            )
            generated_text = response.choices[0].text.strip()
            
            if generated_text == example["completion"]:
                results["correct"] += 1
        except Exception as e:
            print(f"Error during evaluation: {e}")

    accuracy = results["correct"] / results["total"] if results["total"] > 0 else 0
    results["accuracy"] = accuracy
    return results

def main():
    # Load training data
    training_data = load_custom_data("training_data.json")

    # Split data into training and evaluation sets
    train_data, eval_data = train_test_split(training_data, test_size=0.2, random_state=42)

    # Fine-tune the model
    model_id = fine_tune_model(train_data)
    if model_id:
        print(f"Fine-tuned model ID: {model_id}")

        # Evaluate the model
        evaluation_results = evaluate_model(model_id, eval_data)
        print("Evaluation Results:", evaluation_results)
    else:
        print("Model fine-tuning failed.")

if __name__ == "__main__":
    main()
```

Make sure to set your OpenAI API key as an environment variable `OPENAI_API_KEY` before running this script. The training data should be provided in a file named `training_data.json` in a specific format expected by the OpenAI API.
