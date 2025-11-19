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
    def __init__(self, package_name, total_cost):
        """
        Initializes a TourPackage instance.

        :param package_name: str - The name of the tour package
        :param total_cost: float - The total cost of the tour package
        """
        self.package_name = package_name
        self.total_cost = total_cost

    def calculate_payments(self):
        """
        Calculates the upfront and final payment amounts.

        :return: tuple - A tuple containing the upfront payment and final payment
        """
        upfront_payment = self.total_cost * 0.30
        final_payment = self.total_cost * 0.70
        return upfront_payment, final_payment

    def display_payment_schedule(self):
        """
        Displays the payment schedule for the tour package.
        """
        try:
            upfront_payment, final_payment = self.calculate_payments()
            print(f"Tour Package: {self.package_name}")
            print(f"Total Cost: ${self.total_cost:.2f}")
            print(f"Upfront Payment (30%): ${upfront_payment:.2f}")
            print(f"Final Payment (70%): ${final_payment:.2f} (Due 21 days before departure)")
        except Exception as e:
            print(f"An error occurred while calculating payments: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a tour package instance
        tour_package = TourPackage("Adventure in the Alps", 1500.00)
        # Display the payment schedule
        tour_package.display_payment_schedule()
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
