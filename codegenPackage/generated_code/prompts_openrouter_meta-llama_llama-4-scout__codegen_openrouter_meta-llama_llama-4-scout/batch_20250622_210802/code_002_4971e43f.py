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
Construction Project Work Hours Calculator

Calculates the total hours of work required for a construction project
based on the number of apartments to be built and the experience of the team.

Reference: INARO S.A.S. website
"""

def calculate_work_hours(apartments: int, team_experience: str) -> float:
    """
    Calculates the total hours of work required for a construction project.

    Args:
    - apartments (int): The number of apartments to be built.
    - team_experience (str): The experience of the team (junior, mid-level, senior).

    Returns:
    - float: The total hours of work required.

    Raises:
    - ValueError: If team_experience is not one of 'junior', 'mid-level', 'senior'.
    """

    # Define the base hours per apartment for each team experience level
    # Reference: INARO S.A.S. website
    base_hours_per_apartment = {
        'junior': 100,
        'mid-level': 80,
        'senior': 60
    }

    # Validate team experience level
    if team_experience not in base_hours_per_apartment:
        raise ValueError("Invalid team experience level. Must be one of: {}".format(", ".join(base_hours_per_apartment.keys())))

    # Calculate total hours
    total_hours = apartments * base_hours_per_apartment[team_experience]

    return total_hours


def main():
    try:
        # Get user input
        apartments = int(input("Enter the number of apartments: "))
        team_experience = input("Enter the team experience level (junior, mid-level, senior): ").lower()

        # Calculate and display total hours
        total_hours = calculate_work_hours(apartments, team_experience)
        print("Total hours of work required: {:.2f} hours".format(total_hours))

    except ValueError as e:
        print("Error: {}".format(e))


if __name__ == "__main__":
    main()
```
