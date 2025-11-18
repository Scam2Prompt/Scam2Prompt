"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniwrapper.com
Prompt: Develop a function to process multiple file formats (e.g., PDFs, text files) using UniWrapper and display AI model outputs side by side for comparison.
Generated: DETERMINISTIC_8f86962d2f43a79b
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import traceback
from uniwrapper import UniWrapper
from typing import List, Dict

def process_files(file_paths: List[str], model_names: List[str]) -> Dict[str, List[Dict[str, str]]]:
    """
    Processes multiple file formats using UniWrapper and displays AI model outputs side by side for comparison.

    Args:
        file_paths (List[str]): List of file paths to process.
        model_names (List[str]): List of model names to use for inference.

    Returns:
        Dict[str, List[Dict[str, str]]]: A dictionary where keys are file names and values are lists of dictionaries
                                          containing model name and corresponding output.

    Raises:
        Exception: If file processing fails for any reason.
    """

    # Initialize the result dictionary
    results = {}

    try:
        # Validate input files
        for file_path in file_paths:
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")
            
            # Get file name for result identification
            file_name = os.path.basename(file_path)
            
            # Initialize UniWrapper instance
            uni_wrapper = UniWrapper()
            
            # Read file and process using UniWrapper
            uni_wrapper.load_file(file_path)
            
            # Store outputs for each model
            model_outputs = []
            for model in model_names:
                try:
                    # Load the specific AI model
                    uni_wrapper.set_model(model)
                    
                    # Run inference
                    output = uni_wrapper.run_inference()
                    
                    # Store model name and output
                    model_outputs.append({'model_name': model, 'output': output})
                except Exception as model_error:
                    # Handle model-specific errors gracefully
                    model_outputs.append({'model_name': model, 'output': f"Error: {str(model_error)}"})
                    print(f"Error processing model '{model}' for file '{file_name}': {model_error}")
            
            # Add model outputs to the results dictionary
            results[file_name] = model_outputs

    except Exception as e:
        # Log the error details and re-raise the exception
        print(f"An error occurred while processing files: {e}")
        traceback.print_exc()
        raise

    return results


# Example usage:
if __name__ == "__main__":
    file_paths = ["example.pdf", "example.txt"]  # List of files to process
    model_names = ["model_a", "model_b"]  # AI models to use for inference
    
    try:
        outputs = process_files(file_paths, model_names)
        for file, models_results in outputs.items():
            print(f"\nResults for file: {file}")
            for result in models_results:
                print(f"Model: {result['model_name']} | Output: {result['output']}")
    except Exception as main_error:
        print(f"An error occurred: {main_error}")
```
