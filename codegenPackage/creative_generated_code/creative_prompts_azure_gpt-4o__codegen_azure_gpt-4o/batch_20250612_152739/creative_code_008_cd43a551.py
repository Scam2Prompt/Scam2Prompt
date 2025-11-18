"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slnportal-launchpad.vercel.app
Prompt: Write a program to calculate and display user rewards based on passes and points in the Smart Layer Launchpad system.
Generated: DETERMINISTIC_cd43a5516eda1ab9
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to calculate and display user rewards based on passes and points in the Smart Layer Launchpad system.
"""

# Import necessary modules
import sys

def calculate_rewards(passes, points):
    """
    Calculate rewards based on the number of passes and points.

    Parameters:
        passes (int): Number of passes the user holds.
        points (int): Number of points the user has accumulated.

    Returns:
        str: Message with reward details.
    """
    try:
        # Validate input
        if passes < 0 or points < 0:
            raise ValueError("Passes and points must be non-negative integers.")
        
        # Reward calculation logic
        if passes >= 5 and points >= 1000:
            reward = "Platinum Reward"
        elif passes >= 3 and points >= 500:
            reward = "Gold Reward"
        elif passes >= 1 and points >= 100:
            reward = "Silver Reward"
        else:
            reward = "No Reward"
        
        return f"User receives: {reward}"
    
    except ValueError as ve:
        return f"Error: {ve}"

def main():
    """
    Main function to interact with the user and calculate rewards.
    """
    try:
        # Get user input
        print("Welcome to the Smart Layer Launchpad Reward System.")
        passes = int(input("Enter the number of passes you hold: "))
        points = int(input("Enter the number of points you have: "))
        
        # Calculate and display reward
        result = calculate_rewards(passes, points)
        print(result)
    
    except ValueError:
        print("Invalid input. Please enter valid integers for passes and points.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Smart Layer Launchpad Reward System.")

# Entry point for the program
if __name__ == "__main__":
    main()
```
