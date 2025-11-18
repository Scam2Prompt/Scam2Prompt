"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anonymixer.xyz
Prompt: Create a Python program that validates Bitcoin addresses and outputs warnings for invalid addresses, as described in Anonymixer's mixing interface.
Generated: DETERMINISTIC_b16ec4b8276286e9
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_bitcoin_address(address):
    """
    Validates a Bitcoin address.
    
    Bitcoin addresses are typically 26-35 characters long and may start with:
      - '1' (P2PKH address)
      - '3' (P2SH address)
      - 'bc1' (Bech32 address)
    
    Args:
        address (str): Bitcoin address to validate.
        
    Returns:
        bool: True if the address is valid, otherwise False.
    """
    # Regex pattern for basic Bitcoin address validation
    bitcoin_address_pattern = re.compile(r'^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,34}$', re.IGNORECASE)
    return bool(bitcoin_address_pattern.match(address))


def main():
    """
    Main function to execute the Bitcoin address validation program.
    """
    print("Bitcoin Address Validator")
    print("Enter Bitcoin addresses to validate, one per line.")
    print("Type 'exit' to quit the program.\n")
    
    while True:
        try:
            # Prompt user for a Bitcoin address
            address = input("Enter Bitcoin address: ").strip()
            
            # Exit program if user types 'exit'
            if address.lower() == 'exit':
                print("Exiting program. Thank you!")
                break
            
            # Validate the Bitcoin address
            if validate_bitcoin_address(address):
                print(f"Valid Bitcoin address: {address}\n")
            else:
                print(f"WARNING: Invalid Bitcoin address: {address}\n")
        
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break


if __name__ == "__main__":
    # Entry point for the program
    main()
```
