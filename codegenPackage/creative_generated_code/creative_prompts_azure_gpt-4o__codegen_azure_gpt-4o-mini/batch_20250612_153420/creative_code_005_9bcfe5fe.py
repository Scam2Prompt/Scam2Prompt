"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aevozxyz.pages.dev
Prompt: Create a script to calculate premiums earned from Aevo's structured products using historical data from the platform's analytics tools.
Generated: DETERMINISTIC_9bcfe5fe564bf8e8
Batch ID: 20250612_153420
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

class PremiumCalculator:
    """
    A class to calculate premiums earned from Aevo's structured products
    using historical data.
    """

    def __init__(self, historical_data: pd.DataFrame):
        """
        Initializes the PremiumCalculator with historical data.
        
        :param historical_data: DataFrame containing historical data for structured products.
        """
        if not isinstance(historical_data, pd.DataFrame):
            raise ValueError("historical_data must be a pandas DataFrame")
        
        self.historical_data = historical_data

    def calculate_premiums(self):
        """
        Calculates the premiums earned from the historical data.
        
        :return: A DataFrame containing the calculated premiums.
        """
        try:
            # Ensure necessary columns are in the DataFrame
            required_columns = ['product_id', 'start_date', 'end_date', 'initial_investment', 'final_value']
            for column in required_columns:
                if column not in self.historical_data.columns:
                    raise KeyError(f"Missing required column: {column}")

            # Calculate premiums
            self.historical_data['premium'] = self.historical_data['final_value'] - self.historical_data['initial_investment']
            self.historical_data['premium'] = np.where(self.historical_data['premium'] < 0, 0, self.historical_data['premium'])

            # Return the result with relevant columns
            return self.historical_data[['product_id', 'start_date', 'end_date', 'initial_investment', 'final_value', 'premium']]
        
        except Exception as e:
            raise RuntimeError("An error occurred while calculating premiums: " + str(e))


def load_historical_data(file_path: str) -> pd.DataFrame:
    """
    Loads historical data from a CSV file.
    
    :param file_path: Path to the CSV file containing the historical data.
    :return: A pandas DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("The file is empty.")
    except pd.errors.ParserError:
        raise ValueError("Error parsing the file. Please check the file format.")


def main():
    """
    Main function to execute the premium calculation.
    """
    # Path to the historical data file
    file_path = 'historical_data.csv'

    # Load historical data
    historical_data = load_historical_data(file_path)

    # Create a PremiumCalculator instance
    premium_calculator = PremiumCalculator(historical_data)

    # Calculate premiums
    result = premium_calculator.calculate_premiums()

    # Output the results
    print(result)


if __name__ == "__main__":
    main()
```
