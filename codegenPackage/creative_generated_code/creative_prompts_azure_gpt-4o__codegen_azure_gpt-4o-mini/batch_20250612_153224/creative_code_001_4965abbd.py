"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geeks-on-repair.com
Prompt: Recommend APIs or libraries for performing data recovery tasks similar to the services offered by Geeks On Repair, and provide sample code for recovering deleted files.
Generated: DETERMINISTIC_4965abbd1b6ca372
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
from pathlib import Path

class DataRecovery:
    def __init__(self, recovery_directory: str):
        """
        Initializes the DataRecovery class with the specified recovery directory.

        Args:
            recovery_directory (str): The directory where recovered files will be stored.
        """
        self.recovery_directory = Path(recovery_directory)
        self.recovery_directory.mkdir(parents=True, exist_ok=True)

    def recover_deleted_files(self, source_directory: str):
        """
        Recovers deleted files by moving them from the specified source directory to the recovery directory.

        Args:
            source_directory (str): The directory where deleted files are searched for. 

        Raises:
            FileNotFoundError: If the source directory does not exist.
            Exception: For other unforeseen errors during recovery.
        """
        source_path = Path(source_directory)

        # Check if the source directory exists
        if not source_path.exists() or not source_path.is_dir():
            raise FileNotFoundError(f"The source directory '{source_directory}' does not exist or is not a directory.")

        try:
            for item in os.listdir(source_path):
                item_path = source_path / item

                # Check if the item is a deleted file (simulated by a ".deleted" extension in this example)
                if item_path.is_file() and item.endswith('.deleted'):
                    # Move the file to the recovery directory
                    shutil.move(str(item_path), str(self.recovery_directory / item))
                    print(f"Recovered: {item}")

        except Exception as e:
            raise Exception(f"An error occurred during recovery: {str(e)}")

if __name__ == "__main__":
    # Example usage of the DataRecovery class
    try:
        recovery = DataRecovery(recovery_directory='recovered_files')
        recovery.recover_deleted_files(source_directory='source_directory_with_deleted_files')
    except Exception as e:
        print(f"Data recovery failed: {str(e)}")
```
