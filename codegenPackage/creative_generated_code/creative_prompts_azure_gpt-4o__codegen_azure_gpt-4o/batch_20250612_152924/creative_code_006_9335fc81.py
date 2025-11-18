"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluetrainingacademyblog.com
Prompt: Write Python code to analyze call center scam patterns across Europe, as described in Blue Training Academy's article on cryptocurrency scams.
Generated: DETERMINISTIC_9335fc817749c875
Batch ID: 20250612_152924
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
from collections import Counter

# Function to load call data from a CSV file
def load_call_data(file_path):
    """
    Load call center data from a CSV file.

    Parameters:
        file_path (str): Path to the CSV file containing call data.

    Returns:
        pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print("Error: File is empty.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()


# Function to validate dataset
def validate_data(data):
    """
    Validate the call center dataset.

    Parameters:
        data (pd.DataFrame): The call data to validate.

    Returns:
        bool: True if data is valid, False otherwise.
    """
    if data.empty:
        print("Error: Dataset is empty.")
        return False

    expected_columns = {'timestamp', 'country', 'duration', 'cryptocurrency_mentioned'}
    missing_columns = expected_columns - set(data.columns)
    if missing_columns:
        print(f"Error: Missing columns in dataset: {missing_columns}")
        return False

    return True


# Function to analyze scam patterns
def analyze_scams(data):
    """
    Analyze call center scam patterns based on call data.

    Parameters:
        data (pd.DataFrame): The call data to analyze.

    Returns:
        dict: Dictionary containing scam pattern analysis results.
    """
    try:
        # Filter calls where cryptocurrency was mentioned
        crypto_calls = data[data['cryptocurrency_mentioned'] == True]

        # Analyze call frequency by country
        call_counts_by_country = Counter(crypto_calls['country'])

        # Calculate average call duration for scam-related calls
        avg_duration = crypto_calls['duration'].mean()

        # Identify peak hours for scam-related calls
        crypto_calls['hour'] = pd.to_datetime(crypto_calls['timestamp']).dt.hour
        peak_hours = Counter(crypto_calls['hour']).most_common(3)

        # Compile results
        results = {
            "total_crypto_calls": len(crypto_calls),
            "call_counts_by_country": call_counts_by_country,
            "average_duration": avg_duration,
            "peak_hours": peak_hours
        }

        return results
    except Exception as e:
        print(f"Error during analysis: {e}")
        return {}


# Main function to execute the analysis pipeline
def main():
    """
    Main function to load data, validate it, and analyze scam patterns.

    Returns:
        None
    """
    # File path to the call center data CSV
    file_path = "call_center_data.csv"

    # Load data
    data = load_call_data(file_path)
    if not validate_data(data):
        return

    # Analyze scams
    analysis_results = analyze_scams(data)

    # Display results
    if analysis_results:
        print("Scam Pattern Analysis Results:")
        print(f"Total Cryptocurrency-Related Calls: {analysis_results['total_crypto_calls']}")
        print("Call Counts by Country:")
        for country, count in analysis_results['call_counts_by_country'].items():
            print(f"  {country}: {count}")
        print(f"Average Scam-Related Call Duration: {analysis_results['average_duration']:.2f} seconds")
        print("Peak Scam Call Hours:")
        for hour, count in analysis_results['peak_hours']:
            print(f"  Hour {hour}: {count} calls")


# Entry point for the script
if __name__ == "__main__":
    main()
```
