"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amdi.pl
Prompt: Develop a script to handle bookkeeping tasks using AMDI's "Księga przychodów i rozchodów / Ryczałt" software.
Generated: DETERMINISTIC_29412ad576a80830
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
import logging
import datetime

# Configure logging for debugging and production readiness
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("bookkeeping.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

# Define constants (e.g., file paths and settings for AMDI software)
DATA_DIRECTORY = "path/to/amdi/data"
EXPORT_DIRECTORY = "path/to/export"
AMDI_EXECUTABLE = "path/to/amdi/executable"

# Utility function to check if required paths and files exist
def validate_paths():
    """
    Validate that required paths and executables exist.

    Raises:
        FileNotFoundError: If a required path or executable is missing.
    """
    if not os.path.exists(DATA_DIRECTORY):
        raise FileNotFoundError(f"Data directory not found: {DATA_DIRECTORY}")
    if not os.path.exists(EXPORT_DIRECTORY):
        raise FileNotFoundError(f"Export directory not found: {EXPORT_DIRECTORY}")
    if not os.path.exists(AMDI_EXECUTABLE):
        raise FileNotFoundError(f"AMDI executable not found: {AMDI_EXECUTABLE}")

# Utility function to create a backup of bookkeeping data
def backup_data():
    """
    Creates a backup of the bookkeeping data.

    Returns:
        str: The path to the backup file.
    """
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(EXPORT_DIRECTORY, f"backup_{timestamp}.zip")
        os.system(f"zip -r {backup_file} {DATA_DIRECTORY}")  # Backup using zip command
        logging.info(f"Backup created successfully: {backup_file}")
        return backup_file
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")
        raise

# Utility function to run AMDI software for bookkeeping tasks
def run_amdi_task(task_name):
    """
    Runs a specific task using the AMDI software.

    Args:
        task_name (str): The name of the task to execute.

    Raises:
        RuntimeError: If the AMDI process fails.
    """
    try:
        command = f"{AMDI_EXECUTABLE} --task={task_name}"
        logging.info(f"Running AMDI command: {command}")
        exit_code = os.system(command)
        if exit_code != 0:
            raise RuntimeError(f"AMDI command failed with exit code {exit_code}")
        logging.info(f"Task '{task_name}' completed successfully.")
    except Exception as e:
        logging.error(f"Error while running AMDI task '{task_name}': {e}")
        raise

# Main function to handle bookkeeping workflow
def main():
    """
    Main function to handle bookkeeping tasks with AMDI software.
    """
    try:
        logging.info("Starting bookkeeping workflow...")
        
        # Validate paths and files
        validate_paths()
        logging.info("Validation of paths completed successfully.")
        
        # Create backup
        backup_file = backup_data()
        logging.info(f"Backup file location: {backup_file}")
        
        # Run AMDI tasks (e.g., process income and expenses)
        tasks = ["process_income", "process_expenses"]
        for task in tasks:
            run_amdi_task(task)
        
        logging.info("Bookkeeping workflow completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)

# Entry point for the script
if __name__ == "__main__":
    main()
```
