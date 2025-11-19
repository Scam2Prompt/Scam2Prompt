"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Write a script to calculate environmental impact assessments for mining and road construction projects, inspired by MGEL's commitment to environmental responsibility.
Generated: DETERMINISTIC_77519d4f83e1de56
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import json
from typing import Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ProjectType(Enum):
    MINING = "mining"
    ROAD_CONSTRUCTION = "road_construction"

class ImpactCategory(Enum):
    CARBON_EMISSIONS = "carbon_emissions"
    WATER_USAGE = "water_usage"
    LAND_DISTURBANCE = "land_disturbance"
    BIODIVERSITY_IMPACT = "biodiversity_impact"
    AIR_QUALITY = "air_quality"

@dataclass
class EnvironmentalImpact:
    category: ImpactCategory
    value: float
    unit: str
    mitigation_factor: float = 1.0

@dataclass
class ProjectAssessment:
    project_id: str
    project_type: ProjectType
    location: str
    area_affected: float  # in hectares
    duration: float  # in years
    impacts: List[EnvironmentalImpact]
    total_score: float = 0.0

class EnvironmentalImpactCalculator:
    """
    Calculator for environmental impact assessments of mining and road construction projects.
    """
    
    # Default impact factors (per hectare per year)
    IMPACT_FACTORS = {
        ProjectType.MINING: {
            ImpactCategory.CARBON_EMISSIONS: 1500,  # kg CO2/ha/year
            ImpactCategory.WATER_USAGE: 5000,  # m3/ha/year
            ImpactCategory.LAND_DISTURBANCE: 0.8,  # fraction of area
            ImpactCategory.BIODIVERSITY_IMPACT: 0.7,  # biodiversity loss index (0-1)
            ImpactCategory.AIR_QUALITY: 50,  # particulate matter (PM2.5) µg/m3
        },
        ProjectType.ROAD_CONSTRUCTION: {
            ImpactCategory.CARBON_EMISSIONS: 800,  # kg CO2/ha/year
            ImpactCategory.WATER_USAGE: 2000,  # m3/ha/year
            ImpactCategory.LAND_DISTURBANCE: 0.95,  # fraction of area
            ImpactCategory.BIODIVERSITY_IMPACT: 0.6,  # biodiversity loss index (0-1)
            ImpactCategory.AIR_QUALITY: 30,  # particulate matter (PM2.5) µg/m3
        }
    }
    
    # Weightings for each impact category in total score calculation
    IMPACT_WEIGHTS = {
        ImpactCategory.CARBON_EMISSIONS: 0.25,
        ImpactCategory.WATER_USAGE: 0.2,
        ImpactCategory.LAND_DISTURBANCE: 0.2,
        ImpactCategory.BIODIVERSITY_IMPACT: 0.25,
        ImpactCategory.AIR_QUALITY: 0.1,
    }
    
    @staticmethod
    def calculate_impact(
        project_type: ProjectType,
        area_affected: float,
        duration: float,
        mitigation_factors: Optional[Dict[ImpactCategory, float]] = None
    ) -> List[EnvironmentalImpact]:
        """
        Calculate environmental impacts for a project.
        
        Args:
            project_type: Type of project (mining or road construction)
            area_affected: Area affected in hectares
            duration: Project duration in years
            mitigation_factors: Optional dictionary of mitigation factors per impact category
            
        Returns:
            List of EnvironmentalImpact objects
        """
        if area_affected <= 0:
            raise ValueError("Area affected must be positive")
        if duration <= 0:
            raise ValueError("Duration must be positive")
            
        impacts = []
        mitigation_factors = mitigation_factors or {}
        
        for category, factor in EnvironmentalImpactCalculator.IMPACT_FACTORS[project_type].items():
            mitigation = mitigation_factors.get(category, 1.0)
            value = factor * area_affected * duration * mitigation
            
            unit = ""
            if category == ImpactCategory.CARBON_EMISSIONS:
                unit = "kg CO2"
            elif category == ImpactCategory.WATER_USAGE:
                unit = "m3"
            elif category == ImpactCategory.LAND_DISTURBANCE:
                unit = "ha"
            elif category == ImpactCategory.BIODIVERSITY_IMPACT:
                unit = "index (0-1)"
            elif category == ImpactCategory.AIR_QUALITY:
                unit = "µg/m3"
                
            impacts.append(
                EnvironmentalImpact(
                    category=category,
                    value=value,
                    unit=unit,
                    mitigation_factor=mitigation
                )
            )
            
        return impacts
    
    @staticmethod
    def calculate_total_score(impacts: List[EnvironmentalImpact]) -> float:
        """
        Calculate a weighted total environmental impact score.
        
        Args:
            impacts: List of EnvironmentalImpact objects
            
        Returns:
            Total environmental impact score (0-100, higher is worse)
        """
        total = 0.0
        max_possible = 0.0
        
        for impact in impacts:
            weight = EnvironmentalImpactCalculator.IMPACT_WEIGHTS[impact.category]
            
            # Normalize values to 0-100 scale
            if impact.category == ImpactCategory.BIODIVERSITY_IMPACT:
                normalized = impact.value * 100  # already 0-1 scale
            else:
                # For other categories, we need to scale based on typical ranges
                normalized = min(impact.value / 1000, 100)  # arbitrary scaling factor
                
            total += normalized * weight
            max_possible += 100 * weight
            
        # Scale to 0-100 range
        return (total / max_possible) * 100

def load_project_data(file_path: str) -> Dict:
    """
    Load project data from JSON file.
    
    Args:
        file_path: Path to JSON file
        
    Returns:
        Dictionary containing project data
    """
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in file: {file_path}")
        raise
    except Exception as e:
        logger.error(f"Error loading project data: {str(e)}")
        raise

def save_assessment_results(assessment: ProjectAssessment, file_path: str) -> None:
    """
    Save assessment results to JSON file.
    
    Args:
        assessment: ProjectAssessment object
        file_path: Path to output JSON file
    """
    try:
        result = {
            "project_id": assessment.project_id,
            "project_type": assessment.project_type.value,
            "location": assessment.location,
            "area_affected": assessment.area_affected,
            "duration": assessment.duration,
            "total_score": assessment.total_score,
            "impacts": [
                {
                    "category": impact.category.value,
                    "value": impact.value,
                    "unit": impact.unit,
                    "mitigation_factor": impact.mitigation_factor
                }
                for impact in assessment.impacts
            ]
        }
        
        with open(file_path, 'w') as f:
            json.dump(result, f, indent=2)
            
        logger.info(f"Assessment results saved to {file_path}")
    except Exception as e:
        logger.error(f"Error saving assessment results: {str(e)}")
        raise

def assess_project(project_data: Dict) -> ProjectAssessment:
    """
    Perform environmental impact assessment for a project.
    
    Args:
        project_data: Dictionary containing project data
        
    Returns:
        ProjectAssessment object with results
    """
    try:
        project_type = ProjectType(project_data["project_type"])
        mitigation_factors = {
            ImpactCategory(key): float(value) 
            for key, value in project_data.get("mitigation_factors", {}).items()
        }
        
        impacts = EnvironmentalImpactCalculator.calculate_impact(
            project_type=project_type,
            area_affected=float(project_data["area_affected"]),
            duration=float(project_data["duration"]),
            mitigation_factors=mitigation_factors
        )
        
        total_score = EnvironmentalImpactCalculator.calculate_total_score(impacts)
        
        return ProjectAssessment(
            project_id=project_data["project_id"],
            project_type=project_type,
            location=project_data["location"],
            area_affected=float(project_data["area_affected"]),
            duration=float(project_data["duration"]),
            impacts=impacts,
            total_score=total_score
        )
    except KeyError as e:
        logger.error(f"Missing required field in project data: {str(e)}")
        raise
    except ValueError as e:
        logger.error(f"Invalid value in project data: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Error assessing project: {str(e)}")
        raise

def main(input_file: str, output_file: str) ->
