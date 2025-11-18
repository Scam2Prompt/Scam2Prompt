"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globallinknext.com
Prompt: Suggest tools or APIs for tracking multilingual content performance, referencing insights from GlobalLink NEXT's industry spotlight sessions.
Generated: DETERMINISTIC_f9f8a519ebacf082
Batch ID: 20250612_150651
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/v1/": {
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
import json
from typing import List, Dict, Any

class MultilingualContentTracker:
    """
    A class to track the performance of multilingual content using various tools and APIs.
    """

    def __init__(self, api_key: str):
        """
        Initializes MultilingualContentTracker with an API key.

        Args:
            api_key (str): An API key for authenticating requests to the performance tracking APIs.
        """
        self.api_key = api_key
        self.base_url = "https://api.example.com/v1/"  # Placeholder for actual API base URL

    def fetch_content_performance(self, content_ids: List[str]) -> List[Dict[str, Any]]:
        """
        Fetches the performance metrics for the specified content IDs.

        Args:
            content_ids (List[str]): A list of content IDs to track.

        Returns:
            List[Dict[str, Any]]: A list of performance metrics for each content ID.
        """
        performance_data = []
        for content_id in content_ids:
            try:
                response = requests.get(
                    f"{self.base_url}performances/{content_id}",
                    headers={"Authorization": f"Bearer {self.api_key}"}
                )
                response.raise_for_status()  # Raises an HTTPError for bad responses

                # Parse JSON response
                performance_data.append(response.json())
            except requests.exceptions.RequestException as e:
                self.handle_error(e, content_id)

        return performance_data

    def analyze_insights(self, performance_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Analyzes performance data and generates insights.

        Args:
            performance_data (List[Dict[str, Any]]): A list of performance metrics.

        Returns:
            Dict[str, Any]: A dictionary of analyzed insights from performance data.
        """
        insights = {
            "total_views": sum(item.get("views", 0) for item in performance_data),
            "average_engagement": sum(item.get("engagement", 0) for item in performance_data) / max(len(performance_data), 1),
        }
        return insights

    def handle_error(self, error: Exception, content_id: str):
        """
        Handles errors during API requests.

        Args:
            error (Exception): The exception raised during the request.
            content_id (str): The content ID that caused the error.
        """
        print(f"Error fetching performance for content ID {content_id}: {error}")

# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key_here' with an actual API key
    tracker = MultilingualContentTracker(api_key='your_api_key_here')
    content_ids = ['content_1', 'content_2', 'content_3']  # Example content IDs
    performance_data = tracker.fetch_content_performance(content_ids)
    
    if performance_data:
        insights = tracker.analyze_insights(performance_data)
        print(json.dumps(insights, indent=4))  # Pretty-print insights
```
