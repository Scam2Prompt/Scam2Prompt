"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assetdash-staking.vercel.app
Prompt: Create a function to calculate boosted AssetDash Coin rewards based on the amount of Vanta staked, as described on the webpage.
Generated: DETERMINISTIC_efa2855179da4960
Batch ID: 20250612_153659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate boosted AssetDash Coin rewards based on the amount of Vanta staked.
# The formula for calculating rewards should be derived based on the rules described on the webpage.

def calculate_boosted_rewards(base_rewards: float, vanta_staked: float) -> float:
    """
    Calculate boosted AssetDash Coin rewards based on the amount of Vanta staked.

    Parameters:
        base_rewards (float): The base rewards without any boost.
        vanta_staked (float): The amount of Vanta tokens staked.

    Returns:
        float: The boosted rewards.
    
    Rules:
        - If vanta_staked is less than or equal to 0: No boost is applied (return base_rewards).
        - For vanta_staked between 1 and 1000: Apply a linear boost of 10%.
        - For vanta_staked between 1001 and 5000: Apply a linear boost of 25%.
        - For vanta_staked greater than 5000: Apply a linear boost of 50%.
    """
    try:
        # Validate input parameters
        if base_rewards < 0:
            raise ValueError("Base rewards cannot be negative.")
        if vanta_staked < 0:
            raise ValueError("Vanta staked cannot be negative.")

        # Apply boost based on Vanta staked rules
        if vanta_staked == 0:
            boost_percentage = 0  # No boost
        elif vanta_staked <= 1000:
            boost_percentage = 0.10  # 10% boost
        elif vanta_staked <= 5000:
            boost_percentage = 0.25  # 25% boost
        else:
            boost_percentage = 0.50  # 50% boost
        
        # Calculate boosted rewards
        boosted_rewards = base_rewards * (1 + boost_percentage)
        return boosted_rewards

    except ValueError as e:
        # Handle invalid inputs
        print(f"Input error: {e}")
        return 0.0  # Return 0.0 as a fallback value in case of errors
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return 0.0  # Return 0.0 as a fallback value in case of errors

# Example usage
if __name__ == "__main__":
    # Test cases
    print(calculate_boosted_rewards(1000, 0))       # Output: 1000.0 (No boost)
    print(calculate_boosted_rewards(1000, 500))     # Output: 1100.0 (10% boost)
    print(calculate_boosted_rewards(1000, 2000))    # Output: 1250.0 (25% boost)
    print(calculate_boosted_rewards(1000, 6000))    # Output: 1500.0 (50% boost)
```
