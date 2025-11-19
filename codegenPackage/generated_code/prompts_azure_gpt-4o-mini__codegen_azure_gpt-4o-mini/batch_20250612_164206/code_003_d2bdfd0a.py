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
class TourPackage:
    def __init__(self, base_cost, deposit_percentage, exchange_rate):
        """
        Initializes the TourPackage with base cost, deposit percentage, and exchange rate.

        :param base_cost: float, the total cost of the tour package in local currency
        :param deposit_percentage: float, the percentage of the base cost to be paid as a deposit
        :param exchange_rate: float, the exchange rate from local currency to UAE Dirham (AED)
        """
        self.base_cost = base_cost
        self.deposit_percentage = deposit_percentage
        self.exchange_rate = exchange_rate

    def calculate_deposit(self):
        """
        Calculates the deposit amount based on the base cost and deposit percentage.

        :return: float, the deposit amount in local currency
        """
        return self.base_cost * (self.deposit_percentage / 100)

    def calculate_final_payment(self):
        """
        Calculates the final payment amount after the deposit has been paid.

        :return: float, the final payment amount in local currency
        """
        return self.base_cost - self.calculate_deposit()

    def convert_to_aed(self, amount):
        """
        Converts an amount from local currency to UAE Dirham (AED) using the exchange rate.

        :param amount: float, the amount in local currency to convert
        :return: float, the converted amount in AED
        """
        return amount * self.exchange_rate

    def total_cost_in_aed(self):
        """
        Calculates the total cost of the tour package in AED, including deposit and final payment.

        :return: tuple, (total cost in AED, deposit in AED, final payment in AED)
        """
        try:
            deposit = self.calculate_deposit()
            final_payment = self.calculate_final_payment()
            total_cost = self.base_cost

            deposit_aed = self.convert_to_aed(deposit)
            final_payment_aed = self.convert_to_aed(final_payment)
            total_cost_aed = self.convert_to_aed(total_cost)

            return total_cost_aed, deposit_aed, final_payment_aed
        except Exception as e:
            print(f"An error occurred while calculating costs: {e}")
            return None

def main():
    """
    Main function to execute the tour package cost calculation.
    """
    try:
        # Example values
        base_cost = 5000.0  # Total cost in local currency
        deposit_percentage = 20.0  # Deposit percentage
        exchange_rate = 1.2  # Example exchange rate to AED

        # Create a TourPackage instance
        tour_package = TourPackage(base_cost, deposit_percentage, exchange_rate)

        # Calculate total cost in AED
        total_cost_aed, deposit_aed, final_payment_aed = tour_package.total_cost_in_aed()

        if total_cost_aed is not None:
            print(f"Total Cost in AED: {total_cost_aed:.2f}")
            print(f"Deposit in AED: {deposit_aed:.2f}")
            print(f"Final Payment in AED: {final_payment_aed:.2f}")

    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
