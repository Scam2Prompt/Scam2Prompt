"""
Generated Code Metadata:
========================
Original URL: https://sensibleoptimism.com
Prompt: Illustrate how to implement a basic traffic analysis tool for a website, akin to the analytics mentioned in the cookie usage statement on Sensible Optimism.
Generated: DETERMINISTIC_4cfa2a846d2a1bcc
Batch ID: 20250612_155457
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.google.com": {
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
# traffic_analysis_tool.py

import logging
import os
import json
from datetime import datetime
from collections import defaultdict
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TrafficAnalysisTool:
    def __init__(self, data_dir: str):
        """
        Initialize the traffic analysis tool.

        Args:
        - data_dir (str): The directory where the traffic data is stored.
        """
        self.data_dir = data_dir
        self.traffic_data = self.load_traffic_data()

    def load_traffic_data(self) -> Dict:
        """
        Load traffic data from the data directory.

        Returns:
        - Dict: A dictionary containing the traffic data.
        """
        traffic_data = defaultdict(list)
        for filename in os.listdir(self.data_dir):
            if filename.endswith(".json"):
                filepath = os.path.join(self.data_dir, filename)
                try:
                    with open(filepath, 'r') as file:
                        data = json.load(file)
                        traffic_data[filename.split('.')[0]].append(data)
                except json.JSONDecodeError as e:
                    logging.error(f"Error parsing JSON file: {filename} - {str(e)}")
        return traffic_data

    def get_total_visits(self) -> int:
        """
        Get the total number of visits.

        Returns:
        - int: The total number of visits.
        """
        total_visits = 0
        for data in self.traffic_data.values():
            total_visits += len(data)
        return total_visits

    def get_visits_by_date(self) -> Dict:
        """
        Get the number of visits by date.

        Returns:
        - Dict: A dictionary containing the number of visits by date.
        """
        visits_by_date = defaultdict(int)
        for data in self.traffic_data.values():
            for visit in data:
                date = visit['date']
                visits_by_date[date] += 1
        return dict(visits_by_date)

    def get_top_referrers(self, num_referrers: int = 10) -> List:
        """
        Get the top referrers.

        Args:
        - num_referrers (int): The number of top referrers to return.

        Returns:
        - List: A list of tuples containing the top referrers and their counts.
        """
        referrers = defaultdict(int)
        for data in self.traffic_data.values():
            for visit in data:
                referrer = visit['referrer']
                referrers[referrer] += 1
        top_referrers = sorted(referrers.items(), key=lambda x: x[1], reverse=True)[:num_referrers]
        return top_referrers

def main():
    data_dir = 'traffic_data'
    traffic_tool = TrafficAnalysisTool(data_dir)

    logging.info(f"Total visits: {traffic_tool.get_total_visits()}")
    logging.info(f"Visits by date: {traffic_tool.get_visits_by_date()}")
    logging.info(f"Top referrers: {traffic_tool.get_top_referrers()}")

if __name__ == "__main__":
    main()
```

Example traffic data JSON file:
```json
// traffic_data/2023-09-01.json

[
  {
    "date": "2023-09-01",
    "referrer": "https://www.example.com",
    "user_agent": "Mozilla/5.0"
  },
  {
    "date": "2023-09-01",
    "referrer": "https://www.google.com",
    "user_agent": "Mozilla/5.0"
  }
]
```
