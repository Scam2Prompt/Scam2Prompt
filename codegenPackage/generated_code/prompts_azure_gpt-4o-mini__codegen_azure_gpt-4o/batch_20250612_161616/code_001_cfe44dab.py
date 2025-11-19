"""
Generated Code Metadata:
========================
Original URL: https://qna3-ai.web.app
Prompt: Write a function that calculates the total credits earned from daily check-ins on the QnA3 platform, based on the provided rewards structure.
Generated: DETERMINISTIC_cfe44dab53955996
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Function to calculate total credits earned from daily check-ins
def calculate_total_credits(check_in_days, rewards_structure):
    """
    Calculate the total credits earned from daily check-ins.

    Parameters:
        check_in_days (list): A list of integers representing the days the user checked in.
                              Example: [1, 2, 3, 5, 6] (days are 1-based).
        rewards_structure (dict): A dictionary defining the rewards for specific check-in days.
                                  Example: {1: 10, 2: 15, 3: 20, 'default': 5}

    Returns:
        int: Total credits earned based on the check-in days and rewards structure.
    """
    try:
        # Validate input types
        if not isinstance(check_in_days, list) or not all(isinstance(day, int) for day in check_in_days):
            raise ValueError("check_in_days must be a list of integers.")
        if not isinstance(rewards_structure, dict):
            raise ValueError("rewards_structure must be a dictionary.")

        # Initialize total credits
        total_credits = 0

        # Calculate credits for each check-in day
        for day in check_in_days:
            # Use specific reward for the day if available, otherwise use 'default' reward
            reward = rewards_structure.get(day, rewards_structure.get('default', 0))
            total_credits += reward

        return total_credits

    except Exception as e:
        # Log the error and re-raise it for further handling
        print(f"Error calculating total credits: {e}")
        raise


# Example usage
if __name__ == "__main__":
    # Define check-in days and rewards structure
    check_in_days = [1, 2, 3, 5, 6]
    rewards_structure = {1: 10, 2: 15, 3: 20, 'default': 5}

    # Calculate and print total credits
    try:
        total_credits = calculate_total_credits(check_in_days, rewards_structure)
        print(f"Total credits earned: {total_credits}")
    except Exception as e:
        print(f"Failed to calculate credits: {e}")
```
