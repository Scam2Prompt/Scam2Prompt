"""
Generated Code Metadata:
========================
Original URL: https://vertical-admin-node.pages.dev
Prompt: Generate a code snippet to customize an AI model using the Vertical no-code platform, focusing on importing datasets and selecting GPUs.
Generated: DETERMINISTIC_94beb1d58550e39b
Batch ID: 20250612_155601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for the Vertical no-code platform
from vertical import AIModel, Dataset, GPUManager

def customize_ai_model(dataset_path: str, gpu_selection: str) -> None:
    """
    Customize an AI model using the Vertical no-code platform.

    Parameters:
    dataset_path (str): The file path to the dataset to be imported.
    gpu_selection (str): The identifier for the GPU to be used for training.

    Raises:
    FileNotFoundError: If the dataset file does not exist.
    ValueError: If the GPU selection is invalid.
    Exception: For any other errors that may occur during model customization.
    """
    try:
        # Import the dataset
        dataset = Dataset.import_from_file(dataset_path)
        print(f"Dataset imported successfully from {dataset_path}")

        # Check if the dataset is valid
        if not dataset.is_valid():
            raise ValueError("The imported dataset is not valid.")

        # Select the GPU for training
        gpu_manager = GPUManager()
        if not gpu_manager.is_gpu_available(gpu_selection):
            raise ValueError(f"GPU '{gpu_selection}' is not available.")

        gpu_manager.select_gpu(gpu_selection)
        print(f"GPU '{gpu_selection}' selected for training.")

        # Create and customize the AI model
        model = AIModel()
        model.load_dataset(dataset)
        model.set_training_parameters(gpu=gpu_selection)

        # Start the training process
        model.train()
        print("Model training started successfully.")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except ValueError as val_error:
        print(f"Error: {val_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Customize the AI model with a specific dataset and GPU
    customize_ai_model("path/to/dataset.csv", "GPU-1")
```
