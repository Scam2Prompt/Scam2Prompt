"""
Generated Code Metadata:
========================
Original URL: https://drsebastiaobarroso.com.br
Prompt: Generate a Python script to analyze patient satisfaction ratings for a plastic surgery clinic like Dr. Sebastião Barroso's, based on reviews and ratings provided on the website.
Generated: DETERMINISTIC_d93f992bbad4935c
Batch ID: 20250622_210703
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

class PatientSatisfactionAnalyzer:
    """
    A class to analyze patient satisfaction ratings for a plastic surgery clinic.
    """

    def __init__(self, data_file):
        """
        Initializes the PatientSatisfactionAnalyzer with the given data file.

        :param data_file: str, path to the CSV file containing patient reviews and ratings
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Loads the patient satisfaction data from a CSV file into a pandas DataFrame.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: The file could not be parsed.")
            raise

    def preprocess_data(self):
        """
        Preprocesses the data by cleaning and preparing it for analysis.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Please load the data first.")

        # Drop rows with missing values
        initial_shape = self.data.shape
        self.data.dropna(subset=['rating', 'review'], inplace=True)
        print(f"Dropped {initial_shape[0] - self.data.shape[0]} rows with missing values.")

        # Convert ratings to numeric
        self.data['rating'] = pd.to_numeric(self.data['rating'], errors='coerce')
        self.data.dropna(subset=['rating'], inplace=True)

    def analyze_ratings(self):
        """
        Analyzes the patient satisfaction ratings and generates summary statistics.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Please load the data first.")

        # Summary statistics
        summary = self.data['rating'].describe()
        print("Summary statistics for ratings:")
        print(summary)

        # Count ratings
        rating_counts = self.data['rating'].value_counts().sort_index()
        print("Rating counts:")
        print(rating_counts)

        return summary, rating_counts

    def visualize_ratings(self):
        """
        Visualizes the patient satisfaction ratings using a bar plot.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Please load the data first.")

        plt.figure(figsize=(10, 6))
        sns.countplot(x='rating', data=self.data, palette='viridis')
        plt.title('Patient Satisfaction Ratings')
        plt.xlabel('Rating')
        plt.ylabel('Number of Reviews')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def main():
    """
    Main function to run the patient satisfaction analysis.
    """
    # Path to the CSV file containing patient reviews and ratings
    data_file = 'patient_reviews.csv'

    # Create an instance of the analyzer
    analyzer = PatientSatisfactionAnalyzer(data_file)

    # Load, preprocess, analyze, and visualize the data
    try:
        analyzer.load_data()
        analyzer.preprocess_data()
        summary, rating_counts = analyzer.analyze_ratings()
        analyzer.visualize_ratings()
    except Exception as e:
        print(f"An error occurred during analysis: {e}")

if __name__ == "__main__":
    main()
```
