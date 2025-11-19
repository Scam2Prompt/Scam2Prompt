"""
Generated Code Metadata:
========================
Original URL: https://wilsonelectronics.co
Prompt: Generate a Python script to perform a site survey and generate a detailed system design for a corporate campus, using the IBwave design methodology mentioned by CellAntenna Wireless.
Generated: DETERMINISTIC_e294dc3315ac4c76
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Corporate Campus Site Survey and System Design Tool

This script performs a site survey analysis and generates a detailed system design
for a corporate campus using IBwave design methodology.

Features:
- Import building layouts and site data
- Perform RF propagation analysis
- Generate heatmaps and coverage reports
- Export design documentation

Requirements:
- Python 3.8+
- numpy, pandas, matplotlib (included in requirements)
"""

import os
import json
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum, auto


class AntennaType(Enum):
    """Enumeration of supported antenna types"""
    OMNI = auto()
    DIRECTIONAL = auto()
    PANEL = auto()
    SECTOR = auto()


class MaterialType(Enum):
    """Enumeration of building material types"""
    CONCRETE = auto()
    GLASS = auto()
    DRYWALL = auto()
    METAL = auto()
    WOOD = auto()


@dataclass
class BuildingMaterial:
    """Dataclass representing building material properties"""
    name: str
    material_type: MaterialType
    attenuation: float  # dB per meter
    thickness: float    # meters


@dataclass
class Antenna:
    """Dataclass representing antenna properties"""
    name: str
    antenna_type: AntennaType
    gain: float         # dBi
    frequency: float    # MHz
    tilt: float         # degrees
    azimuth: float      # degrees


@dataclass
class AccessPoint:
    """Dataclass representing access point properties"""
    id: str
    antenna: Antenna
    x: float
    y: float
    z: float
    power: float        # dBm


@dataclass
class BuildingFloor:
    """Dataclass representing a building floor"""
    level: int
    width: float        # meters
    length: float       # meters
    height: float       # meters
    materials: List[BuildingMaterial]


@dataclass
class Building:
    """Dataclass representing a building"""
    id: str
    name: str
    floors: List[BuildingFloor]
    ap_locations: List[AccessPoint]


class SiteSurvey:
    """Main class for performing site survey and system design"""
    
    def __init__(self):
        self.buildings: Dict[str, Building] = {}
        self.free_space_path_loss_const = 20  # Constant for free space path loss calculation
    
    def add_building(self, building: Building) -> None:
        """Add a building to the survey"""
        if building.id in self.buildings:
            raise ValueError(f"Building with ID {building.id} already exists")
        self.buildings[building.id] = building
    
    def calculate_path_loss(self, distance: float, frequency: float, 
                           material_attenuation: float = 0.0) -> float:
        """
        Calculate path loss using free space path loss formula with material attenuation
        
        Args:
            distance: Distance between transmitter and receiver (meters)
            frequency: Frequency of transmission (MHz)
            material_attenuation: Additional attenuation from materials (dB)
            
        Returns:
            Path loss in dB
        """
        if distance <= 0:
            raise ValueError("Distance must be positive")
        if frequency <= 0:
            raise ValueError("Frequency must be positive")
            
        # Free space path loss formula
        fspl = self.free_space_path_loss_const * math.log10(distance) + \
               20 * math.log10(frequency) - 27.55
        
        return fspl + material_attenuation
    
    def generate_heatmap(self, building_id: str, floor_level: int, 
                         resolution: float = 1.0) -> np.ndarray:
        """
        Generate a heatmap of signal strength for a building floor
        
        Args:
            building_id: ID of the building
            floor_level: Floor level to analyze
            resolution: Grid resolution in meters
            
        Returns:
            2D numpy array representing signal strength heatmap
        """
        if building_id not in self.buildings:
            raise ValueError(f"Building {building_id} not found")
            
        building = self.buildings[building_id]
        floor = next((f for f in building.floors if f.level == floor_level), None)
        
        if not floor:
            raise ValueError(f"Floor {floor_level} not found in building {building_id}")
            
        # Get APs on this floor
        aps = [ap for ap in building.ap_locations if 
               math.floor(ap.z) == floor_level]
        
        if not aps:
            raise ValueError(f"No access points found on floor {floor_level}")
            
        # Create grid
        x_points = int(floor.width / resolution)
        y_points = int(floor.length / resolution)
        heatmap = np.zeros((x_points, y_points))
        
        # Calculate signal strength at each point
        for i in range(x_points):
            for j in range(y_points):
                x = i * resolution
                y = j * resolution
                
                total_signal = 0
                for ap in aps:
                    # Calculate distance from AP to current point
                    distance = math.sqrt((ap.x - x)**2 + (ap.y - y)**2)
                    
                    # Calculate path loss
                    path_loss = self.calculate_path_loss(
                        distance, ap.antenna.frequency,
                        self._calculate_material_attenuation(floor.materials, distance)
                    )
                    
                    # Calculate received signal strength
                    rss = ap.power + ap.antenna.gain - path_loss
                    total_signal += 10 ** (rss / 10)  # Sum in linear scale
                
                # Convert back to dBm
                if total_signal > 0:
                    heatmap[i, j] = 10 * math.log10(total_signal)
                else:
                    heatmap[i, j] = -100  # Default very low value
        
        return heatmap
    
    def _calculate_material_attenuation(self, materials: List[BuildingMaterial], 
                                       distance: float) -> float:
        """
        Calculate total material attenuation over a distance
        
        Args:
            materials: List of building materials
            distance: Distance through materials
            
        Returns:
            Total attenuation in dB
        """
        total_attenuation = 0.0
        for material in materials:
            total_attenuation += material.attenuation * material.thickness * distance
        return total_attenuation
    
    def generate_report(self, output_dir: str) -> None:
        """
        Generate a comprehensive system design report
        
        Args:
            output_dir: Directory to save report files
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # Generate reports for each building
        for building_id, building in self.buildings.items():
            self._generate_building_report(building, output_dir)
    
    def _generate_building_report(self, building: Building, output_dir: str) -> None:
        """Generate report for a single building"""
        report_data = {
            "building_id": building.id,
            "building_name": building.name,
            "floors": [],
            "ap_summary": []
        }
        
        # Process each floor
        for floor in building.floors:
            floor_data = {
                "level": floor.level,
                "dimensions": f"{floor.width}x{floor.length}x{floor.height}m",
                "materials": [m.name for m in floor.materials],
                "ap_count": sum(1 for ap in building.ap_locations 
                               if math.floor(ap.z) == floor.level)
            }
            report_data["floors"].append(floor_data)
            
            try:
                heatmap = self.generate_heatmap(building.id, floor.level)
                self._save_heatmap_image(heatmap, building.id, floor.level, output_dir)
            except ValueError as e:
                print(f"Warning: Could not generate heatmap for {building.id} floor {floor.level}: {e}")
        
        # Process APs
        for ap in building.ap_locations:
            ap_data = {
                "id": ap.id,
                "location": f"({ap.x}, {ap.y}, {ap.z})",
                "antenna_type": ap.antenna.antenna_type.name,
                "frequency": f"{ap.antenna.frequency} MHz",
                "power": f"{ap.power} dBm"
            }
            report_data["ap_summary"].append(ap_data)
        
        # Save JSON report
        report_path = os.path.join(output_dir, f"{building.id}_report.json")
        with open(report_path, 'w') as f:
            json.dump(report_data, f, indent=2)
    
    def _save_heatmap_image(self, heatmap: np.ndarray, building_id: str, 
                           floor_level: int, output_dir: str) -> None:
        """Save heatmap as an image file"""
        plt.figure(figsize=(10, 8))
        plt.imshow(heatmap.T, origin='lower', cmap='hot', 
                  extent=[0, heatmap.shape[0],
