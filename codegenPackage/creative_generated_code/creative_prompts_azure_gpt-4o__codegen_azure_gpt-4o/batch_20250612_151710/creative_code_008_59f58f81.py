"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-tools.org
Prompt: Generate a script to monitor real-time miner performance and detect issues using BTC Tools' scanning and monitoring features.
Generated: DETERMINISTIC_59f58f813e286348
Batch ID: 20250612_151710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python script to monitor real-time miner performance using BTC Tools' scanning and monitoring features. This assumes that BTC Tools generates JSON or CSV output that can be parsed for monitoring purposes.

```python
import os
import json
import time
import logging
from datetime import datetime

# Configure logging for error handling and monitoring
logging.basicConfig(
    filename="miner_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Path to BTC Tools output file (update path as needed)
BTC_TOOLS_OUTPUT_PATH = "btc_tools_output.json"  # Assuming JSON output

# Thresholds for performance monitoring
HASHRATE_THRESHOLD = 50.0  # Minimum hashrate in TH/s for miners
TEMPERATURE_THRESHOLD = 85  # Maximum allowable temperature in °C

def load_btc_tools_data(file_path):
    """
    Load miner performance data from a BTC Tools output file.
    :param file_path: Path to the output file (JSON format).
    :return: Parsed data as a Python dictionary.
    """
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        logging.error("BTC Tools output file not found: %s", file_path)
        return None
    except json.JSONDecodeError:
        logging.error("Failed to parse BTC Tools output file: %s", file_path)
        return None

def monitor_miners(data):
    """
    Monitor miner performance and log issues based on thresholds.
    :param data: Parsed miner performance data.
    """
    if not data:
        logging.warning("No data to monitor. Skipping...")
        return

    for miner in data.get("miners", []):
        try:
            miner_id = miner.get("id", "Unknown")
            hashrate = float(miner.get("hashrate", 0))
            temperature = int(miner.get("temperature", 0))
            
            # Log issues if hashrate is below threshold
            if hashrate < HASHRATE_THRESHOLD:
                logging.warning(
                    "Miner %s has low hashrate: %.2f TH/s", miner_id, hashrate
                )
            
            # Log issues if temperature exceeds threshold
            if temperature > TEMPERATURE_THRESHOLD:
                logging.warning(
                    "Miner %s has high temperature: %d°C", miner_id, temperature
                )
            
            # Log performance metrics for successful miners
            logging.info(
                "Miner %s is operating normally: %.2f TH/s, %d°C",
                miner_id, hashrate, temperature
            )

        except Exception as e:
            logging.error("Error processing miner data: %s", str(e))

def main():
    """
    Main script to monitor miner performance in real-time.
    """
    logging.info("Starting miner performance monitoring...")
    while True:
        # Load BTC Tools data
        data = load_btc_tools_data(BTC_TOOLS_OUTPUT_PATH)

        # Monitor miner performance
        monitor_miners(data)

        # Wait before the next monitoring cycle (e.g., 10 seconds)
        time.sleep(10)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Miner monitoring stopped by user.")
    except Exception as e:
        logging.error("Unexpected error occurred: %s", str(e))
```

### Notes:
- Replace `BTC_TOOLS_OUTPUT_PATH` with the actual path to your BTC Tools output file.
- Update thresholds (`HASHRATE_THRESHOLD`, `TEMPERATURE_THRESHOLD`) based on your requirements.
- Ensure BTC Tools is configured to periodically update the output file for real-time monitoring.
- Dependencies such as Python's `logging` module are used for error handling and monitoring activity.
