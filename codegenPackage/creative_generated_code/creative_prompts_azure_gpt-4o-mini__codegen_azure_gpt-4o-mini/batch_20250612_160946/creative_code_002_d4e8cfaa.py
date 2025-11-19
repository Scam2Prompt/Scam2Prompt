"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openmse.com
Prompt: Can you provide a code example for importing an operating model from Stock Synthesis 3 using openMSE?
Generated: DETERMINISTIC_d4e8cfaa0dca03e6
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import openMSE as mse

def import_operating_model(file_path: str) -> mse.OperatingModel:
    """
    Import an operating model from Stock Synthesis 3 using openMSE.

    Args:
        file_path (str): The path to the Stock Synthesis 3 model file.

    Returns:
        mse.OperatingModel: An instance of the OperatingModel class.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the file content is invalid or cannot be parsed.
    """
    # Check if the file exists
    try:
        with open(file_path, 'r') as file:
            model_data = file.read()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"The specified file was not found: {file_path}") from e

    # Attempt to parse the model data into an OperatingModel
    try:
        operating_model = mse.OperatingModel.from_stock_synthesis(model_data)
    except Exception as e:
        raise ValueError("Error parsing the operating model from the file.") from e

    return operating_model

# Usage example (uncomment to run)
# if __name__ == "__main__":
#     try:
#         model = import_operating_model('path/to/your/model.ss')
#         print("Operating model imported successfully.")
#     except (FileNotFoundError, ValueError) as error:
#         print(f"An error occurred: {error}")
```
