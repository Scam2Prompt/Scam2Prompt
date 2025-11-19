"""
Generated Code Metadata:
========================
Original URL: https://www.marodconsultores.com.pe
Prompt: Write Python code to calculate electrical system resistance values for grounding systems, referencing methodologies used in industrial audits as described by MAROD Consultores SAC.
Generated: DETERMINISTIC_f4174995998d0d5d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Union, List, Optional

class GroundingResistanceCalculator:
    """
    A class to calculate electrical system resistance values for grounding systems.
    The methodologies are based on industrial audits as described by MAROD Consultores SAC.
    """

    @staticmethod
    def single_rod_resistance(
        soil_resistivity: float,
        rod_length: float,
        rod_diameter: float
    ) -> float:
        """
        Calculate the resistance of a single grounding rod using the Dwight's formula.

        Args:
            soil_resistivity: Soil resistivity in ohm-meters (Ω·m)
            rod_length: Length of the rod in meters (m)
            rod_diameter: Diameter of the rod in meters (m)

        Returns:
            Resistance in ohms (Ω)

        Raises:
            ValueError: If any input parameter is non-positive
        """
        if soil_resistivity <= 0 or rod_length <= 0 or rod_diameter <= 0:
            raise ValueError("All input parameters must be positive values.")

        # Dwight's formula for single rod resistance
        resistance = (soil_resistivity / (2 * math.pi * rod_length)) * (
            math.log(4 * rod_length / rod_diameter) - 1
        )
        return resistance

    @staticmethod
    def multiple_rods_resistance(
        single_rod_resistance: float,
        number_of_rods: int,
        spacing: float,
        rod_length: float,
        arrangement: str = "linear"
    ) -> float:
        """
        Calculate the total resistance of multiple grounding rods considering mutual coupling.

        Args:
            single_rod_resistance: Resistance of a single rod in ohms (Ω)
            number_of_rods: Number of rods in the system
            spacing: Distance between rods in meters (m)
            rod_length: Length of each rod in meters (m)
            arrangement: Arrangement of rods ('linear' or 'grid')

        Returns:
            Total resistance in ohms (Ω)

        Raises:
            ValueError: If any input parameter is invalid
        """
        if single_rod_resistance <= 0 or number_of_rods <= 0 or spacing <= 0 or rod_length <= 0:
            raise ValueError("All input parameters must be positive values.")
        if arrangement not in ["linear", "grid"]:
            raise ValueError("Arrangement must be either 'linear' or 'grid'.")

        if number_of_rods == 1:
            return single_rod_resistance

        # Calculate mutual resistance factor
        if arrangement == "linear":
            mutual_factor = 1 + (2 * rod_length / (math.pi * spacing)) * (
                (number_of_rods - 1) * math.log(2)
            )
        else:  # grid arrangement
            mutual_factor = 1 + (rod_length / (math.pi * spacing)) * (
                (math.sqrt(number_of_rods) - 1) ** 2
            )

        total_resistance = single_rod_resistance * mutual_factor / number_of_rods
        return total_resistance

    @staticmethod
    def mesh_grid_resistance(
        soil_resistivity: float,
        grid_area: float,
        conductor_length: float,
        burial_depth: float,
        conductor_diameter: float
    ) -> float:
        """
        Calculate the resistance of a mesh grounding grid using the Schwarz formula.

        Args:
            soil_resistivity: Soil resistivity in ohm-meters (Ω·m)
            grid_area: Area covered by the grid in square meters (m²)
            conductor_length: Total length of conductors in meters (m)
            burial_depth: Depth of burial in meters (m)
            conductor_diameter: Diameter of conductors in meters (m)

        Returns:
            Grid resistance in ohms (Ω)

        Raises:
            ValueError: If any input parameter is invalid
        """
        if (soil_resistivity <= 0 or grid_area <= 0 or conductor_length <= 0 or
            burial_depth <= 0 or conductor_diameter <= 0):
            raise ValueError("All input parameters must be positive values.")

        # Schwarz formula for mesh grid resistance
        term1 = soil_resistivity / (math.pi * conductor_length)
        term2 = math.log(2 * conductor_length / math.sqrt(grid_area))
        term3 = math.log(conductor_length / (math.pi * burial_depth * conductor_diameter))
        
        grid_resistance = term1 * (term2 + term3 + 1)
        return grid_resistance

    @staticmethod
    def combined_resistance(
        rod_resistance: float,
        grid_resistance: float,
        coupling_factor: float = 0.6
    ) -> float:
        """
        Calculate the combined resistance of rods and grid system.

        Args:
            rod_resistance: Resistance of the rod system in ohms (Ω)
            grid_resistance: Resistance of the grid system in ohms (Ω)
            coupling_factor: Coupling factor between rods and grid (default: 0.6)

        Returns:
            Combined resistance in ohms (Ω)

        Raises:
            ValueError: If resistances are non-positive or coupling factor is invalid
        """
        if rod_resistance <= 0 or grid_resistance <= 0:
            raise ValueError("Resistance values must be positive.")
        if not 0 < coupling_factor < 1:
            raise ValueError("Coupling factor must be between 0 and 1.")

        combined_resistance = (rod_resistance * grid_resistance - 
                             coupling_factor * rod_resistance * grid_resistance) / (
                             rod_resistance + grid_resistance - 
                             2 * coupling_factor * rod_resistance * grid_resistance)
        return combined_resistance
```
