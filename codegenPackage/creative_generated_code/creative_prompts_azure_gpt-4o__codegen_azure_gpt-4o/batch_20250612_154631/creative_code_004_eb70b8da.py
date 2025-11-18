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

class DonationImpactCalculator:
    """
    A class to calculate the donation impact of merchandise sales.
    Tracks contributions to 'Save the Children' from Wow by Doge brand.
    """

    def __init__(self, donation_percentage):
        """
        Initializes the DonationImpactCalculator with the donation percentage.

        :param donation_percentage: Percentage of each sale that is donated (e.g., 10 for 10%)
        """
        if not (0 <= donation_percentage <= 100):
            raise ValueError("donation_percentage must be between 0 and 100 inclusive")
        self.donation_percentage = donation_percentage
        self.total_sales = 0.0
        self.total_donations = 0.0

    def add_sale(self, sale_amount):
        """
        Records a sale and updates total sales and total donations.

        :param sale_amount: The monetary value of the sale
        """
        if sale_amount < 0:
            raise ValueError("sale_amount must be non-negative")
        
        self.total_sales += sale_amount
        donation = (sale_amount * self.donation_percentage) / 100
        self.total_donations += donation

    def get_summary(self):
        """
        Returns a summary of total sales and total donations.

        :return: Dictionary containing total sales and total donations
        """
        return {
            "total_sales": round(self.total_sales, 2),
            "total_donations": round(self.total_donations, 2)
        }

    def save_summary_to_file(self, file_path):
        """
        Saves the summary of sales and donations to a JSON file.

        :param file_path: Path to the file where the summary will be saved
        """
        summary = self.get_summary()
        try:
            with open(file_path, 'w') as file:
                json.dump(summary, file, indent=4)
        except Exception as e:
            raise IOError(f"Failed to save summary to {file_path}: {e}")


# Example usage
if __name__ == '__main__':
    try:
        # Configure donation percentage (e.g., 10% of each sale is donated)
        donation_percentage = 10
        calculator = DonationImpactCalculator(donation_percentage)

        # Add sales amounts
        calculator.add_sale(100.0)  # $100 sale
        calculator.add_sale(50.0)   # $50 sale
        calculator.add_sale(200.0)  # $200 sale

        # Print summary to the console
        summary = calculator.get_summary()
        print("Donation Summary:", summary)

        # Save summary to a file
        output_file = "donation_summary.json"
        calculator.save_summary_to_file(output_file)
        print(f"Summary saved to {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
