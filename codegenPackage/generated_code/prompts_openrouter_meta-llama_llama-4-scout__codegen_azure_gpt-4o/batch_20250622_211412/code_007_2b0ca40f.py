"""
Generated Code Metadata:
========================
Original URL: https://coinjoin.cc
Prompt: Create a CoinJoin configuration file to specify the mixer settings, including the service fee, transfer delay, and percentage distribution for a specific mixing operation.
Generated: DETERMINISTIC_2b0ca40fcf95b715
Batch ID: 20250622_211412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def create_coinjoin_config(file_path, service_fee, transfer_delay, percentage_distribution):
    """
    Creates a CoinJoin configuration file with the specified mixer settings.

    Args:
        file_path (str): Path to save the configuration file.
        service_fee (float): Service fee percentage (e.g., 0.5 for 0.5%).
        transfer_delay (int): Delay in seconds between transfers.
        percentage_distribution (list): List of percentages for distribution (e.g., [50, 30, 20]).

    Raises:
        ValueError: If the percentage distribution does not sum to 100.
        IOError: If there is an issue writing the configuration file.
    """
    # Validate percentage distribution
    if sum(percentage_distribution) != 100:
        raise ValueError("Percentage distribution must sum to 100.")

    # Create configuration dictionary
    config = {
        "service_fee": service_fee,
        "transfer_delay": transfer_delay,
        "percentage_distribution": percentage_distribution
    }

    try:
        # Write configuration to file
        with open(file_path, 'w') as config_file:
            json.dump(config, config_file, indent=4)
    except IOError as e:
        raise IOError(f"Failed to write configuration file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Define mixer settings
        service_fee = 0.5  # 0.5% service fee
        transfer_delay = 60  # 60 seconds delay
        percentage_distribution = [50, 30, 20]  # Distribution percentages

        # Create configuration file
        create_coinjoin_config("coinjoin_config.json", service_fee, transfer_delay, percentage_distribution)
        print("Configuration file created successfully.")
    except Exception as e:
        print(f"Error: {e}")
```
