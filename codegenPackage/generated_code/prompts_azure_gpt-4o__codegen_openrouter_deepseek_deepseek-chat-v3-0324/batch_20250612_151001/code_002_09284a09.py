"""
Generated Code Metadata:
========================
Original URL: https://greencreditbuilder.com
Prompt: Develop a Python script that calculates credit scores based on climate-positive activities, similar to GreenCreditBuilder's model.
Generated: DETERMINISTIC_09284a095ad921b5
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union
from dataclasses import dataclass, field
from enum import Enum, auto
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ActivityType(Enum):
    """Enum representing different types of climate-positive activities."""
    RENEWABLE_ENERGY = auto()
    TREE_PLANTING = auto()
    WASTE_REDUCTION = auto()
    SUSTAINABLE_TRANSPORT = auto()
    ENERGY_EFFICIENCY = auto()

@dataclass
class Activity:
    """Data class representing a climate-positive activity."""
    activity_type: ActivityType
    quantity: float  # e.g., kWh for energy, trees planted, kg of waste reduced
    date: datetime
    description: Optional[str] = None
    verified: bool = False

@dataclass
class CreditScoreParameters:
    """Configuration parameters for credit score calculation."""
    weight_renewable_energy: float = 0.3
    weight_tree_planting: float = 0.25
    weight_waste_reduction: float = 0.2
    weight_sustainable_transport: float = 0.15
    weight_energy_efficiency: float = 0.1
    verification_multiplier: float = 1.5
    base_score: int = 300
    max_score: int = 850

class GreenCreditBuilder:
    """Main class for calculating climate-positive credit scores."""
    
    def __init__(self, parameters: Optional[CreditScoreParameters] = None):
        """Initialize with default or custom parameters."""
        self.parameters = parameters if parameters else CreditScoreParameters()
        self.activities: List[Activity] = []
        
    def add_activity(self, activity: Activity) -> None:
        """Add a climate-positive activity to the user's record."""
        if not isinstance(activity, Activity):
            raise ValueError("Activity must be of type Activity")
        self.activities.append(activity)
        logger.info(f"Added activity: {activity.activity_type.name}")
        
    def calculate_score(self) -> int:
        """Calculate the credit score based on accumulated activities."""
        if not self.activities:
            logger.warning("No activities found for score calculation")
            return self.parameters.base_score
            
        score_components = {
            ActivityType.RENEWABLE_ENERGY: 0,
            ActivityType.TREE_PLANTING: 0,
            ActivityType.WASTE_REDUCTION: 0,
            ActivityType.SUSTAINABLE_TRANSPORT: 0,
            ActivityType.ENERGY_EFFICIENCY: 0
        }
        
        # Aggregate quantities by activity type
        for activity in self.activities:
            multiplier = self.parameters.verification_multiplier if activity.verified else 1.0
            score_components[activity.activity_type] += activity.quantity * multiplier
        
        # Calculate weighted score
        weighted_score = (
            score_components[ActivityType.RENEWABLE_ENERGY] * self.parameters.weight_renewable_energy +
            score_components[ActivityType.TREE_PLANTING] * self.parameters.weight_tree_planting +
            score_components[ActivityType.WASTE_REDUCTION] * self.parameters.weight_waste_reduction +
            score_components[ActivityType.SUSTAINABLE_TRANSPORT] * self.parameters.weight_sustainable_transport +
            score_components[ActivityType.ENERGY_EFFICIENCY] * self.parameters.weight_energy_efficiency
        )
        
        # Normalize to credit score range
        normalized_score = self.parameters.base_score + int(weighted_score)
        final_score = min(normalized_score, self.parameters.max_score)
        
        logger.info(f"Calculated credit score: {final_score}")
        return final_score
    
    def export_activities(self, file_path: str) -> None:
        """Export activities to a JSON file."""
        try:
            activities_data = [
                {
                    "activity_type": activity.activity_type.name,
                    "quantity": activity.quantity,
                    "date": activity.date.isoformat(),
                    "description": activity.description,
                    "verified": activity.verified
                }
                for activity in self.activities
            ]
            
            with open(file_path, 'w') as f:
                json.dump(activities_data, f, indent=2)
            logger.info(f"Activities exported to {file_path}")
        except Exception as e:
            logger.error(f"Failed to export activities: {str(e)}")
            raise
            
    def import_activities(self, file_path: str) -> None:
        """Import activities from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                activities_data = json.load(f)
                
            for activity_data in activities_data:
                activity = Activity(
                    activity_type=ActivityType[activity_data["activity_type"]],
                    quantity=float(activity_data["quantity"]),
                    date=datetime.fromisoformat(activity_data["date"]),
                    description=activity_data.get("description"),
                    verified=bool(activity_data.get("verified", False))
                )
                self.add_activity(activity)
            logger.info(f"Activities imported from {file_path}")
        except Exception as e:
            logger.error(f"Failed to import activities: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    # Initialize the credit builder
    credit_builder = GreenCreditBuilder()
    
    # Add some activities
    credit_builder.add_activity(Activity(
        activity_type=ActivityType.RENEWABLE_ENERGY,
        quantity=1000,  # 1000 kWh
        date=datetime.now(),
        description="Solar panel installation",
        verified=True
    ))
    
    credit_builder.add_activity(Activity(
        activity_type=ActivityType.TREE_PLANTING,
        quantity=10,  # 10 trees
        date=datetime.now(),
        description="Community tree planting event"
    ))
    
    # Calculate and print the score
    score = credit_builder.calculate_score()
    print(f"Climate-positive credit score: {score}")
```
