"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Create a Python script that categorizes DBT therapy groups into children (4-12 years), adolescents (12-18 years), and adults (18+ years), based on the age ranges specified on the Mente Sana Psicología webpage.
Generated: DETERMINISTIC_8cc2ca7dd9ba4e61
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
DBT Therapy Group Categorizer

This script categorizes DBT therapy groups into children (4-12 years), 
adolescents (12-18 years), and adults (18+ years) based on the age ranges 
specified on the Mente Sana Psicología webpage.

Author: [Your Name]
Date: [Today's Date]
"""

def categorize_dbt_group(age: int) -> str:
    """
    Categorize a DBT therapy group based on the age.

    Args:
    age (int): The age of the individual.

    Returns:
    str: The category of the DBT therapy group.

    Raises:
    ValueError: If the age is not a positive integer.
    """

    # Check if age is a positive integer
    if not isinstance(age, int) or age <= 0:
        raise ValueError("Age must be a positive integer.")

    # Define age ranges for each category
    if 4 <= age <= 12: 
        # Children (4-12 years)
        return "children"
    elif 12 < age <= 18: 
        # Adolescents (12-18 years)
        return "adolescents"
    elif age > 18: 
        # Adults (18+ years)
        return "adults"
    else: 
        # Age is below 4, return an appropriate message
        return "Not eligible for DBT therapy group"


def main():
    try:
        # Example usage
        ages = [10, 15, 25, 3, -5, "twenty"]
        
        for age in ages:
            try:
                age = int(age)
                category = categorize_dbt_group(age)
                print(f"Age: {age}, Category: {category}")
            except ValueError as e:
                print(f"Age: {age}, Error: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
