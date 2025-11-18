"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.thedigilancer.com
Prompt: Create a Python program to analyze social media marketing (SMM) campaign effectiveness, referencing Ratul Kalra's focus on boosting visibility and driving engagement.
Generated: DETERMINISTIC_98e2ecbc13f40689
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

class SMMAudit:
    """
    A class to analyze social media marketing (SMM) campaign effectiveness.
    
    Attributes:
        data (pd.DataFrame): DataFrame containing the campaign metrics.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the SMMAudit with the provided campaign data.

        Parameters:
            data (pd.DataFrame): A DataFrame containing campaign metrics.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame.")
        
        self.data = data

    def calculate_engagement_rate(self) -> pd.Series:
        """
        Calculates the engagement rate for the campaign.

        Engagement Rate = (Likes + Comments + Shares) / Total Impressions

        Returns:
            pd.Series: A Series containing the engagement rates for each campaign.
        """
        try:
            engagement_rate = (self.data['Likes'] + self.data['Comments'] + self.data['Shares']) / self.data['Impressions']
            return engagement_rate
        except KeyError as e:
            raise KeyError(f"Missing expected column in data: {e}")

    def visualize_engagement(self) -> None:
        """
        Visualizes the engagement rate of the campaigns using a bar chart.
        """
        try:
            engagement_rate = self.calculate_engagement_rate()
            engagement_rate.plot(kind='bar', color='skyblue', title='Engagement Rate by Campaign')
            plt.xlabel('Campaign')
            plt.ylabel('Engagement Rate')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error during visualization: {e}")

    def summary_statistics(self) -> pd.DataFrame:
        """
        Generates summary statistics of the campaign data.

        Returns:
            pd.DataFrame: A DataFrame containing summary statistics.
        """
        return self.data.describe()

def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads campaign data from a CSV file.

    Parameters:
        file_path (str): The path to the CSV file containing the campaign data.

    Returns:
        pd.DataFrame: A DataFrame containing the loaded campaign data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except pd.errors.EmptyDataError:
        raise ValueError("The CSV file is empty.")
    except Exception as e:
        raise Exception(f"An error occurred while loading data: {e}")

def main():
    """
    Main function to execute the SMM analysis.
    """
    # Load the campaign data
    file_path = 'smm_campaign_data.csv'  # Update with the actual file path
    try:
        data = load_data(file_path)

        # Initialize the SMMAudit class with the loaded data
        audit = SMMAudit(data)

        # Generate and display engagement rate visualization
        audit.visualize_engagement()

        # Display summary statistics of the campaign data
        stats = audit.summary_statistics()
        print("Summary Statistics:\n", stats)

    except Exception as e:
        print(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
```
