"""
Generated Code Metadata:
========================
Original URL: https://kraken-energy.com
Prompt: Write a Python script to automate the process of collecting mineral rights data from sellers in Oklahoma, including fields for first name, last name, email, and comments, as described on Kraken Energy's website.
Generated: DETERMINISTIC_87564f88d9d27a4b
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os
from datetime import datetime
from typing import List, Dict, Optional

class MineralRightsDataCollector:
    """
    A class to automate the collection of mineral rights data from sellers in Oklahoma.
    The data includes first name, last name, email, and comments.
    """

    def __init__(self, output_dir: str = "mineral_rights_data"):
        """
        Initialize the data collector with the output directory.
        
        Args:
            output_dir (str): Directory to store collected data. Defaults to "mineral_rights_data".
        """
        self.output_dir = output_dir
        self._ensure_output_dir_exists()

    def _ensure_output_dir_exists(self) -> None:
        """Ensure the output directory exists; create it if it doesn't."""
        os.makedirs(self.output_dir, exist_ok=True)

    def _get_timestamped_filename(self) -> str:
        """
        Generate a timestamped filename for the CSV file.
        
        Returns:
            str: Filename in the format 'mineral_rights_YYYYMMDD_HHMMSS.csv'.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return os.path.join(self.output_dir, f"mineral_rights_{timestamp}.csv")

    def _validate_input(self, data: Dict[str, str]) -> bool:
        """
        Validate the input data to ensure required fields are present and valid.
        
        Args:
            data (Dict[str, str]): Dictionary containing the mineral rights data.
            
        Returns:
            bool: True if data is valid, False otherwise.
        """
        required_fields = ["first_name", "last_name", "email"]
        for field in required_fields:
            if field not in data or not data[field].strip():
                return False
        
        # Basic email validation
        if "@" not in data["email"] or "." not in data["email"].split("@")[-1]:
            return False
        
        return True

    def collect_data(self, data: Dict[str, str]) -> bool:
        """
        Collect and save mineral rights data to a CSV file.
        
        Args:
            data (Dict[str, str]): Dictionary containing the mineral rights data.
            
        Returns:
            bool: True if data was successfully saved, False otherwise.
        """
        if not self._validate_input(data):
            return False

        filename = self._get_timestamped_filename()
        file_exists = os.path.exists(filename)
        
        try:
            with open(filename, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["first_name", "last_name", "email", "comments"])
                
                if not file_exists:
                    writer.writeheader()
                
                writer.writerow(data)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False

    def collect_data_interactively(self) -> None:
        """
        Collect mineral rights data interactively from the user via command line.
        """
        print("Please enter the mineral rights data:")
        
        data = {
            "first_name": input("First Name: ").strip(),
            "last_name": input("Last Name: ").strip(),
            "email": input("Email: ").strip(),
            "comments": input("Comments (optional): ").strip()
        }
        
        if self.collect_data(data):
            print("Data successfully saved.")
        else:
            print("Invalid data. Please check your inputs and try again.")

if __name__ == "__main__":
    collector = MineralRightsDataCollector()
    collector.collect_data_interactively()
```
