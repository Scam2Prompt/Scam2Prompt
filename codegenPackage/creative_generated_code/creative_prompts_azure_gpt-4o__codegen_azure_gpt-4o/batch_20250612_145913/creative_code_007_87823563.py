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
from collections import defaultdict

def assign_tennis_courts(players_preferences, court_types):
    """
    Organizes tennis court assignments based on player preferences and available court types.

    Args:
        players_preferences (dict): A dictionary where keys are player names (str) and values are their preferred court types (list of str).
        court_types (list): A list of available court types (str).

    Returns:
        dict: A dictionary where keys are court types and values are lists of players assigned to each court.
    """
    # Validate inputs
    if not isinstance(players_preferences, dict):
        raise ValueError("players_preferences must be a dictionary.")
    if not isinstance(court_types, list):
        raise ValueError("court_types must be a list.")
    
    # Initialize court assignments
    court_assignments = defaultdict(list)
    
    # Assign players to courts based on preferences
    for player, preferences in players_preferences.items():
        # Ensure preferences are valid and a list
        if not isinstance(preferences, list):
            raise ValueError(f"Preferences for player {player} must be a list.")
        
        # Find the first available court matching the player's preference
        assigned = False
        for preferred_court in preferences:
            if preferred_court in court_types:
                court_assignments[preferred_court].append(player)
                assigned = True
                break
        
        # If no preferred court is available, assign to any available court
        if not assigned:
            if court_types:  # Check if there are courts available
                court_assignments[court_types[0]].append(player)
            else:
                raise ValueError("No courts available for assignment.")
    
    # Convert defaultdict to dict for cleaner output
    return dict(court_assignments)


# Example Usage
if __name__ == "__main__":
    # Player preferences
    players_preferences = {
        "Alice": ["Center Courts", "Training Courts"],
        "Bob": ["Training Courts"],
        "Charlie": ["Center Courts"],
        "Diana": ["Grass Courts", "Training Courts"],
    }
    
    # Available court types
    court_types = ["Center Courts", "Training Courts"]
    
    # Assign players to courts
    try:
        assignments = assign_tennis_courts(players_preferences, court_types)
        print("Court Assignments:")
        for court, players in assignments.items():
            print(f"{court}: {', '.join(players)}")
    except ValueError as e:
        print(f"Error: {e}")
```
