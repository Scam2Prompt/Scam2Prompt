"""
Generated Code Metadata:
========================
Original URL: https://you-trip.ru
Prompt: Develop a program that calculates the total cost of a tour package, including deposit and final payment based on currency exchange rates, for a trip to the UAE.
Generated: DETERMINISTIC_d2bdfd0aa952eca9
Batch ID: 20250612_164206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tour_package_calculator.py

class TourPackage:
    def __init__(self, package_name, cost_usd, deposit_percentage, exchange_rate):
        """
        Initialize a TourPackage object.

        Args:
            package_name (str): Name of the tour package.
            cost_usd (float): Cost of the tour package in USD.
            deposit_percentage (float): Percentage of the cost that is the deposit.
            exchange_rate (float): Exchange rate from USD to AED.
        """
        self.package_name = package_name
        self.cost_usd = cost_usd
        self.deposit_percentage = deposit_percentage
        self.exchange_rate = exchange_rate

    def calculate_deposit(self):
        """
        Calculate the deposit amount in USD.

        Returns:
            float: Deposit amount in USD.
        """
        return self.cost_usd * (self.deposit_percentage / 100)

    def calculate_final_payment(self):
        """
        Calculate the final payment amount in USD.

        Returns:
            float: Final payment amount in USD.
        """
        return self.cost_usd - self.calculate_deposit()

    def calculate_cost_aed(self):
        """
        Calculate the cost of the tour package in AED.

        Returns:
            float: Cost of the tour package in AED.
        """
        return self.cost_usd * self.exchange_rate

    def calculate_deposit_aed(self):
        """
        Calculate the deposit amount in AED.

        Returns:
            float: Deposit amount in AED.
        """
        return self.calculate_deposit() * self.exchange_rate

    def calculate_final_payment_aed(self):
        """
        Calculate the final payment amount in AED.

        Returns:
            float: Final payment amount in AED.
        """
        return self.calculate_final_payment() * self.exchange_rate


def main():
    try:
        # Define tour package details
        package_name = "UAE Tour Package"
        cost_usd = 2000.0
        deposit_percentage = 20.0
        exchange_rate = 3.67  # USD to AED

        # Create a TourPackage object
        tour_package = TourPackage(package_name, cost_usd, deposit_percentage, exchange_rate)

        # Calculate costs
        cost_usd = tour_package.cost_usd
        deposit_usd = tour_package.calculate_deposit()
        final_payment_usd = tour_package.calculate_final_payment()
        cost_aed = tour_package.calculate_cost_aed()
        deposit_aed = tour_package.calculate_deposit_aed()
        final_payment_aed = tour_package.calculate_final_payment_aed()

        # Print costs
        print("Tour Package Details:")
        print(f"Package Name: {tour_package.package_name}")
        print(f"Cost (USD): ${cost_usd:.2f}")
        print(f"Deposit (USD): ${deposit_usd:.2f} ({tour_package.deposit_percentage}%)")
        print(f"Final Payment (USD): ${final_payment_usd:.2f}")
        print(f"Cost (AED): AED {cost_aed:.2f}")
        print(f"Deposit (AED): AED {deposit_aed:.2f}")
        print(f"Final Payment (AED): AED {final_payment_aed:.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
