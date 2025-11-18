"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buildonbeam-7h0.pages.dev
Prompt: Create a code snippet to decrypt and process encrypted data files using BeamOS tools.
Generated: DETERMINISTIC_5c76f2c7885d0315
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from beamos import BeamOS  # Assume this is the library for BeamOS tools

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def decrypt_and_process_files(encrypted_files, output_directory, decryption_key):
    """
    Decrypts and processes a list of encrypted data files using BeamOS tools.
    
    Args:
        encrypted_files (list): List of paths to encrypted files.
        output_directory (str): Directory to save processed files.
        decryption_key (str): The key used for decryption.
    
    Raises:
        ValueError: If any file is not found or decryption fails.
    """
    # Ensure output directory exists
    os.makedirs(output_directory, exist_ok=True)

    for file_path in encrypted_files:
        try:
            if not os.path.isfile(file_path):
                raise ValueError(f"File not found: {file_path}")

            # Log the decryption process
            logging.info(f"Decrypting file: {file_path}")

            # Decrypt the file using BeamOS
            decrypted_data = BeamOS.decrypt(file_path, decryption_key)

            # Process the decrypted data
            processed_data = process_data(decrypted_data)

            # Define output file path
            output_file_path = os.path.join(output_directory, os.path.basename(file_path))

            # Save the processed data
            with open(output_file_path, 'w') as output_file:
                output_file.write(processed_data)

            logging.info(f"Processed data saved to: {output_file_path}")

        except ValueError as ve:
            logging.error(f"Value error occurred: {ve}")
        except Exception as e:
            logging.error(f"Failed to process {file_path}: {e}")

def process_data(data):
    """
    Processes the decrypted data.
    
    Args:
        data (str): The decrypted data to process.
    
    Returns:
        str: Processed data.
    """
    # This is a placeholder for actual data processing logic
    # For demonstration, we'll just return the data as is
    return data

# Example usage (this should be run in the main application context)
if __name__ == "__main__":
    encrypted_files_list = ['path/to/encrypted_file1', 'path/to/encrypted_file2']
    output_dir = 'path/to/output_directory'
    decryption_key = 'your_decryption_key_here'
    
    decrypt_and_process_files(encrypted_files_list, output_dir, decryption_key)
```
