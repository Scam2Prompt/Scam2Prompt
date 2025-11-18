"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foundationlabs.tech
Prompt: Generate code that demonstrates how to craft tools for preserving and renewing systems, reflecting the ethos of Foundation Labs' focus on civilization-building through computational power.
Generated: DETERMINISTIC_322490045b2828e1
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import logging
from datetime import datetime
from typing import Any, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SystemPreservationTool:
    """A class to manage system preservation and renewal tasks."""
    
    def __init__(self, backup_directory: str):
        """
        Initializes the SystemPreservationTool with a specific backup directory.

        Args:
            backup_directory (str): The directory where backups will be stored.
        """
        self.backup_directory = backup_directory
        self.ensure_directory_exists(self.backup_directory)

    def ensure_directory_exists(self, directory: str) -> None:
        """Ensures that a directory exists; creates it if it does not."""
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
                logging.info(f"Created directory: {directory}")
        except Exception as e:
            logging.error(f"Failed to create directory {directory}: {e}")
            raise

    def create_backup(self, data: Dict[str, Any]) -> str:
        """
        Creates a backup of the provided data and saves it to the backup directory.

        Args:
            data (Dict[str, Any]): The data to back up.
        
        Returns:
            str: The path to the created backup file.
        """
        backup_file = os.path.join(self.backup_directory, f"backup_{datetime.now().isoformat()}.json")
        
        try:
            with open(backup_file, 'w') as f:
                json.dump(data, f, indent=4)
                logging.info(f"Backup created successfully: {backup_file}")
        except Exception as e:
            logging.error(f"Error creating backup file {backup_file}: {e}")
            raise
        
        return backup_file

    def restore_backup(self, backup_file: str) -> Dict[str, Any]:
        """
        Restores data from a backup file.

        Args:
            backup_file (str): The path to the backup file to restore.
        
        Returns:
            Dict[str, Any]: The restored data.
        """
        try:
            with open(backup_file, 'r') as f:
                data = json.load(f)
                logging.info(f"Backup restored successfully from: {backup_file}")
                return data
        except FileNotFoundError:
            logging.error(f"Backup file not found: {backup_file}")
            raise
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON from backup file {backup_file}: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error while restoring backup file {backup_file}: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Initialize the system preservation tool with a backup directory
    tool = SystemPreservationTool(backup_directory='backups')

    # Sample data to back up
    sample_data = {
        "name": "Foundation Labs",
        "mission": "Civilization-building through computational power",
        "core_values": ["innovation", "collaboration", "sustainability"]
    }

    # Create a backup of the sample data
    backup_path = tool.create_backup(sample_data)

    # Restore the backup data
    restored_data = tool.restore_backup(backup_path)
    logging.info(f"Restored data: {restored_data}")
```
