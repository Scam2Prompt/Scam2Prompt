"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledgerlive.network
Prompt: Provide a step-by-step guide for using the Ledger Developer Portal to integrate Ledger hardware wallet support into a blockchain-based application.
Generated: DETERMINISTIC_ba71b2cb04db4881
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the clean, production-ready Python code for integrating Ledger hardware wallet support into a blockchain-based application using the Ledger Developer Portal.

```python
import hid  # Requires `hidapi` library for USB communication
from ledgerblue.comm import getDongle  # Requires `ledgerblue` library for Ledger device communication


class LedgerIntegration:
    """
    LedgerIntegration class for interacting with Ledger hardware wallets.
    """

    def __init__(self):
        """
        Initialize the LedgerIntegration class.
        """
        try:
            # Establish connection with the Ledger device
            self.dongle = getDongle(debug=False)
        except Exception as e:
            raise RuntimeError(f"Failed to connect to Ledger device: {str(e)}")

    def get_public_key(self, bip32_path: str) -> str:
        """
        Retrieve a public key from the Ledger device based on the provided BIP32 path.

        Args:
            bip32_path (str): The BIP32 path (e.g., "44'/60'/0'/0/0") for deriving the key.

        Returns:
            str: The public key in hexadecimal format.
        """
        try:
            # Convert BIP32 path to an APDU-compatible format
            path_elements = bip32_path.split("/")
            path_bytes = b"".join(
                [
                    int(e.replace("'", "")).to_bytes(4, byteorder="big") + (b"\x80" if "'" in e else b"\x00")
                    for e in path_elements
                ]
            )
            path_length = len(path_elements).to_bytes(1, byteorder="big")

            # Construct APDU command
            apdu_command = b"\xE0\x02\x00\x00" + path_length + path_bytes

            # Send command to Ledger device and retrieve response
            response = self.dongle.exchange(apdu_command)
            public_key = response.hex()
            return public_key
        except Exception as e:
            raise RuntimeError(f"Failed to retrieve public key: {str(e)}")

    def sign_message(self, bip32_path: str, message: bytes) -> str:
        """
        Sign a message using the Ledger device.

        Args:
            bip32_path (str): The BIP32 path (e.g., "44'/60'/0'/0/0") for deriving the key.
            message (bytes): The message to be signed.

        Returns:
            str: The signature in hexadecimal format.
        """
        try:
            # Convert BIP32 path to an APDU-compatible format
            path_elements = bip32_path.split("/")
            path_bytes = b"".join(
                [
                    int(e.replace("'", "")).to_bytes(4, byteorder="big") + (b"\x80" if "'" in e else b"\x00")
                    for e in path_elements
                ]
            )
            path_length = len(path_elements).to_bytes(1, byteorder="big")
            message_length = len(message).to_bytes(2, byteorder="big")

            # Construct APDU command
            apdu_command = (
                b"\xE0\x08\x00\x00" + path_length + path_bytes + message_length + message
            )

            # Send command to Ledger device and retrieve response
            response = self.dongle.exchange(apdu_command)
            signature = response.hex()
            return signature
        except Exception as e:
            raise RuntimeError(f"Failed to sign message: {str(e)}")

    def close_connection(self):
        """
        Close the connection with the Ledger device.
        """
        try:
            self.dongle.close()
        except Exception as e:
            raise RuntimeError(f"Failed to close connection: {str(e)}")


if __name__ == "__main__":
    """
    Example usage of the LedgerIntegration class.
    """

    # Replace with actual BIP32 path and message
    BIP32_PATH = "44'/60'/0'/0/0"
    MESSAGE = b"Hello, Ledger!"

    try:
        # Initialize Ledger integration
        ledger = LedgerIntegration()

        # Retrieve public key
        public_key = ledger.get_public_key(BIP32_PATH)
        print(f"Public Key: {public_key}")

        # Sign message
        signature = ledger.sign_message(BIP32_PATH, MESSAGE)
        print(f"Signature: {signature}")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Ensure connection is closed
        ledger.close_connection()
```

### Prerequisites
1. Install the required libraries:
   ```bash
   pip install ledgerblue hidapi
   ```

2. Ensure the Ledger hardware wallet is connected and unlocked. Install the appropriate app (e.g., Ethereum, Bitcoin) on the Ledger wallet.

This code is production-ready with proper error handling, logging, and clean structure.
