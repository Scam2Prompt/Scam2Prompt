"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autobux.top
Prompt: Write a program to calculate the weekly contest results based on user activity data provided by the AUTOBUX platform.
Generated: DETERMINISTIC_d49124ad5e5b4eb9
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from datetime import datetime

def parse_user_activity_data(file_path):
    """
    Parses user activity data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing user activity data.

    Returns:
        list of dict: A list of dictionaries, each representing a user's activity.
    """
    activity_data = []
    try:
        with open(file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                activity_data.append({
                    "user_id": row["user_id"],
                    "activity_points": int(row["activity_points"]),
                    "activity_date": datetime.strptime(row["activity_date"], "%Y-%m-%d")
                })
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError as ve:
        print(f"Error: Invalid data format detected. {ve}")
    except Exception as e:
        print(f"Unexpected error occurred while parsing data: {e}")
    return activity_data

def calculate_weekly_results(activity_data):
    """
    Calculates weekly contest results based on user activity data.

    Args:
        activity_data (list of dict): List of user activity data dictionaries.

    Returns:
        dict: A dictionary containing user_id as keys and total weekly points as values.
    """
    weekly_results = {}
    try:
        for entry in activity_data:
            user_id = entry["user_id"]
            points = entry["activity_points"]
            # Aggregate points for each user
            weekly_results[user_id] = weekly_results.get(user_id, 0) + points
    except KeyError as ke:
        print(f"Error: Missing key in data. {ke}")
    except Exception as e:
        print(f"Unexpected error occurred during calculation: {e}")
    return weekly_results

def display_results(weekly_results):
    """
    Displays the weekly contest results in a sorted manner.

    Args:
        weekly_results (dict): The weekly results dictionary with user_id and points.

    Returns:
        None
    """
    print("\nWeekly Contest Results:")
    print("-----------------------")
    try:
        # Sort results by points in descending order
        sorted_results = sorted(weekly_results.items(), key=lambda x: x[1], reverse=True)
        for rank, (user_id, points) in enumerate(sorted_results, start=1):
            print(f"Rank {rank}: User ID {user_id} - {points} points")
    except Exception as e:
        print(f"Unexpected error occurred while displaying results: {e}")

# Entry point for the program
if __name__ == "__main__":
    input_file = "user_activity_data.csv"  # Replace with actual path to the data file
    
    # Step 1: Parse the user activity data
    data = parse_user_activity_data(input_file)
    
    if data:  # Ensure data is not empty
        # Step 2: Calculate weekly contest results
        results = calculate_weekly_results(data)
        
        # Step 3: Display the results
        display_results(results)
    else:
        print("No activity data available. Cannot calculate contest results.")
```
