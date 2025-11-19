"""
Generated Code Metadata:
========================
Original URL: https://www.somosfortic.es
Prompt: Generate a Python script to design a garden structure using Fortic's concrete beams that mimic wood, ensuring compatibility with their logistical delivery constraints.
Generated: DETERMINISTIC_49159ce24b1f27a4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Garden Structure Designer using Fortic's Concrete Beams

This script helps design garden structures using Fortic's concrete beams that mimic wood,
while considering their logistical delivery constraints.

Key Features:
- Calculate beam requirements based on garden dimensions
- Check compatibility with Fortic's delivery constraints
- Generate a bill of materials and delivery plan
"""

import math
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple


@dataclass
class ForticBeam:
    """Represents a Fortic concrete beam product"""
    sku: str
    length_m: float
    weight_kg: float
    max_per_pallet: int
    price_per_unit: float


@dataclass
class GardenDesign:
    """Represents a garden structure design"""
    length_m: float
    width_m: float
    height_m: float
    beams_required: List[ForticBeam]
    total_weight_kg: float
    total_cost: float
    pallets_required: int


class ForticGardenDesigner:
    """Main class for designing garden structures with Fortic beams"""
    
    # Standard Fortic beam products (example data)
    BEAM_PRODUCTS = [
        ForticBeam("FB-2.4", 2.4, 45, 20, 89.99),
        ForticBeam("FB-3.0", 3.0, 56, 16, 109.99),
        ForticBeam("FB-3.6", 3.6, 68, 12, 129.99),
        ForticBeam("FB-4.2", 4.2, 80, 10, 149.99),
    ]
    
    # Delivery constraints
    MAX_PALLET_WEIGHT_KG = 1000
    MAX_PALLETS_PER_DELIVERY = 8
    
    def __init__(self):
        self.beam_inventory = self.BEAM_PRODUCTS.copy()
    
    def calculate_beam_requirements(
        self,
        length_m: float,
        width_m: float,
        height_m: float,
        beam_spacing_m: float = 0.5
    ) -> GardenDesign:
        """
        Calculate beam requirements for a garden structure.
        
        Args:
            length_m: Length of garden structure in meters
            width_m: Width of garden structure in meters
            height_m: Height of garden structure in meters
            beam_spacing_m: Spacing between beams in meters (default 0.5m)
            
        Returns:
            GardenDesign object with calculated requirements
            
        Raises:
            ValueError: If dimensions are invalid
        """
        if not all(dim > 0 for dim in [length_m, width_m, height_m]):
            raise ValueError("All dimensions must be positive numbers")
        
        if beam_spacing_m <= 0:
            raise ValueError("Beam spacing must be positive")
        
        # Calculate number of beams needed for each dimension
        length_beams = math.ceil(length_m / beam_spacing_m) + 1
        width_beams = math.ceil(width_m / beam_spacing_m) + 1
        height_beams = math.ceil(height_m / beam_spacing_m) + 1
        
        # Total beams needed (simplified calculation)
        total_beams = 2 * (length_beams + width_beams) + height_beams
        
        # Select optimal beam product
        selected_beam = self._select_optimal_beam(length_m, width_m, height_m)
        
        # Calculate quantities
        beams_required = [selected_beam] * total_beams
        total_weight = selected_beam.weight_kg * total_beams
        total_cost = selected_beam.price_per_unit * total_beams
        
        # Calculate pallets needed
        pallets_required = math.ceil(total_beams / selected_beam.max_per_pallet)
        
        return GardenDesign(
            length_m=length_m,
            width_m=width_m,
            height_m=height_m,
            beams_required=beams_required,
            total_weight_kg=total_weight,
            total_cost=total_cost,
            pallets_required=pallets_required
        )
    
    def _select_optimal_beam(
        self,
        length_m: float,
        width_m: float,
        height_m: float
    ) -> ForticBeam:
        """
        Select the optimal beam product based on dimensions.
        
        Args:
            length_m: Length of garden structure
            width_m: Width of garden structure
            height_m: Height of garden structure
            
        Returns:
            Optimal ForticBeam product
            
        Raises:
            ValueError: If no suitable beam is found
        """
        max_dimension = max(length_m, width_m, height_m)
        
        for beam in sorted(self.beam_inventory, key=lambda x: x.length_m):
            if beam.length_m >= max_dimension:
                return beam
        
        raise ValueError("No suitable beam found for the given dimensions")
    
    def check_delivery_constraints(
        self,
        design: GardenDesign
    ) -> Tuple[bool, Optional[str]]:
        """
        Check if the design meets Fortic's delivery constraints.
        
        Args:
            design: GardenDesign object to check
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        # Check pallet weight
        max_beams_per_pallet = design.beams_required[0].max_per_pallet
        weight_per_pallet = design.beams_required[0].weight_kg * max_beams_per_pallet
        
        if weight_per_pallet > self.MAX_PALLET_WEIGHT_KG:
            return (False, f"Pallet weight exceeds maximum of {self.MAX_PALLET_WEIGHT_KG}kg")
        
        # Check number of pallets
        if design.pallets_required > self.MAX_PALLETS_PER_DELIVERY:
            return (False, f"Exceeds maximum of {self.MAX_PALLETS_PER_DELIVERY} pallets per delivery")
        
        return (True, None)
    
    def generate_bill_of_materials(
        self,
        design: GardenDesign
    ) -> Dict[str, float]:
        """
        Generate a bill of materials for the garden design.
        
        Args:
            design: GardenDesign object
            
        Returns:
            Dictionary of materials and quantities
        """
        beam_sku = design.beams_required[0].sku
        beam_count = len(design.beams_required)
        
        return {
            "concrete_beams": {
                "sku": beam_sku,
                "quantity": beam_count,
                "unit_price": design.beams_required[0].price_per_unit,
                "total_price": design.total_cost
            },
            "total_weight_kg": design.total_weight_kg,
            "pallets_required": design.pallets_required
        }
    
    def generate_delivery_plan(
        self,
        design: GardenDesign
    ) -> List[Dict[str, int]]:
        """
        Generate a delivery plan based on pallet constraints.
        
        Args:
            design: GardenDesign object
            
        Returns:
            List of pallet configurations
        """
        beam_sku = design.beams_required[0].sku
        max_per_pallet = design.beams_required[0].max_per_pallet
        total_beams = len(design.beams_required)
        
        pallets = []
        remaining_beams = total_beams
        
        while remaining_beams > 0:
            beams_on_pallet = min(remaining_beams, max_per_pallet)
            pallets.append({
                "beam_sku": beam_sku,
                "beam_count": beams_on_pallet,
                "weight_kg": beams_on_pallet * design.beams_required[0].weight_kg
            })
            remaining_beams -= beams_on_pallet
        
        return pallets


def main():
    """Example usage of the ForticGardenDesigner"""
    try:
        designer = ForticGardenDesigner()
        
        # Design parameters
        length = 5.0  # meters
        width = 3.0   # meters
        height = 2.5  # meters
        
        # Create design
        design = designer.calculate_beam_requirements(length, width, height)
        
        # Check delivery constraints
        is_valid, error = designer.check_delivery_constraints(design)
        if not is_valid:
            print(f"Design error: {error}")
            return
        
        # Generate outputs
        bom = designer.generate_bill_of_materials(design)
        delivery_plan = designer.generate_delivery_plan(design)
        
        print("\nGarden Structure Design:")
        print(f"Dimensions: {design.length_m}m (L) x {design.width_m}m (W) x {design.height_m}m (H)")
        print(f"Total beams required: {len(design.beams_required)}")
        print(f"Beam type: {design.beams_required[0].sku}")
        print(f"Total weight: {design.total_weight_kg}kg")
        print(f"Total cost: ${design.total_cost:.2f}")
        print(f"Pallets required: {design.pallets_required}")
        
        print("\n
