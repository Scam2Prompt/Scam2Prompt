"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yanmaq.cl
Prompt: Generate a script to calculate the rental cost of Yanmar mini excavators based on daily rates and rental duration, including a feature for automatic reservation confirmation.
Generated: DETERMINISTIC_ef34bba787a5fe10
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MiniExcavatorRental:
    def __init__(self, daily_rate):
        """
        Initialize the rental service with a daily rate for the excavator.

        :param daily_rate: Daily rental rate for the mini excavator
        """
        if daily_rate <= 0:
            raise ValueError("Daily rate must be a positive number.")
        self.daily_rate = daily_rate

    def calculate_rental_cost(self, rental_days):
        """
        Calculate the total rental cost based on the number of rental days.

        :param rental_days: Number of days the excavator is rented
        :return: Total rental cost
        """
        if rental_days <= 0:
            raise ValueError("Rental days must be a positive integer.")
        return self.daily_rate * rental_days

    def confirm_reservation(self, rental_days):
        """
        Confirm the reservation and return a summary of the rental details.

        :param rental_days: Number of days the excavator is rented
        :return: Confirmation message with rental details
        """
        try:
            total_cost = self.calculate_rental_cost(rental_days)
            return f"Reservation confirmed for {rental_days} days. Total cost: ${total_cost:.2f}"
        except ValueError as e:
            return f"Error confirming reservation: {str(e)}"


def main():
    """
    Main function to run the rental cost calculator and handle user input.
    """
    daily_rate = 150.00  # Example daily rate
    rental_service = MiniExcavatorRental(daily_rate)

    try:
        rental_days = int(input("Enter the number of rental days: "))
        confirmation_message = rental_service.confirm_reservation(rental_days)
        print(confirmation_message)
    except ValueError:
        print("Please enter a valid number of rental days.")

if __name__ == "__main__":
    main()
```
