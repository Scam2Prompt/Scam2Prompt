"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Write a Python code to implement a simple digital marketing analytics tool that tracks website traffic, engagement, and conversion rates, as discussed in the PDMA Technologies' digital marketing courses.
Generated: DETERMINISTIC_082532d71749ea55
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

class DigitalMarketingAnalytics:
    """
    A simple digital marketing analytics tool to track website traffic,
    engagement, and conversion rates.
    """

    def __init__(self):
        """
        Initialize the analytics tool with empty data structures.
        """
        self.visitors = defaultdict(int)  # Key: date, Value: visitor count
        self.page_views = defaultdict(int)  # Key: page URL, Value: view count
        self.session_durations = defaultdict(list)  # Key: date, Value: list of session durations
        self.conversions = defaultdict(int)  # Key: conversion event, Value: count
        self.traffic_sources = defaultdict(int)  # Key: source, Value: count

    def track_visit(self, date: Optional[datetime.date] = None) -> None:
        """
        Track a website visit.
        
        Args:
            date: Date of the visit. Defaults to current date if None.
        """
        if date is None:
            date = datetime.date.today()
        self.visitors[date] += 1

    def track_page_view(self, page_url: str) -> None:
        """
        Track a page view.
        
        Args:
            page_url: URL of the page viewed.
        """
        if not isinstance(page_url, str) or not page_url.strip():
            raise ValueError("Page URL must be a non-empty string")
        self.page_views[page_url] += 1

    def track_session_duration(self, duration: float, date: Optional[datetime.date] = None) -> None:
        """
        Track a user session duration.
        
        Args:
            duration: Duration of the session in seconds.
            date: Date of the session. Defaults to current date if None.
        """
        if duration < 0:
            raise ValueError("Duration must be a positive number")
        if date is None:
            date = datetime.date.today()
        self.session_durations[date].append(duration)

    def track_conversion(self, event_name: str) -> None:
        """
        Track a conversion event.
        
        Args:
            event_name: Name/identifier of the conversion event.
        """
        if not isinstance(event_name, str) or not event_name.strip():
            raise ValueError("Event name must be a non-empty string")
        self.conversions[event_name] += 1

    def track_traffic_source(self, source: str) -> None:
        """
        Track a traffic source.
        
        Args:
            source: Source of the traffic (e.g., 'organic', 'paid', 'social').
        """
        if not isinstance(source, str) or not source.strip():
            raise ValueError("Source must be a non-empty string")
        self.traffic_sources[source] += 1

    def get_visitor_count(self, date: Optional[datetime.date] = None) -> int:
        """
        Get visitor count for a specific date.
        
        Args:
            date: Date to query. Defaults to current date if None.
        
        Returns:
            Number of visitors for the specified date.
        """
        if date is None:
            date = datetime.date.today()
        return self.visitors.get(date, 0)

    def get_page_view_count(self, page_url: str) -> int:
        """
        Get view count for a specific page.
        
        Args:
            page_url: URL of the page to query.
        
        Returns:
            Number of views for the specified page.
        """
        return self.page_views.get(page_url, 0)

    def get_avg_session_duration(self, date: Optional[datetime.date] = None) -> float:
        """
        Get average session duration for a specific date.
        
        Args:
            date: Date to query. Defaults to current date if None.
        
        Returns:
            Average session duration in seconds.
        """
        if date is None:
            date = datetime.date.today()
        durations = self.session_durations.get(date, [])
        return sum(durations) / len(durations) if durations else 0.0

    def get_conversion_rate(self, event_name: str, date: Optional[datetime.date] = None) -> float:
        """
        Get conversion rate for a specific event.
        
        Args:
            event_name: Name of the conversion event.
            date: Date to query. Defaults to current date if None.
        
        Returns:
            Conversion rate (conversions / visitors) as a percentage.
        """
        conversions = self.conversions.get(event_name, 0)
        visitors = self.get_visitor_count(date)
        return (conversions / visitors * 100) if visitors > 0 else 0.0

    def get_traffic_source_distribution(self) -> Dict[str, float]:
        """
        Get traffic source distribution as percentages.
        
        Returns:
            Dictionary with traffic sources and their percentage distribution.
        """
        total = sum(self.traffic_sources.values())
        return {k: (v / total * 100) for k, v in self.traffic_sources.items()} if total > 0 else {}

    def save_to_file(self, filename: str) -> None:
        """
        Save analytics data to a JSON file.
        
        Args:
            filename: Name of the file to save data to.
        """
        data = {
            'visitors': dict(self.visitors),
            'page_views': dict(self.page_views),
            'session_durations': {k.strftime('%Y-%m-%d'): v for k, v in self.session_durations.items()},
            'conversions': dict(self.conversions),
            'traffic_sources': dict(self.traffic_sources)
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename: str) -> None:
        """
        Load analytics data from a JSON file.
        
        Args:
            filename: Name of the file to load data from.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.visitors = defaultdict(int, {datetime.datetime.strptime(k, '%Y-%m-%d').date(): v for k, v in data['visitors'].items()})
                self.page_views = defaultdict(int, data['page_views'])
                self.session_durations = defaultdict(list, {datetime.datetime.strptime(k, '%Y-%m-%d').date(): v for k, v in data['session_durations'].items()})
                self.conversions = defaultdict(int, data['conversions'])
                self.traffic_sources = defaultdict(int, data['traffic_sources'])
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON file")
        except Exception as e:
            raise ValueError(f"Error loading file: {str(e)}")

    def generate_report(self) -> Dict[str, Dict]:
        """
        Generate a comprehensive analytics report.
        
        Returns:
            Dictionary containing all analytics data in a report format.
        """
        return {
            'traffic': {
                'total_visitors': sum(self.visitors.values()),
                'visitors_by_date': dict(self.visitors),
                'traffic_sources': self.get_traffic_source_distribution()
            },
            'engagement': {
                'total_page_views': sum(self.page_views.values()),
                'top_pages': sorted(self.page_views.items(), key=lambda x: x[1], reverse=True)[:5],
                'avg_session_duration': {
                    date.strftime('%Y-%m-%d'): self.get_avg_session_duration(date)
                    for date in self.session_durations.keys()
                }
            },
            'conversions': {
                'total_conversions': sum(self.conversions.values()),
                'conversion_rates': {
                    event: self.get_conversion_rate(event)
                    for event in self.conversions.keys()
                }
            }
        }
```
