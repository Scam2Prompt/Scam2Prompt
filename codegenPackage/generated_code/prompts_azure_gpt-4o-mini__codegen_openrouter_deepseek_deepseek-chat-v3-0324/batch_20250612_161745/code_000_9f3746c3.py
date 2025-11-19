"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Generate a code snippet for a digital marketing tool that tracks Return on Investment (ROI) for online campaigns, inspired by Romain Rissoan's approach to digital transformation.
Generated: DETERMINISTIC_9f3746c3bd0f6f04
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from datetime import datetime
from typing import Dict, List, Optional

class CampaignROITracker:
    """
    A digital marketing tool to track Return on Investment (ROI) for online campaigns.
    Inspired by Romain Rissoan's approach to digital transformation.
    
    Attributes:
        campaigns (Dict[str, Dict]): Dictionary to store campaign data
        cost_columns (List[str]): List of cost-related columns
        revenue_columns (List[str]): List of revenue-related columns
    """
    
    def __init__(self):
        """Initialize the ROI tracker with empty campaign data."""
        self.campaigns = {}
        self.cost_columns = ['ad_spend', 'agency_fees', 'production_costs']
        self.revenue_columns = ['direct_sales', 'subscriptions', 'leads_converted']
    
    def add_campaign(self, campaign_id: str, name: str, start_date: str, end_date: str) -> None:
        """
        Add a new campaign to track.
        
        Args:
            campaign_id: Unique identifier for the campaign
            name: Human-readable campaign name
            start_date: Campaign start date (YYYY-MM-DD)
            end_date: Campaign end date (YYYY-MM-DD)
            
        Raises:
            ValueError: If campaign_id already exists or dates are invalid
        """
        if campaign_id in self.campaigns:
            raise ValueError(f"Campaign ID {campaign_id} already exists")
            
        try:
            start = datetime.strptime(start_date, '%Y-%m-%d')
            end = datetime.strptime(end_date, '%Y-%m-%d')
            if end < start:
                raise ValueError("End date must be after start date")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {e}")
            
        self.campaigns[campaign_id] = {
            'name': name,
            'start_date': start_date,
            'end_date': end_date,
            'metrics': {
                'costs': {col: 0.0 for col in self.cost_columns},
                'revenue': {col: 0.0 for col in self.revenue_columns}
            }
        }
    
    def update_campaign_metrics(self, campaign_id: str, metric_type: str, metrics: Dict[str, float]) -> None:
        """
        Update cost or revenue metrics for a campaign.
        
        Args:
            campaign_id: ID of the campaign to update
            metric_type: Either 'costs' or 'revenue'
            metrics: Dictionary of metric values to update
            
        Raises:
            ValueError: If campaign doesn't exist or invalid metric type/values
        """
        if campaign_id not in self.campaigns:
            raise ValueError(f"Campaign ID {campaign_id} not found")
            
        if metric_type not in ['costs', 'revenue']:
            raise ValueError("metric_type must be either 'costs' or 'revenue'")
            
        valid_columns = self.cost_columns if metric_type == 'costs' else self.revenue_columns
        
        for metric, value in metrics.items():
            if metric not in valid_columns:
                raise ValueError(f"Invalid metric '{metric}' for type '{metric_type}'")
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError(f"Value for {metric} must be a positive number")
                
            self.campaigns[campaign_id]['metrics'][metric_type][metric] = value
    
    def calculate_roi(self, campaign_id: str) -> float:
        """
        Calculate ROI for a specific campaign.
        
        Args:
            campaign_id: ID of the campaign to analyze
            
        Returns:
            ROI percentage (positive or negative)
            
        Raises:
            ValueError: If campaign doesn't exist
        """
        if campaign_id not in self.campaigns:
            raise ValueError(f"Campaign ID {campaign_id} not found")
            
        campaign = self.campaigns[campaign_id]
        total_cost = sum(campaign['metrics']['costs'].values())
        total_revenue = sum(campaign['metrics']['revenue'].values())
        
        if total_cost == 0:
            return float('inf') if total_revenue > 0 else 0.0
            
        return ((total_revenue - total_cost) / total_cost) * 100
    
    def generate_report(self, campaign_id: Optional[str] = None) -> pd.DataFrame:
        """
        Generate a report for one or all campaigns.
        
        Args:
            campaign_id: Optional specific campaign ID, None for all campaigns
            
        Returns:
            Pandas DataFrame with campaign metrics and ROI
            
        Raises:
            ValueError: If specified campaign doesn't exist
        """
        report_data = []
        
        if campaign_id:
            if campaign_id not in self.campaigns:
                raise ValueError(f"Campaign ID {campaign_id} not found")
            campaigns_to_report = {campaign_id: self.campaigns[campaign_id]}
        else:
            campaigns_to_report = self.campaigns
            
        for cid, data in campaigns_to_report.items():
            row = {
                'campaign_id': cid,
                'name': data['name'],
                'start_date': data['start_date'],
                'end_date': data['end_date'],
                'total_cost': sum(data['metrics']['costs'].values()),
                'total_revenue': sum(data['metrics']['revenue'].values()),
                'roi': self.calculate_roi(cid)
            }
            # Add individual metrics
            row.update({f"cost_{k}": v for k, v in data['metrics']['costs'].items()})
            row.update({f"revenue_{k}": v for k, v in data['metrics']['revenue'].items()})
            report_data.append(row)
            
        return pd.DataFrame(report_data)
    
    def save_to_csv(self, filepath: str, campaign_id: Optional[str] = None) -> None:
        """
        Save campaign report to CSV file.
        
        Args:
            filepath: Path to save the CSV file
            campaign_id: Optional specific campaign ID, None for all campaigns
            
        Raises:
            ValueError: If specified campaign doesn't exist
            IOError: If file cannot be written
        """
        try:
            report = self.generate_report(campaign_id)
            report.to_csv(filepath, index=False)
        except Exception as e:
            raise IOError(f"Failed to save report: {e}")
```
