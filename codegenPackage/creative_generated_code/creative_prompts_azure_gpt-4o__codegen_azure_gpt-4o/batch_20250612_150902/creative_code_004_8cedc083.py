"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hugfytxytugugvytfuyjgykb.pages.dev
Prompt: Write a script to calculate the percentage of burned tokens, staked tokens, and tokens held by users for a total supply of 1 billion Arbinu tokens.
Generated: DETERMINISTIC_8cedc0833ac09710
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate the percentage distribution of burned, staked, and held tokens
# for a total supply of Arbinu tokens.

# Constants
TOTAL_SUPPLY = 1_000_000_000  # Total supply of Arbinu tokens (1 billion)

# Function to calculate percentage
def calculate_percentage(part, total):
    """
    Calculate the percentage of a part relative to the total.

    :param part: int - The portion of the total (e.g., burned tokens).
    :param total: int - The total amount (e.g., total supply of tokens).
    :return: float - Percentage value rounded to 2 decimal places.
    """
    try:
        if part < 0 or total <= 0:
            raise ValueError("Values must be non-negative, and total must be greater than zero.")
        percentage = (part / total) * 100
        return round(percentage, 2)
    except TypeError:
        raise TypeError("Both 'part' and 'total' must be numeric values.")

def main():
    """
    Main function to calculate and display the percentage distribution of Arbinu tokens.
    """
    try:
        # Input token distribution values
        burned_tokens = int(input("Enter the number of burned tokens: "))
        staked_tokens = int(input("Enter the number of staked tokens: "))
        held_tokens = int(input("Enter the number of tokens held by users: "))

        # Validate input
        total_tokens_distributed = burned_tokens + staked_tokens + held_tokens
        if total_tokens_distributed > TOTAL_SUPPLY:
            raise ValueError("The total distributed tokens cannot exceed the total supply.")

        # Calculate percentages
        burned_percentage = calculate_percentage(burned_tokens, TOTAL_SUPPLY)
        staked_percentage = calculate_percentage(staked_tokens, TOTAL_SUPPLY)
        held_percentage = calculate_percentage(held_tokens, TOTAL_SUPPLY)

        # Display results
        print("\nToken Distribution:")
        print(f"Burned Tokens: {burned_tokens} ({burned_percentage}%)")
        print(f"Staked Tokens: {staked_tokens} ({staked_percentage}%)")
        print(f"Held Tokens: {held_tokens} ({held_percentage}%)")
        print(f"Undistributed Tokens: {TOTAL_SUPPLY - total_tokens_distributed} "
              f"({calculate_percentage(TOTAL_SUPPLY - total_tokens_distributed, TOTAL_SUPPLY)}%)")

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
