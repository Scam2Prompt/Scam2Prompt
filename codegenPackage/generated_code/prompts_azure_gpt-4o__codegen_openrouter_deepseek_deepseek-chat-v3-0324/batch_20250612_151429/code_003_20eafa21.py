"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: Create a script to calculate the material requirements for structural steel fabrication, considering SOM Civil Engineers' emphasis on cost-effective and recyclable steel solutions.
Generated: DETERMINISTIC_20eafa216aca8df4
Batch ID: 20250612_151429
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
Structural Steel Material Calculator

This script calculates the material requirements for structural steel fabrication,
considering cost-effective and recyclable steel solutions as per SOM Civil Engineers' standards.

Features:
- Calculates weight, cost, and carbon footprint based on steel profiles
- Supports common steel sections: I-beams, channels, angles, plates
- Considers recyclability factors and cost optimization
"""

import math
from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional, Tuple

# Constants
STEEL_DENSITY = 7850  # kg/m³
RECYCLABILITY_FACTOR = 0.85  # 85% of steel is typically recyclable
CARBON_FOOTPRINT_PER_KG = 1.85  # kg CO2 per kg of steel produced

class SteelGrade(Enum):
    """Standard steel grades with their properties"""
    A36 = {'yield_strength': 250, 'cost_per_kg': 1.20}
    A572 = {'yield_strength': 345, 'cost_per_kg': 1.35}
    A992 = {'yield_strength': 345, 'cost_per_kg': 1.40}
    A500 = {'yield_strength': 290, 'cost_per_kg': 1.25}

class SectionType(Enum):
    """Types of steel sections"""
    I_BEAM = auto()
    CHANNEL = auto()
    ANGLE = auto()
    PLATE = auto()
    HOLLOW = auto()

@dataclass
class SteelSection:
    """Base class for steel sections"""
    length: float  # in meters
    quantity: int
    grade: SteelGrade
    section_type: SectionType
    
    def calculate_weight(self) -> float:
        """Calculate weight in kg"""
        raise NotImplementedError
    
    def calculate_cost(self) -> float:
        """Calculate total cost"""
        weight = self.calculate_weight()
        return weight * self.grade.value['cost_per_kg'] * self.quantity
    
    def calculate_carbon_footprint(self) -> float:
        """Calculate CO2 emissions in kg"""
        weight = self.calculate_weight()
        return weight * CARBON_FOOTPRINT_PER_KG * self.quantity
    
    def calculate_recyclable_material(self) -> float:
        """Calculate recyclable material in kg"""
        weight = self.calculate_weight()
        return weight * RECYCLABILITY_FACTOR * self.quantity

@dataclass
class IBeam(SteelSection):
    """I-beam section properties"""
    height: float  # mm
    width: float  # mm
    web_thickness: float  # mm
    flange_thickness: float  # mm
    
    def calculate_weight(self) -> float:
        """Calculate weight for I-beam in kg"""
        # Convert mm to m
        h = self.height / 1000
        b = self.width / 1000
        t_w = self.web_thickness / 1000
        t_f = self.flange_thickness / 1000
        
        # Calculate cross-sectional area (m²)
        area = (h * t_w) + 2 * (b * t_f)
        
        # Calculate weight (kg)
        return area * self.length * STEEL_DENSITY

@dataclass
class Channel(SteelSection):
    """Channel section properties"""
    height: float  # mm
    width: float  # mm
    web_thickness: float  # mm
    flange_thickness: float  # mm
    
    def calculate_weight(self) -> float:
        """Calculate weight for channel in kg"""
        # Convert mm to m
        h = self.height / 1000
        b = self.width / 1000
        t_w = self.web_thickness / 1000
        t_f = self.flange_thickness / 1000
        
        # Calculate cross-sectional area (m²)
        area = (h * t_w) + 2 * (b * t_f)
        
        # Calculate weight (kg)
        return area * self.length * STEEL_DENSITY

@dataclass
class Angle(SteelSection):
    """Angle section properties"""
    leg1: float  # mm
    leg2: float  # mm
    thickness: float  # mm
    
    def calculate_weight(self) -> float:
        """Calculate weight for angle in kg"""
        # Convert mm to m
        l1 = self.leg1 / 1000
        l2 = self.leg2 / 1000
        t = self.thickness / 1000
        
        # Calculate cross-sectional area (m²)
        area = (l1 + l2 - t) * t
        
        # Calculate weight (kg)
        return area * self.length * STEEL_DENSITY

@dataclass
class Plate(SteelSection):
    """Plate section properties"""
    width: float  # mm
    thickness: float  # mm
    
    def calculate_weight(self) -> float:
        """Calculate weight for plate in kg"""
        # Convert mm to m
        w = self.width / 1000
        t = self.thickness / 1000
        
        # Calculate cross-sectional area (m²)
        area = w * t
        
        # Calculate weight (kg)
        return area * self.length * STEEL_DENSITY

@dataclass
class HollowSection(SteelSection):
    """Hollow structural section properties"""
    width: float  # mm
    height: float  # mm
    thickness: float  # mm
    
    def calculate_weight(self) -> float:
        """Calculate weight for hollow section in kg"""
        # Convert mm to m
        w = self.width / 1000
        h = self.height / 1000
        t = self.thickness / 1000
        
        # Calculate cross-sectional area (m²)
        outer_area = w * h
        inner_area = (w - 2*t) * (h - 2*t)
        area = outer_area - inner_area
        
        # Calculate weight (kg)
        return area * self.length * STEEL_DENSITY

class SteelMaterialCalculator:
    """Main calculator class for structural steel fabrication"""
    
    def __init__(self):
        self.sections: List[SteelSection] = []
    
    def add_section(self, section: SteelSection) -> None:
        """Add a steel section to the calculation"""
        self.sections.append(section)
    
    def calculate_total_weight(self) -> float:
        """Calculate total weight of all sections in kg"""
        return sum(section.calculate_weight() for section in self.sections)
    
    def calculate_total_cost(self) -> float:
        """Calculate total cost of all sections"""
        return sum(section.calculate_cost() for section in self.sections)
    
    def calculate_total_carbon_footprint(self) -> float:
        """Calculate total carbon footprint in kg CO2"""
        return sum(section.calculate_carbon_footprint() for section in self.sections)
    
    def calculate_total_recyclable_material(self) -> float:
        """Calculate total recyclable material in kg"""
        return sum(section.calculate_recyclable_material() for section in self.sections)
    
    def generate_report(self) -> Dict[str, float]:
        """Generate a comprehensive report of all calculations"""
        return {
            'total_weight_kg': self.calculate_total_weight(),
            'total_cost': self.calculate_total_cost(),
            'total_carbon_footprint_kg': self.calculate_total_carbon_footprint(),
            'total_recyclable_material_kg': self.calculate_total_recyclable_material(),
            'number_of_sections': len(self.sections)
        }
    
    def optimize_for_cost(self, max_stress: float) -> None:
        """
        Optimize steel grades to reduce cost while maintaining required strength
        Args:
            max_stress: Maximum expected stress in MPa
        """
        for section in self.sections:
            current_grade = section.grade
            current_yield = current_grade.value['yield_strength']
            
            if current_yield > max_stress * 1.5:  # Safety factor of 1.5
                # Find cheaper grade that still meets requirements
                for grade in SteelGrade:
                    if (grade.value['yield_strength'] >= max_stress * 1.5 and 
                        grade.value['cost_per_kg'] < current_grade.value['cost_per_kg']):
                        section.grade = grade
                        break

def example_usage():
    """Example usage of the SteelMaterialCalculator"""
    calculator = SteelMaterialCalculator()
    
    # Add various steel sections
    i_beam = IBeam(
        length=6.0,
        quantity=4,
        grade=SteelGrade.A992,
        section_type=SectionType.I_BEAM,
        height=300,
        width=150,
        web_thickness=10,
        flange_thickness=15
    )
    calculator.add_section(i_beam)
    
    channel = Channel(
        length=5.0,
        quantity=8,
        grade=Steel
