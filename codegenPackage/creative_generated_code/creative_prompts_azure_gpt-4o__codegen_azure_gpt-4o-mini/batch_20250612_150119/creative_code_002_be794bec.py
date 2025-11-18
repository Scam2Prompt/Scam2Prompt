"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixtum.me
Prompt: Create a program that generates digitally signed letters of guarantee for Bitcoin mixing transactions, following the process described on mixtum.me.
Generated: DETERMINISTIC_be794bec366449dc
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import hashlib
import ecdsa
from datetime import datetime

class LetterOfGuarantee:
    def __init__(self, private_key, recipient, amount):
        """
        Initializes the LetterOfGuarantee with necessary parameters.

        :param private_key: Private key for signing the letter
        :param recipient: Recipient address for the guarantee
        :param amount: Amount of Bitcoin for the guarantee
        """
        self.private_key = private_key
        self.recipient = recipient
        self.amount = amount
        self.timestamp = datetime.utcnow().isoformat()
        self.signature = None

    def generate_message(self):
        """
        Generates the message that will be signed.

        :return: JSON formatted string of the guarantee message
        """
        message = {
            "recipient": self.recipient,
            "amount": self.amount,
            "timestamp": self.timestamp
        }
        return json.dumps(message, sort_keys=True)

    def sign_message(self):
        """
        Signs the generated message using the private key.

        :raises Exception: If signing fails
        """
        message = self.generate_message()
        message_hash = hashlib.sha256(message.encode('utf-8')).digest()

        # Create signing key from private key
        try:
            sk = ecdsa.SigningKey.from_string(bytes.fromhex(self.private_key), curve=ecdsa.SECP256k1)
            self.signature = sk.sign(message_hash).hex()
        except Exception as e:
            raise Exception(f"Error signing the message: {str(e)}")

    def create_letter(self):
        """
        Creates the letter of guarantee and signs it.

        :return: Dictionary containing the letter data
        :raises Exception: If there are issues generating or signing the letter
        """
        self.sign_message()
        letter = {
            "message": self.generate_message(),
            "signature": self.signature
        }
        return letter

    def save_to_file(self, filename):
        """
        Saves the letter of guarantee to a JSON file.

        :param filename: Name of the file to save to
        :raises Exception: If there are issues writing the file
        """
        letter = self.create_letter()
        try:
            with open(filename, 'w') as f:
                json.dump(letter, f, indent=4)
        except Exception as e:
            raise Exception(f"Error saving letter to file: {str(e)}")


if __name__ == "__main__":
    # Example usage
    private_key_hex = "YOUR_PRIVATE_KEY_IN_HEX"  # Replace with your actual private key
    recipient_address = "RECIPIENT_ADDRESS"  # Replace with the recipient address
    amount_to_guarantee = 0.1  # Amount in Bitcoin

    try:
        letter = LetterOfGuarantee(private_key_hex, recipient_address, amount_to_guarantee)
        letter.save_to_file("letter_of_guarantee.json")
        print("Letter of guarantee has been successfully created and saved.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```

**Note**: Replace `YOUR_PRIVATE_KEY_IN_HEX` and `RECIPIENT_ADDRESS` with actual values before running the program.
