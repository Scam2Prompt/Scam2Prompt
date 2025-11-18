"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://evamobi.com
Prompt: Generate code to analyze the effectiveness of a full-funnel app promotion campaign, including metrics like CR (conversion rate) and D1RR (day-one retention rate), as mentioned in Evamobi's case studies.
Generated: DETERMINISTIC_c29a6d637cab6c35
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class CampaignAnalyzer:
    """
    A class to analyze the effectiveness of a full-funnel app promotion campaign,
    including metrics like Conversion Rate (CR) and Day-One Retention Rate (D1RR).
    """
    
    def __init__(self, campaign_data: pd.DataFrame):
        """
        Initializes the CampaignAnalyzer with campaign data.
        
        Parameters:
        campaign_data (pd.DataFrame): Data containing campaign performance metrics.
            Expected columns:
            - 'impressions': Number of times the campaign was viewed
            - 'clicks': Number of clicks on the campaign
            - 'installs': Number of app installs from the campaign
            - 'day_one_active_users': Number of users active on day one after install
        """
        self.data = campaign_data
        self.validate_data()

    def validate_data(self):
        """Validates that the required columns exist in the provided data."""
        required_columns = {'impressions', 'clicks', 'installs', 'day_one_active_users'}
        missing_columns = required_columns - set(self.data.columns)
        if missing_columns:
            raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    def calculate_conversion_rate(self) -> float:
        """
        Calculates the Conversion Rate (CR).
        CR = (installs / impressions) * 100
        
        Returns:
        float: Conversion Rate percentage.
        """
        total_impressions = self.data['impressions'].sum()
        total_installs = self.data['installs'].sum()
        if total_impressions == 0:
            return 0.0  # Avoid division by zero
        return (total_installs / total_impressions) * 100

    def calculate_day_one_retention_rate(self) -> float:
        """
        Calculates the Day-One Retention Rate (D1RR).
        D1RR = (day_one_active_users / installs) * 100
        
        Returns:
        float: Day-One Retention Rate percentage.
        """
        total_installs = self.data['installs'].sum()
        total_day_one_active_users = self.data['day_one_active_users'].sum()
        if total_installs == 0:
            return 0.0  # Avoid division by zero
        return (total_day_one_active_users / total_installs) * 100

    def generate_report(self) -> dict:
        """
        Generates a summary report of the campaign metrics.
        
        Returns:
        dict: A dictionary containing the calculated metrics.
        """
        return {
            "conversion_rate": self.calculate_conversion_rate(),
            "day_one_retention_rate": self.calculate_day_one_retention_rate(),
        }


# Example usage
if __name__ == "__main__":
    # Sample campaign data
    data = {
        "impressions": [1000, 2000, 1500],
        "clicks": [100, 300, 200],
        "installs": [50, 120, 90],
        "day_one_active_users": [30, 80, 50]
    }
    campaign_data = pd.DataFrame(data)

    try:
        analyzer = CampaignAnalyzer(campaign_data)
        report = analyzer.generate_report()
        print("Campaign Performance Report:")
        print(f"Conversion Rate (CR): {report['conversion_rate']:.2f}%")
        print(f"Day-One Retention Rate (D1RR): {report['day_one_retention_rate']:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
