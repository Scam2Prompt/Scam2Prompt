"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimedsonic.pages.dev
Prompt: Generate code for a "Hard Reset" feature to resolve synchronization issues in a blockchain guild management system, referencing Guildhall's use case.
Generated: DETERMINISTIC_ad1185e82861fe0f
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

# Define a function for logging
def log(message: str):
    """Logs a message to the console."""
    print(f"[LOG] {message}")

# Define a function for error logging
def log_error(message: str):
    """Logs an error message to the console."""
    print(f"[ERROR] {message}")

# Define a Hard Reset class
class HardResetManager:
    """
    Manages the Hard Reset process for a blockchain guild management system.
    This ensures synchronization issues are resolved.
    """

    def __init__(self, data_file: str, backup_file: str):
        """
        Initializes the HardResetManager with paths to the data file and backup file.
        
        :param data_file: Path to the guild data file (JSON).
        :param backup_file: Path to the backup file.
        """
        self.data_file = data_file
        self.backup_file = backup_file

    def backup_data(self) -> None:
        """
        Creates a backup of the current guild data file.
        """
        try:
            log("Creating backup...")
            if not os.path.exists(self.data_file):
                raise FileNotFoundError(f"Data file '{self.data_file}' does not exist.")
            with open(self.data_file, "r") as original_file:
                data = original_file.read()
            with open(self.backup_file, "w") as backup_file:
                backup_file.write(data)
            log(f"Backup created successfully at '{self.backup_file}'.")
        except Exception as e:
            log_error(f"Failed to create backup: {str(e)}")
            raise

    def reset_data(self) -> None:
        """
        Resets the guild data file to its default state.
        """
        try:
            log("Resetting data...")
            # Define the default state for the guild data
            default_data = {
                "guilds": [],
                "version": "1.0",
                "last_updated": None
            }
            # Write the default data to the data file
            with open(self.data_file, "w") as data_file:
                json.dump(default_data, data_file, indent=4)
            log(f"Data reset successfully; file '{self.data_file}' updated.")
        except Exception as e:
            log_error(f"Failed to reset data: {str(e)}")
            raise

    def perform_hard_reset(self) -> None:
        """
        Perform a hard reset by backing up the current data and resetting it to its default state.
        """
        try:
            log("Starting hard reset...")
            self.backup_data()
            self.reset_data()
            log("Hard reset completed successfully.")
        except Exception as e:
            log_error(f"Hard reset failed: {str(e)}")
            raise

# Usage example (uncomment and configure paths before running):
# data_file_path = "guild_data.json"
# backup_file_path = "guild_backup.json"
# hard_reset_manager = HardResetManager(data_file_path, backup_file_path)
# hard_reset_manager.perform_hard_reset()
```
