"""
Generated Code Metadata:
========================
Original URL: https://claims-runecoinio.pages.dev
Prompt: Develop an algorithm to optimize the allocation of runes for a large number of RSICs, maximizing the efficiency of the system.
Generated: DETERMINISTIC_f996235529069391
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import heapq
from typing import List, Dict, Tuple

class RuneAllocator:
    """
    Optimizes the allocation of runes to RSICs (Rune-Specific Integrated Circuits)
    to maximize system efficiency.
    """
    
    def __init__(self, rsics: List[Tuple[int, int]], runes: List[int]):
        """
        Initialize the allocator with RSICs and available runes.
        
        Args:
            rsics: List of tuples (power_requirement, efficiency_factor) for each RSIC
            runes: List of available rune power values
        """
        self.rsics = rsics
        self.runes = runes
        self.allocations: Dict[int, int] = {}  # RSIC index -> rune index
    
    def _calculate_efficiency(self, rsic_index: int, rune_power: int) -> float:
        """
        Calculate efficiency score for a RSIC-rune pair.
        
        Args:
            rsic_index: Index of the RSIC
            rune_power: Power of the rune being considered
            
        Returns:
            Efficiency score (higher is better)
        """
        power_req, efficiency_factor = self.rsics[rsic_index]
        return efficiency_factor * min(rune_power, power_req) / power_req
    
    def optimize(self) -> Dict[int, int]:
        """
        Optimize rune allocation to maximize total efficiency.
        
        Returns:
            Dictionary mapping RSIC indices to their allocated rune indices
        """
        # Create a max-heap based on efficiency scores
        efficiency_heap = []
        
        # Generate all possible RSIC-rune pairs with their efficiency scores
        for rsic_idx, _ in enumerate(self.rsics):
            for rune_idx, rune_power in enumerate(self.runes):
                efficiency = self._calculate_efficiency(rsic_idx, rune_power)
                heapq.heappush(efficiency_heap, (-efficiency, rsic_idx, rune_idx))
        
        allocated_rsics = set()
        allocated_runes = set()
        allocations = {}
        
        # Greedily allocate best efficiency pairs first
        while efficiency_heap and len(allocated_rsics) < len(self.rsics) and len(allocated_runes) < len(self.runes):
            neg_efficiency, rsic_idx, rune_idx = heapq.heappop(efficiency_heap)
            
            if rsic_idx not in allocated_rsics and rune_idx not in allocated_runes:
                allocations[rsic_idx] = rune_idx
                allocated_rsics.add(rsic_idx)
                allocated_runes.add(rune_idx)
        
        self.allocations = allocations
        return allocations
    
    def get_total_efficiency(self) -> float:
        """
        Calculate total efficiency of current allocation.
        
        Returns:
            Total system efficiency score
        """
        total = 0.0
        for rsic_idx, rune_idx in self.allocations.items():
            total += self._calculate_efficiency(rsic_idx, self.runes[rune_idx])
        return total
    
    def validate_allocation(self) -> bool:
        """
        Validate that the current allocation is legal.
        
        Returns:
            True if allocation is valid, False otherwise
        """
        # Check for duplicate allocations
        if len(set(self.allocations.values())) != len(self.allocations):
            return False
        
        # Check all rune indices are valid
        for rune_idx in self.allocations.values():
            if rune_idx < 0 or rune_idx >= len(self.runes):
                return False
        
        # Check all RSIC indices are valid
        for rsic_idx in self.allocations.keys():
            if rsic_idx < 0 or rsic_idx >= len(self.rsics):
                return False
        
        return True


# Example usage
if __name__ == "__main__":
    # RSICs defined as (power_requirement, efficiency_factor)
    rsics = [
        (10, 1.5),  # RSIC 0
        (8, 1.2),   # RSIC 1
        (15, 2.0),  # RSIC 2
    ]
    
    # Available runes with their power values
    runes = [12, 9, 7, 18]
    
    allocator = RuneAllocator(rsics, runes)
    allocation = allocator.optimize()
    
    print("Optimal Allocation:")
    for rsic_idx, rune_idx in allocation.items():
        print(f"RSIC {rsic_idx} -> Rune {rune_idx} (Power: {runes[rune_idx]})")
    
    print(f"Total System Efficiency: {allocator.get_total_efficiency():.2f}")
    print(f"Allocation Valid: {allocator.validate_allocation()}")
```
