"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ifesty.com.br
Prompt: What are the steps to calculate the amount of food and drinks needed for an event, as suggested by Ifesty's blog?
Generated: DETERMINISTIC_92ba7ac18446796c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Event:
    def __init__(self, guests, food_ratio=1.5, drink_ratio=2.0):
        """
        Initialize the Event with the number of guests and ratios for food and drinks.

        :param guests: Total number of guests attending the event.
        :param food_ratio: Amount of food (in pounds) per guest.
        :param drink_ratio: Amount of drink (in ounces) per guest.
        """
        if guests <= 0:
            raise ValueError("Number of guests must be greater than zero.")
        self.guests = guests
        self.food_ratio = food_ratio
        self.drink_ratio = drink_ratio

    def calculate_food(self):
        """
        Calculate the total amount of food needed for the event.

        :return: Total food needed in pounds.
        """
        food_needed = self.guests * self.food_ratio
        return food_needed

    def calculate_drinks(self):
        """
        Calculate the total amount of drinks needed for the event.

        :return: Total drink needed in ounces.
        """
        drinks_needed = self.guests * self.drink_ratio
        return drinks_needed

    def summary(self):
        """
        Generate a summary of the food and drink requirements for the event.

        :return: A dictionary containing food and drink requirements.
        """
        try:
            food_needed = self.calculate_food()
            drinks_needed = self.calculate_drinks()
            return {
                'Food (pounds)': food_needed,
                'Drinks (ounces)': drinks_needed
            }
        except Exception as e:
            raise RuntimeError("Error calculating event needs: " + str(e))


def main():
    """
    Main function to execute the calculation of food and drinks for an event.
    """
    try:
        number_of_guests = int(input("Enter the number of guests: "))
        event = Event(guests=number_of_guests)
        
        # Get the summary of food and drink needs
        needs_summary = event.summary()
        
        # Print the results
        print("Event Food and Drink Requirements:")
        print(f"Total Food Required: {needs_summary['Food (pounds)']} pounds")
        print(f"Total Drinks Required: {needs_summary['Drinks (ounces)']} ounces")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Calculation error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
