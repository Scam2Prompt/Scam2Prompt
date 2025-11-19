"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge20-claim.pages.dev
Prompt: Explain how to calculate monthly and daily staking rewards for DOGE20 using the provided annual returns percentage.
Generated: DETERMINISTIC_e579b650fd829de0
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Function to calculate monthly and daily staking rewards for DOGE20
# based on the annual percentage return (APR).

def calculate_staking_rewards(apr_percentage, staked_amount):
    """
    Calculate monthly and daily staking rewards based on annual percentage return (APR).

    Parameters:
        apr_percentage (float): The annual percentage return as a decimal (e.g., 12% = 0.12).
        staked_amount (float): The amount of DOGE20 tokens staked.

    Returns:
        dict: A dictionary containing the monthly and daily rewards.
    """
    try:
        # Validate that inputs are non-negative numbers
        if apr_percentage < 0 or staked_amount < 0:
            raise ValueError("APR percentage and staked amount must be non-negative.")

        # Calculate annual reward
        annual_reward = staked_amount * apr_percentage
        
        # Calculate monthly reward (12 months in a year)
        monthly_reward = annual_reward / 12
        
        # Calculate daily reward (365 days in a year)
        daily_reward = annual_reward / 365
        
        # Return results as a dictionary
        return {
            "monthly_reward": monthly_reward,
            "daily_reward": daily_reward
        }
    except TypeError as e:
        # Handle cases where inputs are not numbers
        raise TypeError("Both APR and staked amount must be numbers.") from e
    except Exception as e:
        # Catch unexpected errors
        raise RuntimeError("An unexpected error occurred while calculating rewards.") from e


# Example usage
if __name__ == "__main__":
    try:
        # Example inputs
        apr_percentage = 0.12  # 12% annual return
        staked_amount = 1000.0  # 1000 DOGE20 tokens staked

        # Calculate rewards
        rewards = calculate_staking_rewards(apr_percentage, staked_amount)

        # Display results
        print(f"Monthly Reward: {rewards['monthly_reward']:.2f} DOGE20")
        print(f"Daily Reward: {rewards['daily_reward']:.2f} DOGE20")
    except Exception as e:
        # Handle errors gracefully
        print(f"Error: {e}")
```
