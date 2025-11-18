"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nc20la24.pages.dev
Prompt: Create a tool to calculate the remaining Notcoin tokens left to distribute based on the $15 Million figure provided on the website.
Generated: DETERMINISTIC_50c605bad0388c16
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_remaining_tokens(total_distribution_amount, distributed_tokens):
    """
    Calculate the remaining tokens left to distribute.

    Args:
        total_distribution_amount (float): The total amount of tokens to be distributed (e.g., $15M).
        distributed_tokens (float): The amount of tokens already distributed.

    Returns:
        float: The remaining tokens left to be distributed.
    """
    try:
        # Ensure input values are valid
        if total_distribution_amount < 0 or distributed_tokens < 0:
            raise ValueError("Token amounts cannot be negative.")
        if distributed_tokens > total_distribution_amount:
            raise ValueError("Distributed tokens cannot exceed the total distribution amount.")
        
        # Calculate remaining tokens
        remaining_tokens = total_distribution_amount - distributed_tokens
        return remaining_tokens
    except ValueError as ve:
        print(f"Error: {ve}")  # Print a user-friendly error message
        sys.exit(1)


def main():
    """
    Main function to execute the token calculation logic.
    """
    # Total token distribution amount provided from the website ($15M)
    total_distribution_amount = 15_000_000.0  # Represented in dollars

    # Prompt user to input the distributed tokens
    try:
        distributed_tokens = float(input("Enter the amount of tokens already distributed: "))
    except ValueError:
        print("Error: Please provide a valid numeric value.")
        sys.exit(1)
    
    # Calculate and display remaining tokens
    remaining_tokens = calculate_remaining_tokens(total_distribution_amount, distributed_tokens)
    print(f"Remaining Notcoin tokens to distribute: {remaining_tokens:.2f}")


if __name__ == "__main__":
    # Entry point of the program
    main()
```
