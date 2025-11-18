"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkrewards-6st.pages.dev
Prompt: Create a program that calculates the total weight of locked $BONK tokens based on user input and displays the impact on the rewards pool percentage as described on the Bonk Rewards page.
Generated: DETERMINISTIC_a939597a94b9e310
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_total_weight_and_rewards():
    """
    Calculates the total weight of locked $BONK tokens based on user input and 
    displays the impact on the rewards pool percentage.
    """

    try:
        # Prompt user for the number of locked $BONK tokens
        locked_tokens = float(input("Enter the number of locked $BONK tokens: "))
        
        if locked_tokens < 0:
            print("Error: Locked tokens cannot be negative.")
            return

        # Prompt user for the total rewards pool weight
        rewards_pool_weight = float(input("Enter the current total rewards pool weight: "))
        
        if rewards_pool_weight <= 0:
            print("Error: Rewards pool weight must be greater than zero.")
            return

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        return

    # Define weight calculation logic (example: weight = locked tokens * multiplier)
    multiplier = 0.5  # Hypothetical multiplier for calculating weight
    total_weight_of_locked_tokens = locked_tokens * multiplier

    # Calculate impact on rewards pool percentage
    impact_percentage = (total_weight_of_locked_tokens / rewards_pool_weight) * 100

    # Display results
    print("\nResults:")
    print(f"Total Weight of Locked $BONK Tokens: {total_weight_of_locked_tokens:.2f}")
    print(f"Impact on Rewards Pool Percentage: {impact_percentage:.2f}%")

if __name__ == "__main__":
    try:
        calculate_total_weight_and_rewards()
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
```
