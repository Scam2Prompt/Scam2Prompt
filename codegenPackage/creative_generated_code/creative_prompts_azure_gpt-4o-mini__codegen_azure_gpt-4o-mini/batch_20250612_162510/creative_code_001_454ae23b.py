"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axos-management.com
Prompt: Write a Python script to analyze target groups for influencer partnerships, inspired by the goal-oriented analysis approach mentioned on axos-management.com.
Generated: DETERMINISTIC_454ae23bccf11ac0
Batch ID: 20250612_162510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class InfluencerAnalysis:
    """A class to analyze target groups for influencer partnerships."""

    def __init__(self, data_file: str):
        """
        Initializes the InfluencerAnalysis with the provided data file.

        Args:
            data_file (str): Path to the CSV file containing influencer data.
        """
        try:
            self.data = pd.read_csv(data_file)
            self.validate_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {data_file} does not exist.")
        except pd.errors.EmptyDataError:
            raise ValueError("The provided CSV file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the data: {e}")

    def validate_data(self):
        """Validates the structure of the loaded data."""
        required_columns = ['influencer_name', 'followers', 'engagement_rate', 'audience_demographics']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def filter_influencers(self, min_followers: int, min_engagement_rate: float):
        """
        Filters influencers based on minimum followers and engagement rate.

        Args:
            min_followers (int): Minimum number of followers.
            min_engagement_rate (float): Minimum engagement rate.

        Returns:
            pd.DataFrame: Filtered DataFrame of influencers.
        """
        filtered = self.data[
            (self.data['followers'] >= min_followers) & 
            (self.data['engagement_rate'] >= min_engagement_rate)
        ]
        return filtered

    def analyze_audience(self, target_demographic: str):
        """
        Analyzes influencers based on the target demographic.

        Args:
            target_demographic (str): The demographic to target.

        Returns:
            pd.DataFrame: DataFrame of influencers who match the target demographic.
        """
        # Assuming 'audience_demographics' is a string representation of a list
        matching_influencers = self.data[self.data['audience_demographics'].str.contains(target_demographic, na=False)]
        return matching_influencers

    def generate_report(self, filtered_data: pd.DataFrame):
        """
        Generates a report of the filtered influencers.

        Args:
            filtered_data (pd.DataFrame): The DataFrame of filtered influencers.
        """
        if filtered_data.empty:
            print("No influencers match the criteria.")
            return

        report = filtered_data[['influencer_name', 'followers', 'engagement_rate', 'audience_demographics']]
        print("Filtered Influencer Report:")
        print(report.to_string(index=False))

if __name__ == "__main__":
    # Define the path to the influencer data CSV file
    data_file = 'influencers.csv'

    # Create an instance of the InfluencerAnalysis class
    analysis = InfluencerAnalysis(data_file)

    # Set criteria for filtering
    min_followers = 10000
    min_engagement_rate = 0.05
    target_demographic = '18-24'

    # Filter influencers and generate a report
    filtered_influencers = analysis.filter_influencers(min_followers, min_engagement_rate)
    audience_analysis = analysis.analyze_audience(target_demographic)
    
    # Combine results and generate reports
    print("\nOverall Filtered Influencers:")
    analysis.generate_report(filtered_influencers)

    print("\nAudience Analysis for demographic '{}':".format(target_demographic))
    analysis.generate_report(audience_analysis)
```
