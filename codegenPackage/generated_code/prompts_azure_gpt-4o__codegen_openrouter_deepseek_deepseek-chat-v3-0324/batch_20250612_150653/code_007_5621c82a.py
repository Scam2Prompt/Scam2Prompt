"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: Develop a Python function to track the progress of women-led civic society actors in advocacy campaigns, using data from Sauti Kenya's peace and governance initiatives.
Generated: DETERMINISTIC_5621c82a580f98bf
Batch ID: 20250612_150653
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
from typing import Dict, List, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AdvocacyProgressTracker:
    """
    A class to track and analyze the progress of women-led civic society actors
    in advocacy campaigns using data from Sauti Kenya's initiatives.
    """
    
    def __init__(self, data_source: str):
        """
        Initialize the tracker with a data source.
        
        Args:
            data_source (str): Path to the data file (CSV, Excel, etc.)
        """
        self.data_source = data_source
        self.data = None
        self._load_data()
        
    def _load_data(self) -> None:
        """
        Load and preprocess the data from the specified source.
        Handles common data loading errors.
        """
        try:
            if self.data_source.endswith('.csv'):
                self.data = pd.read_csv(self.data_source)
            elif self.data_source.endswith(('.xls', '.xlsx')):
                self.data = pd.read_excel(self.data_source)
            else:
                raise ValueError("Unsupported file format. Please provide CSV or Excel file.")
            
            # Basic data validation
            required_columns = ['actor_id', 'campaign_id', 'gender', 'role', 
                              'activity_date', 'activity_type', 'impact_score']
            missing_cols = [col for col in required_columns if col not in self.data.columns]
            
            if missing_cols:
                raise ValueError(f"Missing required columns: {missing_cols}")
                
            # Convert date column to datetime
            self.data['activity_date'] = pd.to_datetime(self.data['activity_date'])
            
            logger.info("Data loaded successfully with %d records", len(self.data))
            
        except FileNotFoundError:
            logger.error("Data file not found at %s", self.data_source)
            raise
        except Exception as e:
            logger.error("Error loading data: %s", str(e))
            raise
    
    def filter_women_led_actors(self) -> pd.DataFrame:
        """
        Filter the dataset to include only women-led actors.
        
        Returns:
            pd.DataFrame: Filtered dataframe containing only women-led actors
        """
        try:
            women_led = self.data[
                (self.data['gender'] == 'female') & 
                (self.data['role'].str.lower().str.contains('leader|director|coordinator'))
            ]
            logger.info("Filtered %d women-led actors", len(women_led))
            return women_led
        except Exception as e:
            logger.error("Error filtering women-led actors: %s", str(e))
            raise
    
    def calculate_campaign_progress(self, campaign_id: str) -> Dict[str, float]:
        """
        Calculate progress metrics for a specific campaign.
        
        Args:
            campaign_id (str): The ID of the campaign to analyze
            
        Returns:
            Dict[str, float]: Dictionary containing progress metrics
        """
        try:
            campaign_data = self.filter_women_led_actors()
            campaign_data = campaign_data[campaign_data['campaign_id'] == campaign_id]
            
            if campaign_data.empty:
                logger.warning("No data found for campaign %s", campaign_id)
                return {}
            
            # Calculate metrics
            metrics = {
                'total_activities': len(campaign_data),
                'unique_actors': campaign_data['actor_id'].nunique(),
                'avg_impact_score': campaign_data['impact_score'].mean(),
                'earliest_activity': campaign_data['activity_date'].min().strftime('%Y-%m-%d'),
                'latest_activity': campaign_data['activity_date'].max().strftime('%Y-%m-%d')
            }
            
            logger.info("Calculated metrics for campaign %s", campaign_id)
            return metrics
            
        except Exception as e:
            logger.error("Error calculating campaign progress: %s", str(e))
            raise
    
    def compare_gender_impact(self, campaign_id: str) -> Dict[str, Dict[str, float]]:
        """
        Compare impact scores between women-led and other actors in a campaign.
        
        Args:
            campaign_id (str): The ID of the campaign to analyze
            
        Returns:
            Dict[str, Dict[str, float]]: Comparison metrics by gender group
        """
        try:
            campaign_data = self.data[self.data['campaign_id'] == campaign_id]
            
            if campaign_data.empty:
                logger.warning("No data found for campaign %s", campaign_id)
                return {}
            
            # Women-led actors
            women_led = self.filter_women_led_actors()
            women_led_campaign = women_led[women_led['campaign_id'] == campaign_id]
            
            # Other actors
            others = campaign_data[~campaign_data['actor_id'].isin(women_led['actor_id'])]
            
            results = {
                'women_led': {
                    'count': len(women_led_campaign),
                    'avg_impact': women_led_campaign['impact_score'].mean(),
                    'max_impact': women_led_campaign['impact_score'].max()
                },
                'other_actors': {
                    'count': len(others),
                    'avg_impact': others['impact_score'].mean(),
                    'max_impact': others['impact_score'].max()
                }
            }
            
            logger.info("Gender comparison completed for campaign %s", campaign_id)
            return results
            
        except Exception as e:
            logger.error("Error comparing gender impact: %s", str(e))
            raise
    
    def generate_progress_report(self, campaign_ids: List[str], 
                               output_format: str = 'dict') -> Optional[Dict[str, Dict]]:
        """
        Generate a comprehensive progress report for multiple campaigns.
        
        Args:
            campaign_ids (List[str]): List of campaign IDs to include in the report
            output_format (str): Output format ('dict' or 'dataframe')
            
        Returns:
            Optional[Dict[str, Dict]]: Report data in specified format, None if error
        """
        try:
            report = {}
            
            for campaign_id in campaign_ids:
                campaign_metrics = self.calculate_campaign_progress(campaign_id)
                gender_comparison = self.compare_gender_impact(campaign_id)
                
                report[campaign_id] = {
                    'progress_metrics': campaign_metrics,
                    'gender_comparison': gender_comparison
                }
            
            if output_format == 'dataframe':
                # Convert to a flattened dataframe for easier analysis
                report_df = pd.json_normalize(
                    report,
                    sep='_'
                ).transpose().reset_index()
                report_df.columns = ['campaign_id', 'metrics']
                return report_df
                
            logger.info("Generated progress report for %d campaigns", len(campaign_ids))
            return report
            
        except Exception as e:
            logger.error("Error generating progress report: %s", str(e))
            return None

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with your data source
        tracker = AdvocacyProgressTracker("sauti_kenya_data.csv")
        
        # Example campaign IDs - replace with actual IDs from your data
        campaign_ids = ["campaign_001", "campaign_002"]
        
        # Generate and print a report
        report = tracker.generate_progress_report(campaign_ids)
        print(report)
        
    except Exception as e:
        logger.error("Application error: %s", str(e))
```
