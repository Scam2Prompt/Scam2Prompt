"""
Generated Code Metadata:
========================
Original URL: https://proposal-ownthedoge.com
Prompt: Create a script to calculate the donation impact of merchandise sales from the Wow by Doge brand, specifically tracking contributions to Save the Children.
Generated: DETERMINISTIC_eb70b8dad5af5352
Batch ID: 20250612_154631
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DonationImpactCalculator:
    def __init__(self, merchandise_data_file, donation_percentage):
        """
        Initializes the DonationImpactCalculator with merchandise data and donation percentage.

        :param merchandise_data_file: Path to the JSON file containing merchandise sales data.
        :param donation_percentage: Percentage of sales that will be donated to Save the Children.
        """
        self.merchandise_data_file = merchandise_data_file
        self.donation_percentage = donation_percentage / 100  # Convert percentage to decimal
        self.sales_data = self.load_merchandise_data()

    def load_merchandise_data(self):
        """
        Loads merchandise sales data from a JSON file.

        :return: A list of merchandise sales data.
        """
        try:
            with open(self.merchandise_data_file, 'r') as file:
                data = json.load(file)
                logging.info("Merchandise data loaded successfully.")
                return data
        except FileNotFoundError:
            logging.error("The merchandise data file was not found.")
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the merchandise data file.")
            raise

    def calculate_total_sales(self):
        """
        Calculates the total sales from the merchandise data.

        :return: Total sales amount.
        """
        total_sales = sum(item['price'] * item['quantity'] for item in self.sales_data)
        logging.info(f"Total sales calculated: ${total_sales:.2f}")
        return total_sales

    def calculate_donation_amount(self):
        """
        Calculates the total donation amount based on total sales and donation percentage.

        :return: Total donation amount.
        """
        total_sales = self.calculate_total_sales()
        donation_amount = total_sales * self.donation_percentage
        logging.info(f"Total donation amount calculated: ${donation_amount:.2f}")
        return donation_amount

    def generate_report(self):
        """
        Generates a report of the donation impact.

        :return: A dictionary containing total sales and donation amount.
        """
        total_sales = self.calculate_total_sales()
        donation_amount = self.calculate_donation_amount()
        report = {
            'total_sales': total_sales,
            'donation_amount': donation_amount
        }
        logging.info("Donation impact report generated.")
        return report

if __name__ == "__main__":
    # Example usage
    try:
        calculator = DonationImpactCalculator('merchandise_sales.json', 10)  # 10% donation
        report = calculator.generate_report()
        print(json.dumps(report, indent=4))
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

**Note:** Ensure that the `merchandise_sales.json` file exists in the same directory as this script and follows the expected structure, e.g.:
```json
[
    {"name": "T-shirt", "price": 20.00, "quantity": 50},
    {"name": "Mug", "price": 10.00, "quantity": 30}
]
```
