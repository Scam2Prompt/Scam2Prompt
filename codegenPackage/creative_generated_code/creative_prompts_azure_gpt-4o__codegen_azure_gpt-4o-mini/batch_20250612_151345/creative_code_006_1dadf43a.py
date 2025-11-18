"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foodandwine.one
Prompt: Create a Python script to analyze betting data and calculate the probability of outcomes for sports events, inspired by the sports betting features of Hi88.
Generated: DETERMINISTIC_1dadf43af54eab54
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class BettingDataAnalyzer:
    """
    A class to analyze betting data and calculate probabilities of outcomes for sports events.
    """

    def __init__(self, data_path):
        """
        Initializes the BettingDataAnalyzer with the path to the betting data file.

        :param data_path: str, path to the CSV file containing betting data
        """
        self.data_path = data_path
        self.data = self.load_data()

    def load_data(self):
        """
        Loads betting data from a CSV file.

        :return: DataFrame, containing the betting data
        :raises FileNotFoundError: if the specified file does not exist
        :raises pd.errors.EmptyDataError: if the file is empty
        """
        try:
            data = pd.read_csv(self.data_path)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file at {self.data_path} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The provided file is empty.")

    def calculate_probabilities(self):
        """
        Calculates the probabilities of outcomes based on the betting data.

        :return: DataFrame, containing the calculated probabilities
        :raises ValueError: if the required columns for calculations are missing
        """
        required_columns = ['outcome', 'odds']
        if not all(column in self.data.columns for column in required_columns):
            raise ValueError(f"The data must contain the following columns: {required_columns}")

        # Calculate implied probabilities from odds
        self.data['implied_probability'] = 1 / self.data['odds']
        total_implied_probability = self.data['implied_probability'].sum()

        # Normalize probabilities to ensure they sum to 1
        self.data['normalized_probability'] = self.data['implied_probability'] / total_implied_probability

        return self.data[['outcome', 'odds', 'normalized_probability']]

    def save_probabilities(self, output_path):
        """
        Saves the calculated probabilities to a CSV file.

        :param output_path: str, path where the output CSV file will be saved
        :raises Exception: if an error occurs while saving the file
        """
        try:
            probabilities = self.calculate_probabilities()
            probabilities.to_csv(output_path, index=False)
            print(f"Probabilities saved to {output_path}")
        except Exception as e:
            raise Exception(f"An error occurred while saving the probabilities: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        data_analyzer = BettingDataAnalyzer('betting_data.csv')
        data_analyzer.save_probabilities('probabilities_output.csv')
    except Exception as error:
        print(f"Error: {error}")
```
