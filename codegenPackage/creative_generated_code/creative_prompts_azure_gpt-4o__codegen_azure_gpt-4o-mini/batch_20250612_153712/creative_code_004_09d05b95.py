"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://legatoltd.net
Prompt: Create a script to securely collect user data (e.g., name, amount lost, deposit method) for scam reporting, modeled after The Legato's consultation form.
Generated: DETERMINISTIC_09d05b95bb6196e0
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from getpass import getpass

class UserDataCollector:
    """
    A class to securely collect user data for scam reporting.
    """

    def __init__(self, data_file='user_data.json'):
        """
        Initializes the UserDataCollector with the specified data file.
        
        Args:
            data_file (str): The name of the file to save user data.
        """
        self.data_file = data_file

    def collect_data(self):
        """
        Collects user data for scam reporting.
        
        Returns:
            dict: A dictionary containing the user's data.
        """
        print("Please enter the following information for scam reporting.")
        
        name = input("Full Name: ")
        amount_lost = self.get_float_input("Amount Lost ($): ")
        deposit_method = input("Deposit Method: ")

        user_data = {
            'name': name,
            'amount_lost': amount_lost,
            'deposit_method': deposit_method
        }
        
        return user_data

    def get_float_input(self, prompt):
        """
        Prompts the user for a float input and handles errors.
        
        Args:
            prompt (str): The input prompt for the user.
        
        Returns:
            float: The validated float input from the user.
        """
        while True:
            try:
                value = float(input(prompt))
                if value < 0:
                    raise ValueError("Amount cannot be negative.")
                return value
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

    def save_data(self, data):
        """
        Saves the user data to a JSON file securely.
        
        Args:
            data (dict): The user data to save.
        """
        try:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)

            with open(self.data_file, 'a') as f:
                json_data = json.dumps(data) + "\n"  # Append each entry on a new line
                f.write(json_data)
            print("Data saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving data: {e}")

    def run(self):
        """
        Runs the data collection and saving process.
        """
        user_data = self.collect_data()
        self.save_data(user_data)


if __name__ == "__main__":
    collector = UserDataCollector()
    collector.run()
```
