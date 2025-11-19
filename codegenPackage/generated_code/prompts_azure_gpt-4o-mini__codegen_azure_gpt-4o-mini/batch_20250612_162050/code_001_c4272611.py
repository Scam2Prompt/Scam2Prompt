"""
Generated Code Metadata:
========================
Original URL: https://proarteasa.com
Prompt: Write a Python script that calculates the total cost of purchasing a lot in Acacias Retiro Campestre, including financing options with 0% interest for up to 36 months.
Generated: DETERMINISTIC_c427261198ab4d19
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LotPurchaseCalculator:
    """
    A class to calculate the total cost of purchasing a lot in Acacias Retiro Campestre,
    including financing options with 0% interest for up to 36 months.
    """

    def __init__(self, lot_price, down_payment_percentage, financing_months):
        """
        Initializes the LotPurchaseCalculator with the lot price, down payment percentage,
        and financing months.

        :param lot_price: The total price of the lot.
        :param down_payment_percentage: The percentage of the lot price to be paid as a down payment.
        :param financing_months: The number of months over which to finance the remaining amount.
        """
        self.lot_price = lot_price
        self.down_payment_percentage = down_payment_percentage
        self.financing_months = financing_months

    def calculate_down_payment(self):
        """
        Calculates the down payment amount based on the lot price and down payment percentage.

        :return: The down payment amount.
        """
        return self.lot_price * (self.down_payment_percentage / 100)

    def calculate_financed_amount(self):
        """
        Calculates the amount that needs to be financed after the down payment.

        :return: The financed amount.
        """
        down_payment = self.calculate_down_payment()
        return self.lot_price - down_payment

    def calculate_monthly_payment(self):
        """
        Calculates the monthly payment amount if the financed amount is spread over the financing months.

        :return: The monthly payment amount.
        """
        financed_amount = self.calculate_financed_amount()
        return financed_amount / self.financing_months

    def calculate_total_cost(self):
        """
        Calculates the total cost of purchasing the lot, including the down payment and total financed amount.

        :return: The total cost of the lot purchase.
        """
        down_payment = self.calculate_down_payment()
        total_financed_amount = self.calculate_financed_amount()
        return down_payment + total_financed_amount

    def display_payment_plan(self):
        """
        Displays the payment plan including down payment, financed amount, and monthly payments.
        """
        try:
            down_payment = self.calculate_down_payment()
            financed_amount = self.calculate_financed_amount()
            monthly_payment = self.calculate_monthly_payment()
            total_cost = self.calculate_total_cost()

            print(f"Total Lot Price: ${self.lot_price:.2f}")
            print(f"Down Payment ({self.down_payment_percentage}%): ${down_payment:.2f}")
            print(f"Financed Amount: ${financed_amount:.2f}")
            print(f"Monthly Payment for {self.financing_months} months: ${monthly_payment:.2f}")
            print(f"Total Cost of Purchase: ${total_cost:.2f}")

        except ZeroDivisionError:
            print("Error: Financing months cannot be zero.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        lot_price = float(input("Enter the total price of the lot: $"))
        down_payment_percentage = float(input("Enter the down payment percentage: "))
        financing_months = int(input("Enter the number of months for financing (up to 36): "))

        if financing_months > 36:
            raise ValueError("Financing months cannot exceed 36.")

        calculator = LotPurchaseCalculator(lot_price, down_payment_percentage, financing_months)
        calculator.display_payment_plan()

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
