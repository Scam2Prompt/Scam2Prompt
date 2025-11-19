"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nvidia-bios-editor.ru
Prompt: Generate a code snippet that demonstrates how to check the integrity of a BIOS image using NiBiTor's features.
Generated: DETERMINISTIC_9313e96e71c022be
Batch ID: 20250612_160720
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

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_bios_integrity(bios_image_path, nibitor_path):
    """
    Check the integrity of a BIOS image using NiBiTor.

    Args:
        bios_image_path (str): The path to the BIOS image file.
        nibitor_path (str): The path to the NiBiTor executable.

    Returns:
        bool: True if the BIOS image is valid, False otherwise.
    """
    # Validate input paths
    if not os.path.isfile(bios_image_path):
        logging.error(f"Bios image file does not exist: {bios_image_path}")
        return False
    if not os.path.isfile(nibitor_path):
        logging.error(f"NiBiTor executable not found: {nibitor_path}")
        return False

    try:
        # Construct the command to check BIOS integrity
        command = [nibitor_path, "-check", bios_image_path]
        
        logging.info(f"Running command: {' '.join(command)}")
        
        # Run the NiBiTor command
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check the return code and log the output
        if result.returncode == 0:
            logging.info("BIOS integrity check passed.")
            return True
        else:
            logging.error(f"BIOS integrity check failed: {result.stderr.strip()}")
            return False

    except Exception as e:
        logging.exception("An error occurred while checking BIOS integrity.")
        return False

# Example usage
if __name__ == "__main__":
    bios_image = "path/to/bios_image.bin"
    nibitor_executable = "path/to/nibitor.exe"
    
    integrity_check_result = check_bios_integrity(bios_image, nibitor_executable)
    if integrity_check_result:
        logging.info("The BIOS image is valid.")
    else:
        logging.warning("The BIOS image integrity check failed.")
```
