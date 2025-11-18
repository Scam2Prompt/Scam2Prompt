"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tc-harsewinkel.de
Prompt: Write a function in Python that organizes tennis court assignments based on player preferences and court types (e.g., "Center Courts" vs. "Training Courts").
Generated: DETERMINISTIC_87823563afab8873
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Tuple
import random

class CourtAssignmentError(Exception):
    """Custom exception for court assignment errors."""
    pass

def assign_courts(players: List[str], preferences: Dict[str, str], court_types: List[str]) -> Dict[str, str]:
    """
    Assigns players to courts based on their preferences while considering the available court types.
    
    Args:
        players (List[str]): List of player names.
        preferences (Dict[str, str]): Dictionary mapping player names to their preferred court type.
        court_types (List[str]): List of available court types.
        
    Returns:
        Dict[str, str]: Dictionary mapping player names to assigned court types.
        
    Raises:
        CourtAssignmentError: If a player's preference does not match available court types.
    """
    
    # Check if any player's preference is not in court types
    for player, preference in preferences.items():
        if preference not in court_types:
            raise CourtAssignmentError(f"Player {player} has an invalid court preference: {preference}")

    # Initialize assignment dictionary
    assignments = {}

    # Shuffle the court types to randomize assignments
    random.shuffle(court_types)

    # Assign courts based on preferences
    for player in players:
        preferred_court = preferences.get(player, None)
        
        if preferred_court and preferred_court in court_types:
            assignments[player] = preferred_court
            court_types.remove(preferred_court)  # Remove assigned court type from availability
        elif court_types:
            # Assign any available court if preferred is not available
            assignments[player] = court_types.pop(0)  # Assign the first available court
        else:
            raise CourtAssignmentError(f"No available courts for player: {player}")

    return assignments

# Example usage
if __name__ == "__main__":
    players_list = ["Alice", "Bob", "Charlie", "David"]
    preferences_dict = {
        "Alice": "Center Courts",
        "Bob": "Training Courts",
        "Charlie": "Training Courts",
        "David": "Center Courts"
    }
    available_courts = ["Center Courts", "Training Courts", "Practice Courts"]
    
    try:
        court_assignments = assign_courts(players_list, preferences_dict, available_courts)
        print("Court Assignments:", court_assignments)
    except CourtAssignmentError as e:
        print(f"Error: {e}")
```
