"""
Generated Code Metadata:
========================
Original URL: https://salesstudios.com
Prompt: Create a Python script to calculate ROI for email marketing campaigns, using metrics like open rates and sales revenue increases, similar to Sales Studios' case studies.
Generated: DETERMINISTIC_4de12088785f91e4
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from typing import Dict, Union, Optional

class EmailMarketingROICalculator:
    """
    A class to calculate the Return on Investment (ROI) for email marketing campaigns.
    
    Attributes:
        campaign_name (str): Name of the email marketing campaign.
        total_emails_sent (int): Total number of emails sent in the campaign.
        open_rate (float): Percentage of emails opened (0-100).
        click_rate (float): Percentage of emails clicked (0-100).
        conversion_rate (float): Percentage of clicks that converted to sales (0-100).
        average_order_value (float): Average revenue per order.
        cost_per_email (float): Cost associated with sending each email.
        additional_costs (float): Any other costs related to the campaign.
    """
    
    def __init__(
        self,
        campaign_name: str,
        total_emails_sent: int,
        open_rate: float,
        click_rate: float,
        conversion_rate: float,
        average_order_value: float,
        cost_per_email: float,
        additional_costs: float = 0.0
    ):
        """
        Initialize the EmailMarketingROICalculator with campaign metrics.
        
        Args:
            campaign_name: Name of the email marketing campaign.
            total_emails_sent: Total number of emails sent in the campaign.
            open_rate: Percentage of emails opened (0-100).
            click_rate: Percentage of emails clicked (0-100).
            conversion_rate: Percentage of clicks that converted to sales (0-100).
            average_order_value: Average revenue per order.
            cost_per_email: Cost associated with sending each email.
            additional_costs: Any other costs related to the campaign. Defaults to 0.
        """
        self.campaign_name = campaign_name
        self.total_emails_sent = total_emails_sent
        self.open_rate = open_rate
        self.click_rate = click_rate
        self.conversion_rate = conversion_rate
        self.average_order_value = average_order_value
        self.cost_per_email = cost_per_email
        self.additional_costs = additional_costs
        
        # Validate inputs
        self._validate_inputs()
    
    def _validate_inputs(self) -> None:
        """Validate the input metrics to ensure they are within reasonable ranges."""
        if not (0 <= self.open_rate <= 100):
            raise ValueError("Open rate must be between 0 and 100.")
        if not (0 <= self.click_rate <= 100):
            raise ValueError("Click rate must be between 0 and 100.")
        if not (0 <= self.conversion_rate <= 100):
            raise ValueError("Conversion rate must be between 0 and 100.")
        if self.total_emails_sent <= 0:
            raise ValueError("Total emails sent must be greater than 0.")
        if self.average_order_value < 0:
            raise ValueError("Average order value cannot be negative.")
        if self.cost_per_email < 0:
            raise ValueError("Cost per email cannot be negative.")
        if self.additional_costs < 0:
            raise ValueError("Additional costs cannot be negative.")
    
    def calculate_roi(self) -> Dict[str, Union[float, int]]:
        """
        Calculate the ROI and related metrics for the email marketing campaign.
        
        Returns:
            A dictionary containing:
                - total_opens: Total number of emails opened.
                - total_clicks: Total number of emails clicked.
                - total_conversions: Total number of conversions.
                - total_revenue: Total revenue generated.
                - total_cost: Total cost of the campaign.
                - roi: Return on Investment as a percentage.
        """
        try:
            total_opens = (self.open_rate / 100) * self.total_emails_sent
            total_clicks = (self.click_rate / 100) * total_opens
            total_conversions = (self.conversion_rate / 100) * total_clicks
            total_revenue = total_conversions * self.average_order_value
            
            total_cost = (self.cost_per_email * self.total_emails_sent) + self.additional_costs
            
            if total_cost == 0:
                roi = float('inf') if total_revenue > 0 else 0.0
            else:
                roi = ((total_revenue - total_cost) / total_cost) * 100
            
            return {
                "campaign_name": self.campaign_name,
                "total_opens": int(round(total_opens)),
                "total_clicks": int(round(total_clicks)),
                "total_conversions": int(round(total_conversions)),
                "total_revenue": round(total_revenue, 2),
                "total_cost": round(total_cost, 2),
                "roi": round(roi, 2)
            }
        except Exception as e:
            raise RuntimeError(f"An error occurred during ROI calculation: {e}")
    
    @staticmethod
    def generate_report(results: Dict[str, Union[float, int]]) -> str:
        """
        Generate a human-readable report from the ROI calculation results.
        
        Args:
            results: Dictionary containing ROI metrics.
            
        Returns:
            A formatted string report.
        """
        report = f"""
        Email Marketing Campaign ROI Report
        ----------------------------------
        Campaign Name: {results['campaign_name']}
        Total Emails Sent: {results.get('total_emails_sent', 'N/A')}
        
        Performance Metrics:
        - Total Opens: {results['total_opens']}
        - Total Clicks: {results['total_clicks']}
        - Total Conversions: {results['total_conversions']}
        
        Financial Metrics:
        - Total Revenue: ${results['total_revenue']:,.2f}
        - Total Cost: ${results['total_cost']:,.2f}
        - ROI: {results['roi']:,.2f}%
        
        """
        return report

def main():
    """Example usage of the EmailMarketingROICalculator."""
    try:
        # Example campaign data (similar to Sales Studios' case studies)
        campaign_data = {
            "campaign_name": "Summer Sale 2023",
            "total_emails_sent": 10000,
            "open_rate": 25.5,  # 25.5% open rate
            "click_rate": 10.2,  # 10.2% click rate
            "conversion_rate": 5.5,  # 5.5% conversion rate
            "average_order_value": 150.0,
            "cost_per_email": 0.02,
            "additional_costs": 500.0
        }
        
        # Create calculator instance
        calculator = EmailMarketingROICalculator(**campaign_data)
        
        # Calculate ROI
        results = calculator.calculate_roi()
        results['total_emails_sent'] = campaign_data['total_emails_sent']
        
        # Generate and print report
        report = EmailMarketingROICalculator.generate_report(results)
        print(report)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
