"""
Generated Code Metadata:
========================
Original URL: https://l2lusty.site
Prompt: Create a Python script to calculate the expected Adena earnings for a player based on the drop rate (x20) and spoil rate (x20) provided on the L2Lusty server.
Generated: DETERMINISTIC_18d97154a30fd164
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Adena Earnings Calculator for L2Lusty Server (x20 rates)
Calculates expected Adena earnings based on drop and spoil rates.
"""

import argparse
from typing import Dict, List, Optional, Union

class AdenaCalculator:
    """
    A class to calculate expected Adena earnings based on drop and spoil rates.
    """
    
    def __init__(self):
        self.drop_rate_multiplier = 20
        self.spoil_rate_multiplier = 20
        self.base_drop_chance = 0.0
        self.base_spoil_chance = 0.0
        self.mob_adena = 0
        self.spoil_adena = 0
        self.kills = 0
        
    def validate_input(self, value: Union[int, float], min_val: float, max_val: float, name: str) -> None:
        """
        Validate input values.
        
        Args:
            value: The value to validate
            min_val: Minimum allowed value
            max_val: Maximum allowed value
            name: Name of the parameter for error message
            
        Raises:
            ValueError: If value is out of bounds
        """
        if not min_val <= value <= max_val:
            raise ValueError(f"{name} must be between {min_val} and {max_val}")
    
    def set_parameters(
        self,
        base_drop_chance: float,
        base_spoil_chance: float,
        mob_adena: int,
        spoil_adena: int,
        kills: int
    ) -> None:
        """
        Set calculation parameters with validation.
        
        Args:
            base_drop_chance: Base drop chance (0-1)
            base_spoil_chance: Base spoil chance (0-1)
            mob_adena: Adena dropped per mob
            spoil_adena: Adena from spoil per mob
            kills: Number of mobs killed
            
        Raises:
            ValueError: If any parameter is invalid
        """
        self.validate_input(base_drop_chance, 0, 1, "Base drop chance")
        self.validate_input(base_spoil_chance, 0, 1, "Base spoil chance")
        self.validate_input(mob_adena, 0, float('inf'), "Mob Adena")
        self.validate_input(spoil_adena, 0, float('inf'), "Spoil Adena")
        self.validate_input(kills, 1, float('inf'), "Number of kills")
        
        self.base_drop_chance = base_drop_chance
        self.base_spoil_chance = base_spoil_chance
        self.mob_adena = mob_adena
        self.spoil_adena = spoil_adena
        self.kills = kills
    
    def calculate_expected_adena(self) -> Dict[str, float]:
        """
        Calculate expected Adena earnings.
        
        Returns:
            Dictionary containing:
            - drop_adena: Expected Adena from drops
            - spoil_adena: Expected Adena from spoils
            - total_adena: Total expected Adena
        """
        effective_drop_chance = min(1.0, self.base_drop_chance * self.drop_rate_multiplier)
        effective_spoil_chance = min(1.0, self.base_spoil_chance * self.spoil_rate_multiplier)
        
        expected_drop_adena = self.kills * effective_drop_chance * self.mob_adena
        expected_spoil_adena = self.kills * effective_spoil_chance * self.spoil_adena
        
        return {
            "drop_adena": round(expected_drop_adena, 2),
            "spoil_adena": round(expected_spoil_adena, 2),
            "total_adena": round(expected_drop_adena + expected_spoil_adena, 2)
        }

def main():
    parser = argparse.ArgumentParser(
        description="Calculate expected Adena earnings for L2Lusty server (x20 rates)"
    )
    parser.add_argument(
        "--drop_chance",
        type=float,
        required=True,
        help="Base drop chance (0-1)"
    )
    parser.add_argument(
        "--spoil_chance",
        type=float,
        required=True,
        help="Base spoil chance (0-1)"
    )
    parser.add_argument(
        "--mob_adena",
        type=int,
        required=True,
        help="Adena dropped per mob"
    )
    parser.add_argument(
        "--spoil_adena",
        type=int,
        required=True,
        help="Adena from spoil per mob"
    )
    parser.add_argument(
        "--kills",
        type=int,
        required=True,
        help="Number of mobs killed"
    )
    
    args = parser.parse_args()
    
    try:
        calculator = AdenaCalculator()
        calculator.set_parameters(
            args.drop_chance,
            args.spoil_chance,
            args.mob_adena,
            args.spoil_adena,
            args.kills
        )
        
        results = calculator.calculate_expected_adena()
        
        print("\nExpected Adena Earnings:")
        print(f"From drops: {results['drop_adena']:,} Adena")
        print(f"From spoils: {results['spoil_adena']:,} Adena")
        print(f"Total expected: {results['total_adena']:,} Adena")
        
    except ValueError as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
```
