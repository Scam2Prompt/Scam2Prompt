"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cegeduc.org
Prompt: Develop a code snippet that tracks donations for sustainability projects, ensuring transparency and community involvement in environmental health initiatives.
Generated: DETERMINISTIC_4e5c8025f8763f7d
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class DonationTracker:
    def __init__(self, project_name: str):
        """
        Initialize the DonationTracker with a specific project name.

        :param project_name: The name of the sustainability project
        """
        self.project_name = project_name
        self.donations: List[Dict[str, Any]] = []
        self.total_amount: float = 0.0

    def add_donation(self, donor_name: str, amount: float, message: str = "") -> None:
        """
        Add a donation to the tracker.

        :param donor_name: Name of the donor
        :param amount: Amount donated
        :param message: Optional message from the donor
        """
        if amount <= 0:
            raise ValueError("Donation amount must be greater than zero.")
        
        donation_entry = {
            'donor_name': donor_name,
            'amount': amount,
            'message': message,
        }
        self.donations.append(donation_entry)
        self.total_amount += amount
        print(f"Donation from {donor_name} of amount ${amount:.2f} added successfully.")

    def get_total_donations(self) -> float:
        """
        Get the total amount of donations received.

        :return: Total donation amount
        """
        return self.total_amount

    def get_donations(self) -> List[Dict[str, Any]]:
        """
        Get the list of all donations.

        :return: List of donations
        """
        return self.donations

    def export_donations(self, file_path: str) -> None:
        """
        Export the donation data to a JSON file for transparency.

        :param file_path: The path to the file where data will be exported
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump({
                    'project_name': self.project_name,
                    'total_amount': self.total_amount,
                    'donations': self.donations
                }, json_file, indent=4)
            print(f"Donation data exported to {file_path} successfully.")
        except IOError as e:
            print(f"An error occurred while writing to file: {e}")

# Example Usage
if __name__ == "__main__":
    tracker = DonationTracker("Clean Water Initiative")
    
    try:
        tracker.add_donation("Alice", 100.0, "Happy to contribute!")
        tracker.add_donation("Bob", 50.0)
        print(f"Total donations: ${tracker.get_total_donations():.2f}")
        
        # Export donations to a file
        tracker.export_donations("donations.json")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
