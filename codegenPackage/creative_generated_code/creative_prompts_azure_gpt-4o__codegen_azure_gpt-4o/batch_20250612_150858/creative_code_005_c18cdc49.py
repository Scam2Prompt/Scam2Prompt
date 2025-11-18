"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tetherbind.web.app
Prompt: Provide a code example for implementing analytics and reporting tools to monitor token usage patterns and track performance, as described on TetherBind's website.
Generated: DETERMINISTIC_c18cdc4990692f07
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging
from collections import defaultdict

# Configure logging for monitoring and debugging
logging.basicConfig(
    filename='token_usage_analytics.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class TokenAnalytics:
    """
    A class to implement analytics and reporting tools for monitoring token usage patterns
    and tracking performance.
    """

    def __init__(self):
        # Dictionary to track token usage by user and endpoint
        self.token_usage = defaultdict(lambda: defaultdict(int))
        # List to store performance metrics for reporting
        self.performance_metrics = []

    def record_usage(self, user_id, endpoint, token_count=1):
        """
        Record token consumption for a specific user and endpoint.

        :param user_id: Unique identifier of the user
        :param endpoint: API endpoint being accessed
        :param token_count: Number of tokens consumed
        """
        try:
            self.token_usage[user_id][endpoint] += token_count
            logging.info(f"Recorded usage: User {user_id}, Endpoint {endpoint}, Tokens {token_count}")
        except Exception as e:
            logging.error(f"Error recording token usage: {str(e)}")

    def track_performance(self, endpoint, response_time):
        """
        Track API endpoint performance by recording response times.

        :param endpoint: API endpoint being accessed
        :param response_time: Time taken to process the request (in seconds)
        """
        try:
            self.performance_metrics.append({"endpoint": endpoint, "response_time": response_time})
            logging.info(f"Performance tracked: Endpoint {endpoint}, Response Time {response_time}s")
        except Exception as e:
            logging.error(f"Error tracking performance: {str(e)}")

    def generate_usage_report(self):
        """
        Generate a report summarizing token usage patterns.

        :return: Dictionary containing usage summary
        """
        try:
            report = {}
            for user_id, endpoints in self.token_usage.items():
                report[user_id] = dict(endpoints)
            logging.info("Generated token usage report successfully.")
            return report
        except Exception as e:
            logging.error(f"Error generating usage report: {str(e)}")
            return {}

    def generate_performance_report(self):
        """
        Generate a report summarizing endpoint performance metrics.

        :return: Dictionary containing performance summary
        """
        try:
            performance_summary = defaultdict(list)
            for metric in self.performance_metrics:
                performance_summary[metric["endpoint"]].append(metric["response_time"])
            for endpoint, times in performance_summary.items():
                performance_summary[endpoint] = {
                    "avg_response_time": sum(times) / len(times),
                    "max_response_time": max(times),
                    "min_response_time": min(times)
                }
            logging.info("Generated performance report successfully.")
            return dict(performance_summary)
        except Exception as e:
            logging.error(f"Error generating performance report: {str(e)}")
            return {}

# Example usage of TokenAnalytics class
if __name__ == "__main__":
    analytics = TokenAnalytics()

    # Simulate recording token usage
    analytics.record_usage(user_id="user123", endpoint="/api/v1/resource", token_count=5)
    analytics.record_usage(user_id="user456", endpoint="/api/v1/resource", token_count=3)
    analytics.record_usage(user_id="user123", endpoint="/api/v2/resource", token_count=2)

    # Simulate tracking API performance
    analytics.track_performance(endpoint="/api/v1/resource", response_time=0.123)
    analytics.track_performance(endpoint="/api/v1/resource", response_time=0.156)
    analytics.track_performance(endpoint="/api/v2/resource", response_time=0.200)

    # Generate and print reports
    usage_report = analytics.generate_usage_report()
    performance_report = analytics.generate_performance_report()

    print("Token Usage Report:", usage_report)
    print("Performance Report:", performance_report)
```
