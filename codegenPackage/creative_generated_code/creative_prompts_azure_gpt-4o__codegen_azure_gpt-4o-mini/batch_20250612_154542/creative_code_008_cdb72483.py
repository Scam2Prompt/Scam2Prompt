"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egatur.edu.pe
Prompt: Create a Python script to generate a report summarizing participation in Egatur events, such as "Feliz Día del Frappe" and "Marcha por la Salud Mental."
Generated: DETERMINISTIC_cdb7248316e44138
Batch ID: 20250612_154542
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
from typing import List, Dict

# Define a function to read event participation data from a CSV file
def read_event_data(file_path: str) -> List[Dict[str, str]]:
    """
    Reads event participation data from a CSV file.

    :param file_path: Location of the CSV file
    :return: A list of dictionaries containing event data
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

# Define a function to summarize participation for events
def summarize_participation(data: List[Dict[str, str]]) -> Dict[str, Dict[str, int]]:
    """
    Summarizes participation in events.

    :param data: List of event data dictionaries
    :return: A dictionary summarizing the participation for each event
    """
    summary = defaultdict(lambda: {'participants': 0, 'dates': set()})

    for entry in data:
        event_name = entry.get('Event Name', '').strip()
        participant_count = int(entry.get('Participants', 0))
        event_date = entry.get('Event Date', '').strip()

        if event_name:
            summary[event_name]['participants'] += participant_count
            summary[event_name]['dates'].add(event_date)

    # Convert dates from set to sorted list for better readability
    for event in summary:
        summary[event]['dates'] = sorted(summary[event]['dates'])
    
    return summary

# Define a function to generate a report
def generate_report(summary: Dict[str, Dict[str, int]], output_path: str) -> None:
    """
    Generates a JSON report summarizing event participation.

    :param summary: Dictionary containing participation summary
    :param output_path: Output file path for the JSON report
    """
    try:
        with open(output_path, mode='w', encoding='utf-8') as file:
            json.dump(summary, file, ensure_ascii=False, indent=4)
        print(f"Report generated successfully: {output_path}")
    except Exception as e:
        print(f"An error occurred while generating the report: {e}")

def main():
    # Define the input CSV file path
    input_file_path = 'event_participation.csv'  # Change as needed
    output_file_path = 'event_participation_report.json'  # Output file for the report

    # Read event data from the CSV file
    event_data = read_event_data(input_file_path)

    # Summarize the participation data
    participation_summary = summarize_participation(event_data)

    # Generate the report in JSON format
    generate_report(participation_summary, output_file_path)

if __name__ == "__main__":
    main()
```
