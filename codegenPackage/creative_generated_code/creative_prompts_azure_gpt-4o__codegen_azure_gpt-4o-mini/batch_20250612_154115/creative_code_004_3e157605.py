"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oasysgames.live
Prompt: Create a function to calculate the remaining time for campaigns listed on the VersePort platform, using local time or UTC as specified.
Generated: DETERMINISTIC_3e1576056fc759fa
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timezone, timedelta
from typing import List, Dict, Union

def calculate_remaining_time(campaigns: List[Dict[str, Union[str, int]]], use_utc: bool = True) -> List[Dict[str, Union[str, int]]]:
    """
    Calculate the remaining time for each campaign.

    Args:
        campaigns (List[Dict[str, Union[str, int]]]): A list of campaigns with their end time.
            Each campaign is a dictionary containing 'name' (str) and 'end_time' (str) in ISO format.
        use_utc (bool): If True, the end times are treated as UTC. If False, they are treated as local time.
        
    Returns:
        List[Dict[str, Union[str, int]]]: A list of campaigns with their remaining time in seconds.
            Each entry includes 'name' and 'remaining_time' (int).
    
    Raises:
        ValueError: If a campaign's end_time is not a valid ISO formatted string.
    """
    remaining_times = []
    
    for campaign in campaigns:
        try:
            # Parse the end_time from ISO format
            end_time = datetime.fromisoformat(campaign['end_time'])
            
            # Convert to UTC if specified
            if use_utc:
                if end_time.tzinfo is None:
                    end_time = end_time.replace(tzinfo=timezone.utc)
            else:
                if end_time.tzinfo is None:
                    # Assume local time if no timezone info is provided
                    end_time = end_time.astimezone()

            # Get the current time in the specified timezone
            current_time = datetime.now(timezone.utc) if use_utc else datetime.now()

            # Calculate remaining time in seconds
            remaining_time = (end_time - current_time).total_seconds()

            # Append result to the list
            remaining_times.append({
                'name': campaign['name'],
                'remaining_time': max(0, int(remaining_time))  # Ensure non-negative time
            })
        
        except ValueError as e:
            # Handle invalid date format
            raise ValueError(f"Invalid end_time for campaign {campaign['name']}: {e}")

    return remaining_times

# Example usage
if __name__ == "__main__":
    campaigns_data = [
        {'name': 'Campaign 1', 'end_time': '2023-12-31T23:59:59'},
        {'name': 'Campaign 2', 'end_time': '2023-11-30T12:00:00+00:00'},
        {'name': 'Campaign 3', 'end_time': 'invalid-date'}  # This will trigger an error
    ]
    
    try:
        results = calculate_remaining_time(campaigns_data, use_utc=True)
        for result in results:
            print(f"{result['name']} - Remaining Time: {result['remaining_time']} seconds")
    except ValueError as e:
        print(e)
```
