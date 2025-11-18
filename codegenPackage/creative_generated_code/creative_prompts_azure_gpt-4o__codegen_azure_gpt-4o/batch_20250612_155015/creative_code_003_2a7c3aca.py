"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superlbride.com
Prompt: Generate code for monitoring and managing connectivity across international markets, reflecting SuperBridge's emphasis on global reach and seamless operations.
Generated: DETERMINISTIC_2a7c3aca250db9dd
Batch ID: 20250612_155015
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://na.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://au.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://eu.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://asia.example.com": {
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
import socket
import requests
from datetime import datetime

class MarketConnectivityMonitor:
    """
    A class to monitor and manage connectivity across international markets.
    """

    def __init__(self, markets):
        """
        Initialize the monitor with a list of markets and their endpoints.
        
        :param markets: A dictionary where keys are market names and values are URLs or IP addresses.
        """
        self.markets = markets
        self.status_log = {}
    
    def _check_connectivity(self, endpoint):
        """
        Check connectivity to a given endpoint (URL or IP address).
        
        :param endpoint: The URL or IP address to check.
        :return: A tuple (status, latency). Status is True if reachable, False otherwise. Latency is time in ms.
        """
        try:
            # Measure the time taken for a successful response
            start_time = datetime.now()
            response = requests.get(endpoint, timeout=5)
            response.raise_for_status()
            latency = (datetime.now() - start_time).total_seconds() * 1000  # Convert to milliseconds
            return True, latency
        except requests.exceptions.RequestException:
            # Catch all connectivity-related errors
            return False, None

    def monitor_markets(self):
        """
        Monitor connectivity for all markets and log the results.
        """
        for market, endpoint in self.markets.items():
            status, latency = self._check_connectivity(endpoint)
            self.status_log[market] = {
                "status": status,
                "latency_ms": latency,
                "last_checked": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    
    def get_market_status(self, market):
        """
        Retrieve the connectivity status of a specific market.
        
        :param market: The name of the market.
        :return: A dictionary containing connectivity status, latency, and timestamp.
        """
        return self.status_log.get(market, "Market not found")
    
    def display_status_report(self):
        """
        Display a report of connectivity statuses for all markets.
        """
        print("Market Connectivity Status Report:")
        print("-" * 50)
        for market, details in self.status_log.items():
            status = "Reachable" if details["status"] else "Unreachable"
            latency = f"{details['latency_ms']} ms" if details["latency_ms"] is not None else "N/A"
            print(f"{market}: Status={status}, Latency={latency}, Last Checked={details['last_checked']}")


if __name__ == "__main__":
    # List of international markets and their endpoints
    market_endpoints = {
        "North America": "https://na.example.com",
        "Europe": "https://eu.example.com",
        "Asia": "https://asia.example.com",
        "Australia": "https://au.example.com",
    }

    # Initialize the monitor
    monitor = MarketConnectivityMonitor(market_endpoints)

    # Periodically monitor connectivity (example: calling monitor_markets once)
    monitor.monitor_markets()

    # Display the status report
    monitor.display_status_report()

    # Example: Get status of a specific market
    print("\nStatus for Europe:")
    print(monitor.get_market_status("Europe"))
```
