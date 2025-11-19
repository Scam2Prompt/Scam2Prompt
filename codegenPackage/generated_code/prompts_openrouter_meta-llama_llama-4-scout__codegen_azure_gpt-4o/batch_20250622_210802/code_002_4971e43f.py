"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: "Write a Python script to calculate the total hours of work required for a construction project, given the number of apartments to be built and the experience of the team, as mentioned in the INARO S.A.S. website."
Generated: DETERMINISTIC_4971e43f3f64698b
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the total hours of work required for a construction project.
The calculation is based on the number of apartments to be built and the experience level of the team.

Inputs:
- Number of apartments to be built
- Experience level of the team (e.g., 'novice', 'intermediate', 'expert')

Outputs:
- Total hours of work required

Author: [Your Name]
Date: [Insert Date]
"""

def calculate_work_hours(apartments, experience_level):
    """
    Calculate the total hours of work required for the construction project.

    Parameters:
        apartments (int): Number of apartments to be built.
        experience_level (str): Experience level of the team ('novice', 'intermediate', 'expert').

    Returns:
        float: Total hours of work required.

    Raises:
        ValueError: If the experience level is invalid or apartments is not a positive integer.
    """
    # Define work hours per apartment based on experience level
    work_hours_per_apartment = {
        'novice': 120,       # Novice team requires 120 hours per apartment
        'intermediate': 90,  # Intermediate team requires 90 hours per apartment
        'expert': 70         # Expert team requires 70 hours per apartment
    }

    # Validate inputs
    if not isinstance(apartments, int) or apartments <= 0:
        raise ValueError("Number of apartments must be a positive integer.")
    if experience_level not in work_hours_per_apartment:
        raise ValueError("Invalid experience level. Choose from 'novice', 'intermediate', or 'expert'.")

    # Calculate total hours
    total_hours = apartments * work_hours_per_apartment[experience_level]
    return total_hours


def main():
    """
    Main function to interact with the user and calculate work hours.
    """
    try:
        # Get user input
        print("Welcome to the Construction Work Hours Calculator!")
        apartments = int(input("Enter the number of apartments to be built: "))
        experience_level = input("Enter the experience level of the team (novice, intermediate, expert): ").strip().lower()

        # Calculate total hours
        total_hours = calculate_work_hours(apartments, experience_level)

        # Display the result
        print(f"\nTotal hours of work required: {total_hours} hours")
    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
