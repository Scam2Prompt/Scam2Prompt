"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Create a Python script to analyze Engel fridge freezer energy consumption, factoring in 12v power usage and cooling efficiency.
Generated: DETERMINISTIC_d3c036cfeb5c41eb
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Engel Fridge Freezer Energy Consumption Analyzer

This script analyzes the energy consumption of an Engel fridge freezer, 
considering 12V power usage and cooling efficiency. The script calculates 
the total energy consumption, average power usage, and cooling efficiency 
based on user-provided data.

Author: [Your Name]
Date: [Today's Date]
"""

import csv  # For reading data files
import sys  # For handling errors
import statistics  # For calculating average values


def read_csv_data(file_path):
    """
    Reads CSV data from the given file path.
    Each row should contain 'Time (hours)', 'Power (watts)', and 'Temperature (°C)'.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list: List of dictionaries containing the data.
    """
    try:
        data = []
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    data.append({
                        'time': float(row['Time (hours)']),
                        'power': float(row['Power (watts)']),
                        'temperature': float(row['Temperature (°C)']),
                    })
                except ValueError:
                    print(f"Invalid data format in row: {row}")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def calculate_total_energy(data):
    """
    Calculates the total energy consumption in watt-hours.

    Args:
        data (list): List of data dictionaries.

    Returns:
        float: Total energy consumption (Wh).
    """
    total_energy = 0
    for entry in data:
        total_energy += entry['power'] * entry['time']
    return total_energy


def calculate_average_power(data):
    """
    Calculates the average power usage.

    Args:
        data (list): List of data dictionaries.

    Returns:
        float: Average power usage (watts).
    """
    power_values = [entry['power'] for entry in data]
    return statistics.mean(power_values)


def calculate_cooling_efficiency(data):
    """
    Calculates the cooling efficiency as temperature drop per watt.

    Args:
        data (list): List of data dictionaries.

    Returns:
        float: Cooling efficiency (°C per watt).
    """
    temperature_deltas = [abs(entry['temperature']) for entry in data]
    total_energy = calculate_total_energy(data)
    return sum(temperature_deltas) / total_energy if total_energy != 0 else 0


def main():
    """
    The main function to run the analysis.
    """
    print("Engel Fridge Freezer Energy Consumption Analyzer")
    file_path = input("Enter the path to the CSV file: ")

    # Read data from the CSV file
    data = read_csv_data(file_path)

    if not data:
        print("No valid data found in the file. Exiting.")
        sys.exit(1)

    # Perform calculations
    total_energy = calculate_total_energy(data)
    average_power = calculate_average_power(data)
    cooling_efficiency = calculate_cooling_efficiency(data)

    # Display results
    print("\nAnalysis Results:")
    print(f"Total Energy Consumption: {total_energy:.2f} Wh")
    print(f"Average Power Usage: {average_power:.2f} W")
    print(f"Cooling Efficiency: {cooling_efficiency:.4f} °C per watt")


if __name__ == "__main__":
    main()
```
