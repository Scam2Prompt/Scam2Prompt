"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.purpledumpster.ca
Prompt: Write a function to validate waste types against the "Do Not Load List" provided by Purple Dumpster before allowing users to book a dumpster rental.
Generated: DETERMINISTIC_ade96ed9b4f12e63
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Waste Type Validation for Dumpster Rental Booking

This module contains a function to validate waste types against the "Do Not Load List"
provided by Purple Dumpster before allowing users to book a dumpster rental.
"""

def validate_waste_types(user_waste_types, do_not_load_list):
    """
    Validates waste types against the "Do Not Load List".

    Parameters:
        user_waste_types (list): A list of waste types provided by the user.
        do_not_load_list (list): A list of waste types not allowed by Purple Dumpster.

    Returns:
        tuple: A boolean indicating whether the waste types are valid,
               and a list of invalid waste types if any are found.

    Raises:
        ValueError: If the input parameters are not lists.
    """
    
    # Validate inputs
    if not isinstance(user_waste_types, list) or not isinstance(do_not_load_list, list):
        raise ValueError("Both user_waste_types and do_not_load_list must be lists.")
    
    # Find invalid waste types that are in the "Do Not Load List"
    invalid_waste_types = [waste for waste in user_waste_types if waste in do_not_load_list]

    # Return validation result
    return (len(invalid_waste_types) == 0, invalid_waste_types)


# Example Usage
if __name__ == "__main__":
    try:
        # Sample inputs
        user_waste_types = ["household garbage", "construction debris", "hazardous chemicals"]
        do_not_load_list = ["hazardous chemicals", "batteries", "paint"]

        # Validate the waste types
        is_valid, invalid_types = validate_waste_types(user_waste_types, do_not_load_list)

        if is_valid:
            print("Waste types are valid. You can proceed with booking.")
        else:
            print("Booking not allowed. Invalid waste types detected:")
            print(", ".join(invalid_types))
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
