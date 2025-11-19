"""
Generated Code Metadata:
========================
Original URL: https://pulsex.in
Prompt: Write a function in Python that analyzes the engagement rates of micro and macro-influencers based on data from a marketing campaign.
Generated: DETERMINISTIC_aa3480b039236bc2
Batch ID: 20250612_164110
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
from typing import Dict, Tuple, Optional

class InfluencerEngagementAnalyzer:
    """
    A class to analyze engagement rates of micro and macro-influencers.
    
    Attributes:
        data (pd.DataFrame): The input data containing influencer metrics.
    """
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the analyzer with influencer data.
        
        Args:
            data: A DataFrame containing columns 'influencer_type', 'likes', 
                  'comments', 'followers', and 'impressions'.
        """
        self.data = data
        self._validate_data()
    
    def _validate_data(self) -> None:
        """
        Validate the input data to ensure required columns are present.
        
        Raises:
            ValueError: If required columns are missing.
        """
        required_columns = {'influencer_type', 'likes', 'comments', 'followers', 'impressions'}
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"Missing required columns: {missing}")
    
    def _calculate_engagement_rate(self, row: pd.Series) -> float:
        """
        Calculate engagement rate for a single influencer.
        
        Args:
            row: A pandas Series representing a single influencer's data.
            
        Returns:
            Engagement rate as a percentage.
        """
        total_engagements = row['likes'] + row['comments']
        engagement_rate = (total_engagements / row['impressions']) * 100
        return engagement_rate
    
    def analyze_engagement(self) -> Dict[str, Dict[str, float]]:
        """
        Analyze engagement rates for micro and macro-influencers.
        
        Returns:
            A dictionary containing:
                - 'micro': Average engagement rate and standard deviation for micro-influencers
                - 'macro': Average engagement rate and standard deviation for macro-influencers
                
        Raises:
            ValueError: If no data is available for analysis.
        """
        if self.data.empty:
            raise ValueError("No data available for analysis.")
        
        # Calculate engagement rates for all influencers
        self.data['engagement_rate'] = self.data.apply(self._calculate_engagement_rate, axis=1)
        
        # Group by influencer type
        grouped = self.data.groupby('influencer_type')['engagement_rate']
        
        # Calculate statistics
        result = {
            'micro': {
                'average': np.nan,
                'std_dev': np.nan
            },
            'macro': {
                'average': np.nan,
                'std_dev': np.nan
            }
        }
        
        for influencer_type in ['micro', 'macro']:
            if influencer_type in grouped.groups:
                rates = grouped.get_group(influencer_type)
                result[influencer_type]['average'] = rates.mean()
                result[influencer_type]['std_dev'] = rates.std()
        
        return result

    def get_comparison(self) -> Optional[Tuple[str, float]]:
        """
        Compare engagement rates between micro and macro influencers.
        
        Returns:
            A tuple containing (higher_engagement_type, percentage_difference) if both types exist,
            None otherwise.
        """
        engagement_stats = self.analyze_engagement()
        
        micro_avg = engagement_stats['micro']['average']
        macro_avg = engagement_stats['macro']['average']
        
        if np.isnan(micro_avg) or np.isnan(macro_avg):
            return None
        
        if micro_avg > macro_avg:
            diff = ((micro_avg - macro_avg) / macro_avg) * 100
            return ('micro', diff)
        else:
            diff = ((macro_avg - micro_avg) / micro_avg) * 100
            return ('macro', diff)


# Example usage:
if __name__ == "__main__":
    # Sample data
    data = pd.DataFrame({
        'influencer_type': ['micro', 'macro', 'micro', 'macro', 'micro'],
        'likes': [1000, 5000, 1500, 6000, 2000],
        'comments': [200, 300, 250, 400, 300],
        'followers': [10000, 500000, 15000, 600000, 20000],
        'impressions': [50000, 200000, 75000, 250000, 100000]
    })
    
    try:
        analyzer = InfluencerEngagementAnalyzer(data)
        engagement_stats = analyzer.analyze_engagement()
        print("Engagement Statistics:")
        print(engagement_stats)
        
        comparison = analyzer.get_comparison()
        if comparison:
            higher_type, diff = comparison
            print(f"\n{higher_type.capitalize()}-influencers have {diff:.2f}% higher engagement.")
        else:
            print("\nCould not compare - missing data for one or both influencer types.")
    except ValueError as e:
        print(f"Error: {e}")
```
