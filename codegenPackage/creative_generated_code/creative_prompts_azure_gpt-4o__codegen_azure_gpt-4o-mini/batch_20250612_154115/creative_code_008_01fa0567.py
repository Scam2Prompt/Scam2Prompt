"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.tax
Prompt: Create a script to handle quarterly estimated tax payments for Polymarket earnings, ensuring compliance with IRS deadlines and avoiding underpayment penalties, as outlined on the PolyTax website.
Generated: DETERMINISTIC_01fa0567efec9b02
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
import requests

class TaxPaymentHandler:
    def __init__(self, earnings, payment_percentage=0.24):
        """
        Initializes the TaxPaymentHandler with earnings and payment percentage.
        
        :param earnings: Total earnings from Polymarket.
        :param payment_percentage: The estimated percentage of earnings to be paid as tax.
        """
        self.earnings = earnings
        self.payment_percentage = payment_percentage
        self.tax_due = self.calculate_tax_due()

    def calculate_tax_due(self):
        """
        Calculates the estimated tax due based on earnings and payment percentage.
        
        :return: The calculated tax due.
        """
        return self.earnings * self.payment_percentage

    def get_quarterly_deadlines(self):
        """
        Retrieves the quarterly estimated tax payment deadlines.
        
        :return: A list of deadlines for each quarter.
        """
        current_year = datetime.datetime.now().year
        deadlines = [
            datetime.date(current_year, 4, 15),   # Q1
            datetime.date(current_year, 6, 15),   # Q2
            datetime.date(current_year, 9, 15),   # Q3
            datetime.date(current_year + 1, 1, 15) # Q4
        ]
        return deadlines

    def check_payment_schedule(self):
        """
        Checks if an estimated tax payment is due today.
        
        :return: A message indicating whether payment is due today.
        """
        today = datetime.date.today()
        deadlines = self.get_quarterly_deadlines()
        if today in deadlines:
            return f"Payment of ${self.tax_due:.2f} is due today!"
        return "No payment due today."

    def make_payment(self):
        """
        Simulates making a payment for the calculated tax due.
        
        :return: A confirmation message if payment is successful.
        """
        try:
            # Here you would implement the actual payment logic
            # For demonstration, we'll mock this with a print statement
            print(f"Making a payment of ${self.tax_due:.2f} for estimated taxes.")
            # Simulate payment success
            return "Payment successful."
        except Exception as e:
            return f"An error occurred while processing payment: {str(e)}"

    def save_payment_record(self):
        """
        Saves the payment record to a JSON file.
        
        :return: A confirmation message indicating record saving status.
        """
        record = {
            "earnings": self.earnings,
            "tax_due": self.tax_due,
            "payment_date": datetime.date.today().isoformat()
        }
        
        try:
            with open("tax_payment_record.json", "a") as file:
                json.dump(record, file)
                file.write("\n")  # New line for each record
            return "Payment record saved successfully."
        except IOError as e:
            return f"An error occurred while saving the record: {str(e)}"

def main():
    # Example earnings from Polymarket
    earnings = float(input("Enter your total earnings from Polymarket: "))
    
    # Create a TaxPaymentHandler instance
    tax_handler = TaxPaymentHandler(earnings)

    # Check if payment is due today
    print(tax_handler.check_payment_schedule())

    # If payment is due, proceed to make payment and save record
    if datetime.date.today() in tax_handler.get_quarterly_deadlines():
        print(tax_handler.make_payment())
        print(tax_handler.save_payment_record())

if __name__ == "__main__":
    main()
```
