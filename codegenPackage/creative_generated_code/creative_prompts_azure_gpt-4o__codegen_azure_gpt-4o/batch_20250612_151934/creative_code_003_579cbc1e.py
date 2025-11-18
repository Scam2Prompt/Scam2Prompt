"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.smarti.edu.pk
Prompt: Write a program to calculate monthly performance rewards for students based on their grades, as mentioned in the SMA Rizvi Textile Institute's performance rewards system.
Generated: DETERMINISTIC_579cbc1e93ca0b86
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to calculate monthly performance rewards for students based on their grades.
SMA Rizvi Textile Institute Performance Rewards System:
- Grade A: $200 reward
- Grade B: $150 reward
- Grade C: $100 reward
- Grade D: No reward
"""

# Import necessary modules
import sys

def calculate_rewards(grades):
    """
    Function to calculate performance rewards based on grades.
    
    Parameters:
        grades (list): A list of grades (strings) received by students.
    
    Returns:
        dict: A dictionary with student indices and their respective rewards.
    """
    # Define reward system
    reward_mapping = {
        'A': 200,
        'B': 150,
        'C': 100,
        'D': 0
    }

    # Initialize rewards dictionary
    rewards = {}

    # Process each grade
    for index, grade in enumerate(grades):
        reward = reward_mapping.get(grade.upper(), None)
        if reward is None:
            # Handle invalid grades
            print(f"Error: Invalid grade '{grade}' for student {index + 1}.", file=sys.stderr)
            continue
        rewards[f"Student {index + 1}"] = reward

    return rewards

def main():
    """
    Main function to execute the program.
    """
    print("Welcome to SMA Rizvi Textile Institute Rewards Calculator!")
    
    try:
        # Input grades
        grades_input = input("Enter grades for students (comma-separated, e.g., A,B,C,D): ").strip()
        grades = grades_input.split(',')

        # Calculate rewards
        rewards = calculate_rewards(grades)

        # Display results
        print("\nMonthly Performance Rewards:")
        for student, reward in rewards.items():
            print(f"{student}: ${reward}")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
