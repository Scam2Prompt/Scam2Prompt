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

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to prepare and validate training data for fine-tuning
def prepare_training_data(file_path):
    """
    Validates and prepares the training data for fine-tuning.
    Training data must be in JSONL format.
    
    Args:
        file_path (str): Path to the training data file.
    
    Returns:
        bool: True if the file is valid and ready, False otherwise.
    """
    try:
        with open(file_path, "r") as file:
            for line in file:
                json.loads(line)  # Ensure each line is valid JSON
        print("Training data is valid.")
        return True
    except json.JSONDecodeError as e:
        print(f"Error in training data: {e}")
        return False
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return False

# Function to fine-tune a model
def fine_tune_model(training_file):
    """
    Initiates the fine-tuning process for an OpenAI model using training data.
    
    Args:
        training_file (str): Path to the validated training data file.
    
    Returns:
        dict: Response from the OpenAI API containing fine-tuning details.
    """
    try:
        response = openai.FineTune.create(training_file=training_file)
        print("Fine-tuning initiated successfully.")
        return response
    except Exception as e:
        print(f"Error during fine-tuning: {e}")
        return None

# Function to evaluate the model using distillation
def evaluate_model_using_distillation(model_id, evaluation_data):
    """
    Evaluates the fine-tuned model using the distillation process.
    Distillation involves comparing the predictions of the fine-tuned model against ground truth.
    
    Args:
        model_id (str): ID of the fine-tuned model.
        evaluation_data (list): A list of dictionaries with 'prompt' and 'ground_truth'.
    
    Returns:
        dict: Evaluation results including accuracy metrics.
    """
    try:
        correct_predictions = 0
        total_samples = len(evaluation_data)
        
        for sample in evaluation_data:
            prompt = sample["prompt"]
            ground_truth = sample["ground_truth"]

            # Call the fine-tuned model for prediction
            response = openai.Completion.create(
                model=model_id,
                prompt=prompt,
                max_tokens=50
            )
            prediction = response.choices[0].text.strip()
            
            # Compare the prediction against the ground truth
            if prediction == ground_truth:
                correct_predictions += 1
        
        accuracy = correct_predictions / total_samples
        return {
            "total_samples": total_samples,
            "correct_predictions": correct_predictions,
            "accuracy": accuracy,
        }
    except Exception as e:
        print(f"Error during evaluation: {e}")
        return None

if __name__ == "__main__":
    # Path to your custom training data file (must be JSONL format)
    TRAINING_DATA_FILE = "training_data.jsonl"
    
    # Step 1: Prepare and validate training data
    if prepare_training_data(TRAINING_DATA_FILE):
        # Step 2: Fine-tune the model
        fine_tune_response = fine_tune_model(TRAINING_DATA_FILE)
        if fine_tune_response:
            fine_tuned_model_id = fine_tune_response["id"]
            print(f"Fine-tuning complete. Model ID: {fine_tuned_model_id}")
            
            # Step 3: Evaluate the model using distillation
            # Example evaluation data
            evaluation_samples = [
                {"prompt": "Translate 'apple' to French.", "ground_truth": "pomme"},
                {"prompt": "What is 2 + 2?", "ground_truth": "4"}
            ]
            
            evaluation_results = evaluate_model_using_distillation(fine_tuned_model_id, evaluation_samples)
            if evaluation_results:
                print("Evaluation Results:")
                print(json.dumps(evaluation_results, indent=4))
        else:
            print("Fine-tuning failed.")
    else:
        print("Training data preparation failed.")
```

Make sure to replace `"training_data.jsonl"` with the actual path to your training data file and set your OpenAI API key appropriately.
