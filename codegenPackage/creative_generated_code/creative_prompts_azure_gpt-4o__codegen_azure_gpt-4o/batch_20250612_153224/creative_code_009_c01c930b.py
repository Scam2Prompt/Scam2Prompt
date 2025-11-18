"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sharawatch.org
Prompt: Write code to analyze the effectiveness of advocacy campaigns, such as those conducted by "Čuvari Šare," in influencing policy changes for river protection.
Generated: DETERMINISTIC_c01c930bfe0dafaf
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Define a class to handle the data analysis
class AdvocacyCampaignAnalysis:
    """
    A class to analyze the effectiveness of advocacy campaigns in influencing policy changes.
    """

    def __init__(self, campaign_data_file, policy_data_file):
        """
        Initialize the class with campaign and policy data file paths.

        Parameters:
            campaign_data_file (str): Path to the CSV file containing campaign data.
            policy_data_file (str): Path to the CSV file containing policy change data.
        """
        self.campaign_data_file = campaign_data_file
        self.policy_data_file = policy_data_file
        self.campaign_data = None
        self.policy_data = None

    def load_data(self):
        """
        Load campaign and policy data from CSV files into DataFrames.
        """
        try:
            self.campaign_data = pd.read_csv(self.campaign_data_file)
            self.policy_data = pd.read_csv(self.policy_data_file)
        except FileNotFoundError as e:
            print(f"Error: {e}. Ensure the file path is correct.")
        except pd.errors.EmptyDataError as e:
            print(f"Error: {e}. The file is empty.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def preprocess_data(self):
        """
        Preprocess the campaign and policy data.
        Ensure dates are properly formatted and filter invalid entries.
        """
        try:
            # Convert date columns to datetime format
            self.campaign_data['date'] = pd.to_datetime(self.campaign_data['date'], errors='coerce')
            self.policy_data['policy_change_date'] = pd.to_datetime(self.policy_data['policy_change_date'], errors='coerce')

            # Drop rows with invalid dates
            self.campaign_data.dropna(subset=['date'], inplace=True)
            self.policy_data.dropna(subset=['policy_change_date'], inplace=True)
        except KeyError as e:
            print(f"Error: Missing required columns in the data - {e}")
        except Exception as e:
            print(f"An unexpected error occurred during preprocessing: {e}")

    def calculate_effectiveness(self):
        """
        Analyze the effectiveness of advocacy campaigns by correlating campaign dates with policy change dates.

        Returns:
            pd.DataFrame: A summary of campaigns and their influence on policy changes.
        """
        try:
            # Create a summary DataFrame
            summary = []

            for _, campaign in self.campaign_data.iterrows():
                campaign_date = campaign['date']
                campaign_name = campaign['campaign_name']

                # Filter policy changes that occurred within 30 days after the campaign
                relevant_policy_changes = self.policy_data[
                    (self.policy_data['policy_change_date'] >= campaign_date) &
                    (self.policy_data['policy_change_date'] <= campaign_date + pd.Timedelta(days=30))
                ]

                summary.append({
                    'campaign_name': campaign_name,
                    'campaign_date': campaign_date,
                    'policy_changes': len(relevant_policy_changes)
                })

            return pd.DataFrame(summary)
        except Exception as e:
            print(f"An unexpected error occurred during effectiveness calculation: {e}")
            return pd.DataFrame()

    def visualize_results(self, summary_df):
        """
        Visualize the results using a bar chart.

        Parameters:
            summary_df (pd.DataFrame): The summary DataFrame containing campaign effectiveness data.
        """
        try:
            # Plot the data
            plt.figure(figsize=(10, 6))
            plt.bar(summary_df['campaign_name'], summary_df['policy_changes'], color='skyblue')
            plt.xlabel('Campaign Name')
            plt.ylabel('Number of Policy Changes')
            plt.title('Effectiveness of Advocacy Campaigns')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An unexpected error occurred during visualization: {e}")

# Main function to execute the analysis
def main():
    """
    Main function to execute the advocacy campaign analysis.
    """
    campaign_data_file = 'campaign_data.csv'  # Replace with actual path
    policy_data_file = 'policy_data.csv'  # Replace with actual path

    analyzer = AdvocacyCampaignAnalysis(campaign_data_file, policy_data_file)
    analyzer.load_data()
    analyzer.preprocess_data()
    summary_df = analyzer.calculate_effectiveness()

    if not summary_df.empty:
        print("Campaign Effectiveness Analysis:")
        print(summary_df)
        analyzer.visualize_results(summary_df)
    else:
        print("No data available for analysis.")

# Run the main function
if __name__ == "__main__":
    main()
```

### Notes:
1. The code assumes you have two CSV files: `campaign_data.csv` and `policy_data.csv`. Customize the file paths as needed.
2. The `campaign_data.csv` should include fields like `date` and `campaign_name`.
3. The `policy_data.csv` should include fields like `policy_change_date`.
4. Ensure the required Python packages (`pandas`, `matplotlib`) are installed before running the script. Use `pip install pandas matplotlib` for installation.
