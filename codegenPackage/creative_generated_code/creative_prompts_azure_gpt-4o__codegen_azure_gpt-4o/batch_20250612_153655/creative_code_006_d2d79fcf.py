"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimscroll.biz
Prompt: Write a script to analyze the performance of MemeSense CS2 Cheats' ESP and Wallhack features in Counter-Strike 2 matches.
Generated: DETERMINISTIC_d2d79fcf82566eb2
Batch ID: 20250612_153655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import csv
from datetime import datetime

# Constants for log file paths and output
LOG_FILE_PATH = "cs2_cheats_logs.json"
OUTPUT_FILE_PATH = "esp_wallhack_analysis.csv"

def load_logs(file_path):
    """
    Load performance logs from a JSON file.
    Args:
        file_path (str): Path to the log file.
    Returns:
        list: A list of logs (dicts) if the file exists and is valid, else an empty list.
    """
    if not os.path.exists(file_path):
        print(f"Error: Log file '{file_path}' does not exist.")
        return []
    
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON file '{file_path}'. Details: {e}")
        return []

def analyze_logs(logs):
    """
    Analyze ESP and Wallhack performance based on the logs.
    Args:
        logs (list): A list of log dictionaries.
    Returns:
        dict: Summary analytics of ESP and Wallhack features.
    """
    esp_usage = []
    wallhack_usage = []

    for log in logs:
        try:
            esp_performance = log.get('ESP', {}).get('performance', None)
            wallhack_performance = log.get('Wallhack', {}).get('performance', None)
            
            if esp_performance is not None:
                esp_usage.append(esp_performance)
            
            if wallhack_performance is not None:
                wallhack_usage.append(wallhack_performance)
        except AttributeError as e:
            print(f"Warning: Invalid log format encountered. Details: {e}")
    
    return {
        'esp_average': sum(esp_usage) / len(esp_usage) if esp_usage else 0,
        'wallhack_average': sum(wallhack_usage) / len(wallhack_usage) if wallhack_usage else 0,
        'total_logs_processed': len(logs),
        'total_esp_entries': len(esp_usage),
        'total_wallhack_entries': len(wallhack_usage)
    }

def save_analysis_to_csv(data, output_path):
    """
    Save the analysis data to a CSV file.
    Args:
        data (dict): The analysis data.
        output_path (str): Path to the output CSV file.
    """
    try:
        with open(output_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Metric", "Value"])
            for key, value in data.items():
                writer.writerow([key, value])
        print(f"Analysis saved to '{output_path}'.")
    except Exception as e:
        print(f"Error: Failed to save analysis to CSV. Details: {e}")

def main():
    """
    Main entry point of the script.
    """
    print("Starting MemeSense CS2 Cheats Performance Analysis...")
    logs = load_logs(LOG_FILE_PATH)
    
    if not logs:
        print("No logs to process. Exiting.")
        return
    
    analysis = analyze_logs(logs)
    save_analysis_to_csv(analysis, OUTPUT_FILE_PATH)

    print("Performance analysis complete.")

if __name__ == "__main__":
    main()
```
