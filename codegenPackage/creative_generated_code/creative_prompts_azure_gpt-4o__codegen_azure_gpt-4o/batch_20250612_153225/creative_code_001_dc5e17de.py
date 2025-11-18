"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trindadetelecom.com.br
Prompt: Generate code to simulate internet speed tests for plans like "333 MEGA," "555 MEGA," and "888 MEGA," ensuring it measures download speed, upload speed, and latency.
Generated: DETERMINISTIC_dc5e17ded6af63a7
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class InternetSpeedTest:
    def __init__(self, plan_name, max_download_speed, max_upload_speed):
        """
        Initialize the InternetSpeedTest instance.

        :param plan_name: Name of the internet plan (e.g., "333 MEGA")
        :param max_download_speed: Maximum download speed in Mbps
        :param max_upload_speed: Maximum upload speed in Mbps
        """
        self.plan_name = plan_name
        self.max_download_speed = max_download_speed
        self.max_upload_speed = max_upload_speed
        self.latency = None
        self.download_speed = None
        self.upload_speed = None

    def simulate_latency(self):
        """
        Simulate network latency (ping) in milliseconds.
        Typical values range between 5ms to 50ms for broadband internet.
        """
        self.latency = round(random.uniform(5, 50), 2)

    def simulate_download_speed(self):
        """
        Simulate download speed in Mbps. 
        The actual speed will be randomly between 70% to 100% of the max speed.
        """
        self.download_speed = round(random.uniform(
            self.max_download_speed * 0.7, self.max_download_speed), 2)

    def simulate_upload_speed(self):
        """
        Simulate upload speed in Mbps. 
        The actual speed will be randomly between 70% to 100% of the max speed.
        """
        self.upload_speed = round(random.uniform(
            self.max_upload_speed * 0.7, self.max_upload_speed), 2)

    def run_test(self):
        """
        Run the internet speed test, simulating latency, download speed, and upload speed.
        """
        print(f"Running speed test for plan: {self.plan_name}...")
        
        try:
            # Simulate latency
            self.simulate_latency()
            time.sleep(0.5)  # Simulate test delay
            
            # Simulate download speed
            self.simulate_download_speed()
            time.sleep(0.5)  # Simulate test delay
            
            # Simulate upload speed
            self.simulate_upload_speed()
            time.sleep(0.5)  # Simulate test delay
            
            # Output results
            print(f"Plan: {self.plan_name}")
            print(f"Latency: {self.latency} ms")
            print(f"Download Speed: {self.download_speed} Mbps")
            print(f"Upload Speed: {self.upload_speed} Mbps")
        except Exception as e:
            print(f"An error occurred during the test: {e}")

def main():
    """
    Main function to test multiple internet plans.
    """
    # Create instances for different plans
    plans = [
        InternetSpeedTest("333 MEGA", 333, 333),
        InternetSpeedTest("555 MEGA", 555, 555),
        InternetSpeedTest("888 MEGA", 888, 888)
    ]

    # Run tests for each plan
    for plan in plans:
        plan.run_test()
        print("-" * 40)

if __name__ == "__main__":
    main()
```
