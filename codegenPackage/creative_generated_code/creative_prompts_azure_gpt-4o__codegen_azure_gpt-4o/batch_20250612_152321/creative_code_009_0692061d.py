"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-bits.com
Prompt: Generate a script to analyze traffic statistics for advertisements, mimicking the detailed analytics offered by Claim-Bits.
Generated: DETERMINISTIC_0692061d7df55cac
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime
from collections import defaultdict

# A class to handle advertisement traffic analytics
class AdvertisementTrafficAnalyzer:
    def __init__(self):
        """
        Initializes the AdvertisementTrafficAnalyzer instance.
        Keeps track of traffic statistics and provides analytics.
        """
        self.logs = []  # List to store advertisement traffic logs
        self.stats = defaultdict(lambda: {"views": 0, "clicks": 0, "ctr": 0.0})  # Traffic statistics
    
    def record_event(self, ad_id, event_type, timestamp=None):
        """
        Records an advertisement event (view or click).

        Args:
            ad_id (str): Advertisement ID.
            event_type (str): Type of event ('view' or 'click').
            timestamp (datetime, optional): Event timestamp. Defaults to current time.
        Raises:
            ValueError: If the event_type is not 'view' or 'click'.
        """
        if event_type not in ("view", "click"):
            raise ValueError("Invalid event type. Must be 'view' or 'click'.")
        
        timestamp = timestamp or datetime.datetime.now()
        self.logs.append({"ad_id": ad_id, "event_type": event_type, "timestamp": timestamp})
        
        self._update_statistics(ad_id, event_type)
    
    def _update_statistics(self, ad_id, event_type):
        """
        Updates traffic statistics based on the recorded event.

        Args:
            ad_id (str): Advertisement ID.
            event_type (str): Type of event ('view' or 'click').
        """
        if event_type == "view":
            self.stats[ad_id]["views"] += 1
        elif event_type == "click":
            self.stats[ad_id]["clicks"] += 1
        
        # Calculate Click-Through Rate (CTR)
        views = self.stats[ad_id]["views"]
        clicks = self.stats[ad_id]["clicks"]
        self.stats[ad_id]["ctr"] = (clicks / views * 100) if views > 0 else 0.0
    
    def get_statistics(self, ad_id):
        """
        Retrieves traffic statistics for a specific advertisement.

        Args:
            ad_id (str): Advertisement ID.
        Returns:
            dict: Traffic statistics (views, clicks, ctr).
        """
        return self.stats.get(ad_id, {"views": 0, "clicks": 0, "ctr": 0.0})
    
    def export_logs(self, file_path="traffic_logs.json"):
        """
        Exports traffic logs to a JSON file.

        Args:
            file_path (str): Path to the JSON file. Defaults to 'traffic_logs.json'.
        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.logs, file, default=str, indent=4)
        except IOError as e:
            print(f"Error exporting logs: {e}")
    
    def load_logs(self, file_path="traffic_logs.json"):
        """
        Loads traffic logs from a JSON file.

        Args:
            file_path (str): Path to the JSON file. Defaults to 'traffic_logs.json'.
        Raises:
            IOError: If there is an error reading the file.
        """
        try:
            with open(file_path, "r") as file:
                self.logs = json.load(file)
                self._recalculate_statistics()
        except IOError as e:
            print(f"Error loading logs: {e}")
    
    def _recalculate_statistics(self):
        """
        Recalculates all statistics based on loaded logs.
        """
        self.stats = defaultdict(lambda: {"views": 0, "clicks": 0, "ctr": 0.0})
        for log in self.logs:
            self._update_statistics(log["ad_id"], log["event_type"])

# Example usage:
if __name__ == "__main__":
    analyzer = AdvertisementTrafficAnalyzer()
    
    # Record some events
    analyzer.record_event("ad1", "view")
    analyzer.record_event("ad1", "click")
    analyzer.record_event("ad2", "view")
    analyzer.record_event("ad2", "view")
    
    # Get statistics for ad1
    print("Ad1 stats:", analyzer.get_statistics("ad1"))
    
    # Export logs to a file
    analyzer.export_logs()
    
    # Load logs from the file
    analyzer.load_logs()
    print("Ad2 stats after reloading:", analyzer.get_statistics("ad2"))
```
