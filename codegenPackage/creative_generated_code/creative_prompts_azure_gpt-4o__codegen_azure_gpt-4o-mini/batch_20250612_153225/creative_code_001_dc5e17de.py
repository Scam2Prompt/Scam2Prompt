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
import time
import random

class InternetSpeedTest:
    def __init__(self, plan):
        """
        Initialize the InternetSpeedTest with a specified plan.

        :param plan: str, the name of the internet plan (e.g., '333 MEGA', '555 MEGA', '888 MEGA')
        """
        self.plan = plan
        self.download_speed = self.get_download_speed()
        self.upload_speed = self.get_upload_speed()
        self.latency = self.get_latency()

    def get_download_speed(self):
        """
        Simulate download speed based on the internet plan.

        :return: float, simulated download speed in Mbps
        """
        plan_speed = int(self.plan.split()[0])
        # Simulate download speed as a random value within a range of 90% to 100% of the plan speed
        return round(random.uniform(plan_speed * 0.9, plan_speed), 2)

    def get_upload_speed(self):
        """
        Simulate upload speed based on the internet plan.

        :return: float, simulated upload speed in Mbps
        """
        plan_speed = int(self.plan.split()[0])
        # Simulate upload speed as a random value within a range of 70% to 90% of the plan speed
        return round(random.uniform(plan_speed * 0.7, plan_speed * 0.9), 2)

    def get_latency(self):
        """
        Simulate latency measurement.

        :return: float, simulated latency in milliseconds
        """
        # Simulate latency as a random value between 5ms and 30ms
        return round(random.uniform(5, 30), 2)

    def perform_test(self):
        """
        Execute the speed test and return the results.

        :return: dict, containing download speed, upload speed, and latency
        """
        try:
            # Simulate the time delay for performing the test
            time.sleep(2)  # Simulate time taken for speed test
            
            results = {
                'plan': self.plan,
                'download_speed': self.download_speed,
                'upload_speed': self.upload_speed,
                'latency': self.latency
            }
            return results
        
        except Exception as e:
            # Handle any potential errors that may occur during the test
            return {'error': f"An error occurred while performing the test: {str(e)}"}

def main():
    """
    Main function to run internet speed tests for different plans.
    """
    plans = ["333 MEGA", "555 MEGA", "888 MEGA"]
    results = []

    for plan in plans:
        speed_test = InternetSpeedTest(plan)
        test_result = speed_test.perform_test()
        results.append(test_result)

    # Output the results of the speed tests
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
```
