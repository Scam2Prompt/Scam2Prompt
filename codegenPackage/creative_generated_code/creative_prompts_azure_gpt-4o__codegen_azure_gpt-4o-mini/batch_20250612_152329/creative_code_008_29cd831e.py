"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rascalsnft.web.app
Prompt: Create a function to calculate the total $Jelly tokens claimed and update the percentage dynamically, based on the data structure described on the website.
Generated: DETERMINISTIC_29cd831e002d77e0
Batch ID: 20250612_152329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class JellyTokenTracker:
    def __init__(self):
        """
        Initializes the JellyTokenTracker with an empty list of claims and a total count.
        """
        self.claims = []  # List to hold Jelly token claims
        self.total_claimed = 0  # Total Jelly tokens claimed

    def add_claim(self, amount):
        """
        Adds a new claim of Jelly tokens.

        Parameters:
        amount (int): The number of Jelly tokens to add to the claims.

        Raises:
        ValueError: If the amount is negative or not an integer.
        """
        if not isinstance(amount, int) or amount < 0:
            raise ValueError("Amount must be a non-negative integer.")
        
        self.claims.append(amount)
        self.total_claimed += amount

    def calculate_percentage(self, total_available):
        """
        Calculates the percentage of Jelly tokens claimed based on the total available.

        Parameters:
        total_available (int): The total number of available Jelly tokens.

        Returns:
        float: The percentage of tokens claimed.

        Raises:
        ValueError: If total_available is not greater than 0.
        """
        if total_available <= 0:
            raise ValueError("Total available must be greater than zero.")

        percentage_claimed = (self.total_claimed / total_available) * 100
        return round(percentage_claimed, 2)  # Return the percentage rounded to 2 decimal places

    def get_total_claimed(self):
        """
        Returns the total Jelly tokens claimed.

        Returns:
        int: The total number of Jelly tokens claimed.
        """
        return self.total_claimed

    def get_claims(self):
        """
        Returns the list of individual claims of Jelly tokens.

        Returns:
        list: A list of amounts claimed.
        """
        return self.claims


# Example usage:
if __name__ == "__main__":
    tracker = JellyTokenTracker()
    
    try:
        tracker.add_claim(100)
        tracker.add_claim(150)
        tracker.add_claim(50)

        total_available_tokens = 500  # Example total available tokens
        percentage_claimed = tracker.calculate_percentage(total_available_tokens)

        print(f"Total Jelly tokens claimed: {tracker.get_total_claimed()}")
        print(f"Percentage of Jelly tokens claimed: {percentage_claimed}%")
    except ValueError as ve:
        print(f"Error: {ve}")
```
