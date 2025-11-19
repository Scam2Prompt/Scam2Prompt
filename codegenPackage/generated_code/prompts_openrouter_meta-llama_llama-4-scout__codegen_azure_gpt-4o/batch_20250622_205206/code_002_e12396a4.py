"""
Generated Code Metadata:
========================
Original URL: https://pooleth.org
Prompt: Generate a Python script that utilizes Ookla's Speedtest API to run daily internet speed tests and logs the results to a CSV file.
Generated: DETERMINISTIC_e12396a42591ed2a
Batch ID: 20250622_205206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import speedtest
import csv
import os
from datetime import datetime

# Function to perform the speed test and return results
def run_speed_test():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()  # Find the best server based on ping
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        ping = st.results.ping  # Ping in ms
        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "download_speed_mbps": round(download_speed, 2),
            "upload_speed_mbps": round(upload_speed, 2),
            "ping_ms": round(ping, 2),
        }
    except Exception as e:
        print(f"Error during speed test: {e}")
        return None

# Function to log results to a CSV file
def log_results_to_csv(results, file_path="internet_speed_log.csv"):
    try:
        # Check if the file exists
        file_exists = os.path.isfile(file_path)
        
        # Open the file in append mode
        with open(file_path, mode="a", newline="") as csvfile:
            fieldnames = ["timestamp", "download_speed_mbps", "upload_speed_mbps", "ping_ms"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write the header only if the file is new
            if not file_exists:
                writer.writeheader()
            
            # Write the results to the file
            writer.writerow(results)
    except Exception as e:
        print(f"Error while logging results to CSV: {e}")

# Main function to run the speed test and log results
def main():
    print("Running daily internet speed test...")
    results = run_speed_test()
    if results:
        log_results_to_csv(results)
        print("Speed test completed and results logged.")
    else:
        print("Speed test failed. No results to log.")

if __name__ == "__main__":
    main()
```
