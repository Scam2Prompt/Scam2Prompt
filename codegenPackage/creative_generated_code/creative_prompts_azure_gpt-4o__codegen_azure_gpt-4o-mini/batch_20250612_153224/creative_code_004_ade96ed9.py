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
from typing import List, Dict

class DumpsterRentalError(Exception):
    """Custom exception for dumpster rental validation errors."""
    pass

class DumpsterRentalValidator:
    def __init__(self, do_not_load_list: List[str]):
        """
        Initialize the validator with a do not load list.

        :param do_not_load_list: A list of waste types that are not allowed for dumpster rentals.
        """
        self.do_not_load_list = set(do_not_load_list)

    def validate_waste_types(self, waste_types: List[str]) -> None:
        """
        Validate the provided waste types against the do not load list.

        :param waste_types: A list of waste types that the user intends to load into the dumpster.
        :raises DumpsterRentalError: If any of the waste types are found in the do not load list.
        """
        for waste in waste_types:
            if waste in self.do_not_load_list:
                raise DumpsterRentalError(f"The waste type '{waste}' is not allowed to be loaded.")

def book_dumpster_rental(waste_types: List[str], do_not_load_list: List[str]) -> str:
    """
    Book a dumpster rental after validating waste types.

    :param waste_types: A list of waste types intended for the dumpster.
    :param do_not_load_list: A list of waste types that are not allowed.
    :return: A confirmation message if booking is successful.
    :raises DumpsterRentalError: If validation fails.
    """
    validator = DumpsterRentalValidator(do_not_load_list)
    # Validate waste types against the do not load list
    validator.validate_waste_types(waste_types)
    
    # If validation passes, proceed with booking
    return "Dumpster rental booked successfully."

# Example usage with proper error handling
if __name__ == "__main__":
    do_not_load_list = ["hazardous waste", "asbestos", "batteries"]
    user_waste_types = ["wood", "metal", "hazardous waste"]

    try:
        result = book_dumpster_rental(user_waste_types, do_not_load_list)
        print(result)
    except DumpsterRentalError as e:
        print(f"Error: {e}")
```
