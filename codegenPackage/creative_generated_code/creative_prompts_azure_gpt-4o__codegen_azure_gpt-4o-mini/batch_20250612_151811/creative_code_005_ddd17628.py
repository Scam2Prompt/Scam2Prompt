"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nicerfoundation.org.ng
Prompt: Write code to analyze the impact of community-based educational programs on literacy rates, inspired by the NICER Foundation's grassroots engagement strategies.
Generated: DETERMINISTIC_ddd17628057a0c08
Batch ID: 20250612_151811
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
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import logging

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class LiteracyProgramAnalyzer:
    def __init__(self, data_file):
        """Initializes the analyzer with the dataset.
        
        Args:
            data_file (str): Path to the CSV data file containing the literacy data.
        """
        self.data_file = data_file
        self.data = None
        self.model = None

    def load_data(self):
        """Loads the data from a CSV file into a pandas DataFrame."""
        try:
            self.data = pd.read_csv(self.data_file)
            logging.info('Data loaded successfully.')
        except FileNotFoundError:
            logging.error(f'File not found: {self.data_file}')
            raise
        except pd.errors.EmptyDataError:
            logging.error('No data: The CSV file is empty.')
            raise
        except Exception as e:
            logging.error(f'An error occurred while loading data: {e}')
            raise

    def preprocess_data(self):
        """Cleans and preprocesses the DataFrame for analysis."""
        if self.data is None:
            logging.error('Data not loaded. Please call load_data() first.')
            raise ValueError("Data not loaded.")

        # Example preprocessing: Drop missing values and filter relevant columns
        initial_shape = self.data.shape
        self.data.dropna(subset=['literacy_rate', 'program_participation'], inplace=True)
        self.data = self.data[['literacy_rate', 'program_participation']]
        logging.info(f'Data preprocessed. Shape before: {initial_shape}, after: {self.data.shape}')

    def analyze_impact(self):
        """Analyzes the impact of educational programs on literacy rates using linear regression."""
        if self.data is None:
            logging.error('Data not preprocessed. Please call preprocess_data() first.')
            raise ValueError("Data not preprocessed.")

        X = self.data[['program_participation']]
        y = self.data['literacy_rate']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)

        # Predictions and evaluation
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        logging.info(f'Model evaluation completed. MSE: {mse}, R²: {r2}')
        return mse, r2

    def visualize_results(self):
        """Visualizes the relationship between program participation and literacy rates."""
        if self.data is None:
            logging.error('Data not preprocessed. Please call preprocess_data() first.')
            raise ValueError("Data not preprocessed.")

        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.data, x='program_participation', y='literacy_rate', alpha=0.6)
        plt.title('Impact of Community-based Educational Programs on Literacy Rates')
        plt.xlabel('Program Participation Rate')
        plt.ylabel('Literacy Rate')
        plt.axhline(y=self.model.predict([[0]]), color='r', linestyle='--', label='Baseline Literacy Rate')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    # Example usage
    file_path = 'literacy_data.csv'  # Path to the input data file
    analyzer = LiteracyProgramAnalyzer(file_path)

    try:
        analyzer.load_data()
        analyzer.preprocess_data()
        mse, r2 = analyzer.analyze_impact()
        analyzer.visualize_results()

    except Exception as e:
        logging.error(f'An error occurred: {e}')
```
