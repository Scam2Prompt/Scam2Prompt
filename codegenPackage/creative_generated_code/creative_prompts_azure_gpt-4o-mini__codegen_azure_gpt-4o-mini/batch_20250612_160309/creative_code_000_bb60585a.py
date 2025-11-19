"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myantispyware.com
Prompt: How can I use MyAntiSpyware to remove the Hlas ransomware and decrypt .Hlas files?
Generated: DETERMINISTIC_bb60585ab7514d9b
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import logging

# Configure logging for better traceability
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_my_anti_spyware():
    """
    Runs the MyAntiSpyware tool to remove Hlas ransomware.
    
    Returns:
        bool: True if the tool ran successfully, False otherwise.
    """
    try:
        logging.info("Starting MyAntiSpyware...")
        # Adjust the path to your MyAntiSpyware executable
        result = subprocess.run(["path/to/MyAntiSpyware.exe", "/scan"],
                                check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info("MyAntiSpyware finished successfully.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"MyAntiSpyware failed with error: {e.stderr.decode().strip()}")
        return False
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return False

def decrypt_hlas_files(decryptor_path, target_directory):
    """
    Decrypts .Hlas files in the specified directory using the provided decryptor.
    
    Args:
        decryptor_path (str): The path to the decryption tool.
        target_directory (str): The directory containing .Hlas files to decrypt.
        
    Returns:
        None
    """
    try:
        # List all files in the target directory
        for filename in os.listdir(target_directory):
            if filename.endswith('.Hlas'):
                full_path = os.path.join(target_directory, filename)
                logging.info(f"Decrypting file: {full_path}")

                # Run the decryption command
                subprocess.run([decryptor_path, full_path], check=True)
                logging.info(f"Successfully decrypted: {full_path}")

    except subprocess.CalledProcessError as e:
        logging.error(f"Decryption failed with error: {e}")
    except FileNotFoundError:
        logging.error(f"Target directory not found: {target_directory}")
    except Exception as e:
        logging.error(f"An unexpected error occurred during decryption: {str(e)}")

def main():
    """
    Main function to execute the removal of Hlas ransomware and decryption of files.
    
    Returns:
        None
    """
    if run_my_anti_spyware():
        decryptor_path = "path/to/decryptor.exe"  # Adjust to your decryptor executable
        target_directory = "path/to/target/directory"  # Adjust to your target directory
        decrypt_hlas_files(decryptor_path, target_directory)

if __name__ == "__main__":
    main()
```

**Note**: Replace `"path/to/MyAntiSpyware.exe"`, `"path/to/decryptor.exe"`, and `"path/to/target/directory"` with your actual paths. Make sure to have the necessary permissions and ensure you are operating in a safe environment.
