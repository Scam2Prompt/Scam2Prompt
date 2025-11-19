"""
Generated Code Metadata:
========================
Original URL: https://you-trip.ru
Prompt: Generate a code snippet to calculate the cost of a tour package, considering the 30% upfront payment and 70% payment 21 days before departure, as described on the YouTrip website.
Generated: DETERMINISTIC_35fd3afc8db06360
Batch ID: 20250622_211832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TourPackage:
    """
    Represents a tour package with its cost and payment schedule.
    """

    def __init__(self, package_name, total_cost):
        """
        Initializes a TourPackage instance.

        Args:
            package_name (str): The name of the tour package.
            total_cost (float): The total cost of the tour package.

        Raises:
            ValueError: If total_cost is not a positive number.
        """
        if total_cost <= 0:
            raise ValueError("Total cost must be a positive number.")

        self.package_name = package_name
        self.total_cost = total_cost

    def calculate_upfront_payment(self):
        """
        Calculates the 30% upfront payment.

        Returns:
            float: The upfront payment amount.
        """
        return self.total_cost * 0.3

    def calculate_balance_payment(self):
        """
        Calculates the 70% balance payment.

        Returns:
            float: The balance payment amount.
        """
        return self.total_cost * 0.7

    def get_payment_schedule(self):
        """
        Generates a payment schedule.

        Returns:
            dict: A dictionary containing the payment schedule.
        """
        upfront_payment = self.calculate_upfront_payment()
        balance_payment = self.calculate_balance_payment()

        return {
            "Upfront Payment (30%):": f"${upfront_payment:.2f}",
            "Balance Payment (70%) 21 days before departure:": f"${balance_payment:.2f}",
        }


def main():
    try:
        package_name = input("Enter the tour package name: ")
        total_cost = float(input("Enter the total cost of the tour package: "))

        tour_package = TourPackage(package_name, total_cost)
        payment_schedule = tour_package.get_payment_schedule()

        print(f"\nPayment Schedule for {tour_package.package_name}:")
        for payment, amount in payment_schedule.items():
            print(f"{payment} {amount}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
