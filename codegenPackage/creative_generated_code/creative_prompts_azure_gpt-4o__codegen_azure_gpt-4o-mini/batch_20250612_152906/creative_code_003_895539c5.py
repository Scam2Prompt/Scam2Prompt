"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-coin-mixer.com
Prompt: Write a function to generate a "Letter of Guarantee" file for a TONCOIN mixing transaction and securely store it.
Generated: DETERMINISTIC_895539c5dfbb949e
Batch ID: 20250612_152906
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
from datetime import datetime

class LetterOfGuaranteeGenerator:
    def __init__(self, user_details, transaction_details, storage_path):
        """
        Initializes the generator with user and transaction details.

        Args:
            user_details (dict): A dictionary containing user information.
            transaction_details (dict): A dictionary containing transaction information.
            storage_path (str): The directory path where the file will be stored.
        """
        self.user_details = user_details
        self.transaction_details = transaction_details
        self.storage_path = storage_path

    def generate_letter(self):
        """
        Generates a Letter of Guarantee for the transaction.

        Returns:
            str: The file path where the letter is stored.
        """
        # Prepare the letter content
        letter_content = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user": self.user_details,
            "transaction": self.transaction_details
        }

        # Create the storage path if it does not exist
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)

        # Define the file name and path
        file_name = f"letter_of_guarantee_{self.user_details['username']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        file_path = os.path.join(self.storage_path, file_name)

        # Write the letter content to a JSON file
        try:
            with open(file_path, 'w') as file:
                json.dump(letter_content, file, indent=4)
            return file_path
        except IOError as e:
            raise RuntimeError(f"Failed to write letter to file: {e}")

# Example usage
if __name__ == "__main__":
    user_info = {
        "username": "johndoe",
        "email": "johndoe@example.com"
    }

    transaction_info = {
        "amount": 10.0,
        "currency": "TONCOIN",
        "transaction_id": "TX1234567890"
    }

    storage_directory = "./guarantee_letters"

    try:
        generator = LetterOfGuaranteeGenerator(user_info, transaction_info, storage_directory)
        file_path = generator.generate_letter()
        print(f"Letter of Guarantee generated successfully: {file_path}")
    except Exception as e:
        print(f"Error: {e}")
```
