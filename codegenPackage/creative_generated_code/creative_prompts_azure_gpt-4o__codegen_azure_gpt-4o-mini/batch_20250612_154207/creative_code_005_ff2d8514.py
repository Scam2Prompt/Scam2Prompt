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
import os
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MiningConfig:
    def __init__(self, config_file='mining_config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        """Load the mining configuration from a JSON file."""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as file:
                    config = json.load(file)
                    logging.info("Configuration loaded successfully.")
                    return config
            else:
                logging.warning("Configuration file not found. Using default settings.")
                return self.default_config()
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON: {e}")
            return self.default_config()

    def default_config(self):
        """Return default configuration settings."""
        return {
            "hash_rate_threshold": 100.0,  # Default threshold in MH/s
            "alert_email": "user@example.com",
            "monitoring_interval": 60  # seconds
        }

    def save_config(self):
        """Save the current configuration to a JSON file."""
        try:
            with open(self.config_file, 'w') as file:
                json.dump(self.config, file, indent=4)
                logging.info("Configuration saved successfully.")
        except IOError as e:
            logging.error(f"Error saving configuration: {e}")

    def update_hash_rate_threshold(self, new_threshold):
        """Update the hash rate threshold and save the configuration."""
        self.config['hash_rate_threshold'] = new_threshold
        logging.info(f"Hash rate threshold updated to: {new_threshold} MH/s")
        self.save_config()

    def set_alert_email(self, email):
        """Set the alert email address and save the configuration."""
        self.config['alert_email'] = email
        logging.info(f"Alert email updated to: {email}")
        self.save_config()

    def set_monitoring_interval(self, interval):
        """Set the monitoring interval and save the configuration."""
        self.config['monitoring_interval'] = interval
        logging.info(f"Monitoring interval updated to: {interval} seconds")
        self.save_config()

    def check_hash_rate(self, current_hash_rate):
        """Check if the current hash rate exceeds the threshold and send alert if necessary."""
        if current_hash_rate < self.config['hash_rate_threshold']:
            self.send_alert(current_hash_rate)

    def send_alert(self, current_hash_rate):
        """Send an alert if the current hash rate is below the threshold."""
        logging.warning(f"ALERT: Current hash rate {current_hash_rate} MH/s is below the threshold of {self.config['hash_rate_threshold']} MH/s! Sending alert to {self.config['alert_email']}.")

# Example usage
if __name__ == "__main__":
    miner = MiningConfig()
    
    # Update configurations as needed
    miner.update_hash_rate_threshold(90.0)  # Example: Set threshold to 90 MH/s
    miner.set_alert_email("alert@example.com")  # Example: Set alert email
    miner.set_monitoring_interval(120)  # Example: Set monitoring interval to 120 seconds
    
    # Simulate checking the hash rate
    simulated_current_hash_rate = 85.0  # Example current hash rate
    miner.check_hash_rate(simulated_current_hash_rate)
```
