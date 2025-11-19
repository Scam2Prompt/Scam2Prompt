"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://you-trip.ru
Prompt: Develop a program that calculates the total cost of a tour package, including deposit and final payment based on currency exchange rates, for a trip to the UAE.
Generated: DETERMINISTIC_d2bdfd0aa952eca9
Batch ID: 20250612_164206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TourPackageCalculator:
    def __init__(self, package_cost_usd, deposit_percentage, exchange_rate):
        """
        Initializes the TourPackageCalculator with necessary parameters.

        :param package_cost_usd: Total cost of the tour package in USD
        :param deposit_percentage: Percentage of the package cost for the deposit
        :param exchange_rate: Current exchange rate from USD to local currency (AED)
        """
        self.package_cost_usd = package_cost_usd
        self.deposit_percentage = deposit_percentage / 100  # Convert to decimal
        self.exchange_rate = exchange_rate

    def calculate_deposit(self):
        """
        Calculates the deposit amount in AED.

        :return: Deposit amount in AED
        """
        deposit_usd = self.package_cost_usd * self.deposit_percentage
        deposit_aed = deposit_usd * self.exchange_rate
        return deposit_aed

    def calculate_final_payment(self):
        """
        Calculates the final payment amount in AED after the deposit.

        :return: Final payment amount in AED
        """
        total_aed = self.package_cost_usd * self.exchange_rate
        deposit_aed = self.calculate_deposit()
        final_payment_aed = total_aed - deposit_aed
        return final_payment_aed

    def display_costs(self):
        """
        Prints the deposit and final payment amounts in AED.
        """
        try:
            deposit_aed = self.calculate_deposit()
            final_payment_aed = self.calculate_final_payment()
            print(f"Deposit Amount (AED): {deposit_aed:.2f}")
            print(f"Final Payment Amount (AED): {final_payment_aed:.2f}")
        except Exception as e:
            print(f"An error occurred while calculating costs: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        # Create an instance of TourPackageCalculator
        calculator = TourPackageCalculator(package_cost_usd=2000, deposit_percentage=20, exchange_rate=3.67)

        # Display the calculated costs
        calculator.display_costs()
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
