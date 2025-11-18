"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hispanicservices.com
Prompt: Write code to validate and format Federal ID numbers for incorporation documents, as required for business startup services offered by Hispanic Services.
Generated: DETERMINISTIC_c884588403bf727d
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class FederalIDValidator:
    """
    A class to validate and format Federal ID numbers (EINs).
    """

    def __init__(self, federal_id: str):
        """
        Initializes the FederalIDValidator with a Federal ID.
        
        :param federal_id: The Federal ID number to validate and format.
        """
        self.federal_id = federal_id.strip()

    def is_valid(self) -> bool:
        """
        Validates the Federal ID number format.
        
        :return: True if valid, False otherwise.
        """
        # Federal ID must be in the format XX-XXXXXXX
        ein_pattern = r'^\d{2}-\d{7}$'
        is_valid = bool(re.match(ein_pattern, self.federal_id))
        return is_valid

    def format(self) -> str:
        """
        Formats the Federal ID number to the standard format.
        
        :return: Formatted Federal ID if valid, raises ValueError otherwise.
        :raises ValueError: If the Federal ID is not valid.
        """
        if not self.is_valid():
            raise ValueError(f"Invalid Federal ID number: {self.federal_id}")

        # Format Federal ID by ensuring it respects the XX-XXXXXXX format
        return self.federal_id

def main():
    """
    Main function to demonstrate Federal ID validation and formatting.
    """
    try:
        # Example Federal ID input
        input_federal_id = "12-3456789"
        validator = FederalIDValidator(input_federal_id)

        if validator.is_valid():
            formatted_id = validator.format()
            print(f"Valid Federal ID: {formatted_id}")
        else:
            print(f"Invalid Federal ID: {input_federal_id}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
