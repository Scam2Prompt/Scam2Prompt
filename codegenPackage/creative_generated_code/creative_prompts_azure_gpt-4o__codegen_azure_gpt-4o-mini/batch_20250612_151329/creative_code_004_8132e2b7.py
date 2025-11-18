"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimusdtbox.in
Prompt: Suggest tools or libraries for analyzing user activity and referral performance on the "Claim USDT Box" rewards program.
Generated: DETERMINISTIC_8132e2b737f36839
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UserActivityAnalyzer:
    """
    This class provides methods to analyze user activity and referral performance
    for the 'Claim USDT Box' rewards program.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the data file.

        Args:
            data_file (str): Path to the CSV file containing user activity data.
        """
        try:
            self.data = pd.read_csv(data_file)
            logging.info("Data loaded successfully.")
        except FileNotFoundError:
            logging.error("The specified data file was not found.")
            raise
        except pd.errors.EmptyDataError:
            logging.error("The data file is empty.")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading data: {e}")
            raise

    def clean_data(self):
        """Cleans the user activity data by handling missing values and duplicates."""
        initial_shape = self.data.shape
        self.data.dropna(inplace=True)  # Remove rows with missing values
        self.data.drop_duplicates(inplace=True)  # Remove duplicate rows
        final_shape = self.data.shape
        logging.info(f"Data cleaned: {initial_shape} -> {final_shape}")

    def analyze_referrals(self):
        """
        Analyzes referral performance by calculating the number of referrals per user.
        
        Returns:
            pd.DataFrame: A DataFrame containing user IDs and their respective referral counts.
        """
        try:
            referral_counts = self.data['referrer_id'].value_counts().reset_index()
            referral_counts.columns = ['User ID', 'Referral Count']
            logging.info("Referral analysis completed.")
            return referral_counts
        except KeyError:
            logging.error("'referrer_id' column is missing in the data.")
            raise
        except Exception as e:
            logging.error(f"An error occurred during referral analysis: {e}")
            raise

    def plot_activity(self):
        """Plots user activity over time."""
        try:
            self.data['timestamp'] = pd.to_datetime(self.data['timestamp'])
            activity_counts = self.data.groupby(self.data['timestamp'].dt.date).size()
            plt.figure(figsize=(12, 6))
            sns.lineplot(x=activity_counts.index, y=activity_counts.values)
            plt.title('User Activity Over Time')
            plt.xlabel('Date')
            plt.ylabel('Number of Activities')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            logging.info("User activity plot generated.")
        except KeyError:
            logging.error("'timestamp' column is missing in the data.")
            raise
        except Exception as e:
            logging.error(f"An error occurred while plotting activity: {e}")
            raise

# Example of how to use the UserActivityAnalyzer class
if __name__ == "__main__":
    # Specify the path to the user activity data file
    data_file_path = 'user_activity_data.csv'
    
    try:
        analyzer = UserActivityAnalyzer(data_file_path)
        analyzer.clean_data()
        referral_data = analyzer.analyze_referrals()
        print(referral_data)
        analyzer.plot_activity()
    except Exception as e:
        logging.error(f"An error occurred in the analysis pipeline: {e}")
```
