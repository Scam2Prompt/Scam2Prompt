"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://revokecashh.info
Prompt: Generate code to validate whether an IMEI number is blacklisted or has a bad ESN, and suggest how UnlockMaker's unblacklist tool could be integrated into the solution.
Generated: DETERMINISTIC_aa3affd14b99d96b
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_imei(imei):
    """
    Validates whether the given IMEI number is syntactically correct.
    IMEI must be 15 digits long and pass the Luhn algorithm check.
    
    Args:
        imei (str): IMEI number to validate.
    
    Returns:
        bool: True if the IMEI is valid, False otherwise.
    """
    # Check if IMEI is 15 digits
    if not re.match(r'^\d{15}$', imei):
        return False

    # Perform Luhn algorithm check
    def luhn_checksum(imei):
        sum = 0
        for i, digit in enumerate(imei):
            digit = int(digit)
            if i % 2 == 1:  # Double every second digit
                digit *= 2
                if digit > 9:
                    digit -= 9
            sum += digit
        return sum % 10 == 0

    return luhn_checksum(imei)


def check_blacklist_status(imei):
    """
    Mock function to simulate checking whether an IMEI is blacklisted or has bad ESN.
    This function would connect to a real database or API in production.

    Args:
        imei (str): IMEI number to check.

    Returns:
        str: Returns 'blacklisted', 'bad_esn', or 'clear' based on the IMEI status.
    """
    # Simulate blacklist database (In production, this would query an actual API or database)
    blacklisted_imeis = {'123456789012345', '987654321098765'}
    bad_esn_imeis = {'111111111111111', '222222222222222'}

    if imei in blacklisted_imeis:
        return 'blacklisted'
    elif imei in bad_esn_imeis:
        return 'bad_esn'
    else:
        return 'clear'


def unlockmaker_integration_tool(imei):
    """
    Suggest integration with UnlockMaker's unblacklist tool.
    Mock implementation showing how to handle an IMEI flagged as problematic.

    Args:
        imei (str): IMEI number to process.

    Returns:
        str: Suggestion message for UnlockMaker integration.
    """
    status = check_blacklist_status(imei)
    if status == 'blacklisted':
        return f"IMEI {imei} is blacklisted. Integrate UnlockMaker's unblacklist tool to remove it from the blacklist."
    elif status == 'bad_esn':
        return f"IMEI {imei} has a bad ESN. Consult UnlockMaker for troubleshooting options."
    else:
        return f"IMEI {imei} is clear and does not require unblacklisting."


# Main Function
if __name__ == "__main__":
    # Example IMEI to validate
    imei_to_check = input("Enter the IMEI number to validate and check status: ").strip()

    try:
        # Validate IMEI
        if not validate_imei(imei_to_check):
            print("Invalid IMEI number. Please provide a valid 15-digit IMEI.")
        else:
            # Check status and suggest UnlockMaker integration
            suggestion = unlockmaker_integration_tool(imei_to_check)
            print(suggestion)
    except Exception as e:
        print(f"An error occurred: {e}")
```
