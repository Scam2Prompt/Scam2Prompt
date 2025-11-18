"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinrush.bet
Prompt: Generate code for calculating rakeback rewards in a casino platform, ensuring accurate percentage-based payouts for users.
Generated: DETERMINISTIC_d3e7a17507a5b5f2
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rakeback_rewards.py
"""
This script calculates rakeback rewards for users on a casino platform.
Rakeback rewards are computed based on the user's total spend and a predefined rakeback percentage.
"""

def calculate_rakeback(total_spend: float, rakeback_percentage: float) -> float:
    """
    Calculate the rakeback reward for a user.

    Args:
        total_spend (float): The total amount spent by the user in the casino.
        rakeback_percentage (float): The percentage of rakeback to be applied.

    Returns:
        float: The rakeback reward amount.

    Raises:
        ValueError: If total_spend or rakeback_percentage is negative.
    """
    if total_spend < 0:
        raise ValueError("Total spend cannot be negative.")
    if rakeback_percentage < 0:
        raise ValueError("Rakeback percentage cannot be negative.")
    
    return total_spend * (rakeback_percentage / 100)

def main():
    """
    Main function to demonstrate rakeback reward calculation.
    """
    try:
        # Example inputs
        total_spend = float(input("Enter the total spend by the user: "))
        rakeback_percentage = float(input("Enter the rakeback percentage: "))
        
        # Calculate rakeback reward
        rakeback_reward = calculate_rakeback(total_spend, rakeback_percentage)
        
        print(f"Rakeback Reward: ${rakeback_reward:.2f}")
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
