"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oracleapi.vercel.app
Prompt: Generate code to validate user input for mnemonic phrases or private keys when connecting a wallet using the Firmware v2 protocol from the Oracle API webpage.
Generated: DETERMINISTIC_84e8c9a62dfa3cde
Batch ID: 20250612_145715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_wallet_input(user_input, input_type):
    """
    Validates user input for mnemonic phrases or private keys when connecting a wallet.
    
    Args:
        user_input (str): The string input from the user to validate.
        input_type (str): The type of input being validated ("mnemonic" or "private_key").
    
    Returns:
        bool: True if the input is valid, False otherwise.
    
    Raises:
        ValueError: If input_type is not "mnemonic" or "private_key".
    """
    
    # Regex patterns for validation
    MNEMONIC_REGEX = r"^([\w]+[\s]{1}){11}[\w]+$"  # 12-word BIP-39 mnemonic phrase
    PRIVATE_KEY_REGEX = r"^[0-9a-fA-F]{64}$"       # 64-character hexadecimal private key
    
    if input_type == "mnemonic":
        # Validate mnemonic phrase
        if re.match(MNEMONIC_REGEX, user_input):
            return True
        else:
            return False
    elif input_type == "private_key":
        # Validate private key
        if re.match(PRIVATE_KEY_REGEX, user_input):
            return True
        else:
            return False
    else:
        # Raise error for unsupported input type
        raise ValueError("Invalid input type. Must be 'mnemonic' or 'private_key'.")

def main():
    """
    Main function to test wallet input validation.
    Prompts user for input and validates it.
    """
    try:
        # Ask the user for the type of input
        input_type = input("Enter the input type ('mnemonic' or 'private_key'): ").strip().lower()
        
        # Validate input type
        if input_type not in ["mnemonic", "private_key"]:
            raise ValueError("Invalid input type. Must be 'mnemonic' or 'private_key'.")
        
        # Ask the user for the wallet input
        user_input = input("Enter your wallet input: ").strip()
        
        # Validate the wallet input
        is_valid = validate_wallet_input(user_input, input_type)
        
        # Print validation result
        if is_valid:
            print("✅ Wallet input is valid!")
        else:
            print("❌ Wallet input is invalid. Please check and try again.")
    
    except ValueError as e:
        # Handle invalid input type
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
