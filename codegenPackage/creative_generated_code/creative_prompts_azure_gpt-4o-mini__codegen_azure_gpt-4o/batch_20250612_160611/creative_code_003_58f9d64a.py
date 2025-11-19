"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdwin.lat
Prompt: Generate a script that calculates potential rewards based on participation in the USDT Reward Program.
Generated: DETERMINISTIC_58f9d64ad42133a0
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_rewards(participation_amount, reward_rate, duration, currency='USDT'):
    """
    Calculate potential rewards based on participation in the USDT Reward Program.

    Parameters:
        participation_amount (float): The amount of participation in the program.
        reward_rate (float): The annual reward rate (as a percentage).
        duration (int): The duration of participation in the program in months.
        currency (str): The currency for rewards, default is 'USDT'.

    Returns:
        float: The calculated reward.
    """
    try:
        # Validate input parameters
        if participation_amount <= 0:
            raise ValueError("Participation amount must be greater than 0.")
        if reward_rate < 0 or reward_rate > 100:
            raise ValueError("Reward rate must be between 0% and 100%.")
        if duration < 0:
            raise ValueError("Duration must be a positive integer.")

        # Convert annual reward rate to monthly rate (percentage to decimal)
        monthly_rate = reward_rate / 100 / 12

        # Calculate reward
        reward = participation_amount * monthly_rate * duration

        return round(reward, 2)

    except ValueError as ve:
        print(f"Value Error: {ve}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """
    Main function to interact with the user and calculate USDT rewards.
    """
    try:
        print("Welcome to the USDT Reward Program Calculator!")

        # Input data from user
        participation_amount = float(input("Enter your participation amount (in USDT): "))
        reward_rate = float(input("Enter the annual reward rate (in %): "))
        duration = int(input("Enter the duration of participation (in months): "))

        # Calculate rewards
        rewards = calculate_rewards(participation_amount, reward_rate, duration)
        
        # Display results
        print(f"\nYour potential rewards after {duration} months: {rewards} USDT")
    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error occurred during execution: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
