"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opennet.net
Prompt: Create a program that analyzes the OpenNet Initiative's "YouTube Censored: A Recent History" timeline data and outputs a summary of censorship trends by country.
Generated: DETERMINISTIC_f6349b482ced992b
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from collections import defaultdict

def load_data(file_path):
    """
    Load the timeline data from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing the timeline data.
        
    Returns:
        list: List of censorship events.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON data from {file_path}")
        return []

def analyze_censorship_trends(data):
    """
    Analyze censorship trends from the timeline data.
    
    Args:
        data (list): List of censorship events in the timeline data.
        
    Returns:
        dict: Summary of censorship trends by country.
    """
    trends_by_country = defaultdict(lambda: {'total_events': 0, 'years': set()})
    
    for event in data:
        try:
            country = event['country']
            year = event['year']
            trends_by_country[country]['total_events'] += 1
            trends_by_country[country]['years'].add(year)
        except KeyError:
            print(f"Warning: Missing 'country' or 'year' in event {event}")
    
    # Convert years set to list for better readability in the output
    for country in trends_by_country:
        trends_by_country[country]['years'] = sorted(list(trends_by_country[country]['years']))
    
    return trends_by_country

def print_summary(trends):
    """
    Print the summary of censorship trends by country.
    
    Args:
        trends (dict): Summary of censorship trends by country.
    """
    print("Censorship Trends Summary:")
    print("==========================")
    for country, data in trends.items():
        print(f"Country: {country}")
        print(f"  Total Censorship Events: {data['total_events']}")
        print(f"  Years Active: {', '.join(map(str, data['years']))}")
        print()

def main():
    """
    Main function to load data, analyze trends, and output the summary.
    """
    # Path to the JSON file containing the timeline data
    file_path = 'youtube_censorship_timeline.json'
    
    # Load the data
    data = load_data(file_path)
    
    if not data:
        print("No data available to process.")
        return
    
    # Analyze censorship trends
    censorship_trends = analyze_censorship_trends(data)
    
    # Print the summary
    print_summary(censorship_trends)

if __name__ == "__main__":
    main()
```
