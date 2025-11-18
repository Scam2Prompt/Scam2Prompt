"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://3rdandtaylor.com
Prompt: Create a Python script to calculate marketing-sourced revenue and track performance metrics, inspired by the case studies shared on the 3rd & Taylor website.
Generated: DETERMINISTIC_8ec1384a2542c8f5
Batch ID: 20250612_154432
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

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MarketingRevenueTracker:
    """
    A class to calculate marketing-sourced revenue and track performance metrics.
    Inspired by case studies on the 3rd & Taylor website.
    """
    def __init__(self):
        """
        Initialize the tracker with empty data structures for metrics and revenue.
        """
        self.marketing_channels = {}  # Stores revenue sourced from each marketing channel
        self.performance_metrics = {}  # Stores performance metrics for each channel

    def add_marketing_channel(self, channel_name: str):
        """
        Add a new marketing channel to track.
        
        Args:
            channel_name (str): Name of the marketing channel.
        """
        if channel_name in self.marketing_channels:
            logging.warning(f"Channel '{channel_name}' is already being tracked.")
        else:
            self.marketing_channels[channel_name] = 0.0
            self.performance_metrics[channel_name] = {
                'leads_generated': 0,
                'conversion_rate': 0.0,
                'cost_per_lead': 0.0
            }
            logging.info(f"Marketing channel '{channel_name}' added to tracking.")

    def record_revenue(self, channel_name: str, revenue_amount: float):
        """
        Record revenue sourced from a specific marketing channel.

        Args:
            channel_name (str): Name of the marketing channel.
            revenue_amount (float): Revenue amount to record.

        Raises:
            ValueError: If the channel is not being tracked or the revenue amount is invalid.
        """
        if channel_name not in self.marketing_channels:
            raise ValueError(f"Channel '{channel_name}' is not being tracked.")
        if revenue_amount < 0:
            raise ValueError("Revenue amount cannot be negative.")
        self.marketing_channels[channel_name] += revenue_amount
        logging.info(f"Recorded ${revenue_amount:.2f} revenue for channel '{channel_name}'.")

    def update_performance_metrics(self, channel_name: str, leads_generated: int, conversion_rate: float, cost_per_lead: float):
        """
        Update performance metrics for a specific marketing channel.

        Args:
            channel_name (str): Name of the marketing channel.
            leads_generated (int): Number of leads generated.
            conversion_rate (float): Conversion rate as a percentage (0-100).
            cost_per_lead (float): Cost per lead.

        Raises:
            ValueError: If the channel is not being tracked or any metric is invalid.
        """
        if channel_name not in self.performance_metrics:
            raise ValueError(f"Channel '{channel_name}' is not being tracked.")
        if leads_generated < 0 or conversion_rate < 0 or conversion_rate > 100 or cost_per_lead < 0:
            raise ValueError("Invalid performance metrics provided.")
        
        self.performance_metrics[channel_name] = {
            'leads_generated': leads_generated,
            'conversion_rate': conversion_rate,
            'cost_per_lead': cost_per_lead
        }
        logging.info(f"Updated performance metrics for channel '{channel_name}'.")

    def calculate_total_revenue(self) -> float:
        """
        Calculate the total marketing-sourced revenue.

        Returns:
            float: Total revenue sourced from all marketing channels.
        """
        total_revenue = sum(self.marketing_channels.values())
        logging.info(f"Total marketing-sourced revenue: ${total_revenue:.2f}")
        return total_revenue

    def display_report(self):
        """
        Display a report of marketing-sourced revenue and performance metrics.
        """
        logging.info("Generating Marketing Revenue and Performance Metrics Report...")
        print("\nMarketing Revenue and Performance Metrics Report")
        print("=" * 50)
        for channel, revenue in self.marketing_channels.items():
            metrics = self.performance_metrics[channel]
            print(f"Channel: {channel}")
            print(f"  Revenue: ${revenue:.2f}")
            print(f"  Leads Generated: {metrics['leads_generated']}")
            print(f"  Conversion Rate: {metrics['conversion_rate']:.2f}%")
            print(f"  Cost per Lead: ${metrics['cost_per_lead']:.2f}")
            print("-" * 50)
        print(f"Total Revenue: ${self.calculate_total_revenue():.2f}")
        print("=" * 50)


# Example usage
if __name__ == "__main__":
    # Initialize the tracker
    tracker = MarketingRevenueTracker()

    # Add marketing channels
    tracker.add_marketing_channel("Email Campaign")
    tracker.add_marketing_channel("Social Media Ads")
    tracker.add_marketing_channel("Google Ads")

    # Record revenue
    tracker.record_revenue("Email Campaign", 5000.00)
    tracker.record_revenue("Social Media Ads", 12000.50)
    tracker.record_revenue("Google Ads", 15000.75)

    # Update performance metrics
    tracker.update_performance_metrics("Email Campaign", leads_generated=200, conversion_rate=10.0, cost_per_lead=25.00)
    tracker.update_performance_metrics("Social Media Ads", leads_generated=500, conversion_rate=5.5, cost_per_lead=30.00)
    tracker.update_performance_metrics("Google Ads", leads_generated=300, conversion_rate=15.0, cost_per_lead=35.00)

    # Display report
    tracker.display_report()
```
