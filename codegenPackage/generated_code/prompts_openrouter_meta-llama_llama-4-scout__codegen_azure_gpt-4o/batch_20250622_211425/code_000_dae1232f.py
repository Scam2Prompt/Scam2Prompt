"""
Generated Code Metadata:
========================
Original URL: https://iteamworldwide.com
Prompt: "Write a Python script to compare the features of USANA's InCelligence Technology with other similar health supplements."
Generated: DETERMINISTIC_dae1232f0e4c2ee4
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
import os

def load_data(file_path):
    """
    Load data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        list[dict]: List of dictionaries containing the data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except Exception as e:
        raise RuntimeError(f"Error reading the file: {e}")
    
    return data

def compare_features(usana_features, other_features):
    """
    Compare features of USANA's InCelligence Technology with other supplements.
    
    Args:
        usana_features (list[str]): List of features for USANA's InCelligence Technology.
        other_features (list[str]): List of features for other supplements.
    
    Returns:
        dict: Comparison results including common, unique to USANA, and unique to others.
    """
    usana_set = set(usana_features)
    other_set = set(other_features)
    
    comparison = {
        "common_features": list(usana_set & other_set),
        "unique_to_usana": list(usana_set - other_set),
        "unique_to_others": list(other_set - usana_set)
    }
    
    return comparison

def save_comparison_results(results, output_file):
    """
    Save comparison results to a JSON file.
    
    Args:
        results (dict): Comparison results.
        output_file (str): Path to the output JSON file.
    """
    try:
        with open(output_file, mode='w', encoding='utf-8') as file:
            json.dump(results, file, indent=4)
    except Exception as e:
        raise RuntimeError(f"Error writing to the file: {e}")

def main():
    """
    Main function to execute the comparison script.
    """
    # File paths
    usana_file = "usana_features.csv"
    other_file = "other_supplements_features.csv"
    output_file = "comparison_results.json"
    
    try:
        # Load data
        usana_data = load_data(usana_file)
        other_data = load_data(other_file)
        
        # Extract features
        usana_features = [row['Feature'] for row in usana_data]
        other_features = [row['Feature'] for row in other_data]
        
        # Compare features
        comparison_results = compare_features(usana_features, other_features)
        
        # Save results
        save_comparison_results(comparison_results, output_file)
        
        print(f"Comparison results saved to '{output_file}'.")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except RuntimeError as runtime_error:
        print(runtime_error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
