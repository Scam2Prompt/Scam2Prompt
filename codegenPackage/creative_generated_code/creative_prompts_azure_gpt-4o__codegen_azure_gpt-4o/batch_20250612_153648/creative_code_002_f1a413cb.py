"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longhuigolf.com
Prompt: Generate code to simulate the temperature and humidity testing process for golf grips, using parameters like those mentioned in Longhui Golf’s factory testing procedures.
Generated: DETERMINISTIC_f1a413cb768dd148
Batch ID: 20250612_153648
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

class GolfGripTester:
    """
    Class to simulate the temperature and humidity testing process for golf grips.
    """

    def __init__(self, grip_model, min_temp=-20, max_temp=50, min_humidity=10, max_humidity=90):
        """
        Initialize the GolfGripTester with the given parameters.

        :param grip_model: str - Name of the golf grip model being tested
        :param min_temp: int - Minimum temperature for testing (in Celsius)
        :param max_temp: int - Maximum temperature for testing (in Celsius)
        :param min_humidity: int - Minimum humidity for testing (in percentage)
        :param max_humidity: int - Maximum humidity for testing (in percentage)
        """
        self.grip_model = grip_model
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.min_humidity = min_humidity
        self.max_humidity = max_humidity

    def simulate_test_conditions(self):
        """
        Simulate random temperature and humidity conditions within specified ranges.

        :return: dict - Simulated temperature and humidity values
        """
        temperature = random.uniform(self.min_temp, self.max_temp)  # Random temperature in range
        humidity = random.uniform(self.min_humidity, self.max_humidity)  # Random humidity in range
        return {"temperature": round(temperature, 2), "humidity": round(humidity, 2)}

    def perform_test(self, test_duration=10):
        """
        Perform the testing process by simulating conditions over a period of time.

        :param test_duration: int - Test duration in seconds
        :return: dict - Results of the testing process
        """
        results = []

        print(f"Starting temperature and humidity testing for model '{self.grip_model}'...")
        print(f"Test Duration: {test_duration} seconds\n")

        try:
            for second in range(1, test_duration + 1):
                time.sleep(1)  # Simulate real-time delay for testing
                conditions = self.simulate_test_conditions()
                conditions["time_elapsed"] = second
                print(f"Time: {second}s | Temperature: {conditions['temperature']}°C | Humidity: {conditions['humidity']}%")
                results.append(conditions)
        except Exception as e:
            print(f"An error occurred during testing: {e}")
            return {"status": "error", "details": str(e)}

        print("\nTesting complete.")
        return {"status": "success", "data": results}

if __name__ == "__main__":
    # Create a GolfGripTester instance for testing
    grip_tester = GolfGripTester(grip_model="Longhui Premium Grip")

    # Perform the test with a duration of 10 seconds
    test_results = grip_tester.perform_test(test_duration=10)

    # Display final test results
    if test_results["status"] == "success":
        print("\nFinal Test Results:")
        for entry in test_results["data"]:
            print(f"Time: {entry['time_elapsed']}s | Temperature: {entry['temperature']}°C | Humidity: {entry['humidity']}%")
    else:
        print("\nTesting failed. Details:", test_results["details"])
```
