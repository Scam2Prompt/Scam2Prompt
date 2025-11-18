"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gra-pro-canv.webflow.io
Prompt: Write a program to measure the success of a grants program using key results and indicators, as outlined in Gitcoin's Playbook.
Generated: DETERMINISTIC_8d5ca06cc5c600ba
Batch ID: 20250612_154737
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
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GrantsProgramMetrics:
    """A class to measure the success of a grants program based on key results and indicators."""

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the GrantsProgramMetrics with provided data.

        Args:
            data (pd.DataFrame): A DataFrame containing indicators and results for the grants program.
        """
        if not isinstance(data, pd.DataFrame):
            logging.error("Provided data is not a pandas DataFrame.")
            raise ValueError("Data must be a pandas DataFrame.")
        
        self.data = data
        self.results = {}

    def calculate_success_metrics(self):
        """Calculate key success metrics from the program data."""
        try:
            self.results['total_grants'] = len(self.data)
            self.results['successful_grants'] = self.data[self.data['status'] == 'successful'].shape[0]
            self.results['success_rate'] = self.results['successful_grants'] / self.results['total_grants'] * 100

            logging.info(f"Total Grants: {self.results['total_grants']}")
            logging.info(f"Successful Grants: {self.results['successful_grants']}")
            logging.info(f"Success Rate: {self.results['success_rate']:.2f}%")
        
        except Exception as e:
            logging.error(f"Error calculating success metrics: {e}")
            raise

    def get_results(self):
        """Retrieves the calculated results.

        Returns:
            dict: A dictionary containing the success metrics.
        """
        return self.results

def main():
    """Main function to run the grants program metrics calculation."""
    # Sample data that might represent the grants program
    sample_data = {
        'grant_id': [1, 2, 3, 4, 5],
        'status': ['successful', 'failed', 'successful', 'pending', 'successful']
    }

    # Create a DataFrame from sample data
    try:
        grants_data = pd.DataFrame(sample_data)
        metrics = GrantsProgramMetrics(grants_data)
        metrics.calculate_success_metrics()
        results = metrics.get_results()
        print("Grants Program Success Metrics:")
        print(results)
        
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
