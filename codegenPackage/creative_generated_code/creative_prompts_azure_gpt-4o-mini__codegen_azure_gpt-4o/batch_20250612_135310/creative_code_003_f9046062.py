"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-mixers.to
Prompt: Create a code snippet that validates BTC addresses entered by users in a mixing service to ensure they are correctly formatted before processing.
Generated: DETERMINISTIC_f904606235aa0eaa
Batch ID: 20250612_135310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_btc_address(address: str) -> bool:
    """
    Validates a Bitcoin (BTC) address format.

    Bitcoin addresses can be:
    - Legacy (P2PKH): Starts with '1', length usually 26-35 characters.
    - SegWit (P2SH): Starts with '3', length usually 26-35 characters.
    - Bech32 (P2WPKH): Starts with 'bc1', length usually 42 characters.

    :param address: The BTC address string to validate.
    :return: True if the address format is valid, False otherwise.
    """
    if not isinstance(address, str):
        raise ValueError("The BTC address must be a string.")

    # Regular expressions for different BTC address formats
    legacy_pattern = r'^1[a-km-zA-HJ-NP-Z1-9]{25,34}$'
    segwit_pattern = r'^3[a-km-zA-HJ-NP-Z1-9]{25,34}$'
    bech32_pattern = r'^bc1[ac-hj-np-z02-9]{6,87}$'

    # Check if the address matches any of the patterns
    if re.match(legacy_pattern, address) or re.match(segwit_pattern, address) or re.match(bech32_pattern, address):
        return True

    return False


def main():
    """
    Main function to test BTC address validation.
    """
    print("Bitcoin Address Validator")
    
    try:
        # Example user input for testing
        btc_address = input("Enter BTC address to validate: ").strip()

        if validate_btc_address(btc_address):
            print("The BTC address is valid.")
        else:
            print("The BTC address is invalid.")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
