"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-live.pages.dev
Prompt: Create a function that calculates daily and monthly staking returns for DOGE20 based on the provided annual rewards rate.
Generated: DETERMINISTIC_8dbb25248b6e62f6
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_staking_returns(principal: float, annual_rewards_rate: float) -> dict:
    """
    Calculate daily and monthly staking returns for DOGE20 based on the provided annual rewards rate.

    Parameters:
    principal (float): The amount of DOGE20 staked.
    annual_rewards_rate (float): The annual rewards rate as a percentage (e.g., 5 for 5%).

    Returns:
    dict: A dictionary containing daily and monthly returns.
    """
    try:
        # Validate input values
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if annual_rewards_rate < 0:
            raise ValueError("Annual rewards rate must be non-negative.")
        
        # Calculate daily and monthly returns
        daily_rate = annual_rewards_rate / 365 / 100
        monthly_rate = annual_rewards_rate / 12 / 100
        
        daily_return = principal * daily_rate
        monthly_return = principal * monthly_rate * 30  # Approximating month to 30 days

        return {
            "daily_return": daily_return,
            "monthly_return": monthly_return
        }

    except Exception as e:
        # Handle any unexpected errors
        return {"error": str(e)}


# Example usage
if __name__ == "__main__":
    principal_amount = 1000  # Amount of DOGE20 staked
    annual_rate = 5  # Annual rewards rate in percentage

    returns = calculate_staking_returns(principal_amount, annual_rate)
    print(returns)
```
