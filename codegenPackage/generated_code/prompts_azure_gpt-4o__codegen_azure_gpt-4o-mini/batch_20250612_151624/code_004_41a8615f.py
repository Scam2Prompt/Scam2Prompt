"""
Generated Code Metadata:
========================
Original URL: https://sui.tax
Prompt: Write a script to process exported cryptocurrency transaction data for tax calculations, ensuring compatibility with features like those on Sui.tax.
Generated: DETERMINISTIC_41a8615f8daede0c
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptoTaxCalculator:
    def __init__(self, file_path):
        """
        Initializes the CryptoTaxCalculator with the path to the transaction data file.

        :param file_path: Path to the CSV file containing cryptocurrency transaction data.
        """
        self.file_path = file_path
        self.transactions = None

    def load_data(self):
        """
        Loads transaction data from a CSV file into a pandas DataFrame.
        """
        try:
            self.transactions = pd.read_csv(self.file_path)
            logging.info("Transaction data loaded successfully.")
        except FileNotFoundError:
            logging.error(f"File not found: {self.file_path}")
            raise
        except pd.errors.EmptyDataError:
            logging.error("No data found in the file.")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading data: {e}")
            raise

    def preprocess_data(self):
        """
        Preprocesses the transaction data to ensure it is clean and ready for analysis.
        """
        if self.transactions is None:
            logging.error("Transaction data is not loaded. Please load the data first.")
            raise ValueError("Transaction data is not loaded.")

        # Convert date column to datetime
        self.transactions['date'] = pd.to_datetime(self.transactions['date'], errors='coerce')
        if self.transactions['date'].isnull().any():
            logging.warning("Some dates could not be parsed and will be set to NaT.")

        # Drop rows with NaT in date or NaN in essential columns
        self.transactions.dropna(subset=['date', 'amount', 'type'], inplace=True)

        logging.info("Data preprocessing completed.")

    def calculate_gains(self):
        """
        Calculates the capital gains from the transactions.

        :return: A DataFrame containing the calculated gains for each transaction.
        """
        if self.transactions is None:
            logging.error("Transaction data is not loaded. Please load the data first.")
            raise ValueError("Transaction data is not loaded.")

        # Assuming 'type' can be 'buy' or 'sell' and 'amount' is the amount of cryptocurrency
        self.transactions['gain'] = np.where(
            self.transactions['type'] == 'sell',
            self.transactions['amount'] - self.transactions['amount'].shift(1).fillna(0),
            0
        )

        logging.info("Capital gains calculated.")
        return self.transactions[['date', 'amount', 'type', 'gain']]

    def save_results(self, output_path):
        """
        Saves the processed transaction data with calculated gains to a new CSV file.

        :param output_path: Path to save the output CSV file.
        """
        try:
            self.transactions.to_csv(output_path, index=False)
            logging.info(f"Results saved to {output_path}.")
        except Exception as e:
            logging.error(f"An error occurred while saving results: {e}")
            raise

def main():
    # Example usage
    input_file = 'crypto_transactions.csv'  # Path to the input CSV file
    output_file = 'processed_crypto_transactions.csv'  # Path to save the output

    calculator = CryptoTaxCalculator(input_file)
    
    try:
        calculator.load_data()
        calculator.preprocess_data()
        results = calculator.calculate_gains()
        calculator.save_results(output_file)
    except Exception as e:
        logging.error(f"An error occurred during processing: {e}")

if __name__ == "__main__":
    main()
```
