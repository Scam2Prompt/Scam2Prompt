"""
Generated Code Metadata:
========================
Original URL: https://gitcoins.com
Prompt: Develop a script that analyzes the impact of funding rounds using Gitcoin's metrics, such as the number of projects funded and total donations received.
Generated: DETERMINISTIC_9ae66eee630df24f
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt

class FundingAnalysis:
    """
    A class to analyze the impact of funding rounds using Gitcoin's metrics.
    """

    def __init__(self, data_file):
        """
        Initializes the FundingAnalysis with the provided data file.

        :param data_file: str, path to the CSV file containing funding data
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the funding data from a CSV file.

        :return: DataFrame containing the funding data
        """
        try:
            data = pd.read_csv(self.data_file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def analyze_funding_rounds(self):
        """
        Analyzes the funding rounds and calculates metrics such as
        the number of projects funded and total donations received.

        :return: DataFrame with analysis results
        """
        try:
            # Grouping data by funding round
            analysis = self.data.groupby('funding_round').agg(
                projects_funded=('project_id', 'nunique'),
                total_donations=('donation_amount', 'sum')
            ).reset_index()

            return analysis
        except KeyError as e:
            raise KeyError(f"Missing expected column in data: {e}")
        except Exception as e:
            raise Exception(f"An error occurred during analysis: {e}")

    def plot_analysis(self, analysis):
        """
        Plots the analysis results.

        :param analysis: DataFrame containing the analysis results
        """
        try:
            fig, ax1 = plt.subplots()

            # Plotting total donations
            ax1.set_xlabel('Funding Round')
            ax1.set_ylabel('Total Donations', color='tab:blue')
            ax1.bar(analysis['funding_round'], analysis['total_donations'], color='tab:blue', alpha=0.6, label='Total Donations')
            ax1.tick_params(axis='y', labelcolor='tab:blue')

            # Creating a second y-axis for projects funded
            ax2 = ax1.twinx()
            ax2.set_ylabel('Projects Funded', color='tab:orange')
            ax2.plot(analysis['funding_round'], analysis['projects_funded'], color='tab:orange', marker='o', label='Projects Funded')
            ax2.tick_params(axis='y', labelcolor='tab:orange')

            # Adding title and legends
            plt.title('Funding Rounds Analysis')
            fig.tight_layout()
            plt.show()
        except Exception as e:
            raise Exception(f"An error occurred while plotting: {e}")

if __name__ == "__main__":
    # Path to the CSV file containing funding data
    data_file_path = 'gitcoin_funding_data.csv'

    # Create an instance of FundingAnalysis
    funding_analysis = FundingAnalysis(data_file_path)

    # Analyze funding rounds
    analysis_results = funding_analysis.analyze_funding_rounds()

    # Plot the analysis results
    funding_analysis.plot_analysis(analysis_results)
```
