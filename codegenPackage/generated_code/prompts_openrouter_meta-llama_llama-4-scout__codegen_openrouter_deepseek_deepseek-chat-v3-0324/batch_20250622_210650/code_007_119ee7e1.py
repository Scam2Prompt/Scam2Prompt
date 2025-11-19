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
import heapq
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from enum import Enum, auto

class ResidentAbility(Enum):
    INDEPENDENT = auto()
    ASSISTED_LIVING = auto()
    MEMORY_CARE = auto()

@dataclass
class Resident:
    id: int
    name: str
    preferred_neighbors: List[int]  # List of resident IDs
    avoided_neighbors: List[int]    # List of resident IDs
    ability_level: ResidentAbility
    preferred_building: Optional[str] = None

@dataclass
class HousingUnit:
    id: int
    building: str
    unit_type: str  # e.g., "studio", "1-bedroom", etc.
    max_capacity: int
    current_residents: List[int]  # List of resident IDs

class CommunityPlacementOptimizer:
    def __init__(self, residents: List[Resident], housing_units: List[HousingUnit]):
        self.residents = {r.id: r for r in residents}
        self.housing_units = {h.id: h for h in housing_units}
        self.placement: Dict[int, int] = {}  # resident_id -> unit_id

    def _calculate_compatibility_score(self, resident1: Resident, resident2: Resident) -> float:
        """Calculate compatibility score between two residents (0-1)."""
        score = 0.0
        
        # Positive factors
        if resident2.id in resident1.preferred_neighbors:
            score += 0.5
        if resident1.id in resident2.preferred_neighbors:
            score += 0.5
        if resident1.ability_level == resident2.ability_level:
            score += 0.3
        
        # Negative factors
        if resident2.id in resident1.avoided_neighbors:
            score -= 0.7
        if resident1.id in resident2.avoided_neighbors:
            score -= 0.7
        
        return max(0.0, min(1.0, score))

    def _get_unit_suitability(self, resident: Resident, unit: HousingUnit) -> float:
        """Calculate how suitable a unit is for a resident (0-1)."""
        score = 0.0
        
        # Check building preference
        if resident.preferred_building and resident.preferred_building == unit.building:
            score += 0.4
            
        # Check unit capacity
        occupancy_ratio = len(unit.current_residents) / unit.max_capacity
        if occupancy_ratio < 0.5:
            score += 0.2
        elif occupancy_ratio > 0.9:
            score -= 0.2
            
        return max(0.0, min(1.0, score))

    def _calculate_placement_cost(self, resident_id: int, unit_id: int) -> float:
        """Calculate the cost of placing a resident in a unit (lower is better)."""
        resident = self.residents[resident_id]
        unit = self.housing_units[unit_id]
        
        # Base cost is inverse of unit suitability
        cost = 1.0 - self._get_unit_suitability(resident, unit)
        
        # Add neighbor compatibility costs
        for neighbor_id in unit.current_residents:
            neighbor = self.residents[neighbor_id]
            compatibility = self._calculate_compatibility_score(resident, neighbor)
            cost += (1.0 - compatibility) * 0.5  # Weighted factor
            
        return cost

    def _find_best_unit_for_resident(self, resident_id: int) -> Optional[int]:
        """Find the best available unit for a resident using a priority queue."""
        resident = self.residents[resident_id]
        priority_queue = []
        
        for unit_id, unit in self.housing_units.items():
            # Skip units that are full or incompatible with ability level
            if (len(unit.current_residents) >= unit.max_capacity or
                (resident.ability_level == ResidentAbility.MEMORY_CARE and 
                 unit.unit_type != "memory-care")):
                continue
                
            cost = self._calculate_placement_cost(resident_id, unit_id)
            heapq.heappush(priority_queue, (cost, unit_id))
        
        return priority_queue[0][1] if priority_queue else None

    def optimize_placement(self) -> Dict[int, int]:
        """Optimize resident placement using a greedy algorithm."""
        # Reset current placements
        self.placement = {}
        for unit in self.housing_units.values():
            unit.current_residents = []
        
        # Prioritize residents with more constraints first
        residents_sorted = sorted(
            self.residents.values(),
            key=lambda r: (
                len(r.avoided_neighbors),
                -len(r.preferred_neighbors),
                r.ability_level.value  # Higher ability levels (e.g., MEMORY_CARE) first
            ),
            reverse=True
        )
        
        for resident in residents_sorted:
            best_unit = self._find_best_unit_for_resident(resident.id)
            if best_unit is not None:
                self.placement[resident.id] = best_unit
                self.housing_units[best_unit].current_residents.append(resident.id)
        
        return self.placement

    def get_placement_score(self) -> float:
        """Calculate overall placement quality score (0-1)."""
        if not self.placement:
            return 0.0
        
        total_score = 0.0
        resident_count = len(self.placement)
        
        for resident_id, unit_id in self.placement.items():
            resident = self.residents[resident_id]
            unit = self.housing_units[unit_id]
            
            # Unit suitability contributes to score
            total_score += self._get_unit_suitability(resident, unit)
            
            # Neighbor compatibility contributes to score
            for neighbor_id in unit.current_residents:
                if neighbor_id == resident_id:
                    continue
                neighbor = self.residents[neighbor_id]
                total_score += self._calculate_compatibility_score(resident, neighbor)
        
        # Normalize score
        max_possible_score = resident_count * (1 + len(self.housing_units[unit_id].current_residents) - 1)
        return total_score / max_possible_score if max_possible_score > 0 else 0.0
```
