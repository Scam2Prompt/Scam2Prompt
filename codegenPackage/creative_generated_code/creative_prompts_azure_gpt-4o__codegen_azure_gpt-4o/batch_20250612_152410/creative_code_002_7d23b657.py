"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playemberssssssssssssss.pages.dev
Prompt: Generate a script to analyze mobile game downloads and user activity, inspired by Playember's reported 120M downloads and 5M monthly active users.
Generated: DETERMINISTIC_7d23b657fe1b2951
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json
from datetime import datetime
from collections import defaultdict

# Constants for file paths
DOWNLOADS_DATA_FILE = "downloads_data.csv"
USER_ACTIVITY_FILE = "user_activity.json"
REPORT_OUTPUT_FILE = "game_analysis_report.txt"

def load_downloads_data(file_path):
    """
    Function to load downloads data from a CSV file.
    Returns a dictionary with game names and corresponding download counts.
    """
    downloads = defaultdict(int)  # Use defaultdict for easier aggregation
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                game_name = row['game_name']
                downloads_count = int(row['downloads_count'])
                downloads[game_name] += downloads_count
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except KeyError:
        print("Error: CSV file format is incorrect. Ensure 'game_name' and 'downloads_count' columns exist.")
    except ValueError:
        print("Error: Ensure downloads_count is a valid integer.")
    return downloads

def load_user_activity_data(file_path):
    """
    Function to load user activity data from a JSON file.
    Returns a dictionary with game names and corresponding active users.
    """
    user_activity = defaultdict(int)
    try:
        with open(file_path, mode='r') as file:
            data = json.load(file)
            for entry in data:
                game_name = entry['game_name']
                active_users = int(entry['active_users'])
                user_activity[game_name] += active_users
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except KeyError:
        print("Error: JSON file format is incorrect. Ensure 'game_name' and 'active_users' keys exist.")
    except ValueError:
        print("Error: Ensure active_users is a valid integer.")
    return user_activity

def generate_report(downloads, user_activity, output_file):
    """
    Function to generate a report based on downloads and user activity data.
    Writes the report to the specified output file.
    """
    try:
        with open(output_file, mode='w') as file:
            file.write(f"Game Analysis Report ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})\n")
            file.write("=" * 50 + "\n")
            file.write(f"{'Game Name':<30}{'Downloads':<10}{'Active Users':<10}\n")
            file.write("=" * 50 + "\n")
            
            # Combine data from both datasets
            all_games = set(downloads.keys()).union(set(user_activity.keys()))
            for game in all_games:
                download_count = downloads.get(game, 0)
                active_users = user_activity.get(game, 0)
                file.write(f"{game:<30}{download_count:<10}{active_users:<10}\n")
            
            file.write("=" * 50 + "\n")
            file.write("Report generated successfully.\n")
    except Exception as e:
        print(f"Error while writing report: {e}")

def main():
    """
    Main function to orchestrate data loading, analysis, and report generation.
    """
    print("Starting game analysis...")
    
    # Load downloads data
    downloads_data = load_downloads_data(DOWNLOADS_DATA_FILE)
    print("Downloads data loaded successfully.")
    
    # Load user activity data
    user_activity_data = load_user_activity_data(USER_ACTIVITY_FILE)
    print("User activity data loaded successfully.")
    
    # Generate report
    generate_report(downloads_data, user_activity_data, REPORT_OUTPUT_FILE)
    print("Report generated successfully.")

if __name__ == "__main__":
    main()
```
