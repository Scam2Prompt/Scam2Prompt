"""
Generated Code Metadata:
========================
Original URL: https://btc-tools.org
Prompt: Write a code snippet to implement power-saving modes for miners using BTC Tools, including setting different power-saving profiles.
Generated: DETERMINISTIC_ca0cf96976285af9
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess

# Define power-saving profiles
POWER_SAVING_PROFILES = {
    "low": {"frequency": 500, "voltage": 700},
    "medium": {"frequency": 600, "voltage": 750},
    "high": {"frequency": 700, "voltage": 800},
}

def set_power_saving_mode(miner_ip, profile_name):
    """
    Set the power-saving mode for a miner using BTC Tools.

    Args:
        miner_ip (str): IP address of the miner.
        profile_name (str): Name of the power-saving profile (low, medium, high).

    Returns:
        bool: True if the operation was successful, False otherwise.
    """
    if profile_name not in POWER_SAVING_PROFILES:
        print(f"Error: Invalid profile name '{profile_name}'. Valid profiles are: {list(POWER_SAVING_PROFILES.keys())}")
        return False

    profile = POWER_SAVING_PROFILES[profile_name]
    frequency = profile["frequency"]
    voltage = profile["voltage"]

    try:
        # Construct the BTC Tools command to set power-saving mode
        command = f"btctools --set-power-mode --ip {miner_ip} --frequency {frequency} --voltage {voltage}"
        
        # Execute the command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Check for errors in the command execution
        if result.returncode != 0:
            print(f"Error: Failed to set power-saving mode for miner {miner_ip}.")
            print(f"Details: {result.stderr}")
            return False

        print(f"Successfully set power-saving mode '{profile_name}' for miner {miner_ip}.")
        return True

    except Exception as e:
        print(f"Exception occurred while setting power-saving mode: {e}")
        return False

def main():
    """
    Main function to demonstrate setting power-saving modes for miners.
    """
    # Example miner IPs
    miner_ips = ["192.168.1.100", "192.168.1.101", "192.168.1.102"]

    # Example usage: Set all miners to 'medium' power-saving mode
    for miner_ip in miner_ips:
        success = set_power_saving_mode(miner_ip, "medium")
        if not success:
            print(f"Failed to configure miner at {miner_ip}. Please check the logs.")

if __name__ == "__main__":
    main()
```
