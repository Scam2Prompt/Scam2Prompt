"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-en.web.app
Prompt: Develop a Python script to calculate the rewards pool distribution for $QUBE token staking, based on the 5% sell tax described in InQubeta's tokenomics.
Generated: DETERMINISTIC_419109d16e3ce6f9
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_rewards_pool_distribution(total_sell_volume):
    """
    Function to calculate the rewards pool distribution based on a 5% sell tax.
    
    Parameters:
    total_sell_volume (float): The total sell volume of $QUBE tokens in USD.

    Returns:
    float: The amount allocated to the rewards pool in USD.
    """
    try:
        # Validate input
        if not isinstance(total_sell_volume, (int, float)) or total_sell_volume < 0:
            raise ValueError("Total sell volume must be a non-negative number.")

        # Define the sell tax percentage
        SELL_TAX_PERCENTAGE = 5

        # Calculate the rewards pool distribution (5% of the total sell volume)
        rewards_pool_amount = (SELL_TAX_PERCENTAGE / 100) * total_sell_volume

        return rewards_pool_amount

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to demonstrate rewards pool calculation.
    """
    try:
        # Prompt user for input
        user_input = input("Enter the total sell volume of $QUBE tokens in USD: ")

        # Convert user input to a float
        total_sell_volume = float(user_input)

        # Calculate rewards pool distribution
        rewards_pool_amount = calculate_rewards_pool_distribution(total_sell_volume)

        # Display the result
        print(f"The rewards pool allocation from a sell volume of ${total_sell_volume:.2f} is ${rewards_pool_amount:.2f}.")
    
    except ValueError:
        print("Please enter a valid numeric value for the total sell volume.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```
