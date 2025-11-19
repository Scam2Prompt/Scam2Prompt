"""
Generated Code Metadata:
========================
Original URL: https://btconbase-ai.pages.dev
Prompt: Generate a Python script to calculate the scarcity of a token, like Bitcoin on Base, given its total supply and burned token percentage.
Generated: DETERMINISTIC_9162dc4a0cbaa143
Batch ID: 20250622_205230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the scarcity of a token based on its total supply and burned token percentage.

This script calculates the remaining supply of a token after a certain percentage of tokens have been burned.
It also provides the scarcity ratio, which is the percentage of tokens remaining compared to the original total supply.
"""

def calculate_scarcity(total_supply: float, burned_percentage: float) -> dict:
    """
    Calculate the remaining supply and scarcity ratio of a token.

    Args:
        total_supply (float): The total supply of the token.
        burned_percentage (float): The percentage of tokens burned (0-100).

    Returns:
        dict: A dictionary containing the remaining supply and scarcity ratio.
    """
    try:
        # Validate inputs
        if total_supply < 0:
            raise ValueError("Total supply must be a non-negative number.")
        if not (0 <= burned_percentage <= 100):
            raise ValueError("Burned percentage must be between 0 and 100.")

        # Calculate remaining supply
        burned_amount = (burned_percentage / 100) * total_supply
        remaining_supply = total_supply - burned_amount

        # Calculate scarcity ratio
        scarcity_ratio = (remaining_supply / total_supply) * 100

        return {
            "remaining_supply": remaining_supply,
            "scarcity_ratio": scarcity_ratio
        }

    except ValueError as ve:
        # Handle invalid input errors
        print(f"Input Error: {ve}")
        return {}
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return {}

def main():
    """
    Main function to interact with the user and calculate token scarcity.
    """
    print("Token Scarcity Calculator")
    print("=========================")

    try:
        # Get user input
        total_supply = float(input("Enter the total supply of the token: "))
        burned_percentage = float(input("Enter the burned token percentage (0-100): "))

        # Perform calculation
        result = calculate_scarcity(total_supply, burned_percentage)

        if result:
            # Display results
            print("\nResults:")
            print(f"Remaining Supply: {result['remaining_supply']:.2f}")
            print(f"Scarcity Ratio: {result['scarcity_ratio']:.2f}%")
        else:
            print("Failed to calculate scarcity due to invalid inputs.")

    except ValueError:
        print("Invalid input. Please enter numeric values for total supply and burned percentage.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
