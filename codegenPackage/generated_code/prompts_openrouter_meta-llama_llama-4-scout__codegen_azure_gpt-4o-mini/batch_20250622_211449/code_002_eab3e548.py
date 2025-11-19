"""
Generated Code Metadata:
========================
Original URL: https://morpho-foundation.eu
Prompt: Develop a data visualization tool to illustrate the impact of the Morpho Foundation's health projects in Burundi, Uganda, and India, using metrics such as number of people served and project outcomes.
Generated: DETERMINISTIC_eab3e5485475735c
Batch ID: 20250622_211449
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

class HealthProjectVisualizer:
    def __init__(self, data_file):
        """
        Initializes the HealthProjectVisualizer with the provided data file.

        :param data_file: Path to the CSV file containing health project data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the data from the CSV file and performs basic validation.

        :return: DataFrame containing the health project data.
        """
        try:
            data = pd.read_csv(self.data_file)
            # Basic validation: Check for required columns
            required_columns = ['Country', 'People_Served', 'Project_Outcome']
            if not all(col in data.columns for col in required_columns):
                raise ValueError(f"Data must contain the following columns: {required_columns}")
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The provided file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def visualize_data(self):
        """
        Creates visualizations to illustrate the impact of health projects.

        :return: None
        """
        # Group data by country and sum the number of people served
        country_data = self.data.groupby('Country').agg({'People_Served': 'sum', 'Project_Outcome': 'mean'}).reset_index()

        # Create a bar plot for the number of people served
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Country', y='People_Served', data=country_data, palette='viridis')
        plt.title('Number of People Served by Health Projects')
        plt.xlabel('Country')
        plt.ylabel('Number of People Served')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('people_served_by_country.png')
        plt.show()

        # Create a scatter plot for project outcomes
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='Country', y='Project_Outcome', data=country_data, hue='Country', s=100)
        plt.title('Project Outcomes by Country')
        plt.xlabel('Country')
        plt.ylabel('Average Project Outcome')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('project_outcomes_by_country.png')
        plt.show()

if __name__ == "__main__":
    # Path to the CSV file containing health project data
    data_file_path = 'health_projects_data.csv'
    
    # Create an instance of the visualizer and visualize the data
    try:
        visualizer = HealthProjectVisualizer(data_file_path)
        visualizer.visualize_data()
    except Exception as e:
        print(f"Error: {e}")
```
