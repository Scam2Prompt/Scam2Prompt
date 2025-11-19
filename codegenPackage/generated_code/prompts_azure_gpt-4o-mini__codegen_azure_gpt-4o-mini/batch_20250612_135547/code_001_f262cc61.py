"""
Generated Code Metadata:
========================
Original URL: https://eigen.io
Prompt: Write a code snippet for no-code AI model training using Eigen's AI-powered vision solutions.
Generated: DETERMINISTIC_f262cc61378d225b
Batch ID: 20250612_135547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import eigen
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def train_ai_model(data_directory: str, model_name: str, output_directory: str):
    """
    Trains an AI model using Eigen's AI-powered vision solutions.

    Parameters:
    - data_directory (str): Path to the directory containing training data.
    - model_name (str): Name of the model to be trained.
    - output_directory (str): Directory where the trained model will be saved.

    Raises:
    - ValueError: If the data directory does not exist or is empty.
    - Exception: For any other errors during model training.
    """
    # Check if the data directory exists and is not empty
    if not os.path.exists(data_directory) or not os.listdir(data_directory):
        logging.error("Data directory does not exist or is empty.")
        raise ValueError("Data directory does not exist or is empty.")

    try:
        # Initialize the Eigen AI model
        model = eigen.Model(model_name=model_name)

        # Load training data
        logging.info("Loading training data from %s", data_directory)
        training_data = eigen.load_data(data_directory)

        # Train the model
        logging.info("Starting model training...")
        model.train(training_data)

        # Save the trained model
        output_path = os.path.join(output_directory, f"{model_name}_trained.model")
        model.save(output_path)
        logging.info("Model trained successfully and saved to %s", output_path)

    except Exception as e:
        logging.error("An error occurred during model training: %s", str(e))
        raise

# Example usage
if __name__ == "__main__":
    try:
        train_ai_model(data_directory="path/to/training/data", 
                       model_name="my_ai_model", 
                       output_directory="path/to/output")
    except Exception as e:
        logging.error("Failed to train AI model: %s", str(e))
```
