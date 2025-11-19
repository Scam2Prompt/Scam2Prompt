"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Develop an algorithm to optimize housing arrangements in a Kallimos community, balancing privacy and community interaction as described in the co-living principles.
Generated: DETERMINISTIC_a051a3aa503b0005
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

class Resident:
    """Represents a resident in the Kallimos community."""
    
    def __init__(self, name: str, preferred_privacy_level: int, preferred_interaction_level: int):
        """
        Initializes a Resident object.

        Args:
        - name (str): The resident's name.
        - preferred_privacy_level (int): The resident's preferred privacy level (1-10).
        - preferred_interaction_level (int): The resident's preferred interaction level (1-10).
        """
        self.name = name
        self.preferred_privacy_level = preferred_privacy_level
        self.preferred_interaction_level = preferred_interaction_level


class HousingArrangement:
    """Represents a housing arrangement in the Kallimos community."""
    
    def __init__(self, residents: List[Resident], private_rooms: int, shared_rooms: int):
        """
        Initializes a HousingArrangement object.

        Args:
        - residents (List[Resident]): The list of residents in the arrangement.
        - private_rooms (int): The number of private rooms available.
        - shared_rooms (int): The number of shared rooms available.
        """
        self.residents = residents
        self.private_rooms = private_rooms
        self.shared_rooms = shared_rooms


def calculate_utility(resident: Resident, room_type: str, roommates: List[Resident] = None) -> float:
    """
    Calculates the utility of a resident in a given room arrangement.

    Args:
    - resident (Resident): The resident.
    - room_type (str): The type of room ('private' or 'shared').
    - roommates (List[Resident], optional): The list of roommates. Defaults to None.

    Returns:
    - float: The utility value.
    """
    if room_type == 'private':
        return resident.preferred_privacy_level
    elif room_type == 'shared':
        if roommates is None:
            raise ValueError("Roommates must be provided for shared rooms")
        interaction_level = sum(roommate.preferred_interaction_level for roommate in roommates) / len(roommates)
        return (resident.preferred_interaction_level * interaction_level) / 10


def optimize_housing_arrangement(residents: List[Resident], private_rooms: int, shared_rooms: int) -> Dict[str, List[Resident]]:
    """
    Optimizes the housing arrangement to balance privacy and community interaction.

    Args:
    - residents (List[Resident]): The list of residents.
    - private_rooms (int): The number of private rooms available.
    - shared_rooms (int): The number of shared rooms available.

    Returns:
    - Dict[str, List[Resident]]: A dictionary with the optimized room assignments.
    """
    # Sort residents by their preferred privacy levels in descending order
    residents.sort(key=lambda resident: resident.preferred_privacy_level, reverse=True)

    # Assign residents to private rooms first
    private_room_assignments = residents[:private_rooms]
    remaining_residents = residents[private_rooms:]

    # Assign remaining residents to shared rooms
    shared_room_assignments = []
    for _ in range(shared_rooms):
        roommates = []
        for _ in range(min(len(remaining_residents), 4)):  # Limit to 4 roommates per room
            roommates.append(remaining_residents.pop(0))
        shared_room_assignments.append(roommates)

    # Create the optimized housing arrangement
    arrangement = {
        'private_rooms': [[resident.name for resident in room] for room in [private_room_assignments]],
        'shared_rooms': [[resident.name for resident in room] for room in shared_room_assignments]
    }

    return arrangement


def main():
    # Example usage
    residents = [
        Resident('Alice', 8, 6),
        Resident('Bob', 5, 8),
        Resident('Charlie', 9, 4),
        Resident('David', 6, 7),
        Resident('Eve', 7, 5),
        Resident('Frank', 4, 9),
    ]

    private_rooms = 2
    shared_rooms = 1

    try:
        arrangement = optimize_housing_arrangement(residents, private_rooms, shared_rooms)
        print("Optimized Housing Arrangement:")
        print(arrangement)
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
