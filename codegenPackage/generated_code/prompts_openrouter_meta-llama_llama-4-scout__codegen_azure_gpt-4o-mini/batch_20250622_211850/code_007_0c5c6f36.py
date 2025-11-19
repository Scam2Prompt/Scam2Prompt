"""
Generated Code Metadata:
========================
Original URL: https://awards-lidofinance.com
Prompt: How does the Discover it ® Miles Credit Card's unlimited Discover Match ® feature work, and what are the benefits of its 1.5x Miles on every dollar of every purchase?
Generated: DETERMINISTIC_0c5c6f36b116274b
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DiscoverItMilesCard:
    """
    A class to represent the Discover it® Miles Credit Card and its features.
    """

    def __init__(self):
        """
        Initializes the Discover it® Miles Credit Card with default values.
        """
        self.miles_earned = 0.0
        self.discover_match = 1.0  # Initial match multiplier for Discover Match

    def earn_miles(self, amount_spent):
        """
        Earn miles based on the amount spent.

        Parameters:
        amount_spent (float): The amount spent on purchases.

        Returns:
        float: The miles earned from the purchase.
        """
        if amount_spent < 0:
            raise ValueError("Amount spent cannot be negative.")
        
        miles = amount_spent * 1.5  # 1.5x miles on every dollar spent
        self.miles_earned += miles
        return miles

    def apply_discover_match(self):
        """
        Applies the Discover Match feature to the total miles earned.

        Returns:
        float: The total miles after applying the Discover Match.
        """
        matched_miles = self.miles_earned * self.discover_match
        self.miles_earned += matched_miles
        return self.miles_earned

    def get_total_miles(self):
        """
        Returns the total miles earned.

        Returns:
        float: The total miles earned.
        """
        return self.miles_earned

    def reset_miles(self):
        """
        Resets the miles earned to zero.
        """
        self.miles_earned = 0.0


# Example usage
if __name__ == "__main__":
    try:
        card = DiscoverItMilesCard()
        card.earn_miles(100)  # Spend $100
        print(f"Miles earned: {card.get_total_miles()}")  # Should print 150.0
        card.apply_discover_match()  # Apply Discover Match
        print(f"Total miles after Discover Match: {card.get_total_miles()}")  # Should print 300.0
    except ValueError as e:
        print(f"Error: {e}")
```
