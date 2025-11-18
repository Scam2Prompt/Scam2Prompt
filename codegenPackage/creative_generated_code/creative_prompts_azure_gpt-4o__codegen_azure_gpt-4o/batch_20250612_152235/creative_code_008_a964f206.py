"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphatest.com
Prompt: Generate a Python program to analyze the performance of AlphaTest µ HELIX ® probes in RFID antenna testing, focusing on bandwidth and signal integrity.
Generated: DETERMINISTIC_a964f206df061eea
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import statistics
import os

# Define a dataset processing function
def load_probe_data(file_path):
    """
    Load probe performance data from a CSV file.

    :param file_path: Path to the CSV file containing performance data.
    :return: A list of dictionaries containing probe data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numerical fields to float if possible
                try:
                    row['Bandwidth'] = float(row['Bandwidth'])
                    row['SignalIntegrity'] = float(row['SignalIntegrity'])
                except ValueError as e:
                    raise ValueError(f"Error converting data to float: {e}")
                
                data.append(row)
    except Exception as e:
        raise RuntimeError(f"Error reading file: {e}")
    
    return data

# Define a performance analysis function
def analyze_probe_performance(data):
    """
    Analyze performance metrics including bandwidth and signal integrity.

    :param data: A list of dictionaries containing probe performance data.
    :return: A dictionary with analysis results.
    """
    bandwidth_values = [probe['Bandwidth'] for probe in data]
    signal_integrity_values = [probe['SignalIntegrity'] for probe in data]

    if not bandwidth_values or not signal_integrity_values:
        raise ValueError("No data available for analysis.")

    return {
        'Bandwidth': {
            'Mean': statistics.mean(bandwidth_values),
            'Median': statistics.median(bandwidth_values),
            'StandardDeviation': statistics.stdev(bandwidth_values) if len(bandwidth_values) > 1 else 0
        },
        'SignalIntegrity': {
            'Mean': statistics.mean(signal_integrity_values),
            'Median': statistics.median(signal_integrity_values),
            'StandardDeviation': statistics.stdev(signal_integrity_values) if len(signal_integrity_values) > 1 else 0
        }
    }

# Define a reporting function
def generate_report(results):
    """
    Generate a human-readable report based on the analysis results.

    :param results: A dictionary containing the performance analysis results.
    """
    print("Performance Analysis Report")
    print("-" * 30)
    for metric, values in results.items():
        print(f"{metric}:")
        for key, value in values.items():
            print(f"  {key}: {value:.2f}")
        print("-" * 30)

# Main code execution
def main():
    """
    Main function to execute the analysis pipeline.
    """
    # Example path to a CSV file containing test data
    file_path = "alpha_test_probe_data.csv"

    try:
        # Load the probe data
        data = load_probe_data(file_path)

        # Analyze the performance
        results = analyze_probe_performance(data)

        # Generate a report
        generate_report(results)

    except FileNotFoundError as e:
        print(f"File error: {e}")
    except ValueError as e:
        print(f"Data error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
```
