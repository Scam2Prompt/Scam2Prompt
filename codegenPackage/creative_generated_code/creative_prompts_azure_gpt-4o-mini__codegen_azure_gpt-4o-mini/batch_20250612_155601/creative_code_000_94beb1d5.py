"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertical-admin-node.pages.dev
Prompt: Generate a code snippet to customize an AI model using the Vertical no-code platform, focusing on importing datasets and selecting GPUs.
Generated: DETERMINISTIC_94beb1d58550e39b
Batch ID: 20250612_155601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import vertical_ai as va

def customize_ai_model(dataset_path, model_name, gpu_type):
    """
    Customize an AI model using the Vertical no-code platform.

    Parameters:
    dataset_path (str): The file path to the dataset to be imported.
    model_name (str): The name to assign to the customized AI model.
    gpu_type (str): The type of GPU to be used for training.

    Raises:
    ValueError: If the dataset path is invalid or the GPU type is unsupported.
    IOError: If there is an issue importing the dataset.
    """

    # Validate the dataset path
    if not isinstance(dataset_path, str) or not dataset_path.endswith(('.csv', '.json')):
        raise ValueError("Invalid dataset path. Please provide a valid CSV or JSON file path.")

    # Attempt to import the dataset
    try:
        dataset = va.Dataset.import_from_file(dataset_path)
    except Exception as e:
        raise IOError(f"Failed to import the dataset: {e}")

    # Check for supported GPU types and set the GPU
    supported_gpus = ['NVIDIA_T4', 'NVIDIA_V100', 'NVIDIA_A100']
    if gpu_type not in supported_gpus:
        raise ValueError(f"Unsupported GPU type. Supported types: {supported_gpus}")

    # Create a new AI model with the specified parameters
    try:
        model = va.Model.create(name=model_name, dataset=dataset, gpu=gpu_type)
    except Exception as e:
        raise RuntimeError(f"Failed to create the AI model: {e}")

    # Print confirmation message
    print(f"Successfully created model '{model_name}' using dataset '{dataset_path}' with GPU '{gpu_type}'.")

# Example usage:
# customize_ai_model('path/to/dataset.csv', 'MyCustomModel', 'NVIDIA_T4')
```
