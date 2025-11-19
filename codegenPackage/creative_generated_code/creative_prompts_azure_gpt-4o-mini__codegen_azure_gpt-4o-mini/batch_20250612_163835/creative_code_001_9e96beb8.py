"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galmudugmof.so
Prompt: How can I implement a public procurement system for the Ministry of Finance Galmudug that aligns with the PFM Regulations mentioned on their website?
Generated: DETERMINISTIC_9e96beb88886155e
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# procurement_system.py

import json
from datetime import datetime

class ProcurementSystem:
    def __init__(self):
        """Initialize the procurement system with a list to store procurement records."""
        self.procurements = []

    def add_procurement(self, title, description, budget, start_date, end_date):
        """Add a new procurement record.

        Args:
            title (str): Title of the procurement.
            description (str): Description of the procurement.
            budget (float): Budget allocated for the procurement.
            start_date (str): Start date in 'YYYY-MM-DD' format.
            end_date (str): End date in 'YYYY-MM-DD' format.
        """
        # Validate inputs
        self.validate_procurement(title, description, budget, start_date, end_date)

        procurement_record = {
            "id": len(self.procurements) + 1,
            "title": title,
            "description": description,
            "budget": budget,
            "start_date": start_date,
            "end_date": end_date,
            "created_at": datetime.now().isoformat()
        }
        
        self.procurements.append(procurement_record)

    def validate_procurement(self, title, description, budget, start_date, end_date):
        """Validate procurement data.

        Args:
            title (str): Title of the procurement.
            description (str): Description of the procurement.
            budget (float): Budget allocated for the procurement.
            start_date (str): Start date in 'YYYY-MM-DD' format.
            end_date (str): End date in 'YYYY-MM-DD' format.

        Raises:
            ValueError: If any of the validations fail.
        """
        if not title or not description:
            raise ValueError("Title and description cannot be empty.")
        if budget <= 0:
            raise ValueError("Budget must be a positive number.")
        if not self.validate_date_format(start_date) or not self.validate_date_format(end_date):
            raise ValueError("Date must be in 'YYYY-MM-DD' format.")
        if start_date >= end_date:
            raise ValueError("End date must be after the start date.")

    @staticmethod
    def validate_date_format(date_str):
        """Check if the date is in 'YYYY-MM-DD' format.

        Args:
            date_str (str): Date string to validate.

        Returns:
            bool: True if valid format, False otherwise.
        """
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def export_procurement_data(self, filename):
        """Export procurement data to a JSON file.

        Args:
            filename (str): Path to the JSON file where data will be saved.
        """
        try:
            with open(filename, 'w') as json_file:
                json.dump(self.procurements, json_file, indent=4)
        except IOError as e:
            print(f"Error writing to file {filename}: {e}")

    def load_procurement_data(self, filename):
        """Load procurement data from a JSON file.

        Args:
            filename (str): Path to the JSON file to load data from.
        """
        try:
            with open(filename, 'r') as json_file:
                self.procurements = json.load(json_file)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty procurement list.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    system = ProcurementSystem()
    
    try:
        system.add_procurement("Road Construction", "Construction of a new road.", 500000, "2023-01-01", "2023-06-01")
        system.export_procurement_data("procurement_data.json")
        system.load_procurement_data("procurement_data.json")
        print("Procurement records loaded successfully.")
    except ValueError as e:
        print(f"Error adding procurement: {e}")
```
