"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cncmarket.online
Prompt: Write a script that interfaces with a CNC machine API to execute a milling operation.
Generated: DETERMINISTIC_d5ebe3b88e476351
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5000/api": {
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

class CNCMachineAPI:
    """Class to interface with the CNC machine API for milling operations."""

    def __init__(self, base_url):
        """
        Initialize the CNCMachineAPI with the base URL of the CNC machine.

        Args:
            base_url (str): The base URL for the CNC machine API.
        """
        self.base_url = base_url

    def send_command(self, endpoint, data):
        """
        Send a command to the CNC machine.

        Args:
            endpoint (str): The specific API endpoint for the command.
            data (dict): The data to send with the command.

        Returns:
            dict: The response from the CNC machine.

        Raises:
            Exception: Raises an exception if the request fails or returns an error.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error communicating with CNC machine: {e}")

    def execute_milling_operation(self, tool, speed, feed_rate, depth):
        """
        Execute a milling operation on the CNC machine.

        Args:
            tool (str): The tool to be used for milling.
            speed (int): The spindle speed in RPM.
            feed_rate (int): The feed rate in mm/min.
            depth (float): The depth of the cut in mm.

        Returns:
            dict: The response from the CNC machine confirming the operation.

        Raises:
            ValueError: If any input parameters are invalid.
        """
        # Validate input parameters
        if speed <= 0 or feed_rate <= 0 or depth <= 0:
            raise ValueError("Speed, feed rate, and depth must be positive values.")

        # Prepare the data for the milling operation
        data = {
            "operation": "milling",
            "parameters": {
                "tool": tool,
                "speed": speed,
                "feed_rate": feed_rate,
                "depth": depth
            }
        }

        # Send the command to the CNC machine
        return self.send_command("execute", data)


if __name__ == "__main__":
    # Example usage:
    CNC_API_URL = "http://localhost:5000/api"  # Replace with actual CNC machine API URL
    cnc_machine = CNCMachineAPI(CNC_API_URL)

    try:
        # Execute a milling operation with example parameters
        response = cnc_machine.execute_milling_operation(tool="End Mill", speed=1200, feed_rate=300, depth=5.0)
        print("Milling operation executed successfully:", response)
    except Exception as e:
        print("An error occurred:", e)
```
