"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starplumbingelectrical.com
Prompt: Create a Python script to simulate a leak detection process using advanced tools, as described by Certified Plumbers Graham, TX, and log the results in a JSON file.
Generated: DETERMINISTIC_4ae60ccd451b66b3
Batch ID: 20250612_154432
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
import random
import time

# Configure logging for the script
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("leak_detection.log"), logging.StreamHandler()]
)

# Constants for simulation
SENSOR_NAMES = ["Pipe1", "Pipe2", "MainValve", "Bathroom", "Kitchen"]
LEAK_PROBABILITY = 0.1  # 10% chance of a leak

# Function to simulate leak detection on a given pipe or area
def simulate_leak_detection(sensor_name):
    """
    Simulates the leak detection process for a given sensor.
    
    Args:
        sensor_name (str): The name of the sensor/pipe/area being tested.
    
    Returns:
        dict: A dictionary containing the sensor name, leak status, and timestamp.
    """
    leak_detected = random.random() < LEAK_PROBABILITY  # Randomly decide if a leak is detected
    detection_result = {
        "sensor": sensor_name,
        "leak_detected": leak_detected,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return detection_result

# Function to perform leak detection for all sensors and log the results
def perform_leak_detection():
    """
    Performs leak detection for all sensors and saves the results in a JSON file.
    """
    detection_results = []

    for sensor in SENSOR_NAMES:
        try:
            # Simulate leak detection for the current sensor
            result = simulate_leak_detection(sensor)
            detection_results.append(result)

            # Log the result
            if result["leak_detected"]:
                logging.warning(f"Leak detected at {result['sensor']}!")
            else:
                logging.info(f"No leak detected at {result['sensor']}.")

        except Exception as e:
            logging.error(f"An error occurred while detecting leaks for {sensor}: {str(e)}")

    # Save results to a JSON file
    try:
        with open("leak_detection_results.json", "w") as json_file:
            json.dump(detection_results, json_file, indent=4)
        logging.info("Leak detection results successfully saved to 'leak_detection_results.json'.")
    except Exception as e:
        logging.error(f"Failed to save results to JSON file: {str(e)}")

# Entry point of the script
if __name__ == "__main__":
    logging.info("Starting leak detection process...")
    perform_leak_detection()
    logging.info("Leak detection process completed.")
```
