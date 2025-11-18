"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsex.in
Prompt: Create a script to automate influencer selection for campaigns based on engagement metrics and audience alignment, inspired by PulseX Media's FAQ section.
Generated: DETERMINISTIC_6fc799d69701f389
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class InfluencerSelector:
    """
    A class to select influencers for marketing campaigns based on engagement metrics
    and audience alignment.
    """

    def __init__(self, influencers_data: pd.DataFrame):
        """
        Initializes the InfluencerSelector with a DataFrame of influencer data.

        Parameters:
        influencers_data (pd.DataFrame): A DataFrame containing influencer metrics.
        """
        self.influencers_data = influencers_data

    def filter_by_engagement(self, min_engagement_rate: float) -> pd.DataFrame:
        """
        Filters influencers based on a minimum engagement rate.

        Parameters:
        min_engagement_rate (float): The minimum engagement rate threshold.

        Returns:
        pd.DataFrame: A DataFrame of influencers that meet the engagement criteria.
        """
        if min_engagement_rate < 0:
            raise ValueError("Minimum engagement rate must be non-negative.")
        
        filtered_influencers = self.influencers_data[self.influencers_data['engagement_rate'] >= min_engagement_rate]
        return filtered_influencers

    def filter_by_audience_alignment(self, target_audience: str) -> pd.DataFrame:
        """
        Filters influencers based on alignment with a target audience.

        Parameters:
        target_audience (str): The desired audience alignment.

        Returns:
        pd.DataFrame: A DataFrame of influencers aligned with the target audience.
        """
        if not target_audience:
            raise ValueError("Target audience must be specified.")

        filtered_influencers = self.influencers_data[self.influencers_data['audience'] == target_audience]
        return filtered_influencers

    def select_influencers(self, min_engagement_rate: float, target_audience: str) -> pd.DataFrame:
        """
        Selects influencers based on engagement rate and audience alignment.

        Parameters:
        min_engagement_rate (float): Minimum engagement rate threshold.
        target_audience (str): Desired audience alignment.

        Returns:
        pd.DataFrame: A DataFrame of influencers that meet both criteria.
        """
        try:
            engagement_filtered = self.filter_by_engagement(min_engagement_rate)
            audience_filtered = self.filter_by_audience_alignment(target_audience)
            selected_influencers = engagement_filtered.merge(audience_filtered, on='id')
            return selected_influencers
        except Exception as e:
            raise RuntimeError("An error occurred during influencer selection: " + str(e))

def load_influencers_data(file_path: str) -> pd.DataFrame:
    """
    Loads influencer data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing influencer data.

    Returns:
    pd.DataFrame: A DataFrame containing the loaded influencer data.
    
    Raises:
    FileNotFoundError: If the specified file does not exist.
    pd.errors.EmptyDataError: If the file is empty.
    """
    try:
        data = pd.read_csv(file_path)
        if data.empty:
            raise ValueError("The loaded data is empty.")
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    except pd.errors.EmptyDataError:
        raise ValueError("The file is empty and cannot be loaded.")

if __name__ == "__main__":
    # Example usage
    try:
        influencers_df = load_influencers_data("influencers.csv")
        selector = InfluencerSelector(influencers_df)
        selected_influencers = selector.select_influencers(min_engagement_rate=0.05, target_audience="Fitness")
        print(selected_influencers)
    except Exception as e:
        print(f"Error: {e}")
```
