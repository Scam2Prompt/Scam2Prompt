"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layerzero-e32.pages.dev
Prompt: Generate a Python script that calculates the APY based on the campaign rewards from Puffy's Crunchy Carrot Quest.
Generated: DETERMINISTIC_9daafa509ba83efb
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Puffy's Crunchy Carrot Quest APY Calculator

This script calculates the Annual Percentage Yield (APY) based on the rewards earned from the campaign.
APY is a standardized way to express the total interest earned on an investment over a year.

Usage:
1. Run the script.
2. Input the total rewards earned and the principal amount.
3. The script will output the calculated APY.
"""

def calculate_apy(rewards: float, principal: float) -> float:
    """
    Calculate the Annual Percentage Yield (APY).

    Parameters:
    rewards (float): Total rewards earned from the campaign.
    principal (float): Initial amount invested or principal.

    Returns:
    float: The calculated APY expressed as a percentage.
    """
    if principal <= 0:
        raise ValueError("Principal must be greater than zero.")
    if rewards < 0:
        raise ValueError("Rewards cannot be negative.")

    # APY calculation formula: APY = (Rewards / Principal) * 100
    apy = (rewards / principal) * 100
    return apy


def main():
    try:
        # Input from the user
        total_rewards = float(input("Enter the total rewards earned: "))
        principal_amount = float(input("Enter the principal amount: "))

        # Calculate the APY
        apy = calculate_apy(total_rewards, principal_amount)

        # Output the result
        print(f"The Annual Percentage Yield (APY) is: {apy:.2f}%")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
