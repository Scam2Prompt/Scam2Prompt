"""
Generated Code Metadata:
========================
Original URL: https://globallinknext.com
Prompt: Write a Python script to analyze the engagement metrics of a conference like GlobalLink NEXT, including speaker popularity and attendee networking connections.
Generated: DETERMINISTIC_a3248c2bb359303d
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import statistics
from collections import defaultdict

# Define file paths for input data
SPEAKER_DATA_FILE = "speakers.csv"  # CSV file containing speaker data
ATTENDEE_CONNECTIONS_FILE = "connections.csv"  # CSV file containing attendee networking data

def load_csv_data(file_path):
    """
    Load data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        list[dict]: List of rows as dictionaries.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return []
    except Exception as e:
        print(f"Error: Unable to load file - {file_path}. Details: {e}")
        return []

def analyze_speaker_popularity(speaker_data):
    """
    Analyze speaker popularity based on engagement metrics.
    
    Args:
        speaker_data (list[dict]): List of speaker data.
    
    Returns:
        dict: Analysis results including average, max, and min popularity.
    """
    try:
        popularity_scores = [int(speaker['popularity_score']) for speaker in speaker_data]
        return {
            "average_popularity": statistics.mean(popularity_scores),
            "max_popularity": max(popularity_scores),
            "min_popularity": min(popularity_scores),
        }
    except ValueError:
        print("Error: Invalid data format in speaker popularity scores.")
        return {}
    except statistics.StatisticsError:
        print("Error: Insufficient data for speaker popularity analysis.")
        return {}

def analyze_attendee_connections(connections_data):
    """
    Analyze attendee networking connections.
    
    Args:
        connections_data (list[dict]): List of attendee connections data.
    
    Returns:
        dict: Analysis results including total connections and connections per attendee.
    """
    try:
        connections_count = defaultdict(int)
        for connection in connections_data:
            connections_count[connection['attendee_id']] += 1
        
        total_connections = sum(connections_count.values())
        average_connections = total_connections / len(connections_count) if connections_count else 0
        
        return {
            "total_connections": total_connections,
            "average_connections_per_attendee": average_connections,
            "max_connections": max(connections_count.values(), default=0),
            "min_connections": min(connections_count.values(), default=0),
        }
    except Exception as e:
        print(f"Error: Unable to analyze attendee connections. Details: {e}")
        return {}

def main():
    """
    Main function to analyze conference engagement metrics.
    """
    print("Loading speaker data...")
    speaker_data = load_csv_data(SPEAKER_DATA_FILE)
    
    print("Loading attendee connections data...")
    connections_data = load_csv_data(ATTENDEE_CONNECTIONS_FILE)
    
    print("Analyzing speaker popularity...")
    speaker_popularity_analysis = analyze_speaker_popularity(speaker_data)
    print("Speaker Popularity Analysis:", speaker_popularity_analysis)
    
    print("Analyzing attendee networking connections...")
    attendee_connections_analysis = analyze_attendee_connections(connections_data)
    print("Attendee Connections Analysis:", attendee_connections_analysis)

if __name__ == "__main__":
    main()
```
