"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-is.pages.dev
Prompt: Write a Python script to calculate the APY for staking WienerAI tokens, given the current staking rewards and token supply.
Generated: DETERMINISTIC_783a5662499da394
Batch ID: 20250622_204551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_apy(
    annual_rewards: float,
    total_staked: float,
    decimals: int = 18
) -> float:
    """
    Calculate the Annual Percentage Yield (APY) for staking WienerAI tokens.

    Args:
        annual_rewards: Total annual rewards distributed (in tokens)
        total_staked: Total amount of tokens currently staked (in tokens)
        decimals: Number of decimal places for the token (default: 18)

    Returns:
        float: The calculated APY as a percentage

    Raises:
        ValueError: If total_staked is zero (division by zero)
    """
    if total_staked <= 0:
        raise ValueError("Total staked tokens must be greater than zero")
    
    # Calculate APY: (annual_rewards / total_staked) * 100
    apy = (annual_rewards / total_staked) * 100
    
    return apy

def main():
    try:
        # Example usage
        annual_rewards = float(input("Enter annual rewards (in tokens): "))
        total_staked = float(input("Enter total staked tokens: "))
        decimals = int(input("Enter token decimals (default 18): ") or 18)
        
        apy = calculate_apy(annual_rewards, total_staked, decimals)
        print(f"APY: {apy:.2f}%")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
