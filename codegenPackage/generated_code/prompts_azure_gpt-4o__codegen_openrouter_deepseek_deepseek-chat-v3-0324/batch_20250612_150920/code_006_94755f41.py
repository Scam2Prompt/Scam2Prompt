"""
Generated Code Metadata:
========================
Original URL: https://cryptexbit.com
Prompt: Create a script to calculate the Cryco governance model's resource allocation percentages for holders, members, leaders, founders, and co-creators.
Generated: DETERMINISTIC_94755f4107c15f21
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Dict, Tuple

class CrycoGovernanceModel:
    """
    A class to calculate resource allocation percentages based on the Cryco governance model.
    The model allocates resources to holders, members, leaders, founders, and co-creators.
    """
    
    def __init__(self):
        """
        Initialize the governance model with default allocation parameters.
        These can be modified as needed.
        """
        self.default_allocation = {
            'holders': 0.40,    # 40% for token holders
            'members': 0.25,    # 25% for active members
            'leaders': 0.15,    # 15% for project leaders
            'founders': 0.10,   # 10% for founders
            'co_creators': 0.10 # 10% for co-creators
        }
    
    def validate_inputs(self, allocations: Dict[str, float]) -> Tuple[bool, str]:
        """
        Validate that allocation inputs sum to 1 (100%) and all values are positive.
        
        Args:
            allocations: Dictionary of allocation percentages
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        total = sum(allocations.values())
        if not (0.999 <= total <= 1.001):  # Allow for floating point precision
            return False, f"Allocations must sum to 100% (current sum: {total*100:.2f}%)"
        
        for role, percentage in allocations.items():
            if percentage < 0:
                return False, f"Negative allocation for {role}: {percentage}"
                
        return True, ""
    
    def calculate_allocations(self, custom_allocations: Dict[str, float] = None) -> Dict[str, float]:
        """
        Calculate the resource allocations, using either default values or custom inputs.
        
        Args:
            custom_allocations: Optional dictionary to override default allocations
            
        Returns:
            Dictionary of calculated allocations
            
        Raises:
            ValueError: If custom allocations are invalid
        """
        allocations = self.default_allocation.copy()
        
        if custom_allocations:
            # Update with custom values where provided
            for role in custom_allocations:
                if role not in allocations:
                    raise ValueError(f"Invalid role '{role}' in custom allocations")
                allocations[role] = custom_allocations[role]
            
            # Validate the modified allocations
            is_valid, error_msg = self.validate_inputs(allocations)
            if not is_valid:
                raise ValueError(error_msg)
        
        return allocations
    
    def print_allocations(self, allocations: Dict[str, float]):
        """
        Print the allocation percentages in a readable format.
        
        Args:
            allocations: Dictionary of allocation percentages
        """
        print("Cryco Governance Resource Allocation:")
        print("------------------------------------")
        for role, percentage in allocations.items():
            print(f"{role.replace('_', ' ').title():<12}: {percentage*100:.2f}%")
        print("------------------------------------")
        print(f"Total: {sum(allocations.values())*100:.2f}%")

def main():
    """
    Main function to demonstrate the Cryco governance model calculations.
    """
    try:
        governance = CrycoGovernanceModel()
        
        # Example 1: Use default allocations
        print("\nExample 1: Default Allocations")
        default_alloc = governance.calculate_allocations()
        governance.print_allocations(default_alloc)
        
        # Example 2: Use custom allocations
        print("\nExample 2: Custom Allocations")
        custom_alloc = {
            'holders': 0.35,
            'members': 0.30,
            'leaders': 0.15,
            'founders': 0.10,
            'co_creators': 0.10
        }
        calculated_alloc = governance.calculate_allocations(custom_alloc)
        governance.print_allocations(calculated_alloc)
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
