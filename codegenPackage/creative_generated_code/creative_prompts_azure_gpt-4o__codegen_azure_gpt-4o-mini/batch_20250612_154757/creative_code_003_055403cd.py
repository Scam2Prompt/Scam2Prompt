"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://com-eligibility-checker.live
Prompt: Write a function to analyze user interaction metrics, such as bounce rate and traffic source, for a website using cookies categorized as "Analytics."
Generated: DETERMINISTIC_055403cdf8522fda
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from http.cookies import SimpleCookie
from typing import Dict, Any

class UserInteractionAnalyzer:
    def __init__(self, cookie_string: str):
        """
        Initializes the UserInteractionAnalyzer with a cookie string.
        
        :param cookie_string: A string representing the HTTP cookies.
        """
        self.cookie_string = cookie_string
        self.analytics_data = self._load_analytics_data()

    def _load_analytics_data(self) -> Dict[str, Any]:
        """
        Parses the cookie string and extracts analytics data.
        
        :return: A dictionary containing analytics data.
        """
        try:
            cookie = SimpleCookie(self.cookie_string)
            analytics_cookie = cookie.get('Analytics')

            if not analytics_cookie:
                raise ValueError("No 'Analytics' cookie found.")

            # Assuming the cookie value is a JSON string
            analytics_data = json.loads(analytics_cookie.value)
            return analytics_data
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in 'Analytics' cookie.")
        except Exception as e:
            raise RuntimeError(f"Failed to load analytics data: {str(e)}")

    def calculate_bounce_rate(self) -> float:
        """
        Calculates the bounce rate based on the analytics data.
        
        :return: Bounce rate as a percentage.
        """
        try:
            total_visits = self.analytics_data.get('total_visits', 0)
            bounced_visits = self.analytics_data.get('bounced_visits', 0)

            if total_visits == 0:
                raise ValueError("Total visits cannot be zero.")

            bounce_rate = (bounced_visits / total_visits) * 100
            return bounce_rate
        except Exception as e:
            raise RuntimeError(f"Error calculating bounce rate: {str(e)}")

    def get_traffic_sources(self) -> Dict[str, int]:
        """
        Retrieves traffic sources from the analytics data.
        
        :return: A dictionary of traffic sources and their respective counts.
        """
        try:
            traffic_sources = self.analytics_data.get('traffic_sources', {})
            if not isinstance(traffic_sources, dict):
                raise ValueError("Traffic sources data is not in the expected format.")
            return traffic_sources
        except Exception as e:
            raise RuntimeError(f"Error retrieving traffic sources: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Example cookie string (in a real scenario, this would be received from an HTTP request)
    example_cookie_string = "Analytics={\"total_visits\": 1000, \"bounced_visits\": 300, \"traffic_sources\": {\"direct\": 500, \"referral\": 300, \"social\": 200}}"
    
    try:
        analyzer = UserInteractionAnalyzer(example_cookie_string)
        bounce_rate = analyzer.calculate_bounce_rate()
        traffic_sources = analyzer.get_traffic_sources()
        
        print(f"Bounce Rate: {bounce_rate:.2f}%")
        print("Traffic Sources:", traffic_sources)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
