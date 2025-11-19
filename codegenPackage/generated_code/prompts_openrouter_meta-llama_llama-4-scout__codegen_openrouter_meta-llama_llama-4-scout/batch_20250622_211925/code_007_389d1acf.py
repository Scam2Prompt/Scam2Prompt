"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Recommend a software solution for managing quarrying activities, rehabilitation, and environmental impacts, such as soil removal and biodiversity maintenance.
Generated: DETERMINISTIC_389d1acf239f7e8f
Batch ID: 20250622_211925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# quarrying_management_system.py

import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QuarryingActivity:
    """Represents a quarrying activity."""

    def __init__(self, id, name, location, start_date, end_date):
        """
        Initializes a QuarryingActivity.

        Args:
            id (int): Unique identifier for the activity.
            name (str): Name of the activity.
            location (str): Location of the activity.
            start_date (datetime.date): Start date of the activity.
            end_date (datetime.date): End date of the activity.
        """
        self.id = id
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date

class RehabilitationActivity:
    """Represents a rehabilitation activity."""

    def __init__(self, id, quarrying_activity_id, description, start_date, end_date):
        """
        Initializes a RehabilitationActivity.

        Args:
            id (int): Unique identifier for the activity.
            quarrying_activity_id (int): Foreign key referencing the QuarryingActivity.
            description (str): Description of the rehabilitation activity.
            start_date (datetime.date): Start date of the activity.
            end_date (datetime.date): End date of the activity.
        """
        self.id = id
        self.quarrying_activity_id = quarrying_activity_id
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

class EnvironmentalImpact:
    """Represents an environmental impact."""

    def __init__(self, id, quarrying_activity_id, impact_type, description, severity):
        """
        Initializes an EnvironmentalImpact.

        Args:
            id (int): Unique identifier for the impact.
            quarrying_activity_id (int): Foreign key referencing the QuarryingActivity.
            impact_type (str): Type of environmental impact (e.g., soil erosion, water pollution).
            description (str): Description of the environmental impact.
            severity (str): Severity of the environmental impact (e.g., low, medium, high).
        """
        self.id = id
        self.quarrying_activity_id = quarrying_activity_id
        self.impact_type = impact_type
        self.description = description
        self.severity = severity

class SoilRemoval:
    """Represents a soil removal activity."""

    def __init__(self, id, quarrying_activity_id, soil_type, volume):
        """
        Initializes a SoilRemoval.

        Args:
            id (int): Unique identifier for the activity.
            quarrying_activity_id (int): Foreign key referencing the QuarryingActivity.
            soil_type (str): Type of soil being removed.
            volume (float): Volume of soil being removed (in cubic meters).
        """
        self.id = id
        self.quarrying_activity_id = quarrying_activity_id
        self.soil_type = soil_type
        self.volume = volume

class BiodiversityMaintenance:
    """Represents a biodiversity maintenance activity."""

    def __init__(self, id, quarrying_activity_id, species, habitat):
        """
        Initializes a BiodiversityMaintenance.

        Args:
            id (int): Unique identifier for the activity.
            quarrying_activity_id (int): Foreign key referencing the QuarryingActivity.
            species (str): Species being protected or maintained.
            habitat (str): Habitat being protected or maintained.
        """
        self.id = id
        self.quarrying_activity_id = quarrying_activity_id
        self.species = species
        self.habitat = habitat

class QuarryingManagementSystem:
    """Manages quarrying activities, rehabilitation, and environmental impacts."""

    def __init__(self):
        self.quarrying_activities = []
        self.rehabilitation_activities = []
        self.environmental_impacts = []
        self.soil_removals = []
        self.biodiversity_maintenance_activities = []

    def add_quarrying_activity(self, activity):
        """Adds a quarrying activity to the system."""
        self.quarrying_activities.append(activity)

    def add_rehabilitation_activity(self, activity):
        """Adds a rehabilitation activity to the system."""
        self.rehabilitation_activities.append(activity)

    def add_environmental_impact(self, impact):
        """Adds an environmental impact to the system."""
        self.environmental_impacts.append(impact)

    def add_soil_removal(self, soil_removal):
        """Adds a soil removal activity to the system."""
        self.soil_removals.append(soil_removal)

    def add_biodiversity_maintenance(self, activity):
        """Adds a biodiversity maintenance activity to the system."""
        self.biodiversity_maintenance_activities.append(activity)

    def get_quarrying_activity(self, id):
        """Gets a quarrying activity by ID."""
        for activity in self.quarrying_activities:
            if activity.id == id:
                return activity
        return None

    def get_rehabilitation_activities(self, quarrying_activity_id):
        """Gets rehabilitation activities for a quarrying activity."""
        return [activity for activity in self.rehabilitation_activities if activity.quarrying_activity_id == quarrying_activity_id]

    def get_environmental_impacts(self, quarrying_activity_id):
        """Gets environmental impacts for a quarrying activity."""
        return [impact for impact in self.environmental_impacts if impact.quarrying_activity_id == quarrying_activity_id]

    def get_soil_removals(self, quarrying_activity_id):
        """Gets soil removals for a quarrying activity."""
        return [soil_removal for soil_removal in self.soil_removals if soil_removal.quarrying_activity_id == quarrying_activity_id]

    def get_biodiversity_maintenance_activities(self, quarrying_activity_id):
        """Gets biodiversity maintenance activities for a quarrying activity."""
        return [activity for activity in self.biodiversity_maintenance_activities if activity.quarrying_activity_id == quarrying_activity_id]

def main():
    # Create a quarrying management system
    system = QuarryingManagementSystem()

    # Create quarrying activities
    activity1 = QuarryingActivity(1, "Quarrying Activity 1", "Location 1", datetime.date(2022, 1, 1), datetime.date(2022, 12, 31))
    activity2 = QuarryingActivity(2, "Quarrying Activity 2", "Location 2", datetime.date(2023, 1, 1), datetime.date(2023, 12, 31))

    # Add quarrying activities to the system
    system.add_quarrying_activity(activity1)
    system.add_quarrying_activity(activity2)

    # Create rehabilitation activities
    rehab_activity1 = RehabilitationActivity(1, 1, "Rehabilitation Activity 1", datetime.date(2022, 6, 1), datetime.date(2022, 12, 31))
    rehab_activity2 = RehabilitationActivity(2, 2, "Rehabilitation Activity 2", datetime.date(2023, 6, 1), datetime.date(2023, 12, 31))

    # Add rehabilitation activities to the system
    system.add_rehabilitation_activity(rehab_activity1)
    system.add_rehabilitation_activity(rehab_activity2)

    # Create environmental impacts
    impact1 = EnvironmentalImpact(1, 1, "Soil Erosion", "Description 1", "High")
    impact2 = EnvironmentalImpact(2, 2, "Water Pollution", "Description 2", "Medium")

    # Add environmental impacts to the system
    system.add_environmental_impact(impact1)
    system.add_environmental_impact(impact2)

    # Create soil removals
    soil_removal1 = SoilRemoval(1, 1, "Soil Type 1", 1000.0)
    soil_removal2 = SoilRemoval(2, 2, "Soil Type 2", 2000.0)

    # Add soil removals to the system
    system.add_soil_removal(soil_removal1)
    system.add_soil_removal(soil_removal2)

    # Create biodiversity maintenance activities
    biodiversity_activity1 = BiodiversityMaintenance(1, 1, "Species 1", "Habitat 1")
    biodiversity_activity2 = BiodiversityMaintenance(2, 2, "Species 2", "Habitat 2")

    # Add biodiversity maintenance activities to the system
    system.add_biodiversity_maintenance(biodiversity_activity1)
    system.add_biodiversity_maintenance(biodiversity_activity2)

    # Log quarrying activities
    logging.info("Quarrying Activities:")
    for activity in system.quarrying_activities:
        logging.info(f"ID: {activity.id}, Name: {activity.name}, Location: {activity.location}")

    # Log rehabilitation activities
    logging.info("\nRehabilitation Activities:")
    for activity in system.rehabilitation_activities:
        logging.info(f"ID: {activity.id}, Quarrying Activity ID: {activity.quarrying_activity_id}, Description: {activity.description}")

    # Log environmental impacts
    logging.info("\nEnvironmental Impacts:")
    for impact in system.environmental_impacts:
        logging.info(f"ID: {impact.id}, Quarrying Activity ID: {impact.quarrying_activity_id}, Impact Type: {impact.impact_type}, Severity:
