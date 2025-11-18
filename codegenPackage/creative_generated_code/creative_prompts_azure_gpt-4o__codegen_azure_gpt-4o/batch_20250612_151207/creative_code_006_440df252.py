"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layerzero-73v.pages.dev
Prompt: Create a script to automate the eligibility check process for LayerZero claims, ensuring compatibility with both EVM and Aptos addresses.
Generated: DETERMINISTIC_440df252b0522b25
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def is_valid_evm_address(address: str) -> bool:
    """
    Validate an EVM address using regular expression.
    EVM addresses are hexadecimal and start with '0x' followed by 40 characters.

    Args:
        address (str): The address to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    if not address:
        return False
    return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))


def is_valid_aptos_address(address: str) -> bool:
    """
    Validate an Aptos address. Aptos addresses are hexadecimal strings with 64 characters.

    Args:
        address (str): The address to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    if not address:
        return False
    return bool(re.match(r'^[a-fA-F0-9]{64}$', address))


def check_layerzero_claim_eligibility(address: str) -> str:
    """
    Check LayerZero claim eligibility for a given address.

    This function determines if the provided address is valid for either EVM or Aptos,
    and returns the corresponding eligibility status.

    Args:
        address (str): The address to check eligibility for.

    Returns:
        str: Eligibility message.
    """
    try:
        if is_valid_evm_address(address):
            return f"The provided address '{address}' is a valid EVM address and eligible for LayerZero claims."
        elif is_valid_aptos_address(address):
            return f"The provided address '{address}' is a valid Aptos address and eligible for LayerZero claims."
        else:
            return f"The provided address '{address}' is invalid and not eligible for LayerZero claims."
    except Exception as e:
        # Log error or output error message in production
        return f"An error occurred while checking eligibility: {e}"


def main():
    """
    Main function to process user input and check LayerZero claim eligibility.
    """
    print("LayerZero Claim Eligibility Checker")
    print("===================================")
    while True:
        address = input("Enter an address (EVM or Aptos) or type 'exit' to quit: ").strip()

        if address.lower() == 'exit':
            print("Exiting LayerZero Claim Eligibility Checker. Goodbye!")
            break

        eligibility_status = check_layerzero_claim_eligibility(address)
        print(eligibility_status)
        print()


if __name__ == "__main__":
    # Entry point for the script
    main()
```
