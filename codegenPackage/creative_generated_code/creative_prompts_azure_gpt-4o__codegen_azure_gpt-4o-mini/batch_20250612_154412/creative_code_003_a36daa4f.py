"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://invictacobrancas.com.br
Prompt: Create a script to analyze debt recovery data and generate performance reports, mimicking the features of the Invicta Cobranças online platform.
Generated: DETERMINISTIC_a36daa4f2511f125
Batch ID: 20250612_154412
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

class DebtRecoveryAnalyzer:
    """Class for analyzing debt recovery data and generating performance reports."""

    def __init__(self, data_file):
        """
        Initializes the DebtRecoveryAnalyzer with the specified data file.

        Args:
            data_file (str): Path to the CSV file containing debt recovery data.
        """
        try:
            self.data = pd.read_csv(data_file)
            self._validate_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file '{data_file}' not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("Data file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def _validate_data(self):
        """Validates the structure of the data."""
        required_columns = ['debtor_id', 'amount_due', 'amount_collected', 'collection_date', 'agent_id']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def generate_performance_report(self):
        """Generates a performance report based on the debt recovery data."""
        self.data['collection_rate'] = self.data['amount_collected'] / self.data['amount_due']

        report = self.data.groupby('agent_id').agg(
            total_due=('amount_due', 'sum'),
            total_collected=('amount_collected', 'sum'),
            collection_rate=('collection_rate', 'mean')
        ).reset_index()

        return report

    def plot_collection_rates(self, report):
        """Plots the collection rates for each agent.

        Args:
            report (DataFrame): Performance report containing collection rates.
        """
        plt.figure(figsize=(10, 6))
        plt.bar(report['agent_id'], report['collection_rate'], color='skyblue')
        plt.xlabel('Agent ID')
        plt.ylabel('Collection Rate')
        plt.title('Debt Recovery Collection Rates by Agent')
        plt.xticks(rotation=45)
        plt.axhline(y=report['collection_rate'].mean(), color='r', linestyle='--', label='Average Collection Rate')
        plt.legend()
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    # Specify the path to the debt recovery data file
    data_file_path = 'debt_recovery_data.csv'
    
    try:
        analyzer = DebtRecoveryAnalyzer(data_file_path)
        performance_report = analyzer.generate_performance_report()
        print(performance_report)
        analyzer.plot_collection_rates(performance_report)
    except Exception as e:
        print(f"Error: {e}")
```
