"""
Generated Code Metadata:
========================
Original URL: https://amirinternationalcharity.org
Prompt: Write a Python script to manage donations for a charity organization like Amir International Charity Organization, which has programs for nutritional support, education assistance, and medical care.
Generated: DETERMINISTIC_41693a74a32c3a49
Batch ID: 20250622_210348
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
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DonationManager:
    def __init__(self, filename: str):
        """
        Initializes the DonationManager with a specified JSON file to store donations.
        
        :param filename: The name of the JSON file to store donation records.
        """
        self.filename = filename
        self.donations = self.load_donations()

    def load_donations(self) -> List[Dict[str, Any]]:
        """
        Loads donations from the JSON file.
        
        :return: A list of donation records.
        """
        try:
            with open(self.filename, 'r') as file:
                donations = json.load(file)
                logging.info("Donations loaded successfully.")
                return donations
        except FileNotFoundError:
            logging.warning("Donation file not found. Starting with an empty donation list.")
            return []
        except json.JSONDecodeError:
            logging.error("Error decoding JSON. Starting with an empty donation list.")
            return []

    def save_donations(self) -> None:
        """
        Saves the current donations to the JSON file.
        """
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.donations, file, indent=4)
                logging.info("Donations saved successfully.")
        except IOError as e:
            logging.error(f"Error saving donations: {e}")

    def add_donation(self, donor_name: str, amount: float, program: str) -> None:
        """
        Adds a new donation to the list and saves it to the file.
        
        :param donor_name: The name of the donor.
        :param amount: The amount donated.
        :param program: The program the donation is supporting.
        """
        if amount <= 0:
            logging.error("Donation amount must be greater than zero.")
            raise ValueError("Donation amount must be greater than zero.")
        
        donation_record = {
            "donor_name": donor_name,
            "amount": amount,
            "program": program
        }
        self.donations.append(donation_record)
        self.save_donations()
        logging.info(f"Added donation: {donation_record}")

    def get_donations(self) -> List[Dict[str, Any]]:
        """
        Retrieves the list of all donations.
        
        :return: A list of donation records.
        """
        return self.donations

    def get_total_donations(self) -> float:
        """
        Calculates the total amount of donations received.
        
        :return: The total donation amount.
        """
        total = sum(donation['amount'] for donation in self.donations)
        logging.info(f"Total donations calculated: {total}")
        return total

def main():
    donation_manager = DonationManager('donations.json')

    # Example usage
    try:
        donation_manager.add_donation("Alice Smith", 100.0, "Nutritional Support")
        donation_manager.add_donation("Bob Johnson", 50.0, "Education Assistance")
        donation_manager.add_donation("Charlie Brown", 75.0, "Medical Care")

        total_donations = donation_manager.get_total_donations()
        print(f"Total donations received: ${total_donations:.2f}")

        all_donations = donation_manager.get_donations()
        print("All donations:")
        for donation in all_donations:
            print(donation)

    except ValueError as e:
        logging.error(f"ValueError: {e}")

if __name__ == "__main__":
    main()
```
