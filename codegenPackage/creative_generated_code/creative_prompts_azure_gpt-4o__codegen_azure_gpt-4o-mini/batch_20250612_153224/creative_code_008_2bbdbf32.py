"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gesec.com.co
Prompt: Write a Python script to calculate and track key safety indicators for reducing workplace incidents, following GESEC's methodology for improving organizational processes.
Generated: DETERMINISTIC_2bbdbf32fb3b0499
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SafetyIndicatorTracker:
    """A class to track safety indicators based on GESEC methodology."""
    
    def __init__(self, data_file):
        """
        Initializes the SafetyIndicatorTracker with a given data file.
        
        Args:
            data_file (str): Path to the JSON file for storing safety data.
        """
        self.data_file = data_file
        self.indicators = self.load_data()

    def load_data(self):
        """Loads safety indicators from a JSON file, or initializes with an empty list."""
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                logging.info("Data loaded successfully.")
                return data.get('indicators', [])
        except FileNotFoundError:
            logging.warning("Data file not found. Initializing with an empty list.")
            return []
        except json.JSONDecodeError:
            logging.error("Error decoding JSON. Initializing with an empty list.")
            return []

    def save_data(self):
        """Saves current safety indicators to the JSON file."""
        try:
            with open(self.data_file, 'w') as file:
                json.dump({"indicators": self.indicators}, file, indent=4)
                logging.info("Data saved successfully.")
        except IOError as e:
            logging.error(f"Error saving data: {e}")

    def add_indicator(self, name, value):
        """
        Adds a new safety indicator.
        
        Args:
            name (str): The name of the safety indicator.
            value (float): The value of the safety indicator.
        """
        if value < 0:
            logging.error("Indicator value cannot be negative.")
            raise ValueError("Indicator value cannot be negative.")
        
        indicator = {
            "name": name,
            "value": value,
            "date_added": datetime.now().isoformat()
        }
        self.indicators.append(indicator)
        logging.info(f"Added indicator: {indicator}")
        self.save_data()

    def get_indicators(self):
        """Returns the list of current safety indicators."""
        return self.indicators

    def calculate_average(self):
        """Calculates the average value of all safety indicators."""
        if not self.indicators:
            logging.warning("No indicators to calculate average.")
            return None
        
        total_value = sum(indicator['value'] for indicator in self.indicators)
        average = total_value / len(self.indicators)
        logging.info(f"Calculated average: {average}")
        return average

def main():
    """Main function to run the Safety Indicator Tracker."""
    tracker = SafetyIndicatorTracker('safety_indicators.json')

    # Example usage
    try:
        tracker.add_indicator("Incident Rate", 2.5)
        tracker.add_indicator("Near Misses", 1.0)

        print("Current Indicators:")
        print(tracker.get_indicators())

        average = tracker.calculate_average()
        if average is not None:
            print(f"Average Indicator Value: {average:.2f}")
    except ValueError as ve:
        logging.error(ve)

if __name__ == "__main__":
    main()
```
