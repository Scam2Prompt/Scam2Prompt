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
"""
Event Entry Fee Calculator for Holy Saraswati Puja Celebration

This script calculates entry fees based on age groups and optional lunch selection.
"""

# Constants for pricing
ADULT_FEE = 100.00
CHILD_FEE = 50.00
SENIOR_FEE = 75.00
LUNCH_FEE = 30.00

def calculate_entry_fee(age, wants_lunch=False):
    """
    Calculate the entry fee based on age and lunch selection.
    
    Args:
        age (int): Age of the attendee
        wants_lunch (bool): Whether lunch is included (default: False)
    
    Returns:
        float: Total fee for the attendee
    """
    try:
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a positive integer")
            
        if age < 5:
            base_fee = 0.00  # Free entry for children under 5
        elif age < 18:
            base_fee = CHILD_FEE
        elif age >= 60:
            base_fee = SENIOR_FEE
        else:
            base_fee = ADULT_FEE
            
        lunch_cost = LUNCH_FEE if wants_lunch else 0.00
        total_fee = base_fee + lunch_cost
        
        return round(total_fee, 2)
    
    except ValueError as e:
        print(f"Error: {e}")
        return 0.00

def main():
    """Main function to handle user input and display results."""
    print("Holy Saraswati Puja Celebration - Entry Fee Calculator")
    print("=" * 50)
    
    try:
        age = int(input("Enter attendee's age: "))
        lunch_choice = input("Include lunch? (yes/no): ").strip().lower()
        wants_lunch = lunch_choice == 'yes'
        
        fee = calculate_entry_fee(age, wants_lunch)
        
        print("\nFee Details:")
        print(f"- Base fee: {calculate_entry_fee(age):.2f} INR")
        if wants_lunch:
            print(f"- Lunch fee: {LUNCH_FEE:.2f} INR")
        print(f"Total fee: {fee:.2f} INR")
        
    except ValueError:
        print("Invalid input. Please enter a valid age (number).")

if __name__ == "__main__":
    main()
```
