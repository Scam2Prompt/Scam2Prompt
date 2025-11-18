"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qnwnfewifjdsifjfdsoifj.pages.dev
Prompt: Write a function to calculate and display TONCOIN prize ranges (e.g., 50-75 TONCOIN) after a virtual spin, as described on the webpage.
Generated: DETERMINISTIC_bfa7571c33b8738d
Batch ID: 20250612_153916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def calculate_toncoin_prize():
    """
    Calculate and display a random prize range for TONCOIN after a virtual spin.
    The prize range is between 50 and 100 TONCOIN, with a lower limit of 50 and
    an upper limit of 75. The upper limit is randomly selected between 75 and 100.

    Returns:
        str: A formatted string representing the TONCOIN prize range.
    """
    try:
        # Define lower and upper limits for the prize range
        lower_limit = 50
        upper_limit = random.randint(75, 100)  # Random upper limit between 75 and 100
        
        # Ensure the upper limit is greater than or equal to the lower limit
        if upper_limit < lower_limit:
            raise ValueError("Upper limit must be greater than or equal to lower limit.")
        
        # Format the prize range as a string
        prize_range = f"{lower_limit}-{upper_limit} TONCOIN"
        
        # Display the prize range
        print(f"Congratulations! You've won a prize range of: {prize_range}")
        
        return prize_range

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while calculating the prize: {e}")
        return None

# Example usage
if __name__ == "__main__":
    calculate_toncoin_prize()
```
