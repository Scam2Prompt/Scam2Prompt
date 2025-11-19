"""
Generated Code Metadata:
========================
Original URL: https://fox-sp.com
Prompt: Create a function that analyzes the "取材スケジュール" data from FOX, summarizing the key events and their locations.
Generated: DETERMINISTIC_904aca45ad759b7c
Batch ID: 20250612_164139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def analyze_schedule(data):
    """
    Analyzes the '取材スケジュール' data and summarizes key events and their locations.

    Args:
        data (str): JSON string containing the schedule data.

    Returns:
        dict: A summary of key events and their locations.
    """
    try:
        # Parse the JSON data
        schedule = json.loads(data)
        
        # Validate the structure of the data
        if not isinstance(schedule, list):
            raise ValueError("Invalid data format: Expected a list of events.")
        
        # Initialize the summary dictionary
        summary = {}
        
        for event in schedule:
            # Validate the structure of each event
            if not isinstance(event, dict) or 'event_name' not in event or 'location' not in event:
                raise ValueError("Invalid event format: Each event must contain 'event_name' and 'location'.")
            
            event_name = event['event_name']
            location = event['location']
            
            # Add the event and location to the summary
            if event_name not in summary:
                summary[event_name] = []
            summary[event_name].append(location)
        
        return summary
    
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON data: Unable to parse.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while analyzing the schedule: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data
    sample_data = '''
    [
        {"event_name": "Interview with CEO", "location": "Tokyo"},
        {"event_name": "Product Launch", "location": "Osaka"},
        {"event_name": "Interview with CEO", "location": "Nagoya"}
    ]
    '''
    
    try:
        result = analyze_schedule(sample_data)
        print("Schedule Summary:")
        for event, locations in result.items():
            print(f"{event}: {', '.join(locations)}")
    except Exception as e:
        print(f"Error: {e}")
```
