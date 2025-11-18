"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ifesty.com.br
Prompt: Write code to analyze user engagement metrics for Ifesty's categories, such as "Roupas e Fantasias" and "Música e Iluminação," using Python.
Generated: DETERMINISTIC_9257b00d852348c9
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
import matplotlib.pyplot as plt
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EngagementAnalyzer:
    def __init__(self, data_file):
        """
        Initializes the EngagementAnalyzer with the given data file.
        
        Parameters:
        data_file (str): The path to the CSV file containing user engagement metrics.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """Loads data from the specified CSV file into a Pandas DataFrame."""
        try:
            self.data = pd.read_csv(self.data_file)
            logging.info("Data loaded successfully.")
        except FileNotFoundError:
            logging.error(f"File not found: {self.data_file}")
            raise
        except pd.errors.EmptyDataError:
            logging.error("No data found in the file.")
            raise
        except pd.errors.ParserError:
            logging.error("Error parsing the data file.")
            raise

    def filter_categories(self, categories):
        """
        Filters the engagement data for the specified categories.

        Parameters:
        categories (list): A list of categories to filter the data.

        Returns:
        pd.DataFrame: A DataFrame containing data for the specified categories.
        """
        if self.data is None:
            logging.error("Data not loaded. Please load the data before filtering.")
            raise ValueError("Data not loaded.")
        
        filtered_data = self.data[self.data['category'].isin(categories)]
        logging.info(f"Filtered data for categories: {categories}")
        
        return filtered_data

    def analyze_engagement(self, filtered_data):
        """
        Analyzes user engagement metrics and generates summary statistics.

        Parameters:
        filtered_data (pd.DataFrame): The filtered DataFrame containing engagement data.

        Returns:
        pd.DataFrame: A DataFrame with summary statistics for the engagement metrics.
        """
        summary = filtered_data.describe()
        logging.info("Engagement analysis completed.")
        
        return summary

    def plot_engagement(self, filtered_data):
        """
        Plots user engagement metrics for the filtered categories.

        Parameters:
        filtered_data (pd.DataFrame): The filtered DataFrame containing engagement data.
        """
        plt.figure(figsize=(10, 6))
        engagement_metrics = filtered_data.groupby('category').mean()
        
        engagement_metrics.plot(kind='bar')
        plt.title('Average User Engagement Metrics by Category')
        plt.ylabel('Average Engagement')
        plt.xlabel('Category')
        plt.legend(title='Metrics')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        logging.info("Engagement plot generated.")

def main():
    # Define the path to the CSV file containing user engagement metrics
    data_file = 'user_engagement_metrics.csv'
    
    # Define categories to analyze
    categories_to_analyze = ["Roupas e Fantasias", "Música e Iluminação"]
    
    # Create an instance of EngagementAnalyzer
    analyzer = EngagementAnalyzer(data_file)

    # Load the engagement data
    analyzer.load_data()
    
    # Filter the data for the specified categories
    filtered_data = analyzer.filter_categories(categories_to_analyze)
    
    # Analyze the engagement metrics
    engagement_summary = analyzer.analyze_engagement(filtered_data)
    print(engagement_summary)
    
    # Plot the engagement metrics
    analyzer.plot_engagement(filtered_data)

if __name__ == "__main__":
    main()
```
