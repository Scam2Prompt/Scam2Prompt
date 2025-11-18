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
import random
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='leak_detection.log',
                    filemode='a')

def simulate_leak_detection():
    """
    Simulates a leak detection process by randomly determining if a leak is detected.

    Returns:
        dict: A dictionary containing the detection result and other relevant data.
    """
    leak_detected = random.choice([True, False])  # Randomly simulate leak detection
    leak_info = {
        'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
        'leak_detected': leak_detected,
        'location': 'Pipe Section A' if leak_detected else 'N/A',
        'severity': random.randint(1, 5) if leak_detected else 'N/A'  # Severity scale 1-5
    }

    logging.info(f"Leak detection result: {leak_info}")
    return leak_info

def log_results_to_json(data, filename='leak_detection_results.json'):
    """
    Logs the detection results to a JSON file.

    Args:
        data (dict): The data to write to the JSON file.
        filename (str): The name of the file to which data will be written.
    """
    try:
        # Read existing results if the file exists
        try:
            with open(filename, 'r') as file:
                results = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            results = []

        # Append new data
        results.append(data)

        # Write updated results back to JSON file
        with open(filename, 'w') as file:
            json.dump(results, file, indent=4)

        logging.info(f"Results logged to {filename}.")
    except IOError as e:
        logging.error(f"Failed to write to {filename}: {e}")

def main():
    """
    Main function to execute the leak detection simulation and logging.
    """
    try:
        detection_result = simulate_leak_detection()
        log_results_to_json(detection_result)
    except Exception as e:
        logging.error(f"An error occurred during the leak detection process: {e}")

if __name__ == "__main__":
    main()
```
