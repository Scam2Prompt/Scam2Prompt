"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherealspamassagetherapist.com
Prompt: Write a function that calculates the total cost for a client booking a 60-minute hot stone massage and includes enhancements like aromatherapy.
Generated: DETERMINISTIC_31758740b569d902
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MassageBooking:
    """
    A class to represent a massage booking with costs for services.
    """

    BASE_COST = 100.00  # Base cost for a 60-minute hot stone massage
    AROMATHERAPY_COST = 20.00  # Additional cost for aromatherapy enhancement

    def __init__(self, include_aromatherapy=False):
        """
        Initialize a booking with an optional aromatherapy enhancement.

        :param include_aromatherapy: Boolean indicating whether aromatherapy is included
        """
        self.include_aromatherapy = include_aromatherapy

    def calculate_total_cost(self):
        """
        Calculate the total cost for the massage booking.

        :return: Total cost as a float
        :raises ValueError: If an invalid cost calculation is attempted
        """
        try:
            total_cost = self.BASE_COST
            if self.include_aromatherapy:
                total_cost += self.AROMATHERAPY_COST
            
            if total_cost < 0:
                raise ValueError("Total cost cannot be negative.")
            
            return total_cost
        
        except Exception as e:
            print(f"Error calculating total cost: {str(e)}")
            raise

# Example usage:
if __name__ == "__main__":
    try:
        # Create a booking with aromatherapy included
        booking_with_aromatherapy = MassageBooking(include_aromatherapy=True)
        total_with_aromatherapy = booking_with_aromatherapy.calculate_total_cost()
        print(f"Total cost with aromatherapy: ${total_with_aromatherapy:.2f}")

        # Create a booking without aromatherapy
        booking_without_aromatherapy = MassageBooking(include_aromatherapy=False)
        total_without_aromatherapy = booking_without_aromatherapy.calculate_total_cost()
        print(f"Total cost without aromatherapy: ${total_without_aromatherapy:.2f}")

    except Exception as e:
        print(f"An error occurred during booking: {str(e)}")
```
