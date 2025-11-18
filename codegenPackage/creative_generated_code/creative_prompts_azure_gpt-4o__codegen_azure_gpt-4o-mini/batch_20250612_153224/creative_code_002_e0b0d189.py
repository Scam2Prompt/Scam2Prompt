"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ifesty.com.br
Prompt: Generate code to calculate the quantity of beverages needed for a party, referencing Ifesty's blog post on beverage calculation for events.
Generated: DETERMINISTIC_e0b0d1892951af5a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BeverageCalculator:
    def __init__(self, guests: int, duration_hours: int):
        """
        Initialize the BeverageCalculator with the number of guests and duration of the event.
        
        :param guests: Number of guests attending the party
        :param duration_hours: Duration of the party in hours
        """
        self.guests = guests
        self.duration_hours = duration_hours

        # Check for valid input
        if guests <= 0 or duration_hours <= 0:
            raise ValueError("Number of guests and duration must be greater than zero.")

    def calculate_beverages(self):
        """
        Calculate the total quantity of beverages needed for the party.

        :return: A dictionary with the quantities of beer, wine, and soft drinks needed
        """
        # Constants for calculations (average consumption)
        BEER_PER_GUEST_PER_HOUR = 0.5  # in bottles
        WINE_PER_GUEST_PER_HOUR = 0.25  # in bottles
        SOFT_DRINK_PER_GUEST_PER_HOUR = 0.75  # in bottles

        # Calculate total drinks needed
        total_beer = self.guests * BEER_PER_GUEST_PER_HOUR * self.duration_hours
        total_wine = self.guests * WINE_PER_GUEST_PER_HOUR * self.duration_hours
        total_soft_drinks = self.guests * SOFT_DRINK_PER_GUEST_PER_HOUR * self.duration_hours

        # Prepare results
        return {
            'beer': round(total_beer),
            'wine': round(total_wine),
            'soft_drinks': round(total_soft_drinks)
        }

def main():
    """
    Main function to execute the beverage calculation.
    """
    try:
        # Example input: 20 guests for 4 hours
        guests = int(input("Enter the number of guests: "))
        duration = int(input("Enter the duration of the party in hours: "))

        calculator = BeverageCalculator(guests, duration)
        beverages_needed = calculator.calculate_beverages()

        # Output the results
        print("Beverages needed for the party:")
        print(f"Beer: {beverages_needed['beer']} bottles")
        print(f"Wine: {beverages_needed['wine']} bottles")
        print(f"Soft Drinks: {beverages_needed['soft_drinks']} bottles")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
