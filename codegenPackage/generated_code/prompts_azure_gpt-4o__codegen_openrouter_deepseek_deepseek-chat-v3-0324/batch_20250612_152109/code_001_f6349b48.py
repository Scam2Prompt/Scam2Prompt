"""
Generated Code Metadata:
========================
Original URL: https://opennet.net
Prompt: Create a program that analyzes the OpenNet Initiative's "YouTube Censored: A Recent History" timeline data and outputs a summary of censorship trends by country.
Generated: DETERMINISTIC_f6349b482ced992b
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import csv
from collections import defaultdict
from datetime import datetime
import argparse

def load_data(file_path):
    """
    Load JSON data from the given file path.
    
    Args:
        file_path (str): Path to the JSON file.
        
    Returns:
        dict: Parsed JSON data.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        raise
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}")
        raise
    except Exception as e:
        print(f"Unexpected error loading data: {e}")
        raise

def parse_dates(events):
    """
    Parse date strings into datetime objects and validate them.
    
    Args:
        events (list): List of event dictionaries.
        
    Returns:
        list: List of events with parsed dates.
    """
    parsed_events = []
    for event in events:
        try:
            date_str = event.get('date')
            if not date_str:
                continue
            event['parsed_date'] = datetime.strptime(date_str, '%Y-%m-%d')
            parsed_events.append(event)
        except ValueError:
            print(f"Warning: Invalid date format in event: {event}")
    return parsed_events

def analyze_censorship(events):
    """
    Analyze censorship events and generate trends by country.
    
    Args:
        events (list): List of event dictionaries with parsed dates.
        
    Returns:
        dict: Analysis results with counts and trends by country.
    """
    country_stats = defaultdict(lambda: {
        'total_events': 0,
        'first_event': None,
        'last_event': None,
        'event_types': defaultdict(int)
    })
    
    for event in events:
        country = event.get('country', 'Unknown')
        stats = country_stats[country]
        
        # Update counts
        stats['total_events'] += 1
        event_type = event.get('type', 'Unknown')
        stats['event_types'][event_type] += 1
        
        # Update date ranges
        event_date = event['parsed_date']
        if stats['first_event'] is None or event_date < stats['first_event']:
            stats['first_event'] = event_date
        if stats['last_event'] is None or event_date > stats['last_event']:
            stats['last_event'] = event_date
    
    return country_stats

def generate_report(country_stats, output_format='csv'):
    """
    Generate a report from the analysis results.
    
    Args:
        country_stats (dict): Analysis results from analyze_censorship.
        output_format (str): Format of the output ('csv' or 'console').
    """
    if output_format == 'csv':
        with open('youtube_censorship_report.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'Country',
                'Total Events',
                'First Event Date',
                'Last Event Date',
                'Event Types'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for country, stats in sorted(country_stats.items()):
                writer.writerow({
                    'Country': country,
                    'Total Events': stats['total_events'],
                    'First Event Date': stats['first_event'].strftime('%Y-%m-%d') if stats['first_event'] else 'N/A',
                    'Last Event Date': stats['last_event'].strftime('%Y-%m-%d') if stats['last_event'] else 'N/A',
                    'Event Types': ', '.join([f"{k}:{v}" for k, v in stats['event_types'].items()])
                })
        print("Report generated as 'youtube_censorship_report.csv'")
    else:
        print("\nYouTube Censorship Trends by Country:")
        print("-" * 50)
        for country, stats in sorted(country_stats.items()):
            print(f"\nCountry: {country}")
            print(f"Total Events: {stats['total_events']}")
            print(f"First Event: {stats['first_event'].strftime('%Y-%m-%d') if stats['first_event'] else 'N/A'}")
            print(f"Last Event: {stats['last_event'].strftime('%Y-%m-%d') if stats['last_event'] else 'N/A'}")
            print("Event Types:")
            for event_type, count in stats['event_types'].items():
                print(f"  - {event_type}: {count}")

def main():
    parser = argparse.ArgumentParser(description='Analyze YouTube censorship trends by country.')
    parser.add_argument('input_file', help='Path to the JSON data file')
    parser.add_argument('--format', choices=['csv', 'console'], default='console',
                       help='Output format (csv or console)')
    
    args = parser.parse_args()
    
    try:
        # Load and process data
        data = load_data(args.input_file)
        events = parse_dates(data.get('events', []))
        
        # Analyze and generate report
        country_stats = analyze_censorship(events)
        generate_report(country_stats, args.format)
        
    except Exception as e:
        print(f"Program failed: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    main()
```
