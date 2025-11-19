"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playland.co.ke
Prompt: Generate a Python script to calculate the total cost for a family visiting Playland Kenya, including entry fees for the trampoline park, bowling, and virtual reality sessions.
Generated: DETERMINISTIC_8b36a5b8d016e388
Batch ID: 20250612_162544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the total cost for a family visiting Playland Kenya.
Includes entry fees for trampoline park, bowling, and virtual reality (VR) sessions.
"""

# Constants for pricing
TRAMPOLINE_COST_PER_PERSON = 500  # Kenyan Shillings
BOWLING_COST_PER_PERSON = 700    # Kenyan Shillings
VR_COST_PER_PERSON = 800         # Kenyan Shillings

def calculate_total_cost(family_members, trampoline_count, bowling_count, vr_count):
    """
    Calculate the total cost for a family visiting Playland.

    Args:
        family_members (int): Total number of family members.
        trampoline_count (int): Number of family members participating in trampoline park.
        bowling_count (int): Number of family members participating in bowling.
        vr_count (int): Number of family members participating in virtual reality sessions.

    Returns:
        int: Total cost in Kenyan Shillings.
    """
    if family_members < 0 or trampoline_count < 0 or bowling_count < 0 or vr_count < 0:
        raise ValueError("Counts cannot be negative.")
    if trampoline_count > family_members or bowling_count > family_members or vr_count > family_members:
        raise ValueError("Activity counts cannot exceed total family members.")

    # Calculate costs for each activity
    trampoline_cost = trampoline_count * TRAMPOLINE_COST_PER_PERSON
    bowling_cost = bowling_count * BOWLING_COST_PER_PERSON
    vr_cost = vr_count * VR_COST_PER_PERSON

    # Calculate total cost
    total_cost = trampoline_cost + bowling_cost + vr_cost
    
    return total_cost

def main():
    """
    Main function to prompt user for input and calculate the total cost.
    """
    try:
        # Get user inputs
        family_members = int(input("Enter the total number of family members: "))
        trampoline_count = int(input("Enter the number of family members participating in trampoline park: "))
        bowling_count = int(input("Enter the number of family members participating in bowling: "))
        vr_count = int(input("Enter the number of family members participating in virtual reality sessions: "))
        
        # Calculate the total cost
        total_cost = calculate_total_cost(family_members, trampoline_count, bowling_count, vr_count)
        
        # Display the result
        print(f"The total cost for the family is: {total_cost} Kenyan Shillings")
    
    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
```
