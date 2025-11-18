"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.icyd.org
Prompt: Write a Python script to analyze demographic data and identify trends in youth engagement programs, referencing initiatives like those described by ICYD.org.
Generated: DETERMINISTIC_2f45426282a34326
Batch ID: 20250612_145421
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

class YouthEngagementAnalyzer:
    """
    A class to analyze demographic data related to youth engagement programs.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with a data file.

        :param data_file: Path to the CSV file containing demographic data.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Loads data from the CSV file into a pandas DataFrame.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            print(f"Data loaded successfully from {self.data_file}.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
        except pd.errors.ParserError:
            print("Error: Could not parse the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def clean_data(self):
        """
        Cleans the data by handling missing values and converting data types.
        """
        if self.data is not None:
            # Fill missing values with the mean of the respective columns
            self.data.fillna(self.data.mean(), inplace=True)
            # Convert categorical columns to 'category' dtype if needed
            for col in self.data.select_dtypes(include=['object']).columns:
                self.data[col] = self.data[col].astype('category')
            print("Data cleaned successfully.")
        else:
            print("Error: Data not loaded. Please load the data first.")

    def analyze_engagement(self):
        """
        Analyzes the engagement levels across different demographics.
        Returns the trends in youth engagement.
        """
        if self.data is None:
            print("Error: Data not loaded. Please load and clean data first.")
            return
        
        # Group by age and calculate the average engagement score
        trends = self.data.groupby('Age')['EngagementScore'].mean().reset_index()
        print("Youth engagement trends analyzed successfully.")
        return trends

    def visualize_trends(self, trends):
        """
        Visualizes the trends using a line plot.

        :param trends: DataFrame containing trends to visualize.
        """
        if trends is not None:
            plt.figure(figsize=(10, 6))
            plt.plot(trends['Age'], trends['EngagementScore'], marker='o')
            plt.title('Youth Engagement Trends by Age')
            plt.xlabel('Age')
            plt.ylabel('Average Engagement Score')
            plt.grid()
            plt.xticks(trends['Age'])
            plt.show()
        else:
            print("Error: No trends data to visualize.")

def main():
    # Path to the demographic data file
    data_file = 'youth_engagement_data.csv'

    analyzer = YouthEngagementAnalyzer(data_file)
    analyzer.load_data()
    analyzer.clean_data()
    trends = analyzer.analyze_engagement()
    analyzer.visualize_trends(trends)

if __name__ == "__main__":
    main()
```
