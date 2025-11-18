"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toolfix.online
Prompt: Write a code snippet to validate and check MICR codes for cheque verification, as outlined in the MICR Code Checker tool on the IFSC Finder site.
Generated: DETERMINISTIC_9d35a732de3295be
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_micr_code(micr_code):
    """
    Validates the given MICR code based on standard MICR specifications.
    
    MICR code is a 9-digit numeric code used for cheque processing. 
    The format is as follows:
       - The first 3 digits represent the city (related to the PIN code of the area).
       - The next 3 digits represent the bank code.
       - The last 3 digits represent the branch code.
    
    Args:
        micr_code (str): The MICR code to validate.
    
    Returns:
        bool: True if the MICR code is valid, False otherwise.
    """
    # Check if the MICR code is exactly 9 digits long and numeric
    micr_pattern = re.compile(r"^\d{9}$")
    if not micr_pattern.match(micr_code):
        return False
    
    # Additional validation could be added here if specific bank/city/branch patterns are required
    
    return True

def main():
    """
    Main function to test MICR code validation.
    """
    try:
        # Sample MICR codes for testing
        sample_codes = [
            "123456789",  # Valid MICR code
            "12345",      # Invalid MICR code (too short)
            "12345678A",  # Invalid MICR code (contains non-numeric character)
            "987654321"   # Valid MICR code
        ]
        
        for code in sample_codes:
            if validate_micr_code(code):
                print(f"MICR Code '{code}' is valid.")
            else:
                print(f"MICR Code '{code}' is invalid.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
