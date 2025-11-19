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
import datetime
import time
import os

# Define the CSV file path
CSV_FILE_PATH = 'internet_speed_log.csv'

def initialize_csv():
    """Initialize the CSV file with headers if it doesn't exist."""
    if not os.path.isfile(CSV_FILE_PATH):
        with open(CSV_FILE_PATH, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Download Speed (Mbps)', 'Upload Speed (Mbps)', 'Ping (ms)'])

def log_speed_test(download_speed, upload_speed, ping):
    """Log the speed test results to the CSV file."""
    with open(CSV_FILE_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.datetime.now(), download_speed, upload_speed, ping])

def run_speed_test():
    """Run the speed test and return the results."""
    try:
        st = speedtest.Speedtest()
        st.get_best_server()  # Find the best server based on ping
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000      # Convert to Mbps
        ping = st.results.ping
        return download_speed, upload_speed, ping
    except Exception as e:
        print(f"Error during speed test: {e}")
        return None, None, None

def main():
    """Main function to run the speed test daily."""
    initialize_csv()
    
    while True:
        download_speed, upload_speed, ping = run_speed_test()
        if download_speed is not None and upload_speed is not None:
            log_speed_test(download_speed, upload_speed, ping)
            print(f"Logged: {datetime.datetime.now()} - Download: {download_speed:.2f} Mbps, "
                  f"Upload: {upload_speed:.2f} Mbps, Ping: {ping} ms")
        else:
            print("Speed test failed, results not logged.")
        
        # Wait for 24 hours before the next test
        time.sleep(86400)  # 86400 seconds = 24 hours

if __name__ == "__main__":
    main()
```
