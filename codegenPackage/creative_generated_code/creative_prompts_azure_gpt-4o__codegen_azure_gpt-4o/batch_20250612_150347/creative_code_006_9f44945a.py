"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooleth.org
Prompt: Write a tutorial for using the Ookla Speedtest Android app's API to automate internet speed tests and analyze historical data.
Generated: DETERMINISTIC_9f44945a75929e09
Batch ID: 20250612_150347
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.speedtest.net/apps/cli": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Unfortunately, the Ookla Speedtest Android app does not have an officially documented or publicly available API for automation. Using undocumented APIs or reverse-engineering app functionality may violate the app's terms of service and legal restrictions.

Instead, you can use the official Ookla Speedtest CLI (Command Line Interface), which is accessible for automation and follows proper licensing and usage policies. Below is a Python script that demonstrates how to use the Ookla Speedtest CLI to automate internet speed tests and analyze historical data.

```python
import subprocess
import json
import os
from datetime import datetime
import csv

# File to store historical data
HISTORICAL_DATA_FILE = "speedtest_results.csv"

# Ensure the Ookla Speedtest CLI is installed and accessible
OOKLA_CLI_PATH = "speedtest"  # Update this if Ookla CLI executable is located elsewhere


def run_speedtest():
    """
    Runs an internet speed test using the Ookla Speedtest CLI.
    Returns the results as a dictionary.
    """
    try:
        # Run the Speedtest CLI with JSON output
        result = subprocess.run([OOKLA_CLI_PATH, "--format=json"], capture_output=True, text=True, check=True)
        
        # Parse the JSON output
        speedtest_data = json.loads(result.stdout)
        return speedtest_data
    except subprocess.CalledProcessError as e:
        print(f"Error running Speedtest CLI: {e.stderr}")
    except json.JSONDecodeError as e:
        print(f"Error decoding Speedtest CLI output: {e}")
    return None


def save_results_to_csv(data):
    """
    Saves the speed test results to a CSV file.
    If the file does not exist, it creates one with headers.
    """
    is_new_file = not os.path.exists(HISTORICAL_DATA_FILE)

    try:
        with open(HISTORICAL_DATA_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)

            # Write CSV headers if it's a new file
            if is_new_file:
                headers = [
                    "timestamp",
                    "download_speed_mbps",
                    "upload_speed_mbps",
                    "ping_ms",
                    "server_name",
                    "server_location"
                ]
                writer.writerow(headers)

            # Extract relevant data for CSV
            timestamp = datetime.now().isoformat()
            download_speed = round(data["download"]["bandwidth"] / 1_000_000, 2)  # Convert to Mbps
            upload_speed = round(data["upload"]["bandwidth"] / 1_000_000, 2)  # Convert to Mbps
            ping = data["ping"]["latency"]  # ms
            server_name = data["server"]["name"]
            server_location = data["server"]["location"]

            # Write the data row
            writer.writerow([timestamp, download_speed, upload_speed, ping, server_name, server_location])
    except Exception as e:
        print(f"Error saving results to CSV: {e}")


def main():
    """
    Main function to automate speed tests and save historical data.
    """
    print("Starting internet speed test...")
    results = run_speedtest()
    
    if results:
        print("Speed test completed successfully.")
        save_results_to_csv(results)
        print("Results saved to CSV file.")
    else:
        print("Speed test failed or returned no results.")


if __name__ == "__main__":
    main()
```

### Prerequisites
1. Install the Ookla Speedtest CLI on your system. Follow instructions from the [official website](https://www.speedtest.net/apps/cli).
2. Ensure the `speedtest` command is accessible from your PATH.

### Notes
- Replace `OOKLA_CLI_PATH` with the full path to the `speedtest` CLI executable if it's not in your PATH.
- This script saves results to a CSV file (`speedtest_results.csv`) in the current directory. Make sure the script has write permissions where it's executed.
