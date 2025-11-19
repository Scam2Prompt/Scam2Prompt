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
import random
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from enum import Enum, auto

class ResidentPreference(Enum):
    """Enum representing resident's preference for privacy vs community interaction."""
    HIGH_PRIVACY = auto()
    BALANCED = auto()
    HIGH_COMMUNITY = auto()

@dataclass
class Resident:
    """Class representing a resident with their preferences."""
    id: int
    name: str
    preference: ResidentPreference
    compatibility_scores: Dict[int, float]  # Maps resident_id to compatibility score

@dataclass
class HousingUnit:
    """Class representing a housing unit with its properties."""
    id: int
    capacity: int
    privacy_score: float  # 0-1 scale where 1 is most private
    community_score: float  # 0-1 scale where 1 is most community-oriented

class HousingOptimizer:
    """Optimizes housing arrangements based on resident preferences and unit properties."""
    
    def __init__(self, residents: List[Resident], units: List[HousingUnit]):
        self.residents = residents
        self.units = units
        self.resident_map = {r.id: r for r in residents}
        self.unit_map = {u.id: u for u in units}
        
    def _calculate_fitness(self, assignment: Dict[int, List[int]]) -> float:
        """
        Calculate the fitness score of a housing assignment.
        Higher scores indicate better balance between privacy and community.
        """
        total_score = 0.0
        
        for unit_id, resident_ids in assignment.items():
            unit = self.unit_map[unit_id]
            
            for resident_id in resident_ids:
                resident = self.resident_map[resident_id]
                
                # Calculate preference match score
                if resident.preference == ResidentPreference.HIGH_PRIVACY:
                    pref_score = unit.privacy_score
                elif resident.preference == ResidentPreference.HIGH_COMMUNITY:
                    pref_score = unit.community_score
                else:  # BALANCED
                    pref_score = (unit.privacy_score + unit.community_score) / 2
                
                # Calculate compatibility with housemates
                compat_score = 0.0
                for other_id in resident_ids:
                    if other_id != resident_id:
                        compat_score += resident.compatibility_scores.get(other_id, 0.5)
                if len(resident_ids) > 1:
                    compat_score /= (len(resident_ids) - 1)
                
                total_score += (pref_score * 0.7) + (compat_score * 0.3)
        
        return total_score
    
    def _generate_random_assignment(self) -> Dict[int, List[int]]:
        """Generate a random valid housing assignment."""
        assignment = {unit.id: [] for unit in self.units}
        residents = [r.id for r in self.residents]
        random.shuffle(residents)
        
        for resident_id in residents:
            assigned = False
            # Try to assign to a unit with available capacity
            for unit_id in assignment:
                unit = self.unit_map[unit_id]
                if len(assignment[unit_id]) < unit.capacity:
                    assignment[unit_id].append(resident_id)
                    assigned = True
                    break
            
            if not assigned:
                raise ValueError("No available units with capacity for all residents")
        
        return assignment
    
    def optimize(self, iterations: int = 1000) -> Dict[int, List[int]]:
        """
        Optimize housing arrangements using a hill-climbing algorithm.
        
        Args:
            iterations: Number of optimization iterations to perform
            
        Returns:
            Best found assignment mapping unit IDs to lists of resident IDs
        """
        current_assignment = self._generate_random_assignment()
        current_score = self._calculate_fitness(current_assignment)
        
        for _ in range(iterations):
            # Generate a neighbor by swapping two random residents
            neighbor = {k: v.copy() for k, v in current_assignment.items()}
            
            # Find two random residents in different units
            units = list(neighbor.keys())
            random.shuffle(units)
            
            resident1 = None
            resident2 = None
            unit1 = None
            unit2 = None
            
            for u1 in units:
                if neighbor[u1]:
                    for u2 in units:
                        if u1 != u2 and neighbor[u2]:
                            resident1 = random.choice(neighbor[u1])
                            resident2 = random.choice(neighbor[u2])
                            unit1 = u1
                            unit2 = u2
                            break
                    if resident1:
                        break
            
            if not resident1:
                continue  # No possible swaps
            
            # Perform the swap
            neighbor[unit1].remove(resident1)
            neighbor[unit2].remove(resident2)
            neighbor[unit1].append(resident2)
            neighbor[unit2].append(resident1)
            
            # Evaluate the neighbor
            neighbor_score = self._calculate_fitness(neighbor)
            
            # Keep the better assignment
            if neighbor_score > current_score:
                current_assignment = neighbor
                current_score = neighbor_score
        
        return current_assignment

def generate_sample_data() -> Tuple[List[Resident], List[HousingUnit]]:
    """Generate sample data for testing the optimizer."""
    residents = [
        Resident(1, "Alice", ResidentPreference.HIGH_PRIVACY, {2: 0.3, 3: 0.8, 4: 0.5}),
        Resident(2, "Bob", ResidentPreference.BALANCED, {1: 0.3, 3: 0.6, 4: 0.9}),
        Resident(3, "Charlie", ResidentPreference.HIGH_COMMUNITY, {1: 0.8, 2: 0.6, 4: 0.7}),
        Resident(4, "Dana", ResidentPreference.BALANCED, {1: 0.5, 2: 0.9, 3: 0.7}),
    ]
    
    units = [
        HousingUnit(1, 2, 0.9, 0.2),  # High privacy unit
        HousingUnit(2, 2, 0.5, 0.5),  # Balanced unit
        HousingUnit(3, 2, 0.3, 0.8),  # High community unit
    ]
    
    return residents, units

def print_assignment(assignment: Dict[int, List[int]], residents: List[Resident], units: List[HousingUnit]) -> None:
    """Print the housing assignment in a human-readable format."""
    resident_map = {r.id: r for r in residents}
    unit_map = {u.id: u for u in units}
    
    for unit_id, resident_ids in assignment.items():
        unit = unit_map[unit_id]
        print(f"Unit {unit_id} (Privacy: {unit.privacy_score:.1f}, Community: {unit.community_score:.1f}):")
        for rid in resident_ids:
            resident = resident_map[rid]
            print(f"  - {resident.name} (Prefers: {resident.preference.name})")
        print()

def main():
    """Main function to demonstrate the housing optimizer."""
    try:
        residents, units = generate_sample_data()
        optimizer = HousingOptimizer(residents, units)
        best_assignment = optimizer.optimize(iterations=1000)
        
        print("Optimized Housing Arrangement:")
        print_assignment(best_assignment, residents, units)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
