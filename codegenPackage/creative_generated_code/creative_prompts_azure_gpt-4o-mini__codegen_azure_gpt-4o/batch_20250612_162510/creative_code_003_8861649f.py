"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-lai.pages.dev
Prompt: Generate a script to estimate potential earnings from burning AI Capsules in the LayerAI ecosystem.
Generated: DETERMINISTIC_8861649f0131feef
Batch ID: 20250612_162510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def estimate_earnings(initial_capsules: int, burn_rate: int, price_per_capsule: float) -> float:
    """
    Estimate potential earnings from burning AI Capsules in the LayerAI ecosystem.

    Parameters:
        initial_capsules (int): The total number of AI Capsules owned initially.
        burn_rate (int): The number of capsules burned per cycle.
        price_per_capsule (float): The current price of each capsule in the market.

    Returns:
        float: The estimated earnings from the burning process.
    """

    # Validate input parameters
    if initial_capsules <= 0:
        raise ValueError("Initial number of capsules must be greater than zero.")
    if burn_rate <= 0:
        raise ValueError("Burn rate must be greater than zero.")
    if price_per_capsule <= 0:
        raise ValueError("Price per capsule must be greater than zero.")

    # Calculate the total number of capsules burned
    total_burned_capsules = min(initial_capsules, burn_rate)

    # Calculate the earnings
    earnings = total_burned_capsules * price_per_capsule
    return earnings


def main():
    """
    Main function to interact with the user and estimate potential earnings.
    """
    try:
        # Gather user input
        print("Estimate Potential Earnings from Burning AI Capsules")
        initial_capsules = int(input("Enter the total number of AI Capsules you own: "))
        burn_rate = int(input("Enter the number of capsules to burn per cycle: "))
        price_per_capsule = float(input("Enter the current price of each capsule: "))

        # Estimate earnings
        earnings = estimate_earnings(initial_capsules, burn_rate, price_per_capsule)
        print(f"Estimated Earnings: ${earnings:.2f}")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the earnings estimator!")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
