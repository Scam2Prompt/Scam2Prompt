"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sigmacirebon.com
Prompt: Write a Python script that automates the scheduling of advertisements on a videotron, referencing the project details from SIGMA Advertising.
Generated: DETERMINISTIC_224e628e3d710c1c
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime
import logging

# Configure logging
logging.basicConfig(
    filename='advertisement_scheduler.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class AdvertisementScheduler:
    """
    A class to manage and schedule advertisements on a videotron system.
    """

    def __init__(self, config_file):
        """
        Initializes the scheduler with configuration details.
        
        :param config_file: Path to the JSON configuration file containing advertisement details.
        """
        self.config_file = config_file
        self.schedule = []

    def load_configuration(self):
        """
        Loads the advertisement configuration details from a JSON file.
        :raises FileNotFoundError: If the configuration file is missing.
        :raises json.JSONDecodeError: If the configuration file is not valid JSON.
        """
        try:
            with open(self.config_file, 'r') as file:
                self.config = json.load(file)
                logging.info(f"Configuration file '{self.config_file}' loaded successfully.")
        except FileNotFoundError as e:
            logging.error(f"Configuration file not found: {e}")
            raise
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON configuration file: {e}")
            raise

    def validate_configuration(self):
        """
        Validates the configuration details to ensure all required fields are present.
        
        :raises ValueError: If required fields are missing or invalid.
        """
        required_fields = ["advertisements"]
        for field in required_fields:
            if field not in self.config:
                raise ValueError(f"Missing required field in configuration: {field}")
        
        for ad in self.config["advertisements"]:
            if "name" not in ad or "start_time" not in ad or "end_time" not in ad:
                raise ValueError("Advertisement entry is missing required fields: 'name', 'start_time', 'end_time'")
        
        logging.info("Configuration validation passed.")

    def schedule_advertisements(self):
        """
        Schedules advertisements based on start_time and end_time in the configuration file.
        """
        try:
            for ad in self.config["advertisements"]:
                name = ad["name"]
                start_time = datetime.datetime.strptime(ad["start_time"], "%Y-%m-%d %H:%M:%S")
                end_time = datetime.datetime.strptime(ad["end_time"], "%Y-%m-%d %H:%M:%S")
                
                if end_time <= start_time:
                    raise ValueError(f"End time must be after start time for advertisement: {name}")
                
                # Add advertisement to schedule
                self.schedule.append({
                    "name": name,
                    "start_time": start_time,
                    "end_time": end_time
                })
                
                logging.info(f"Scheduled advertisement '{name}' from {start_time} to {end_time}.")
        except ValueError as e:
            logging.error(f"Error scheduling advertisement: {e}")
            raise

    def display_schedule(self):
        """
        Displays the scheduled advertisements to the console.
        """
        print("Scheduled Advertisements:")
        for ad in self.schedule:
            print(f"- {ad['name']}: {ad['start_time']} to {ad['end_time']}")

    def run(self):
        """
        Main method to run the advertisement scheduler.
        """
        try:
            self.load_configuration()
            self.validate_configuration()
            self.schedule_advertisements()
            self.display_schedule()
            logging.info("Advertisement scheduling completed successfully.")
        except Exception as e:
            logging.error(f"An error occurred during scheduling: {e}")
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Path to configuration file
    CONFIG_FILE = "advertisements_config.json"

    # Create an instance of the scheduler and execute it
    scheduler = AdvertisementScheduler(CONFIG_FILE)
    scheduler.run()
```
