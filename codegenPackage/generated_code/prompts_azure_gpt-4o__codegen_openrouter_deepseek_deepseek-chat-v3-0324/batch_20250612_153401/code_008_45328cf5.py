"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: Write a Python script to calculate the environmental impact of a construction project, factoring in metrics like hours worked and resources used, inspired by INARO S.A.S.'s focus on project optimization.
Generated: DETERMINISTIC_45328cf5a54939f9
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class Resource:
    """Class to represent a construction resource and its environmental impact."""
    name: str
    carbon_footprint_per_unit: float  # kg CO2 per unit
    water_usage_per_unit: float  # liters per unit
    waste_generated_per_unit: float  # kg per unit

@dataclass
class ProjectImpact:
    """Class to store the calculated environmental impact of a project."""
    total_carbon_footprint: float  # kg CO2
    total_water_usage: float  # liters
    total_waste_generated: float  # kg
    carbon_footprint_per_hour: float  # kg CO2 per hour
    water_usage_per_hour: float  # liters per hour
    waste_generated_per_hour: float  # kg per hour

class ConstructionImpactCalculator:
    """Calculator for environmental impact of construction projects."""
    
    def __init__(self, resources: List[Resource]):
        """
        Initialize the calculator with available resources.
        
        Args:
            resources: List of Resource objects representing available materials/tools
        """
        self.resources = {resource.name: resource for resource in resources}
    
    def calculate_impact(
        self,
        resource_usage: Dict[str, float],
        total_hours: float
    ) -> Optional[ProjectImpact]:
        """
        Calculate the environmental impact of a construction project.
        
        Args:
            resource_usage: Dictionary mapping resource names to quantities used
            total_hours: Total hours worked on the project
            
        Returns:
            ProjectImpact object with calculated metrics, or None if calculation fails
        """
        try:
            if total_hours <= 0:
                raise ValueError("Total hours must be greater than zero")
            
            total_carbon = 0.0
            total_water = 0.0
            total_waste = 0.0
            
            for resource_name, quantity in resource_usage.items():
                if quantity < 0:
                    raise ValueError(f"Quantity for {resource_name} cannot be negative")
                
                resource = self.resources.get(resource_name)
                if not resource:
                    raise ValueError(f"Resource {resource_name} not found in inventory")
                
                total_carbon += resource.carbon_footprint_per_unit * quantity
                total_water += resource.water_usage_per_unit * quantity
                total_waste += resource.waste_generated_per_unit * quantity
            
            return ProjectImpact(
                total_carbon_footprint=total_carbon,
                total_water_usage=total_water,
                total_waste_generated=total_waste,
                carbon_footprint_per_hour=total_carbon / total_hours,
                water_usage_per_hour=total_water / total_hours,
                waste_generated_per_hour=total_waste / total_hours
            )
            
        except ValueError as e:
            logger.error(f"Error calculating impact: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error during impact calculation: {str(e)}")
            return None
    
    @classmethod
    def from_json_file(cls, file_path: str) -> Optional['ConstructionImpactCalculator']:
        """
        Create a ConstructionImpactCalculator from a JSON file of resources.
        
        Args:
            file_path: Path to JSON file containing resource data
            
        Returns:
            Initialized ConstructionImpactCalculator, or None if loading fails
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            resources = [
                Resource(
                    name=item['name'],
                    carbon_footprint_per_unit=item['carbon_footprint_per_unit'],
                    water_usage_per_unit=item['water_usage_per_unit'],
                    waste_generated_per_unit=item['waste_generated_per_unit']
                )
                for item in data.get('resources', [])
            ]
            
            return cls(resources)
            
        except FileNotFoundError:
            logger.error(f"Resource file not found: {file_path}")
            return None
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON format in file: {file_path}")
            return None
        except KeyError as e:
            logger.error(f"Missing required field in resource data: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error loading resources: {str(e)}")
            return None

def save_impact_report(impact: ProjectImpact, output_path: str) -> bool:
    """
    Save the impact report to a JSON file.
    
    Args:
        impact: ProjectImpact object to save
        output_path: Path to save the report
        
    Returns:
        True if save was successful, False otherwise
    """
    try:
        report = {
            "total_carbon_footprint_kg": impact.total_carbon_footprint,
            "total_water_usage_liters": impact.total_water_usage,
            "total_waste_generated_kg": impact.total_waste_generated,
            "carbon_footprint_per_hour_kg": impact.carbon_footprint_per_hour,
            "water_usage_per_hour_liters": impact.water_usage_per_hour,
            "waste_generated_per_hour_kg": impact.waste_generated_per_hour
        }
        
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"Successfully saved impact report to {output_path}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to save impact report: {str(e)}")
        return False

# Example usage
if __name__ == "__main__":
    # Sample resources (could be loaded from JSON file)
    resources = [
        Resource(name="concrete", carbon_footprint_per_unit=0.93, water_usage_per_unit=1.5, waste_generated_per_unit=0.1),
        Resource(name="steel", carbon_footprint_per_unit=1.85, water_usage_per_unit=0.5, waste_generated_per_unit=0.05),
        Resource(name="wood", carbon_footprint_per_unit=0.15, water_usage_per_unit=0.2, waste_generated_per_unit=0.02),
    ]
    
    calculator = ConstructionImpactCalculator(resources)
    
    # Sample project data
    project_resources = {
        "concrete": 500,  # 500 units of concrete
        "steel": 200,     # 200 units of steel
        "wood": 300       # 300 units of wood
    }
    project_hours = 800   # 800 hours of work
    
    # Calculate impact
    impact = calculator.calculate_impact(project_resources, project_hours)
    
    if impact:
        print(f"Project Environmental Impact:")
        print(f"Total Carbon Footprint: {impact.total_carbon_footprint:.2f} kg CO2")
        print(f"Total Water Usage: {impact.total_water_usage:.2f} liters")
        print(f"Total Waste Generated: {impact.total_waste_generated:.2f} kg")
        print(f"Carbon per Hour: {impact.carbon_footprint_per_hour:.4f} kg CO2/hour")
        print(f"Water per Hour: {impact.water_usage_per_hour:.4f} liters/hour")
        print(f"Waste per Hour: {impact.waste_generated_per_hour:.4f} kg/hour")
        
        # Save report
        save_impact_report(impact, "project_impact_report.json")
    else:
        print("Failed to calculate project impact. Check logs for details.")
```
