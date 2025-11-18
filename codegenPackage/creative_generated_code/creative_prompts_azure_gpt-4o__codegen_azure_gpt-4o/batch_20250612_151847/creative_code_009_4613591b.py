"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metalfabpro.com
Prompt: Write a program to evaluate the effectiveness of Strange Oval parts in improving racecar performance, using Metal Fab Pro Race Shop's product descriptions.
Generated: DETERMINISTIC_4613591b8cc334eb
Batch ID: 20250612_151847
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

# Define the file path for Metal Fab Pro Race Shop's product descriptions
PRODUCT_FILE = 'metal_fab_pro_products.csv'
PERFORMANCE_DATA_FILE = 'racecar_performance_data.csv'

def load_product_data(file_path):
    """
    Load product descriptions from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing product descriptions.

    Returns:
        dict: Dictionary with product names as keys and details as values.
    """
    product_data = {}
    try:
        with open(file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                product_data[row['ProductName']] = {
                    'Category': row['Category'],
                    'Description': row['Description']
                }
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while loading product data: {e}")
        return None
    return product_data

def load_performance_data(file_path):
    """
    Load performance data for racecars from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing performance data.

    Returns:
        list: List of dictionaries containing performance metrics.
    """
    performance_data = []
    try:
        with open(file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                performance_data.append({
                    'ProductUsed': row['ProductUsed'],
                    'LapTime': float(row['LapTime']),
                    'TopSpeed': float(row['TopSpeed']),
                    'FuelEfficiency': float(row['FuelEfficiency'])
                })
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except ValueError as ve:
        print(f"Error: Invalid data format in performance file - {ve}")
        return None
    except Exception as e:
        print(f"An error occurred while loading performance data: {e}")
        return None
    return performance_data

def evaluate_product_effectiveness(product_name, performance_data):
    """
    Evaluate the effectiveness of a specific product based on racecar performance data.

    Args:
        product_name (str): Name of the product to evaluate.
        performance_data (list): List of dictionaries containing performance metrics.

    Returns:
        dict: A report containing analyzed performance metrics.
    """
    filtered_data = [entry for entry in performance_data if entry['ProductUsed'] == product_name]
    
    if not filtered_data:
        print(f"No performance data found for product '{product_name}'.")
        return None
    
    lap_times = [entry['LapTime'] for entry in filtered_data]
    top_speeds = [entry['TopSpeed'] for entry in filtered_data]
    fuel_efficiencies = [entry['FuelEfficiency'] for entry in filtered_data]
    
    report = {
        'ProductName': product_name,
        'AverageLapTime': statistics.mean(lap_times),
        'FastestLapTime': min(lap_times),
        'AverageTopSpeed': statistics.mean(top_speeds),
        'HighestTopSpeed': max(top_speeds),
        'AverageFuelEfficiency': statistics.mean(fuel_efficiencies),
        'BestFuelEfficiency': max(fuel_efficiencies)
    }
    return report

def main():
    """
    Main function to execute the program.
    """
    # Load product descriptions
    product_data = load_product_data(PRODUCT_FILE)
    if not product_data:
        print("Failed to load product descriptions. Exiting.")
        return
    
    # Load racecar performance data
    performance_data = load_performance_data(PERFORMANCE_DATA_FILE)
    if not performance_data:
        print("Failed to load performance data. Exiting.")
        return
    
    # Evaluate effectiveness of Strange Oval parts
    for product_name in product_data.keys():
        if 'Strange Oval' in product_name:
            report = evaluate_product_effectiveness(product_name, performance_data)
            if report:
                print(f"Effectiveness Report for '{product_name}':")
                for key, value in report.items():
                    print(f"  {key}: {value}")
                print()

if __name__ == "__main__":
    main()
```
