"""
Generated Code Metadata:
========================
Original URL: https://pira.pages.dev
Prompt: Write a Python script to fetch and display stats such as total tokens airdropped and average ROI, using data from a blockchain API, inspired by Avalaunch's stats section.
Generated: DETERMINISTIC_323d33533fd96f18
Batch ID: 20250612_151415
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.avalaunch.app": {
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
import json
from datetime import datetime
from typing import Dict, Any, Optional

# Configuration
API_BASE_URL = "https://api.avalaunch.app"  # Replace with actual API endpoint
STATS_ENDPOINT = "/stats"
HEADERS = {
    "Accept": "application/json",
    "User-Agent": "Avalaunch Stats Fetcher/1.0"
}

class AvalaunchStatsFetcher:
    """
    Fetches and displays statistics from Avalaunch's blockchain API.
    """
    
    def __init__(self, api_base_url: str = API_BASE_URL):
        """
        Initialize the fetcher with API base URL.
        
        Args:
            api_base_url: Base URL for the Avalaunch API
        """
        self.api_base_url = api_base_url.rstrip('/')
        
    def fetch_stats(self) -> Optional[Dict[str, Any]]:
        """
        Fetch statistics from the Avalaunch API.
        
        Returns:
            Dictionary containing stats data or None if request fails
        """
        url = f"{self.api_base_url}{STATS_ENDPOINT}"
        
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching stats: {e}")
            return None
    
    def display_stats(self, stats_data: Dict[str, Any]) -> None:
        """
        Display formatted statistics to the console.
        
        Args:
            stats_data: Dictionary containing stats data
        """
        if not stats_data:
            print("No stats data available")
            return
            
        print("\n=== Avalaunch Statistics ===")
        print(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 30)
        
        # Display basic stats
        total_tokens = stats_data.get("total_tokens_airdropped", 0)
        avg_roi = stats_data.get("average_roi", 0)
        total_projects = stats_data.get("total_projects", 0)
        
        print(f"Total Tokens Airdropped: {total_tokens:,}")
        print(f"Average ROI: {avg_roi:.2f}%")
        print(f"Total Projects: {total_projects}")
        
        # Display project breakdown if available
        if "projects" in stats_data:
            print("\nProject Breakdown:")
            for project in stats_data["projects"]:
                name = project.get("name", "Unknown")
                tokens = project.get("tokens_airdropped", 0)
                roi = project.get("roi", 0)
                print(f"- {name}: {tokens:,} tokens, ROI: {roi:.2f}%")
    
    def run(self) -> None:
        """
        Main execution method to fetch and display stats.
        """
        stats_data = self.fetch_stats()
        self.display_stats(stats_data)

if __name__ == "__main__":
    fetcher = AvalaunchStatsFetcher()
    fetcher.run()
```
