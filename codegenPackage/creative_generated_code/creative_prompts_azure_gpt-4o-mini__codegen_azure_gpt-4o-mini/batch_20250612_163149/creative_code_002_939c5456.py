"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wynn-seven.vercel.app
Prompt: Generate a function that calculates potential earnings based on user engagement and multipliers for a rewards program similar to $WYNN Hunt.
Generated: DETERMINISTIC_939c5456d4c25e7c
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_potential_earnings(user_engagement, base_multiplier=1.0, engagement_multiplier=1.0):
    """
    Calculate potential earnings based on user engagement and multipliers.

    Parameters:
        user_engagement (float): The level of user engagement, should be a non-negative value.
        base_multiplier (float, optional): A base multiplier for earnings, defaults to 1.0.
        engagement_multiplier (float, optional): A multiplier based on user engagement, defaults to 1.0.

    Returns:
        float: The calculated potential earnings.

    Raises:
        ValueError: If user_engagement is negative or if multipliers are not positive.
    """
    
    # Validate input parameters
    if user_engagement < 0:
        raise ValueError("User engagement must be a non-negative value.")
    if base_multiplier <= 0:
        raise ValueError("Base multiplier must be a positive value.")
    if engagement_multiplier <= 0:
        raise ValueError("Engagement multiplier must be a positive value.")

    # Calculate potential earnings
    potential_earnings = user_engagement * base_multiplier * engagement_multiplier

    return potential_earnings

# Example usage
if __name__ == "__main__":
    try:
        user_engagement = float(input("Enter user engagement level: "))
        base_multiplier = float(input("Enter base multiplier (default 1.0): ") or 1.0)
        engagement_multiplier = float(input("Enter engagement multiplier (default 1.0): ") or 1.0)
        
        earnings = calculate_potential_earnings(user_engagement, base_multiplier, engagement_multiplier)
        print(f"Potential earnings: ${earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
