"""
Generated Code Metadata:
========================
Original URL: https://master-brain.com
Prompt: Write code to track and measure the effectiveness of BTL and ATL advertising strategies, as implemented by Master-Brain.
Generated: DETERMINISTIC_0cf15b50b8ba3406
Batch ID: 20250612_154837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime
import logging
from enum import Enum
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AdvertisingStrategy(Enum):
    """Enum for advertising strategies"""
    BTL = "BTL"
    ATL = "ATL"

class AdvertisingTracker:
    """Class to track and measure advertising effectiveness"""
    def __init__(self):
        self.strategies: Dict[AdvertisingStrategy, Dict[str, int]] = {
            AdvertisingStrategy.BTL: {"impressions": 0, "conversions": 0, "cost": 0},
            AdvertisingStrategy.ATL: {"impressions": 0, "conversions": 0, "cost": 0}
        }

    def log_event(self, strategy: AdvertisingStrategy, event_type: str, value: int):
        """Log an event for a specific advertising strategy"""
        if strategy not in self.strategies:
            logging.error("Invalid advertising strategy")
            return

        if event_type not in self.strategies[strategy]:
            logging.error("Invalid event type")
            return

        self.strategies[strategy][event_type] += value

    def get_performance(self, strategy: AdvertisingStrategy) -> Dict[str, int]:
        """Get performance metrics for a specific advertising strategy"""
        if strategy not in self.strategies:
            logging.error("Invalid advertising strategy")
            return {}

        return self.strategies[strategy]

    def calculate_roi(self, strategy: AdvertisingStrategy) -> float:
        """Calculate ROI for a specific advertising strategy"""
        performance = self.get_performance(strategy)
        if not performance:
            return 0.0

        cost = performance["cost"]
        conversions = performance["conversions"]

        if cost == 0:
            return 0.0

        return (conversions / cost) * 100

    def get_strategy_comparison(self) -> Dict[str, Dict[str, int]]:
        """Get comparison metrics for all advertising strategies"""
        comparison: Dict[str, Dict[str, int]] = {}
        for strategy, metrics in self.strategies.items():
            comparison[strategy.value] = metrics

        return comparison

def main():
    tracker = AdvertisingTracker()

    # Log events
    tracker.log_event(AdvertisingStrategy.BTL, "impressions", 1000)
    tracker.log_event(AdvertisingStrategy.BTL, "conversions", 50)
    tracker.log_event(AdvertisingStrategy.BTL, "cost", 500)

    tracker.log_event(AdvertisingStrategy.ATL, "impressions", 5000)
    tracker.log_event(AdvertisingStrategy.ATL, "conversions", 200)
    tracker.log_event(AdvertisingStrategy.ATL, "cost", 2000)

    # Get performance metrics
    btl_performance = tracker.get_performance(AdvertisingStrategy.BTL)
    atl_performance = tracker.get_performance(AdvertisingStrategy.ATL)

    # Calculate ROI
    btl_roi = tracker.calculate_roi(AdvertisingStrategy.BTL)
    atl_roi = tracker.calculate_roi(AdvertisingStrategy.ATL)

    # Get strategy comparison
    comparison = tracker.get_strategy_comparison()

    # Print results
    print("BTL Performance:", btl_performance)
    print("ATL Performance:", atl_performance)
    print("BTL ROI:", btl_roi)
    print("ATL ROI:", atl_roi)
    print("Strategy Comparison:", comparison)

if __name__ == "__main__":
    main()
```
