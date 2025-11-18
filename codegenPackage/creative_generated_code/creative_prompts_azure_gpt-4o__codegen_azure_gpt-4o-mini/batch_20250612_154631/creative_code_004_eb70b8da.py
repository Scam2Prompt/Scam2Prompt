"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposal-ownthedoge.com
Prompt: Create a script to calculate the donation impact of merchandise sales from the Wow by Doge brand, specifically tracking contributions to Save the Children.
Generated: DETERMINISTIC_eb70b8dad5af5352
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class DonationCalculator:
    """
    A class to calculate the donation impact of merchandise sales.
    Specifically, it tracks contributions to Save the Children.
    """

    def __init__(self, merchandise_data_file):
        """
        Initialize the DonationCalculator with merchandise data.

        Parameters:
        merchandise_data_file (str): Path to the JSON file containing merchandise sales data.
        """
        self.merchandise_data_file = merchandise_data_file
        self.merchandise_sales = []
        self.load_merchandise_data()

    def load_merchandise_data(self):
        """
        Load merchandise sales data from a JSON file.
        """
        try:
            with open(self.merchandise_data_file, 'r') as file:
                self.merchandise_sales = json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {self.merchandise_data_file} was not found.")
            self.merchandise_sales = []
        except json.JSONDecodeError:
            print(f"Error: The file {self.merchandise_data_file} does not contain valid JSON.")
            self.merchandise_sales = []

    def calculate_total_sales(self):
        """
        Calculate the total sales amount from merchandise sales.

        Returns:
        float: Total sales amount.
        """
        total_sales = sum(item['price'] * item['quantity'] for item in self.merchandise_sales)
        return total_sales

    def calculate_donation_amount(self, percentage):
        """
        Calculate the total donation amount based on merchandise sales.

        Parameters:
        percentage (float): The percentage of sales to donate.

        Returns:
        float: Total donation amount.
        """
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")
        
        total_sales = self.calculate_total_sales()
        donation_amount = total_sales * (percentage / 100)
        return donation_amount

    def generate_report(self, percentage):
        """
        Generate a report of the total sales and donation amount.

        Parameters:
        percentage (float): The percentage of sales to donate.
        
        Returns:
        dict: A report containing total sales and donation amount.
        """
        try:
            donation_amount = self.calculate_donation_amount(percentage)
            total_sales = self.calculate_total_sales()

            report = {
                'total_sales': total_sales,
                'donation_amount': donation_amount,
                'donation_percentage': percentage
            }
            return report
        except ValueError as e:
            print(f"Error: {e}")
            return {}

# Example usage:
if __name__ == "__main__":
    # Path to the merchandise data JSON file
    merchandise_data_file = 'merchandise_sales.json'
    
    # Donation percentage to Save the Children
    donation_percentage = 10.0  # 10%

    # Create a DonationCalculator instance
    calculator = DonationCalculator(merchandise_data_file)

    # Generate and print the report
    report = calculator.generate_report(donation_percentage)
    print(json.dumps(report, indent=4))
```
