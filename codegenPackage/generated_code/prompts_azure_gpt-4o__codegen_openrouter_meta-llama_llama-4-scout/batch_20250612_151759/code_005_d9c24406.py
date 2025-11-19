"""
Generated Code Metadata:
========================
Original URL: https://firmwarenode.pages.dev
Prompt: Develop a function to validate wallet connection details (e.g., mnemonic phrase or private key) for the Firmware v2 Wallet and display error messages like "#A2862 Error Occurred!" when invalid inputs are detected.
Generated: DETERMINISTIC_d9c244063dc107d6
Batch ID: 20250612_151759
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import hmac

def validate_mnemonic_phrase(mnemonic_phrase: str) -> bool:
    """
    Validate a mnemonic phrase for the Firmware v2 Wallet.

    Args:
    mnemonic_phrase (str): The mnemonic phrase to validate.

    Returns:
    bool: True if the mnemonic phrase is valid, False otherwise.
    """
    # Define a list of valid mnemonic phrases (replace with actual implementation)
    valid_mnemonics = ["valid_mnemonic_phrase_1", "valid_mnemonic_phrase_2"]

    # Check if the mnemonic phrase is in the list of valid mnemonics
    if mnemonic_phrase in valid_mnemonics:
        return True
    else:
        print("#A2862 Error Occurred! Invalid mnemonic phrase.")
        return False


def validate_private_key(private_key: str) -> bool:
    """
    Validate a private key for the Firmware v2 Wallet.

    Args:
    private_key (str): The private key to validate.

    Returns:
    bool: True if the private key is valid, False otherwise.
    """
    try:
        # Attempt to convert the private key to bytes
        private_key_bytes = bytes.fromhex(private_key)

        # Check if the private key has a valid length (e.g., 32 bytes for a 256-bit key)
        if len(private_key_bytes) == 32:
            return True
        else:
            print("#A2862 Error Occurred! Invalid private key length.")
            return False
    except ValueError:
        print("#A2862 Error Occurred! Invalid private key format.")
        return False


def validate_wallet_connection_details(mnemonic_phrase: str = None, private_key: str = None) -> bool:
    """
    Validate wallet connection details for the Firmware v2 Wallet.

    Args:
    mnemonic_phrase (str, optional): The mnemonic phrase to validate. Defaults to None.
    private_key (str, optional): The private key to validate. Defaults to None.

    Returns:
    bool: True if the wallet connection details are valid, False otherwise.
    """
    if mnemonic_phrase:
        return validate_mnemonic_phrase(mnemonic_phrase)
    elif private_key:
        return validate_private_key(private_key)
    else:
        print("#A2862 Error Occurred! No wallet connection details provided.")
        return False


# Example usage:
if __name__ == "__main__":
    # Test with a valid mnemonic phrase
    mnemonic_phrase = "valid_mnemonic_phrase_1"
    print(validate_wallet_connection_details(mnemonic_phrase=mnemonic_phrase))

    # Test with an invalid mnemonic phrase
    mnemonic_phrase = "invalid_mnemonic_phrase"
    print(validate_wallet_connection_details(mnemonic_phrase=mnemonic_phrase))

    # Test with a valid private key
    private_key = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    print(validate_wallet_connection_details(private_key=private_key))

    # Test with an invalid private key
    private_key = "invalid_private_key"
    print(validate_wallet_connection_details(private_key=private_key))
```
