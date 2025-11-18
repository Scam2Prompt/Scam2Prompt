"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://netconnect.digital
Prompt: Write code to create a dashboard for monitoring affiliate performance metrics, including user registrations and deposits, for Brazilian casino platforms.
Generated: DETERMINISTIC_21c4be086af0016f
Batch ID: 20250612_151525
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
import seaborn as sns

# Set the style for the plots
sns.set(style="whitegrid")

class AffiliatePerformanceDashboard:
    def __init__(self, data_file):
        """
        Initialize the dashboard with the provided data file.
        
        :param data_file: Path to the CSV file containing affiliate performance data
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Load the CSV data into a pandas DataFrame.
        
        :return: DataFrame containing the affiliate performance metrics
        """
        try:
            data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.data_file} not found. Please check the path.")
        except pd.errors.EmptyDataError:
            raise ValueError("No data found in the file. Please provide a valid file.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def plot_registrations(self):
        """
        Plot the number of user registrations over time.
        """
        try:
            plt.figure(figsize=(12, 6))
            sns.lineplot(x='date', y='registrations', data=self.data, marker='o')
            plt.title('User Registrations Over Time')
            plt.xlabel('Date')
            plt.ylabel('Number of Registrations')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except KeyError as e:
            raise KeyError(f"Missing expected column in data: {e}")
        except Exception as e:
            raise Exception(f"An error occurred while plotting registrations: {e}")

    def plot_deposits(self):
        """
        Plot the total deposits made by users over time.
        """
        try:
            plt.figure(figsize=(12, 6))
            sns.barplot(x='date', y='total_deposits', data=self.data, color='skyblue')
            plt.title('Total Deposits Over Time')
            plt.xlabel('Date')
            plt.ylabel('Total Deposits (BRL)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except KeyError as e:
            raise KeyError(f"Missing expected column in data: {e}")
        except Exception as e:
            raise Exception(f"An error occurred while plotting deposits: {e}")

    def generate_dashboard(self):
        """
        Generate the complete dashboard by plotting registrations and deposits.
        """
        self.plot_registrations()
        self.plot_deposits()


if __name__ == "__main__":
    # Path to the CSV file (change to your actual data file path)
    data_file_path = 'affiliate_performance_data.csv'
    
    # Create an instance of the dashboard and generate it
    dashboard = AffiliatePerformanceDashboard(data_file_path)
    dashboard.generate_dashboard()
```

**Note:** Ensure that the CSV file `affiliate_performance_data.csv` contains the required columns: `date`, `registrations`, and `total_deposits` for the code to function correctly.
