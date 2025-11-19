"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tejasmaxtech.com
Prompt: Write a Python function that estimates the durability of UPVC roofing tiles under various weather conditions, referencing their resistance to UV radiation and chemical corrosion.
Generated: DETERMINISTIC_ec11e0198bb87650
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class UPVCTile:
    """
    A class to represent a UPVC roofing tile and its durability under various weather conditions.
    """

    def __init__(self, uv_resistance: float, chemical_resistance: float):
        """
        Initializes the UPVC tile with its resistance properties.

        Parameters:
        uv_resistance (float): A value representing the tile's resistance to UV radiation (0 to 1).
        chemical_resistance (float): A value representing the tile's resistance to chemical corrosion (0 to 1).
        """
        if not (0 <= uv_resistance <= 1):
            raise ValueError("UV resistance must be between 0 and 1.")
        if not (0 <= chemical_resistance <= 1):
            raise ValueError("Chemical resistance must be between 0 and 1.")
            
        self.uv_resistance = uv_resistance
        self.chemical_resistance = chemical_resistance

    def estimate_durability(self, uv_exposure: float, chemical_exposure: float) -> str:
        """
        Estimates the durability of the UPVC tile based on UV and chemical exposure.

        Parameters:
        uv_exposure (float): The expected UV exposure level (0 to 1).
        chemical_exposure (float): The expected chemical exposure level (0 to 1).

        Returns:
        str: A message indicating the estimated durability of the tile.
        """
        if not (0 <= uv_exposure <= 1):
            raise ValueError("UV exposure must be between 0 and 1.")
        if not (0 <= chemical_exposure <= 1):
            raise ValueError("Chemical exposure must be between 0 and 1.")
        
        # Calculate effective durability based on resistance and exposure
        effective_uv_durability = self.uv_resistance - uv_exposure
        effective_chemical_durability = self.chemical_resistance - chemical_exposure
        
        # Determine final durability status
        if effective_uv_durability < 0 or effective_chemical_durability < 0:
            return "The UPVC tile is at risk of deterioration."
        elif effective_uv_durability > 0.5 and effective_chemical_durability > 0.5:
            return "The UPVC tile is expected to remain durable under these conditions."
        else:
            return "The UPVC tile has moderate durability under these conditions."

# Example usage:
if __name__ == "__main__":
    try:
        # Create a UPVC tile with specific resistances
        tile = UPVCTile(uv_resistance=0.8, chemical_resistance=0.9)
        
        # Estimate durability based on expected exposure levels
        result = tile.estimate_durability(uv_exposure=0.6, chemical_exposure=0.4)
        print(result)  # Output the durability estimation
    except ValueError as e:
        print(f"Error: {e}")
```
