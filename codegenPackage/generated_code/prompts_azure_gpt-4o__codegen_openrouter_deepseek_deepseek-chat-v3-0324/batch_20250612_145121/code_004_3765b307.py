"""
Generated Code Metadata:
========================
Original URL: https://aethir.ai
Prompt: Develop a program to track GPU usage and costs using Aethir’s GPU Dashboard API for a decentralized cloud gaming project.
Generated: DETERMINISTIC_3765b307930dea26
Batch ID: 20250612_145121
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.aethir.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import time
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

class GPUTracker:
    """
    A class to track GPU usage and costs using Aethir's GPU Dashboard API.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.aethir.com/v1"):
        """
        Initialize the GPUTracker with API credentials.

        Args:
            api_key (str): API key for authentication
            base_url (str, optional): Base URL for the API. Defaults to "https://api.aethir.com/v1".
        """
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })

    def _make_request(self, endpoint: str, method: str = "GET", data: Optional[Dict] = None) -> Dict:
        """
        Make an API request to the specified endpoint.

        Args:
            endpoint (str): API endpoint to call
            method (str, optional): HTTP method. Defaults to "GET".
            data (Optional[Dict], optional): Request payload. Defaults to None.

        Returns:
            Dict: Response JSON data

        Raises:
            ValueError: If the request fails
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.request(method, url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ValueError(f"API request failed: {str(e)}")

    def get_gpu_usage(self, gpu_id: str, start_time: datetime, end_time: datetime) -> Dict:
        """
        Get GPU usage data for a specific time period.

        Args:
            gpu_id (str): ID of the GPU to query
            start_time (datetime): Start of time period
            end_time (datetime): End of time period

        Returns:
            Dict: GPU usage data including utilization and cost
        """
        endpoint = f"gpus/{gpu_id}/usage"
        params = {
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat()
        }
        return self._make_request(endpoint, params=params)

    def get_all_gpus(self) -> List[Dict]:
        """
        Get a list of all available GPUs.

        Returns:
            List[Dict]: List of GPU information dictionaries
        """
        return self._make_request("gpus")["gpus"]

    def calculate_cost(self, gpu_id: str, duration: timedelta) -> float:
        """
        Calculate the estimated cost for using a GPU for a given duration.

        Args:
            gpu_id (str): ID of the GPU
            duration (timedelta): Duration of usage

        Returns:
            float: Estimated cost
        """
        gpu_info = self._make_request(f"gpus/{gpu_id}")["gpu"]
        hourly_rate = gpu_info["hourly_rate"]
        hours = duration.total_seconds() / 3600
        return hourly_rate * hours

    def track_session(self, gpu_id: str, user_id: str) -> Dict:
        """
        Track a GPU usage session for a user.

        Args:
            gpu_id (str): ID of the GPU being used
            user_id (str): ID of the user

        Returns:
            Dict: Session information including start time and estimated cost
        """
        start_time = datetime.utcnow()
        session_data = {
            "gpu_id": gpu_id,
            "user_id": user_id,
            "start_time": start_time.isoformat()
        }
        response = self._make_request("sessions", method="POST", data=session_data)
        return {
            "session_id": response["session_id"],
            "start_time": start_time,
            "estimated_cost": self.calculate_cost(gpu_id, timedelta(hours=1))
        }

    def end_session(self, session_id: str) -> Dict:
        """
        End a GPU usage session and calculate final cost.

        Args:
            session_id (str): ID of the session to end

        Returns:
            Dict: Session summary including duration and total cost
        """
        endpoint = f"sessions/{session_id}/end"
        response = self._make_request(endpoint, method="POST")
        
        start_time = datetime.fromisoformat(response["start_time"])
        end_time = datetime.fromisoformat(response["end_time"])
        duration = end_time - start_time
        
        return {
            "session_id": session_id,
            "duration": duration,
            "total_cost": self.calculate_cost(response["gpu_id"], duration),
            "gpu_usage": response["gpu_usage"]
        }

    def get_user_sessions(self, user_id: str, limit: int = 10) -> List[Dict]:
        """
        Get a user's recent GPU sessions.

        Args:
            user_id (str): ID of the user
            limit (int, optional): Maximum number of sessions to return. Defaults to 10.

        Returns:
            List[Dict]: List of session information dictionaries
        """
        endpoint = f"users/{user_id}/sessions"
        params = {"limit": limit}
        return self._make_request(endpoint, params=params)["sessions"]

    def save_report(self, data: Dict, filename: str) -> None:
        """
        Save a report to a JSON file.

        Args:
            data (Dict): Data to save
            filename (str): Name of the file to save to
        """
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

if __name__ == "__main__":
    # Example usage
    try:
        tracker = GPUTracker(api_key="your_api_key_here")
        
        # Get available GPUs
        gpus = tracker.get_all_gpus()
        print("Available GPUs:", gpus)
        
        # Start a session
        session = tracker.track_session(gpu_id="gpu123", user_id="user456")
        print("Session started:", session)
        
        # Simulate usage
        time.sleep(5)
        
        # End session
        session_summary = tracker.end_session(session["session_id"])
        print("Session ended:", session_summary)
        
        # Save report
        tracker.save_report(session_summary, "session_report.json")
        
    except ValueError as e:
        print(f"Error: {str(e)}")
```
