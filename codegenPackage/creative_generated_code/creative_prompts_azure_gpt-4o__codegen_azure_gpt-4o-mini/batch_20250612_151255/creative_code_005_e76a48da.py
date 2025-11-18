"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beacons-dabcat.pages.dev
Prompt: Generate code to calculate the remaining time until the Dabcat token sale ends, using the sale end time `2024-07-19 20:00:00`.
Generated: DETERMINISTIC_e76a48dac6b7afc0
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class TokenSale:
    def __init__(self, end_time_str: str):
        """
        Initialize the TokenSale with the end time.

        :param end_time_str: The end time of the token sale as a string in 'YYYY-MM-DD HH:MM:SS' format.
        """
        self.end_time = self.parse_end_time(end_time_str)

    @staticmethod
    def parse_end_time(end_time_str: str) -> datetime:
        """
        Parse the end time string into a datetime object.

        :param end_time_str: The end time of the token sale as a string.
        :return: A datetime object representing the end time.
        """
        try:
            return datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')
        except ValueError as e:
            raise ValueError(f"Invalid date format: {end_time_str}. Expected format: YYYY-MM-DD HH:MM:SS") from e

    def remaining_time(self) -> timedelta:
        """
        Calculate the remaining time until the token sale ends.

        :return: A timedelta object representing the remaining time.
        """
        now = datetime.now()
        if now >= self.end_time:
            return timedelta(0)  # Sale has ended
        return self.end_time - now

    def time_remaining_str(self) -> str:
        """
        Get a string representation of the remaining time until the token sale ends.

        :return: A string indicating the remaining time in a human-readable format.
        """
        remaining = self.remaining_time()
        if remaining.total_seconds() <= 0:
            return "The token sale has ended."
        days, seconds = remaining.days, remaining.seconds
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        return f"Remaining time: {days} days, {hours} hours, {minutes} minutes."

if __name__ == "__main__":
    # Define the end time for the token sale
    end_time = "2024-07-19 20:00:00"
    
    # Create a TokenSale instance
    token_sale = TokenSale(end_time)
    
    # Print the remaining time until the token sale ends
    print(token_sale.time_remaining_str())
```
