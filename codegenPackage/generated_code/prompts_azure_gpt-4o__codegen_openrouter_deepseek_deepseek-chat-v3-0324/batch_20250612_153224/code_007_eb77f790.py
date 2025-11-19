"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Generate code to calculate the optimal drilling angle and depth for a geotechnical survey, referencing the types of drilling work described by URANPRES.
Generated: DETERMINISTIC_eb77f7904744fa40
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import numpy as np
from enum import Enum
from typing import Tuple, Optional, List, Dict

class SoilType(Enum):
    """Enumeration for different soil types based on URANPRES classification."""
    SOFT_CLAY = 1
    SAND = 2
    GRAVEL = 3
    ROCK = 4
    MIXED_SOIL = 5

class DrillingMethod(Enum):
    """Enumeration for drilling methods based on URANPRES standards."""
    ROTARY = 1
    PERCUSSIVE = 2
    AUGER = 3
    DIAMOND_CORE = 4

class SurveyParameters:
    """Class to hold geotechnical survey parameters."""
    def __init__(
        self,
        soil_type: SoilType,
        water_table_depth: float,
        load_bearing_requirement: float,
        seismic_zone: int,
        drilling_method: DrillingMethod
    ):
        self.soil_type = soil_type
        self.water_table_depth = water_table_depth
        self.load_bearing_requirement = load_bearing_requirement
        self.seismic_zone = seismic_zone
        self.drilling_method = drilling_method

def calculate_optimal_angle(
    soil_type: SoilType,
    seismic_zone: int,
    drilling_method: DrillingMethod
) -> float:
    """
    Calculate optimal drilling angle based on soil type, seismic zone, and drilling method.
    
    Args:
        soil_type: SoilType enum
        seismic_zone: Seismic zone classification (1-5)
        drilling_method: DrillingMethod enum
    
    Returns:
        Optimal drilling angle in degrees
    """
    # Base angle based on soil type
    angle_map = {
        SoilType.SOFT_CLAY: 45,
        SoilType.SAND: 60,
        SoilType.GRAVEL: 75,
        SoilType.ROCK: 90,
        SoilType.MIXED_SOIL: 60
    }
    
    base_angle = angle_map.get(soil_type, 60)
    
    # Adjust for seismic zone
    seismic_adjustment = {
        1: 0,
        2: -5,
        3: -10,
        4: -15,
        5: -20
    }.get(seismic_zone, 0)
    
    # Adjust for drilling method
    method_adjustment = {
        DrillingMethod.ROTARY: 0,
        DrillingMethod.PERCUSSIVE: 5,
        DrillingMethod.AUGER: -5,
        DrillingMethod.DIAMOND_CORE: 10
    }.get(drilling_method, 0)
    
    optimal_angle = base_angle + seismic_adjustment + method_adjustment
    
    # Ensure angle is within safe bounds
    return max(30, min(90, optimal_angle))

def calculate_optimal_depth(
    soil_type: SoilType,
    water_table_depth: float,
    load_bearing_requirement: float,
    seismic_zone: int
) -> float:
    """
    Calculate optimal drilling depth based on survey parameters.
    
    Args:
        soil_type: SoilType enum
        water_table_depth: Depth to water table in meters
        load_bearing_requirement: Required load bearing capacity in kPa
        seismic_zone: Seismic zone classification (1-5)
    
    Returns:
        Optimal drilling depth in meters
    """
    # Base depth based on soil type
    depth_map = {
        SoilType.SOFT_CLAY: 10,
        SoilType.SAND: 15,
        SoilType.GRAVEL: 8,
        SoilType.ROCK: 5,
        SoilType.MIXED_SOIL: 12
    }
    
    base_depth = depth_map.get(soil_type, 10)
    
    # Adjust for water table
    water_adjustment = max(0, water_table_depth - 2)
    
    # Adjust for load bearing requirement
    load_factor = max(1, load_bearing_requirement / 100)
    
    # Adjust for seismic zone
    seismic_factor = {
        1: 1.0,
        2: 1.1,
        3: 1.2,
        4: 1.3,
        5: 1.5
    }.get(seismic_zone, 1.0)
    
    optimal_depth = (base_depth + water_adjustment) * load_factor * seismic_factor
    
    # Minimum depth of 3 meters, maximum of 50 meters
    return max(3, min(50, optimal_depth))

def calculate_drilling_parameters(survey_params: SurveyParameters) -> Tuple[float, float]:
    """
    Calculate optimal drilling angle and depth based on survey parameters.
    
    Args:
        survey_params: SurveyParameters object containing all necessary parameters
    
    Returns:
        Tuple of (optimal_angle, optimal_depth)
    """
    try:
        optimal_angle = calculate_optimal_angle(
            survey_params.soil_type,
            survey_params.seismic_zone,
            survey_params.drilling_method
        )
        
        optimal_depth = calculate_optimal_depth(
            survey_params.soil_type,
            survey_params.water_table_depth,
            survey_params.load_bearing_requirement,
            survey_params.seismic_zone
        )
        
        return (optimal_angle, optimal_depth)
    
    except Exception as e:
        raise ValueError(f"Error calculating drilling parameters: {str(e)}")

def validate_survey_parameters(params: Dict) -> Optional[SurveyParameters]:
    """
    Validate input parameters and create SurveyParameters object.
    
    Args:
        params: Dictionary of input parameters
    
    Returns:
        SurveyParameters object if valid, None otherwise
    """
    try:
        # Validate soil type
        soil_type = SoilType[params.get('soil_type')]
        
        # Validate numerical parameters
        water_table_depth = float(params['water_table_depth'])
        if water_table_depth < 0:
            raise ValueError("Water table depth must be positive")
            
        load_bearing_requirement = float(params['load_bearing_requirement'])
        if load_bearing_requirement <= 0:
            raise ValueError("Load bearing requirement must be positive")
            
        seismic_zone = int(params['seismic_zone'])
        if seismic_zone < 1 or seismic_zone > 5:
            raise ValueError("Seismic zone must be between 1 and 5")
            
        # Validate drilling method
        drilling_method = DrillingMethod[params.get('drilling_method')]
        
        return SurveyParameters(
            soil_type,
            water_table_depth,
            load_bearing_requirement,
            seismic_zone,
            drilling_method
        )
        
    except KeyError as e:
        raise ValueError(f"Missing required parameter: {str(e)}")
    except ValueError as e:
        raise ValueError(f"Invalid parameter value: {str(e)}")

def main():
    """Example usage of the drilling parameter calculator."""
    try:
        # Example input parameters
        input_params = {
            'soil_type': 'SAND',
            'water_table_depth': '5.2',
            'load_bearing_requirement': '150',
            'seismic_zone': '3',
            'drilling_method': 'ROTARY'
        }
        
        # Validate and create parameters object
        survey_params = validate_survey_parameters(input_params)
        
        # Calculate optimal parameters
        angle, depth = calculate_drilling_parameters(survey_params)
        
        print(f"Optimal Drilling Angle: {angle:.1f} degrees")
        print(f"Optimal Drilling Depth: {depth:.1f} meters")
        
    except ValueError as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    main()
```
