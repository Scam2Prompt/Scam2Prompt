"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Design an algorithm to optimize the placement of residents in a Kallimos community, taking into account their needs, preferences, and abilities.
Generated: DETERMINISTIC_119ee7e11656d6c9
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Resident:
    """
    Represents a resident in the Kallimos community.
    Attributes:
        name (str): Name of the resident.
        preferences (list): List of preferences (e.g., quiet environment, proximity to amenities).
        abilities (list): List of abilities (e.g., gardening, cooking, teaching).
        needs (list): List of needs (e.g., wheelchair accessibility, social interaction).
    """
    def __init__(self, name, preferences, abilities, needs):
        self.name = name
        self.preferences = preferences
        self.abilities = abilities
        self.needs = needs


class HousingUnit:
    """
    Represents a housing unit in the Kallimos community.
    Attributes:
        unit_id (int): Unique identifier for the housing unit.
        features (list): List of features (e.g., garden, wheelchair ramp, quiet location).
        capacity (int): Maximum number of residents the unit can accommodate.
    """
    def __init__(self, unit_id, features, capacity):
        self.unit_id = unit_id
        self.features = features
        self.capacity = capacity
        self.residents = []


def optimize_placement(residents, housing_units):
    """
    Optimizes the placement of residents into housing units based on their needs, preferences, and abilities.
    Args:
        residents (list): List of Resident objects.
        housing_units (list): List of HousingUnit objects.
    Returns:
        dict: Mapping of housing unit IDs to lists of assigned residents.
    """
    # Initialize the placement dictionary
    placement = {unit.unit_id: [] for unit in housing_units}

    # Sort residents by the number of needs (prioritize those with more needs)
    residents.sort(key=lambda r: len(r.needs), reverse=True)

    # Attempt to place each resident in the best housing unit
    for resident in residents:
        best_unit = None
        best_score = -1

        for unit in housing_units:
            # Skip units that are already at capacity
            if len(unit.residents) >= unit.capacity:
                continue

            # Calculate a score based on how well the unit matches the resident's needs and preferences
            match_score = (
                sum(1 for need in resident.needs if need in unit.features) +
                sum(1 for preference in resident.preferences if preference in unit.features)
            )

            # Update the best unit if this one has a higher score
            if match_score > best_score:
                best_unit = unit
                best_score = match_score

        # Place the resident in the best unit found
        if best_unit:
            best_unit.residents.append(resident)
            placement[best_unit.unit_id].append(resident.name)
        else:
            print(f"Warning: Could not find a suitable housing unit for resident {resident.name}")

    return placement


# Example usage
if __name__ == "__main__":
    # Create sample residents
    residents = [
        Resident("Alice", preferences=["quiet", "garden"], abilities=["gardening"], needs=["wheelchair"]),
        Resident("Bob", preferences=["proximity to amenities"], abilities=["cooking"], needs=["social interaction"]),
        Resident("Charlie", preferences=["quiet"], abilities=["teaching"], needs=["wheelchair", "garden"]),
    ]

    # Create sample housing units
    housing_units = [
        HousingUnit(1, features=["quiet", "garden", "wheelchair"], capacity=2),
        HousingUnit(2, features=["proximity to amenities", "social interaction"], capacity=1),
    ]

    # Optimize placement
    placement = optimize_placement(residents, housing_units)

    # Print the results
    print("Optimized Placement:")
    for unit_id, assigned_residents in placement.items():
        print(f"Unit {unit_id}: {', '.join(assigned_residents)}")
```
