"""
Generated Code Metadata:
========================
Original URL: https://mahnoorpc.net
Prompt: "Write a Python script using Windows PowerShell 7.4.3 to automate a system task."
Generated: DETERMINISTIC_b62e1cbda9df07a1
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_powershell_script(script_path):
    """
    Executes a PowerShell script using subprocess.

    Args:
        script_path (str): The path to the PowerShell script to execute.

    Raises:
        FileNotFoundError: If the specified script does not exist.
        subprocess.CalledProcessError: If the PowerShell command fails.
    """
    try:
        # Check if the script file exists
        with open(script_path, 'r') as file:
            logging.info(f"Found PowerShell script: {script_path}")

        # Construct the PowerShell command
        command = ["pwsh", script_path]

        # Execute the PowerShell script
        logging.info("Executing PowerShell script...")
        result = subprocess.run(command, check=True, capture_output=True, text=True)

        # Log the output from the script
        logging.info("PowerShell script executed successfully.")
        logging.info(f"Output:\n{result.stdout}")
        
    except FileNotFoundError:
        logging.error(f"PowerShell script not found: {script_path}")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing PowerShell script: {e}")
        logging.error(f"Output:\n{e.output}")
        sys.exit(1)

if __name__ == "__main__":
    # Define the path to the PowerShell script
    script_path = "C:\\path\\to\\your\\script.ps1"  # Update this path accordingly

    # Run the PowerShell script
    run_powershell_script(script_path)
```
