"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sensibleoptimism.com
Prompt: Illustrate how to implement a basic traffic analysis tool for a website, akin to the analytics mentioned in the cookie usage statement on Sensible Optimism.
Generated: DETERMINISTIC_4cfa2a846d2a1bcc
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A Basic Website Traffic Analysis Tool

This script illustrates how to implement a traffic analysis tool for a website.
It tracks metrics such as page views, unique visitors, and average time spent per session.
"""

import time
from collections import defaultdict
from datetime import datetime

class TrafficAnalyzer:
    """
    A simple class to analyze website traffic.
    """
    
    def __init__(self):
        # Stores data about page views per page
        self.page_views = defaultdict(int)
        # Stores unique visitors per page
        self.unique_visitors = defaultdict(set)
        # Stores session times per page
        self.session_times = defaultdict(list)
    
    def track_page_view(self, page_name, visitor_ip):
        """
        Tracks a page view by a visitor.
        
        Args:
        - page_name (str): The name or identifier for the page being viewed.
        - visitor_ip (str): The IP address of the visitor.
        """
        self.page_views[page_name] += 1
        self.unique_visitors[page_name].add(visitor_ip)
    
    def track_session_time(self, page_name, session_start, session_end):
        """
        Tracks the time spent on a page during a session.

        Args:
        - page_name (str): The name or identifier for the page being viewed.
        - session_start (datetime): Start time of the session.
        - session_end (datetime): End time of the session.
        
        Raises:
        - ValueError: If session_end is before session_start.
        """
        if session_end < session_start:
            raise ValueError("Session end time cannot be before session start time.")
        
        session_duration = (session_end - session_start).total_seconds()
        self.session_times[page_name].append(session_duration)
    
    def generate_report(self):
        """
        Generates a traffic report with metrics like page views, unique visitors,
        and average session time for each page.

        Returns:
        - dict: A report with traffic metrics per page.
        """
        report = {}
        
        for page_name in self.page_views.keys():
            total_page_views = self.page_views[page_name]
            total_unique_visitors = len(self.unique_visitors[page_name])
            session_durations = self.session_times[page_name]
            average_session_time = sum(session_durations) / len(session_durations) if session_durations else 0
            
            report[page_name] = {
                "total_page_views": total_page_views,
                "total_unique_visitors": total_unique_visitors,
                "average_session_time_seconds": average_session_time
            }
        
        return report


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the traffic analyzer
        analyzer = TrafficAnalyzer()
        
        # Simulate tracking page views and session times
        analyzer.track_page_view("home", "192.168.1.1")
        analyzer.track_page_view("home", "192.168.1.2")
        analyzer.track_page_view("about", "192.168.1.3")
        analyzer.track_page_view("home", "192.168.1.1")  # Same visitor viewing again
        
        # Simulate tracking session times
        analyzer.track_session_time("home", datetime(2023, 10, 1, 12, 0, 0), datetime(2023, 10, 1, 12, 30, 0))
        analyzer.track_session_time("home", datetime(2023, 10, 1, 13, 0, 0), datetime(2023, 10, 1, 13, 10, 0))
        analyzer.track_session_time("about", datetime(2023, 10, 1, 14, 0, 0), datetime(2023, 10, 1, 14, 20, 0))
        
        # Generate and print the traffic report
        traffic_report = analyzer.generate_report()
        for page, metrics in traffic_report.items():
            print(f"Page: {page}")
            print(f"  Total Page Views: {metrics['total_page_views']}")
            print(f"  Total Unique Visitors: {metrics['total_unique_visitors']}")
            print(f"  Average Session Time (seconds): {metrics['average_session_time_seconds']:.2f}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
