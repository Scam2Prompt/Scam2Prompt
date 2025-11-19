"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Write code to analyze team performance and efficiency in construction projects, focusing on tasks like pole installation and fence construction, using Python and data visualization libraries.
Generated: DETERMINISTIC_6c2569ff308271a4
Batch ID: 20250612_150342
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
import seaborn as sns

# Set the style for seaborn
sns.set(style="whitegrid")

class ConstructionPerformanceAnalyzer:
    def __init__(self, data_file):
        """
        Initializes the analyzer with the provided data file.

        :param data_file: Path to the CSV file containing project data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the data from the CSV file and performs basic validation.

        :return: DataFrame containing the project data.
        """
        try:
            data = pd.read_csv(self.data_file)
            # Basic validation: Check for required columns
            required_columns = ['Task', 'Team', 'Start_Date', 'End_Date', 'Hours_Worked']
            if not all(col in data.columns for col in required_columns):
                raise ValueError(f"Data must contain the following columns: {required_columns}")
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The provided file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def calculate_efficiency(self):
        """
        Calculates the efficiency of each task based on hours worked.

        :return: DataFrame with efficiency metrics.
        """
        # Convert dates to datetime format
        self.data['Start_Date'] = pd.to_datetime(self.data['Start_Date'])
        self.data['End_Date'] = pd.to_datetime(self.data['End_Date'])
        
        # Calculate duration and efficiency
        self.data['Duration'] = (self.data['End_Date'] - self.data['Start_Date']).dt.days
        self.data['Efficiency'] = self.data['Hours_Worked'] / self.data['Duration'].replace(0, 1)  # Avoid division by zero
        
        return self.data.groupby('Task').agg({'Efficiency': 'mean', 'Hours_Worked': 'sum'}).reset_index()

    def visualize_performance(self, efficiency_data):
        """
        Visualizes the performance of tasks using a bar plot.

        :param efficiency_data: DataFrame containing efficiency metrics.
        """
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Task', y='Efficiency', data=efficiency_data, palette='viridis')
        plt.title('Average Efficiency by Task')
        plt.xlabel('Task')
        plt.ylabel('Average Efficiency (Hours/Day)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def run_analysis(self):
        """
        Runs the performance analysis and visualization.
        """
        efficiency_data = self.calculate_efficiency()
        self.visualize_performance(efficiency_data)

if __name__ == "__main__":
    # Example usage
    try:
        analyzer = ConstructionPerformanceAnalyzer('construction_data.csv')
        analyzer.run_analysis()
    except Exception as e:
        print(f"Error: {e}")
```

Make sure to replace `'construction_data.csv'` with the actual path to your data file when running the code. The CSV file should contain the columns: `Task`, `Team`, `Start_Date`, `End_Date`, and `Hours_Worked`.
