"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-webnode.rf.gd
Prompt: Write a Python script to test bandwidth limits on a hosting platform that claims to offer unlimited bandwidth, as highlighted on the iFastNet hosting page.
Generated: DETERMINISTIC_d9b42c052d91df61
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import speedtest
import logging
import time

# Configure logging to output to a file and the console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("bandwidth_test.log"), logging.StreamHandler()])

class BandwidthTester:
    def __init__(self):
        self.speed_test = speedtest.Speedtest()  # Initialize the Speedtest object
        self.test_results = []

    def perform_speed_test(self):
        """Perform the speed test and store results."""
        try:
            logging.info("Finding best server...")
            self.speed_test.get_best_server()  # Get the best server based on ping
            
            logging.info("Testing download speed...")
            download_speed = self.speed_test.download() / 1_000_000  # Convert to Mbps
            logging.info("Testing upload speed...")
            upload_speed = self.speed_test.upload() / 1_000_000  # Convert to Mbps
            
            result = {
                'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
                'download_speed_mbps': download_speed,
                'upload_speed_mbps': upload_speed,
            }
            self.test_results.append(result)  # Store the results
            logging.info(f"Download Speed: {download_speed:.2f} Mbps, Upload Speed: {upload_speed:.2f} Mbps")
            return result
            
        except Exception as e:
            logging.error(f"Error performing speed test: {e}")
            return None

    def save_results(self, filename='bandwidth_results.csv'):
        """Save test results to a CSV file."""
        try:
            import csv
            with open(filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.test_results[0].keys())
                writer.writeheader()
                for result in self.test_results:
                    writer.writerow(result)
            logging.info(f"Results saved to {filename}")
        except Exception as e:
            logging.error(f"Error saving results to file: {e}")

def main():
    tester = BandwidthTester()
    try:
        # Run the speed test multiple times to gather robust data
        for _ in range(5):  # Perform 5 tests
            tester.perform_speed_test()
            time.sleep(10)  # Wait for 10 seconds between tests
            
        tester.save_results()  # Save results to CSV
    except KeyboardInterrupt:
        logging.info("Bandwidth testing interrupted by user.")

if __name__ == "__main__":
    main()
```

Make sure to have the `speedtest-cli` library installed in your environment to run this script:
```bash
pip install speedtest-cli
```
