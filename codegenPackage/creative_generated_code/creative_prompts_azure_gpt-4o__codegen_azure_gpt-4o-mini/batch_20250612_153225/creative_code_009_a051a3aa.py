"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kallimos.com
Prompt: Develop an algorithm to optimize housing arrangements in a Kallimos community, balancing privacy and community interaction as described in the co-living principles.
Generated: DETERMINISTIC_a051a3aa503b0005
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Tuple

# Define a class to represent a person in the Kallimos community
class Person:
    def __init__(self, name: str, privacy_preference: int, interaction_preference: int):
        """
        Initialize a Person instance.

        :param name: The name of the person
        :param privacy_preference: A score from 1-10 indicating how much privacy they prefer
        :param interaction_preference: A score from 1-10 indicating how much interaction they desire
        """
        self.name = name
        self.privacy_preference = privacy_preference
        self.interaction_preference = interaction_preference

# Define a class to represent a housing arrangement
class HousingArrangement:
    def __init__(self, name: str, capacity: int):
        """
        Initialize a HousingArrangement instance.

        :param name: The name of the housing unit
        :param capacity: The maximum number of people that can live in the unit
        """
        self.name = name
        self.capacity = capacity
        self.residents: List[Person] = []

    def add_resident(self, person: Person) -> bool:
        """
        Add a resident to the housing arrangement if capacity allows.

        :param person: The Person instance to add
        :return: True if the person was added, False otherwise
        """
        if len(self.residents) < self.capacity:
            self.residents.append(person)
            return True
        return False

# Function to calculate the compatibility score for a housing arrangement
def calculate_compatibility_score(arrangement: HousingArrangement) -> float:
    """
    Calculate a compatibility score based on residents' preferences.

    :param arrangement: The HousingArrangement instance
    :return: A compatibility score between 0 and 1
    """
    if len(arrangement.residents) == 0:
        return 0.0

    total_score = 0
    for i in range(len(arrangement.residents)):
        for j in range(i + 1, len(arrangement.residents)):
            # Calculate difference in preferences
            privacy_diff = abs(arrangement.residents[i].privacy_preference - arrangement.residents[j].privacy_preference)
            interaction_diff = abs(arrangement.residents[i].interaction_preference - arrangement.residents[j].interaction_preference)
            # Compatibility score is inversely proportional to preference differences
            total_score += max(0, 10 - (privacy_diff + interaction_diff))

    return total_score / (len(arrangement.residents) * (len(arrangement.residents) - 1) / 2)

# Function to optimize housing arrangements based on compatibility scores
def optimize_housing_arrangements(people: List[Person], arrangements: List[HousingArrangement]) -> Dict[str, List[str]]:
    """
    Optimize housing arrangements to balance privacy and community interaction.

    :param people: List of Person instances
    :param arrangements: List of HousingArrangement instances
    :return: A dictionary mapping arrangement names to their residents
    """
    optimized_arrangements = {arrangement.name: [] for arrangement in arrangements}

    # Shuffle people to randomize arrangements
    random.shuffle(people)

    # Assign people to arrangements based on their preferences
    for person in people:
        best_arrangement = None
        best_score = float('-inf')

        for arrangement in arrangements:
            if arrangement.add_resident(person):  # Try to add the person
                # Calculate compatibility score if added
                score = calculate_compatibility_score(arrangement)
                # If score is better, keep this arrangement
                if score > best_score:
                    best_score = score
                    best_arrangement = arrangement
            else:
                # If the arrangement is full, remove the last added resident for recalibration
                arrangement.residents.pop()

        # Finalize the decision for this person
        if best_arrangement:
            best_arrangement.add_resident(person)

    # Populate the output dictionary with residents in each arrangement
    for arrangement in arrangements:
        optimized_arrangements[arrangement.name] = [resident.name for resident in arrangement.residents]

    return optimized_arrangements

# Example usage
if __name__ == "__main__":
    # Sample data
    people = [
        Person("Alice", 7, 8),
        Person("Bob", 6, 7),
        Person("Charlie", 4, 5),
        Person("Diana", 8, 9)
    ]

    arrangements = [
        HousingArrangement("Unit A", 2),
        HousingArrangement("Unit B", 2)
    ]

    # Optimize arrangements
    result = optimize_housing_arrangements(people, arrangements)

    # Display optimized housing arrangements
    for unit, residents in result.items():
        print(f"{unit}: {', '.join(residents)}")
```
