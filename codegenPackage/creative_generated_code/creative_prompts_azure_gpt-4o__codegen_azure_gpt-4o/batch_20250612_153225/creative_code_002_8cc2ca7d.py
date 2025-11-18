"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Create a Python script that categorizes DBT therapy groups into children (4-12 years), adolescents (12-18 years), and adults (18+ years), based on the age ranges specified on the Mente Sana Psicología webpage.
Generated: DETERMINISTIC_8cc2ca7dd9ba4e61
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to categorize individuals into DBT therapy groups based on age.
Groups: 
- Children: 4-12 years
- Adolescents: 12-18 years
- Adults: 18+ years
"""

# Import necessary modules
import sys

def categorize_age(age):
    """
    Categorizes the given age into DBT therapy groups.
    
    Parameters:
        age (int): Age of the individual.
        
    Returns:
        str: The category (Children, Adolescents, Adults) or an error message.
    """
    try:
        # Validate that age is a positive integer
        if age < 0:
            return "Error: Age cannot be negative."
        elif 4 <= age < 12:
            return "Children group (4-12 years)"
        elif 12 <= age < 18:
            return "Adolescent group (12-18 years)"
        elif age >= 18:
            return "Adult group (18+ years)"
        else:
            return "Error: Age is out of range for DBT therapy groups."
    except Exception as e:
        return f"Error: An unexpected issue occurred - {str(e)}"


def main():
    """
    Main function to run the script.
    Prompts the user for input and displays the age category.
    """
    try:
        # Prompt user for age input
        age_input = input("Please enter the age of the individual: ")
        
        # Convert input to integer and handle invalid input
        try:
            age = int(age_input)
        except ValueError:
            print("Error: Age must be a valid integer.")
            sys.exit(1)
        
        # Categorize age and print result
        result = categorize_age(age)
        print(result)
    
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        sys.exit(0)


if __name__ == "__main__":
    # Entry point for the script
    main()
```
