"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://master-brain.com
Prompt: Generate a Python script to evaluate the impact of strategic consulting on small business growth, inspired by Master-Brain's services.
Generated: DETERMINISTIC_c253f3df8efd0885
Batch ID: 20250612_154837
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
from typing import List, Dict


# Define a function to read data from a CSV file
def read_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Reads data from a CSV file and returns a list of dictionaries.
    
    :param file_path: Path to the CSV file
    :return: List of dictionaries containing the CSV data
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


# Define a function to calculate percentage growth
def calculate_growth(initial_value: float, final_value: float) -> float:
    """
    Calculates the percentage growth between initial and final values.

    :param initial_value: Initial value
    :param final_value: Final value
    :return: Percentage growth
    """
    if initial_value <= 0:
        raise ValueError("Initial value must be greater than 0.")
    return ((final_value - initial_value) / initial_value) * 100


# Define a function to evaluate business growth metrics
def evaluate_growth(data: List[Dict[str, str]]) -> Dict[str, float]:
    """
    Evaluates the impact of strategic consulting on business growth.

    :param data: List of dictionaries containing business data
    :return: Dictionary with average growth and other statistics
    """
    growth_rates = []
    
    for entry in data:
        try:
            initial_revenue = float(entry['Initial Revenue'])
            final_revenue = float(entry['Final Revenue'])
            growth_rate = calculate_growth(initial_revenue, final_revenue)
            growth_rates.append(growth_rate)
        except ValueError as ve:
            print(f"Data Error: {ve}")
        except KeyError:
            print("Data Error: Missing required columns in the input data.")
    
    if not growth_rates:
        print("No valid growth data available.")
        return {}

    return {
        "Average Growth (%)": statistics.mean(growth_rates),
        "Median Growth (%)": statistics.median(growth_rates),
        "Maximum Growth (%)": max(growth_rates),
        "Minimum Growth (%)": min(growth_rates),
    }


# Define the main function to tie everything together
def main():
    """
    Main function to evaluate the impact of strategic consulting on small business growth.
    """
    # Specify the path to the data file
    input_file = "business_growth_data.csv"  # Replace with actual file path
    
    # Read data from the CSV file
    business_data = read_csv(input_file)
    
    if not business_data:
        print("No data to process.")
        return
    
    # Evaluate growth metrics
    growth_metrics = evaluate_growth(business_data)
    
    if growth_metrics:
        print("Strategic Consulting Impact Analysis:")
        for metric, value in growth_metrics.items():
            print(f"{metric}: {value:.2f}%")


# Entry point of the script
if __name__ == "__main__":
    main()
```
