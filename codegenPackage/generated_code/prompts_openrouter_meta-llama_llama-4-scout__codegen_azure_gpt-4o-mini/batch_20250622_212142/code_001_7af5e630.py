"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: "Write a Python script to manage a grants program, including tools for measuring program success and maximizing engagement."
Generated: DETERMINISTIC_7af5e630e98ec5cf
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Grant:
    """Class to represent a grant in the program."""
    
    def __init__(self, title: str, amount: float, recipient: str, date_awarded: str):
        self.title = title
        self.amount = amount
        self.recipient = recipient
        self.date_awarded = datetime.strptime(date_awarded, '%Y-%m-%d')
        self.success_metrics = {}

    def add_success_metric(self, metric_name: str, value: Any):
        """Add a success metric for the grant."""
        self.success_metrics[metric_name] = value

    def __repr__(self):
        return f"Grant(title={self.title}, amount={self.amount}, recipient={self.recipient}, date_awarded={self.date_awarded})"


class GrantsProgram:
    """Class to manage the grants program."""
    
    def __init__(self):
        self.grants: List[Grant] = []

    def add_grant(self, title: str, amount: float, recipient: str, date_awarded: str):
        """Add a new grant to the program."""
        try:
            grant = Grant(title, amount, recipient, date_awarded)
            self.grants.append(grant)
            logging.info(f"Grant added: {grant}")
        except Exception as e:
            logging.error(f"Error adding grant: {e}")

    def measure_success(self) -> Dict[str, Any]:
        """Measure the success of the grants program."""
        total_amount = sum(grant.amount for grant in self.grants)
        total_grants = len(self.grants)
        success_metrics = {
            "total_amount_awarded": total_amount,
            "total_grants": total_grants,
            "average_grant_amount": total_amount / total_grants if total_grants > 0 else 0
        }
        logging.info(f"Success metrics calculated: {success_metrics}")
        return success_metrics

    def save_grants_to_file(self, filename: str):
        """Save the grants data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json_data = [grant.__dict__ for grant in self.grants]
                json.dump(json_data, file, default=str)
                logging.info(f"Grants data saved to {filename}")
        except IOError as e:
            logging.error(f"Error saving grants to file: {e}")

    def load_grants_from_file(self, filename: str):
        """Load grants data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                grants_data = json.load(file)
                for grant_data in grants_data:
                    grant = Grant(**grant_data)
                    self.grants.append(grant)
                logging.info(f"Grants data loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Error loading grants from file: {e}")

# Example usage
if __name__ == "__main__":
    program = GrantsProgram()
    program.add_grant("Research Grant", 5000, "University A", "2023-01-15")
    program.add_grant("Community Development Grant", 3000, "Nonprofit B", "2023-02-20")
    
    metrics = program.measure_success()
    print(metrics)

    program.save_grants_to_file("grants_data.json")
    program.load_grants_from_file("grants_data.json")
```
