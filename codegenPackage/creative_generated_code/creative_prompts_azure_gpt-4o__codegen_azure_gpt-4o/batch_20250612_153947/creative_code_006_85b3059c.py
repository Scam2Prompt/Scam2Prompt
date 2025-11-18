"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tunfush-airdrop.pages.dev
Prompt: Write code to calculate the market cap of the Tanfush (Tan) token and display progress toward key milestones, such as $76,869 for bonding curve graduation and $37,142 for "king of the hill."
Generated: DETERMINISTIC_85b3059cd3135321
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the market cap of the Tanfush (Tan) token and display progress toward key milestones.
The script defines key milestones and calculates progress toward each based on the current market cap.
"""

# Import necessary modules
import sys


def calculate_market_cap(current_price, circulating_supply):
    """
    Calculate the market cap of the Tan token.

    :param current_price: Current price of the token (float)
    :param circulating_supply: Total circulating supply of the token (integer)
    :return: Market capitalization (float)
    """
    try:
        # Ensure inputs are valid
        if current_price < 0 or circulating_supply < 0:
            raise ValueError("Price and supply must be non-negative.")

        # Calculate market cap
        return current_price * circulating_supply

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)


def display_progress(market_cap, milestones):
    """
    Display progress toward key milestones.

    :param market_cap: Current market cap of the token (float)
    :param milestones: Dictionary with milestone names and values (dict)
    :return: None
    """
    try:
        print(f"Current Market Cap: ${market_cap:,.2f}\n")

        for milestone_name, milestone_value in milestones.items():
            # Calculate progress percentage
            progress_percentage = min((market_cap / milestone_value) * 100, 100.0)
            status = "Reached" if market_cap >= milestone_value else "In Progress"

            # Display milestone status
            print(f"Milestone: {milestone_name}")
            print(f"  Target Value: ${milestone_value:,.2f}")
            print(f"  Progress: {progress_percentage:.2f}% ({status})\n")

    except Exception as e:
        print(f"An error occurred while displaying progress: {e}")
        sys.exit(1)


def main():
    """
    Main function to handle user input and display results.

    :return: None
    """
    try:
        # Define milestones
        milestones = {
            "Bonding Curve Graduation": 76869,
            "King of the Hill": 37142,
        }

        # Prompt user for input
        current_price = float(input("Enter current price of Tan token ($): "))
        circulating_supply = int(input("Enter circulating supply of Tan token: "))

        # Calculate market cap
        market_cap = calculate_market_cap(current_price, circulating_supply)

        # Display progress toward milestones
        display_progress(market_cap, milestones)

    except ValueError:
        print("Invalid input. Please enter numeric values for price and supply.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the main function
if __name__ == "__main__":
    main()
```
