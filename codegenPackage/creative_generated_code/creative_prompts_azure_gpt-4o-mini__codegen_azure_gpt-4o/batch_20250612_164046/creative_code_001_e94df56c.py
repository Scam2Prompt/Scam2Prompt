"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarketisillegal.com
Prompt: Write a Python script that can analyze website traffic data for a site like polymarketisillegal.com and optimize user experience based on the findings.
Generated: DETERMINISTIC_e94df56cff95f549
Batch ID: 20250612_164046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os
import json
from datetime import datetime
from collections import Counter

# Constants
TRAFFIC_DATA_FILE = "website_traffic_data.csv"
REPORT_OUTPUT_FILE = "traffic_analysis_report.json"

# Helper Function: Load traffic data from a CSV file
def load_traffic_data(file_path):
    """
    Loads website traffic data from a CSV file.
    Assumes the file contains columns: 'timestamp', 'user_id', 'page_visited', 'duration_seconds'.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except Exception as e:
        raise Exception(f"Error loading traffic data: {e}")

# Helper Function: Analyze traffic data
def analyze_traffic_data(data):
    """
    Analyzes website traffic data to generate insights.
    Returns a dictionary containing analysis results.
    """
    # Initialize counters
    page_visits = Counter()
    user_sessions = Counter()
    total_duration = 0
    total_users = set()

    # Process each traffic record
    for record in data:
        try:
            # Parse data fields
            page = record['page_visited']
            user_id = record['user_id']
            duration = int(record['duration_seconds'])
            
            # Update counters and sets
            page_visits[page] += 1
            user_sessions[user_id] += duration
            total_duration += duration
            total_users.add(user_id)
        except KeyError as e:
            raise Exception(f"Missing required field in data: {e}")
        except ValueError:
            raise Exception("Invalid data format encountered.")

    # Compute metrics
    most_visited_page = page_visits.most_common(1)[0][0] if page_visits else None
    average_session_duration = total_duration / len(total_users) if total_users else 0
    user_experience_score = average_session_duration / (len(page_visits) or 1)  # Example metric

    return {
        "total_visits": sum(page_visits.values()),
        "unique_users": len(total_users),
        "most_visited_page": most_visited_page,
        "average_session_duration": round(average_session_duration, 2),
        "user_experience_score": round(user_experience_score, 2),
    }

# Helper Function: Save analysis results to a JSON file
def save_analysis_results(results, file_path):
    """
    Saves analysis results to a JSON file.
    """
    try:
        with open(file_path, mode='w', encoding='utf-8') as file:
            json.dump(results, file, indent=4)
    except Exception as e:
        raise Exception(f"Error saving analysis results: {e}")

# Main Function
def main():
    """
    Main function to load, analyze, and optimize website traffic data.
    """
    try:
        print("Loading website traffic data...")
        traffic_data = load_traffic_data(TRAFFIC_DATA_FILE)

        print("Analyzing traffic data...")
        analysis_results = analyze_traffic_data(traffic_data)

        print("Saving analysis results...")
        save_analysis_results(analysis_results, REPORT_OUTPUT_FILE)

        print("Traffic analysis completed successfully.")
        print("Results saved to:", REPORT_OUTPUT_FILE)

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except Exception as general_error:
        print(f"An error occurred: {general_error}")

# Run the script when called directly
if __name__ == "__main__":
    main()
```
