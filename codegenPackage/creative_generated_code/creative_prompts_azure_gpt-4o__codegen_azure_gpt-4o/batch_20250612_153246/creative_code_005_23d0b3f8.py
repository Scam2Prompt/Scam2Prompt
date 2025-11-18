"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mctsummit.org
Prompt: Develop a script to analyze attendee data for networking events at the MCT Summit, including metrics like registered candidates and global speakers.
Generated: DETERMINISTIC_23d0b3f874f12323
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from collections import defaultdict

def load_attendee_data(file_path):
    """
    Load attendee data from a CSV file. 
    
    Args:
        file_path (str): Path to the CSV file containing attendee data.

    Returns:
        list[dict]: List of dictionaries containing attendee details.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        print(f"Error: File at '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error loading attendee data: {e}")
        return []

def analyze_attendee_data(attendee_data):
    """
    Analyze attendee data and calculate metrics.
    
    Args:
        attendee_data (list[dict]): List of dictionaries containing attendee details.
    
    Returns:
        dict: Dictionary containing metrics like total registered candidates and global speakers.
    """
    metrics = {
        "total_registered_candidates": 0,
        "global_speakers_count": 0,
    }
    
    # Using defaultdict to group attendees by country (for additional analysis if needed in the future)
    attendees_by_country = defaultdict(list)
    
    for attendee in attendee_data:
        try:
            # Increment registered candidates
            metrics["total_registered_candidates"] += 1
            
            # Check if the attendee is a global speaker
            if attendee.get("Role") == "Global Speaker":
                metrics["global_speakers_count"] += 1
            
            # Group attendees by country
            country = attendee.get("Country", "Unknown")
            attendees_by_country[country].append(attendee)
            
        except KeyError as e:
            print(f"Missing expected data field: {e}")
    
    return metrics

def display_metrics(metrics):
    """
    Display metrics in a user-friendly way.
    
    Args:
        metrics (dict): Dictionary containing metrics data.
    """
    print("Networking Event Metrics:")
    print(f"Total Registered Candidates: {metrics['total_registered_candidates']}")
    print(f"Global Speakers Count: {metrics['global_speakers_count']}")

def main():
    """
    Main function to execute the script.
    """
    # Path to the CSV file containing attendee data
    file_path = "attendee_data.csv"
    
    # Load the attendee data
    attendee_data = load_attendee_data(file_path)
    
    # If data is successfully loaded, analyze and display metrics
    if attendee_data:
        metrics = analyze_attendee_data(attendee_data)
        display_metrics(metrics)
    else:
        print("No data available to process.")

if __name__ == "__main__":
    main()
```
