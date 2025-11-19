"""
Generated Code Metadata:
========================
Original URL: https://mommymilestones.com
Prompt: Write a code snippet that generates a personalized message for a Mommaversary celebration based on user input.
Generated: DETERMINISTIC_15e28a5d72cf19de
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from datetime import datetime

def generate_mommaversary_message(name, child_name, years_as_mom):
    """
    Generates a personalized Mommaversary message.

    Parameters:
        name (str): The name of the mom.
        child_name (str): The name of the child.
        years_as_mom (int): The number of years the person has been a mom.

    Returns:
        str: A personalized Mommaversary message.
    """
    try:
        # Validate input types
        if not isinstance(name, str) or not isinstance(child_name, str) or not isinstance(years_as_mom, int):
            raise ValueError("Invalid input types. 'name' and 'child_name' must be strings, 'years_as_mom' must be an integer.")

        # Validate years_as_mom is non-negative
        if years_as_mom < 0:
            raise ValueError("'years_as_mom' must be a non-negative integer.")

        # Generate the message
        current_year = datetime.now().year
        message = (
            f"Happy Mommaversary, {name}!\n"
            f"Today, we celebrate {years_as_mom} wonderful years of being an amazing mom to {child_name}.\n"
            f"Thank you for all the love, care, and dedication you've shown since {current_year - years_as_mom}.\n"
            f"Here's to many more years of cherished memories and joy!"
        )
        return message

    except ValueError as ve:
        # Handle invalid input errors
        return f"Error: {ve}"

    except Exception as e:
        # Handle unexpected errors
        return f"An unexpected error occurred: {e}"


# Example usage
if __name__ == "__main__":
    # Gather user input
    try:
        mom_name = input("Enter the mom's name: ").strip()
        child_name = input("Enter the child's name: ").strip()
        years_as_mom = int(input("Enter the number of years as a mom: ").strip())

        # Generate and display the message
        message = generate_mommaversary_message(mom_name, child_name, years_as_mom)
        print("\n" + message)

    except ValueError:
        print("Invalid input. Please ensure the number of years is a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
