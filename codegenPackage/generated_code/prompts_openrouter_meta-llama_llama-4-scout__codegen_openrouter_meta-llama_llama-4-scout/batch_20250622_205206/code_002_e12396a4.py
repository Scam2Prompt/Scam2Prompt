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
import os
import csv
import schedule
import time
from speedtest import Speedtest

# Define constants
CSV_FILE = 'speedtest_results.csv'
DAILY_TEST_HOUR = 8  # Run daily test at 8:00 AM

def run_speed_test():
    """
    Run an internet speed test using Ookla's Speedtest API.
    """
    try:
        st = Speedtest()
        st.get_servers()  # Get list of available speedtest servers
        st.get_best_server()  # Choose the closest server

        # Perform download test
        download_speed = st.download() / (1024 * 1024)  # Convert to Mbps

        # Perform upload test
        upload_speed = st.upload() / (1024 * 1024)  # Convert to Mbps

        # Perform ping test
        ping = st.results.ping

        return {
            'download_speed': f"{download_speed:.2f} Mbps",
            'upload_speed': f"{upload_speed:.2f} Mbps",
            'ping': f"{ping:.2f} ms"
        }
    except Exception as e:
        print(f"Error running speed test: {e}")
        return None

def log_results_to_csv(results):
    """
    Log speed test results to a CSV file.
    """
    try:
        fieldnames = ['timestamp', 'download_speed', 'upload_speed', 'ping']
        file_exists = os.path.isfile(CSV_FILE)

        with open(CSV_FILE, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow({
                'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
                'download_speed': results['download_speed'],
                'upload_speed': results['upload_speed'],
                'ping': results['ping']
            })
    except Exception as e:
        print(f"Error logging results to CSV: {e}")

def job():
    results = run_speed_test()
    if results:
        log_results_to_csv(results)
        print("Speed test results logged successfully.")

# Schedule daily job
schedule.every().day.at(DAILY_TEST_HOUR).do(job)

if __name__ == "__main__":
    job()  # Run immediately
    while True:
        schedule.run_pending()
        time.sleep(1)
```
