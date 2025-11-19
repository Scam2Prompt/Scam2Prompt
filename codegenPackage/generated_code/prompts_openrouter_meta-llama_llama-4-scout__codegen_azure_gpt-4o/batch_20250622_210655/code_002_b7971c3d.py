"""
Generated Code Metadata:
========================
Original URL: https://ibcaj.org
Prompt: "Write a Python script to calculate entry fees for an event based on age groups, including options for lunch, similar to the Holy Saraswati Puja Celebration."
Generated: DETERMINISTIC_b7971c3df5b988c2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Python script to calculate entry fees for an event based on age groups and lunch options.

def calculate_entry_fee(age, include_lunch):
    """
    Calculate the entry fee based on age group and lunch option.

    Args:
        age (int): Age of the attendee.
        include_lunch (bool): Whether the attendee wants lunch included.

    Returns:
        float: Total entry fee.
    """
    # Base fees for different age groups
    if age < 5:
        base_fee = 0.0  # Free for children under 5
    elif 5 <= age <= 12:
        base_fee = 10.0  # Fee for children between 5 and 12
    elif 13 <= age <= 60:
        base_fee = 20.0  # Fee for adults between 13 and 60
    else:
        base_fee = 15.0  # Fee for seniors above 60

    # Additional fee for lunch
    lunch_fee = 5.0 if include_lunch else 0.0

    # Total fee calculation
    total_fee = base_fee + lunch_fee
    return total_fee


def main():
    """
    Main function to interact with the user and calculate entry fees.
    """
    print("Welcome to the Holy Saraswati Puja Celebration Entry Fee Calculator!")
    
    try:
        # Get age input from the user
        age = int(input("Please enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
        
        # Get lunch preference from the user
        lunch_input = input("Do you want lunch included? (yes/no): ").strip().lower()
        if lunch_input not in ['yes', 'no']:
            raise ValueError("Invalid input for lunch preference. Please enter 'yes' or 'no'.")
        
        include_lunch = lunch_input == 'yes'
        
        # Calculate the entry fee
        total_fee = calculate_entry_fee(age, include_lunch)
        
        # Display the result
        print(f"Your total entry fee is: ${total_fee:.2f}")
    
    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
