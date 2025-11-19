"""
Generated Code Metadata:
========================
Original URL: https://mommyanew.com
Prompt: Develop a Python script to analyze screen time data exported from iOS devices, providing insights for single moms as described in the "6 Simple Steps to Manage Your Child’s Screen Time" article on Mommy Anew.
Generated: DETERMINISTIC_e1141c562c8e49eb
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# screen_time_analyzer.py

import json
import csv
from datetime import datetime
from typing import Dict, List

def load_screen_time_data(file_path: str) -> List[Dict]:
    """
    Load screen time data from a JSON file.

    Args:
    file_path (str): Path to the JSON file containing screen time data.

    Returns:
    List[Dict]: A list of dictionaries containing screen time data.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON - {e}")
        return []

def calculate_total_screen_time(data: List[Dict]) -> int:
    """
    Calculate the total screen time in minutes.

    Args:
    data (List[Dict]): A list of dictionaries containing screen time data.

    Returns:
    int: The total screen time in minutes.
    """
    total_screen_time = 0
    for entry in data:
        try:
            start_time = datetime.strptime(entry['start_time'], '%Y-%m-%d %H:%M:%S')
            end_time = datetime.strptime(entry['end_time'], '%Y-%m-%d %H:%M:%S')
            screen_time = (end_time - start_time).total_seconds() / 60
            total_screen_time += screen_time
        except KeyError as e:
            print(f"Error: Missing key - {e}")
        except ValueError as e:
            print(f"Error: Invalid date format - {e}")
    return int(total_screen_time)

def calculate_average_screen_time(data: List[Dict]) -> float:
    """
    Calculate the average screen time in minutes.

    Args:
    data (List[Dict]): A list of dictionaries containing screen time data.

    Returns:
    float: The average screen time in minutes.
    """
    total_screen_time = calculate_total_screen_time(data)
    return total_screen_time / len(data) if data else 0

def get_most_used_apps(data: List[Dict]) -> Dict:
    """
    Get the most used apps.

    Args:
    data (List[Dict]): A list of dictionaries containing screen time data.

    Returns:
    Dict: A dictionary containing the most used apps and their screen time.
    """
    app_usage = {}
    for entry in data:
        try:
            app_name = entry['app_name']
            start_time = datetime.strptime(entry['start_time'], '%Y-%m-%d %H:%M:%S')
            end_time = datetime.strptime(entry['end_time'], '%Y-%m-%d %H:%M:%S')
            screen_time = (end_time - start_time).total_seconds() / 60
            if app_name in app_usage:
                app_usage[app_name] += screen_time
            else:
                app_usage[app_name] = screen_time
        except KeyError as e:
            print(f"Error: Missing key - {e}")
    return dict(sorted(app_usage.items(), key=lambda item: item[1], reverse=True))

def export_to_csv(data: List[Dict], file_path: str) -> None:
    """
    Export screen time data to a CSV file.

    Args:
    data (List[Dict]): A list of dictionaries containing screen time data.
    file_path (str): Path to the CSV file.
    """
    try:
        with open(file_path, 'w', newline='') as file:
            fieldnames = ['date', 'app_name', 'start_time', 'end_time', 'screen_time']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for entry in data:
                writer.writerow({
                    'date': entry.get('date', ''),
                    'app_name': entry.get('app_name', ''),
                    'start_time': entry.get('start_time', ''),
                    'end_time': entry.get('end_time', ''),
                    'screen_time': (datetime.strptime(entry['end_time'], '%Y-%m-%d %H:%M:%S') - datetime.strptime(entry['start_time'], '%Y-%m-%d %H:%M:%S')).total_seconds() / 60
                })
    except Exception as e:
        print(f"Error: Failed to export to CSV - {e}")

def main():
    file_path = 'screen_time_data.json'
    data = load_screen_time_data(file_path)
    
    if data:
        total_screen_time = calculate_total_screen_time(data)
        average_screen_time = calculate_average_screen_time(data)
        most_used_apps = get_most_used_apps(data)

        print(f"Total Screen Time: {total_screen_time} minutes")
        print(f"Average Screen Time: {average_screen_time} minutes")
        print("Most Used Apps:")
        for app, screen_time in most_used_apps.items():
            print(f"{app}: {screen_time} minutes")

        export_to_csv(data, 'screen_time_data.csv')

if __name__ == "__main__":
    main()
```
