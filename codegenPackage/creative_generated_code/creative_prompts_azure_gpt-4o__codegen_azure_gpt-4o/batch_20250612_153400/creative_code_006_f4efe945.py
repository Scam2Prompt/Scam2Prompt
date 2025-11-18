"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cokiessnew.pages.dev
Prompt: Write a program to calculate the total points for a user by summing their community points, referral points, and ecosystem points, as per the Cookie Community scoring system.
Generated: DETERMINISTIC_f4efe945dfbca2d3
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate total points based on the Cookie Community scoring system.

def calculate_total_points(community_points, referral_points, ecosystem_points):
    """
    Calculate the total points by summing up community points, referral points, and ecosystem points.

    Args:
        community_points (int): Points earned from community activities.
        referral_points (int): Points earned from referrals.
        ecosystem_points (int): Points earned from ecosystem participation.

    Returns:
        int: Total points calculated.
    """
    try:
        # Ensure all inputs are valid integers
        if not all(isinstance(x, int) and x >= 0 for x in [community_points, referral_points, ecosystem_points]):
            raise ValueError("All point values must be non-negative integers.")
        
        # Calculate the total points
        total_points = community_points + referral_points + ecosystem_points
        
        return total_points
    except Exception as e:
        # Log the error and re-raise it
        print(f"Error calculating total points: {e}")
        raise


def main():
    """
    Main function to demonstrate the calculation of total points.
    """
    try:
        # Example user input for points
        community_points = int(input("Enter community points: "))
        referral_points = int(input("Enter referral points: "))
        ecosystem_points = int(input("Enter ecosystem points: "))

        # Calculate total points
        total_points = calculate_total_points(community_points, referral_points, ecosystem_points)
        
        # Display the result
        print(f"Total Points: {total_points}")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Run the main function
    main()
```
