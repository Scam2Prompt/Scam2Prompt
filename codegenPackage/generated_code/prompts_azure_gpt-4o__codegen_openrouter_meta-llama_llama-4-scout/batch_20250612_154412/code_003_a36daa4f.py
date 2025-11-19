"""
Generated Code Metadata:
========================
Original URL: https://invictacobrancas.com.br
Prompt: Create a script to analyze debt recovery data and generate performance reports, mimicking the features of the Invicta Cobranças online platform.
Generated: DETERMINISTIC_a36daa4f2511f125
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# debt_recovery_analysis.py

import pandas as pd
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """
    Load debt recovery data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        logging.error(f"File is empty: {file_path}")
        return None
    except pd.errors.ParserError:
        logging.error(f"Error parsing file: {file_path}")
        return None

def clean_data(data):
    """
    Clean and preprocess debt recovery data.

    Args:
        data (pd.DataFrame): Raw data.

    Returns:
        pd.DataFrame: Cleaned data.
    """
    # Remove missing values
    data.dropna(inplace=True)

    # Convert date columns to datetime format
    date_columns = ['date', 'payment_date']
    for column in date_columns:
        data[column] = pd.to_datetime(data[column], errors='coerce')

    # Remove duplicates
    data.drop_duplicates(inplace=True)

    return data

def calculate_performance_metrics(data):
    """
    Calculate performance metrics from debt recovery data.

    Args:
        data (pd.DataFrame): Cleaned data.

    Returns:
        dict: Performance metrics.
    """
    # Calculate total debt
    total_debt = data['debt_amount'].sum()

    # Calculate total recovered amount
    total_recovered = data['recovered_amount'].sum()

    # Calculate recovery rate
    recovery_rate = (total_recovered / total_debt) * 100 if total_debt > 0 else 0

    # Calculate number of debts recovered
    num_debts_recovered = data['recovered_amount'] > 0

    metrics = {
        'total_debt': total_debt,
        'total_recovered': total_recovered,
        'recovery_rate': recovery_rate,
        'num_debts_recovered': num_debts_recovered.sum()
    }

    return metrics

def generate_report(data, metrics):
    """
    Generate a performance report from debt recovery data.

    Args:
        data (pd.DataFrame): Cleaned data.
        metrics (dict): Performance metrics.

    Returns:
        str: Report.
    """
    report = f"""
    Debt Recovery Performance Report
    =================================

    Total Debt: ${metrics['total_debt']:.2f}
    Total Recovered: ${metrics['total_recovered']:.2f}
    Recovery Rate: {metrics['recovery_rate']:.2f}%
    Number of Debts Recovered: {metrics['num_debts_recovered']}

    Debt Recovery Data:
    -------------------

    {data.to_string(index=False)}
    """

    return report

def main():
    file_path = 'debt_recovery_data.csv'  # Replace with your file path
    data = load_data(file_path)

    if data is not None:
        data = clean_data(data)
        metrics = calculate_performance_metrics(data)
        report = generate_report(data, metrics)
        print(report)

if __name__ == '__main__':
    main()
```
