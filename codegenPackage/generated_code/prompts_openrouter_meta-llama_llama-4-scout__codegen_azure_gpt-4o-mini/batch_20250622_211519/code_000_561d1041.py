"""
Generated Code Metadata:
========================
Original URL: https://a-step.site
Prompt: "Generate a Python script to automate a partnership program for earning money online, focusing on financial independence and work-life balance."
Generated: DETERMINISTIC_561d104126d209e0
Batch ID: 20250622_211519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PartnershipProgram:
    def __init__(self, program_name, earnings_file):
        """
        Initializes the PartnershipProgram with a name and a CSV file for earnings.

        :param program_name: Name of the partnership program
        :param earnings_file: Path to the CSV file to store earnings data
        """
        self.program_name = program_name
        self.earnings_file = earnings_file
        self.partners = {}

    def add_partner(self, partner_name, email):
        """
        Adds a new partner to the program.

        :param partner_name: Name of the partner
        :param email: Email of the partner
        """
        if partner_name in self.partners:
            logging.warning(f"Partner '{partner_name}' already exists.")
            return
        
        self.partners[partner_name] = {
            'email': email,
            'earnings': 0.0
        }
        logging.info(f"Added partner: {partner_name}")

    def record_earnings(self, partner_name, amount):
        """
        Records earnings for a specific partner.

        :param partner_name: Name of the partner
        :param amount: Amount earned
        """
        if partner_name not in self.partners:
            logging.error(f"Partner '{partner_name}' not found.")
            return
        
        if amount < 0:
            logging.error("Earnings amount must be non-negative.")
            return
        
        self.partners[partner_name]['earnings'] += amount
        logging.info(f"Recorded earnings for {partner_name}: ${amount:.2f}")

    def save_earnings_to_csv(self):
        """
        Saves the earnings data to a CSV file.
        """
        try:
            with open(self.earnings_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Partner Name', 'Email', 'Earnings'])
                for partner, data in self.partners.items():
                    writer.writerow([partner, data['email'], data['earnings']])
            logging.info(f"Earnings data saved to {self.earnings_file}")
        except Exception as e:
            logging.error(f"Failed to save earnings data: {e}")

    def display_partners(self):
        """
        Displays the list of partners and their earnings.
        """
        if not self.partners:
            logging.info("No partners found.")
            return
        
        logging.info("Current Partners and Earnings:")
        for partner, data in self.partners.items():
            logging.info(f"{partner}: ${data['earnings']:.2f}")

def main():
    # Initialize the partnership program
    program = PartnershipProgram("Online Earnings Program", "earnings.csv")

    # Add partners
    program.add_partner("Alice Smith", "alice@example.com")
    program.add_partner("Bob Johnson", "bob@example.com")

    # Record earnings
    program.record_earnings("Alice Smith", 150.00)
    program.record_earnings("Bob Johnson", 200.00)

    # Display partners and their earnings
    program.display_partners()

    # Save earnings to CSV
    program.save_earnings_to_csv()

if __name__ == "__main__":
    main()
```
