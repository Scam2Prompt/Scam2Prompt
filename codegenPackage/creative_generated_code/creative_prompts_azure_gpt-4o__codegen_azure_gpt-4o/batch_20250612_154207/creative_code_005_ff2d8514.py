"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hashminer.pro
Prompt: Generate code to automate the configuration of cryptocurrency mining software, including setting up hash rate thresholds and alerts.
Generated: DETERMINISTIC_ff2d851429df8762
Batch ID: 20250612_154207
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
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] - %(message)s",
    handlers=[
        logging.FileHandler("mining_config.log"),
        logging.StreamHandler()
    ]
)

# Default configuration values
DEFAULT_CONFIG = {
    "mining_software_path": "/usr/local/bin/mining_software",
    "hash_rate_threshold": 50,  # Hash rate threshold in MH/s
    "alert_email": "admin@example.com",
    "monitor_interval": 60  # Interval to check hash rate, in seconds
}

CONFIG_FILE = "mining_config.json"

def load_config(config_file):
    """
    Load configuration from file. If file does not exist, create a default configuration.
    """
    if not os.path.exists(config_file):
        logging.warning("Configuration file not found, creating default configuration.")
        save_config(config_file, DEFAULT_CONFIG)
        return DEFAULT_CONFIG
    
    try:
        with open(config_file, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as e:
        logging.error(f"Failed to load configuration: {e}")
        logging.info("Using default configuration.")
        return DEFAULT_CONFIG


def save_config(config_file, config):
    """
    Save the configuration to a file.
    """
    try:
        with open(config_file, "w") as file:
            json.dump(config, file, indent=4)
            logging.info("Configuration saved successfully.")
    except IOError as e:
        logging.error(f"Failed to save configuration: {e}")


def configure_mining_software(config):
    """
    Configure the mining software with the given settings.
    """
    mining_software_path = config.get("mining_software_path")
    if not os.path.exists(mining_software_path):
        logging.error(f"Mining software not found at path: {mining_software_path}")
        return False

    try:
        # Simulate configuration of mining software (e.g., writing config files, etc.)
        logging.info(f"Configuring mining software at {mining_software_path}...")
        logging.info(f"Setting hash rate threshold to {config['hash_rate_threshold']} MH/s")
        logging.info(f"Alerts will be sent to {config['alert_email']}")
        return True
    except Exception as e:
        logging.error(f"Failed to configure mining software: {e}")
        return False


def monitor_hash_rate(config):
    """
    Monitor the hash rate and send an alert if it drops below the threshold.
    """
    import random  # For simulation purposes. Replace with actual hash rate monitoring logic.

    try:
        current_hash_rate = random.uniform(30, 70)  # Simulated hash rate value
        logging.info(f"Current hash rate: {current_hash_rate} MH/s")

        if current_hash_rate < config["hash_rate_threshold"]:
            logging.warning(f"Hash rate below threshold! ({current_hash_rate} MH/s)")
            send_alert(config["alert_email"], current_hash_rate)
    except Exception as e:
        logging.error(f"Error while monitoring hash rate: {e}")


def send_alert(email, hash_rate):
    """
    Send an alert via email. Placeholder function for actual email-sending logic.
    """
    try:
        # Simulate sending an email alert
        logging.info(f"Sending alert to {email} about low hash rate: {hash_rate} MH/s")
    except Exception as e:
        logging.error(f"Failed to send alert email: {e}")


def main():
    """
    Main entry point for the script.
    """
    config = load_config(CONFIG_FILE)

    if not configure_mining_software(config):
        logging.error("Failed to configure mining software. Exiting.")
        return

    # Monitor hash rate periodically
    import time
    logging.info("Starting hash rate monitoring...")
    while True:
        monitor_hash_rate(config)
        time.sleep(config["monitor_interval"])


if __name__ == "__main__":
    main()
```
