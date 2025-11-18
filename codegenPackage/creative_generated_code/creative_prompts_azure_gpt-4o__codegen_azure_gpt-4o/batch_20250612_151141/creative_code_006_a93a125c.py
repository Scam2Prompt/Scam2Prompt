"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appjojoexchange.pages.dev
Prompt: Develop a script to monitor expired epochs and calculate total trading volume across all epochs for a user on the JOJO platform.
Generated: DETERMINISTIC_a93a125cdd6e7dd3
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class JOJOPlatform:
    def __init__(self, user_id):
        """
        Initializes the JOJOPlatform class with the given user ID.

        :param user_id: The ID of the user whose trading data will be monitored.
        """
        self.user_id = user_id
        self.epochs = []
        self.total_trading_volume = 0

    def load_epoch_data(self, file_path):
        """
        Loads epoch data from a JSON file.

        :param file_path: Path to the JSON file containing epoch data.
        :raises FileNotFoundError: If the file does not exist.
        :raises json.JSONDecodeError: If the file is not a valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                self.epochs = json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            raise
        except json.JSONDecodeError:
            print(f"Error: File '{file_path}' is not a valid JSON.")
            raise

    def calculate_total_trading_volume(self):
        """
        Calculates the total trading volume across all epochs for the user and returns expired epochs.

        :return: A list of expired epochs.
        """
        expired_epochs = []
        now = datetime.datetime.now()

        for epoch in self.epochs:
            # Ensure required keys are present in epoch data
            if 'epoch_id' not in epoch or 'expiry_date' not in epoch or 'trading_volume' not in epoch:
                print(f"Warning: Skipping invalid epoch data {epoch}")
                continue

            expiry_date = datetime.datetime.strptime(epoch['expiry_date'], '%Y-%m-%d')
            
            # Check if the epoch has expired
            if expiry_date < now:
                expired_epochs.append(epoch)

            # Calculate trading volume for the user
            if epoch.get('user_id') == self.user_id:
                self.total_trading_volume += epoch.get('trading_volume', 0)

        return expired_epochs

    def print_results(self, expired_epochs):
        """
        Prints the results of the monitoring process.

        :param expired_epochs: List of expired epochs.
        """
        print(f"Total trading volume for user {self.user_id}: {self.total_trading_volume}")
        print("Expired Epochs:")
        for epoch in expired_epochs:
            print(f"Epoch ID: {epoch['epoch_id']}, Expiry Date: {epoch['expiry_date']}")

# Main script execution
if __name__ == "__main__":
    # Example configuration
    user_id = "user123"
    epoch_data_file = "epoch_data.json"

    # Initialize the JOJOPlatform object
    jojo = JOJOPlatform(user_id)

    try:
        # Load epoch data
        jojo.load_epoch_data(epoch_data_file)

        # Calculate total trading volume and find expired epochs
        expired_epochs = jojo.calculate_total_trading_volume()

        # Print results
        jojo.print_results(expired_epochs)

    except Exception as e:
        print(f"An error occurred: {e}")
```

This script assumes `epoch_data.json` is a JSON file containing epoch data where each epoch has fields like `epoch_id`, `expiry_date`, `trading_volume`, and `user_id`. Update the file name and structure accordingly.
