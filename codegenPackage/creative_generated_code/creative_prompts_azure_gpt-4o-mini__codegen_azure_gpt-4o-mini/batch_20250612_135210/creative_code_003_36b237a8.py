"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metandmask.org
Prompt: "How can I use metandmask to perform batch processing on multiple files?"
Generated: DETERMINISTIC_36b237a8c4f24dc5
Batch ID: 20250612_135210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import metandmask

def process_files_in_batch(input_directory, output_directory, mask_parameters):
    """
    Processes multiple files in a specified directory using metandmask.

    Args:
        input_directory (str): The path to the directory containing input files.
        output_directory (str): The path to the directory to save processed files.
        mask_parameters (dict): Parameters to be used with the metandmask processing.

    Raises:
        FileNotFoundError: If the input directory does not exist.
        Exception: For any other processing errors.
    """
    # Check if input directory exists
    if not os.path.exists(input_directory):
        raise FileNotFoundError(f"Input directory '{input_directory}' not found.")

    # Create output directory if it does not exist
    os.makedirs(output_directory, exist_ok=True)

    # Process each file in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.tif') or filename.endswith('.png'):  # Assuming image files
            input_file_path = os.path.join(input_directory, filename)
            output_file_path = os.path.join(output_directory, filename)

            try:
                # Perform masking operation using metandmask
                metandmask.apply_mask(input_file_path, output_file_path, **mask_parameters)
                print(f"Processed file: {filename} -> Saved to: {output_file_path}")
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    input_dir = '/path/to/input/files'  # Change to your input directory
    output_dir = '/path/to/output/files'  # Change to your output directory
    mask_params = {
        'mask_type': 'example_mask',
        'threshold': 0.5,
        # Add other parameters as needed
    }

    process_files_in_batch(input_dir, output_dir, mask_params)
```
