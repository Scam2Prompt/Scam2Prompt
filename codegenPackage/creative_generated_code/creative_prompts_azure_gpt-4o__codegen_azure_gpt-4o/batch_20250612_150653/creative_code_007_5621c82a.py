"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sautikenya.com
Prompt: Develop a Python function to track the progress of women-led civic society actors in advocacy campaigns, using data from Sauti Kenya's peace and governance initiatives.
Generated: DETERMINISTIC_5621c82a580f98bf
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

def track_progress(data: List[Dict[str, str]]) -> Dict[str, Dict[str, float]]:
    """
    Tracks the progress of women-led civic society actors in advocacy campaigns.
    
    Parameters:
        data (List[Dict[str, str]]): A list of dictionaries containing campaign data. 
                                     Each dictionary should include 'actor', 'campaign', 
                                     and 'progress' (percentage completed as a string).
    
    Returns:
        Dict[str, Dict[str, float]]: A dictionary where keys are actor names and values are dictionaries 
                                     with campaign names and their respective progress percentages.
    
    Raises:
        ValueError: If progress data is not in a valid percentage format.
    """
    # Initialize a dictionary to store the progress data
    progress_tracker = {}
    
    for entry in data:
        try:
            # Validate the input data format
            actor = entry.get('actor')
            campaign = entry.get('campaign')
            progress = entry.get('progress')
            
            if not (actor and campaign and progress):
                raise ValueError("Missing necessary fields in input data.")
            
            # Convert progress percentage from string to float
            progress_percentage = float(progress.strip('%'))
            
            # Ensure progress is in the valid range of 0 to 100
            if not (0 <= progress_percentage <= 100):
                raise ValueError("Progress percentage must be between 0 and 100.")
            
            # Store the progress data in the tracker
            if actor not in progress_tracker:
                progress_tracker[actor] = {}
            
            progress_tracker[actor][campaign] = progress_percentage
        
        except ValueError as e:
            print(f"Error processing entry {entry}: {e}")
    
    return progress_tracker

# Example usage:
if __name__ == "__main__":
    # Sample data from Sauti Kenya's peace and governance initiatives
    sample_data = [
        {"actor": "Alice", "campaign": "Campaign A", "progress": "75%"},
        {"actor": "Alice", "campaign": "Campaign B", "progress": "50%"},
        {"actor": "Mary", "campaign": "Campaign C", "progress": "90%"},
        {"actor": "Mary", "campaign": "Campaign D", "progress": "100%"},
        {"actor": "Jane", "campaign": "Campaign E", "progress": "40%"},
    ]
    
    # Track progress and print the result
    progress = track_progress(sample_data)
    print(json.dumps(progress, indent=4))
```
