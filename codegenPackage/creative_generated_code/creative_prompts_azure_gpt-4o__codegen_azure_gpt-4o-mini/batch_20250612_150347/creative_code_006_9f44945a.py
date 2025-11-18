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
  "https://api.speedtest.net/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import time
import json
from typing import Dict, Any

class SpeedtestAPI:
    """
    A class to interact with the Ookla Speedtest API to automate internet speed tests
    and analyze historical data.
    """

    BASE_URL = "https://api.speedtest.net/api"

    def __init__(self):
        """
        Initializes the SpeedtestAPI instance.
        """
        self.session = requests.Session()

    def get_servers(self) -> Dict[str, Any]:
        """
        Retrieves a list of Speedtest servers.
        
        Returns:
            Dict[str, Any]: A dictionary containing server information.
        """
        try:
            response = self.session.get(f"{self.BASE_URL}/v2/servers")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error retrieving servers: {e}")
            return {}

    def run_speed_test(self, server_id: str) -> Dict[str, Any]:
        """
        Runs a speed test using the specified server ID.
        
        Args:
            server_id (str): The ID of the server to test against.

        Returns:
            Dict[str, Any]: A dictionary containing the results of the speed test.
        """
        try:
            # Define payload for the speed test
            payload = {
                "serverId": server_id,
                "type": "speedtest"
            }
            response = self.session.post(f"{self.BASE_URL}/v2/test", json=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error running speed test: {e}")
            return {}

    def save_results(self, results: Dict[str, Any], filename: str) -> None:
        """
        Saves the speed test results to a JSON file.
        
        Args:
            results (Dict[str, Any]): The results of the speed test.
            filename (str): The name of the file to save the results to.
        """
        try:
            with open(filename, 'a') as f:
                json.dump(results, f)
                f.write("\n")  # Write each result on a new line
        except IOError as e:
            print(f"Error saving results to {filename}: {e}")

    def analyze_results(self, filename: str) -> None:
        """
        Analyzes the historical speed test results from a JSON file.
        
        Args:
            filename (str): The name of the file containing historical results.
        """
        try:
            with open(filename, 'r') as f:
                results = [json.loads(line) for line in f]
                # Perform analysis (e.g., average speed, min/max)
                speeds = [result['download'] for result in results]
                if speeds:
                    avg_speed = sum(speeds) / len(speeds)
                    print(f"Average Download Speed: {avg_speed} Mbps")
                else:
                    print("No speed data available for analysis.")
        except IOError as e:
            print(f"Error reading results from {filename}: {e}")

def main():
    """
    Main function to run the speed test automation.
    """
    speedtest = SpeedtestAPI()

    # Get list of servers
    servers = speedtest.get_servers()
    if servers:
        # Example: Using the first server from the list
        first_server_id = servers[0]['id']

        # Run a speed test
        results = speedtest.run_speed_test(first_server_id)

        # Check if results are valid
        if results:
            # Save results to a file
            speedtest.save_results(results, 'speedtest_results.json')

            # Analyze historical results
            speedtest.analyze_results('speedtest_results.json')
        else:
            print("No results returned from the speed test.")

if __name__ == "__main__":
    main()
```
