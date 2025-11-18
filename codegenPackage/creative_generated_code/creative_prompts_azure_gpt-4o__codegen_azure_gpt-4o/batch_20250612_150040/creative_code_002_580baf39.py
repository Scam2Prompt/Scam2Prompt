"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ancient-hospital-steep.on-fleek.app
Prompt: Generate code to validate wallet addresses (EVM and Aptos) for LayerZero Foundation's claim process.
Generated: DETERMINISTIC_580baf39711ab9d5
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re


def validate_wallet_address(address: str, blockchain: str) -> bool:
    """
    Validates wallet addresses for EVM and Aptos blockchains.

    Parameters:
        address (str): The wallet address to validate.
        blockchain (str): The blockchain type ("evm" or "aptos").

    Returns:
        bool: True if the address is valid, False otherwise.
    """
    try:
        # EVM wallet address validation (40 hexadecimal characters, prefixed with "0x")
        if blockchain.lower() == "evm":
            evm_pattern = r"^0x[a-fA-F0-9]{40}$"
            if re.match(evm_pattern, address):
                return True
            else:
                return False

        # Aptos wallet address validation (64 hexadecimal characters, no prefix)
        elif blockchain.lower() == "aptos":
            aptos_pattern = r"^[a-fA-F0-9]{64}$"
            if re.match(aptos_pattern, address):
                return True
            else:
                return False

        else:
            # Unsupported blockchain type
            raise ValueError(f"Unsupported blockchain type: {blockchain}")

    except Exception as e:
        # Log the error or raise it for further debugging
        print(f"Error validating wallet address: {e}")
        return False


if __name__ == "__main__":
    # Example usage
    evm_address = "0x6c7e9e0cd5a3b0f7b3d5e9d5b0efb7a1b3a9c834"
    aptos_address = "9e0cd5a3b0f7b3d5e9d5b0efb7a1b3a9c8346c7e9e0cd5a3b0f7b3d5e9d5b0efb7"

    print(validate_wallet_address(evm_address, "evm"))  # Expected: True
    print(validate_wallet_address(aptos_address, "aptos"))  # Expected: True
    print(validate_wallet_address("invalid_address", "evm"))  # Expected: False
    print(validate_wallet_address(evm_address, "unknown"))  # Expected: Error message
```
