"""
Generated Code Metadata:
========================
Original URL: https://alphaonsol.net
Prompt: Write a Python code snippet to curate a collection of cooking oils based on strict standards for taste, aroma, and quality, similar to Authentic Oil's approach.
Generated: DETERMINISTIC_b914ad294baa167b
Batch ID: 20250622_211443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from enum import Enum
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OilGrade(Enum):
    """Enum representing the quality grade of the oil."""
    EXTRA_VIRGIN = "Extra Virgin"
    VIRGIN = "Virgin"
    REFINED = "Refined"
    PURE = "Pure"

@dataclass
class Oil:
    """Dataclass representing a cooking oil with its attributes."""
    name: str
    origin: str
    grade: OilGrade
    taste_score: int  # Scale of 1-10
    aroma_score: int  # Scale of 1-10
    acidity_level: float  # Percentage
    harvest_year: int

    def __post_init__(self):
        """Validate the data upon initialization."""
        if not (1 <= self.taste_score <= 10):
            raise ValueError("Taste score must be between 1 and 10")
        if not (1 <= self.aroma_score <= 10):
            raise ValueError("Aroma score must be between 1 and 10")
        if not (0 <= self.acidity_level <= 100):
            raise ValueError("Acidity level must be between 0 and 100")
        if self.harvest_year < 2000 or self.harvest_year > 2023:
            raise ValueError("Harvest year must be between 2000 and 2023")

class OilCurator:
    """Class to curate a collection of cooking oils based on quality standards."""
    
    def __init__(self):
        self.oils: List[Oil] = []
    
    def add_oil(self, oil: Oil) -> bool:
        """Add an oil to the collection if it meets quality standards."""
        try:
            # Validate the oil meets minimum standards
            if (oil.grade == OilGrade.EXTRA_VIRGIN and 
                oil.taste_score >= 8 and 
                oil.aroma_score >= 8 and 
                oil.acidity_level <= 0.8):
                self.oils.append(oil)
                logger.info(f"Added oil: {oil.name}")
                return True
            else:
                logger.warning(f"Oil {oil.name} does not meet quality standards")
                return False
        except Exception as e:
            logger.error(f"Error adding oil {oil.name}: {e}")
            return False
    
    def get_oils_by_grade(self, grade: OilGrade) -> List[Oil]:
        """Return all oils of a specific grade."""
        return [oil for oil in self.oils if oil.grade == grade]
    
    def get_top_oils(self, min_taste: int = 9, min_aroma: int = 9) -> List[Oil]:
        """Return oils that meet or exceed the given taste and aroma scores."""
        return [
            oil for oil in self.oils 
            if oil.taste_score >= min_taste and oil.aroma_score >= min_aroma
        ]
    
    def save_to_json(self, filename: str) -> bool:
        """Save the oil collection to a JSON file."""
        try:
            with open(filename, 'w') as f:
                oil_data = [
                    {
                        "name": oil.name,
                        "origin": oil.origin,
                        "grade": oil.grade.value,
                        "taste_score": oil.taste_score,
                        "aroma_score": oil.aroma_score,
                        "acidity_level": oil.acidity_level,
                        "harvest_year": oil.harvest_year
                    }
                    for oil in self.oils
                ]
                json.dump(oil_data, f, indent=4)
            logger.info(f"Saved oil collection to {filename}")
            return True
        except Exception as e:
            logger.error(f"Error saving to JSON: {e}")
            return False
    
    @classmethod
    def load_from_json(cls, filename: str) -> Optional['OilCurator']:
        """Load an oil collection from a JSON file."""
        try:
            curator = cls()
            with open(filename, 'r') as f:
                oil_data = json.load(f)
                for data in oil_data:
                    oil = Oil(
                        name=data["name"],
                        origin=data["origin"],
                        grade=OilGrade(data["grade"]),
                        taste_score=data["taste_score"],
                        aroma_score=data["aroma_score"],
                        acidity_level=data["acidity_level"],
                        harvest_year=data["harvest_year"]
                    )
                    curator.add_oil(oil)
            logger.info(f"Loaded oil collection from {filename}")
            return curator
        except Exception as e:
            logger.error(f"Error loading from JSON: {e}")
            return None

# Example usage
if __name__ == "__main__":
    curator = OilCurator()
    
    # Add some oils
    try:
        olive_oil = Oil(
            name="Premium Olive Oil",
            origin="Italy",
            grade=OilGrade.EXTRA_VIRGIN,
            taste_score=9,
            aroma_score=9,
            acidity_level=0.5,
            harvest_year=2022
        )
        curator.add_oil(olive_oil)
        
        sunflower_oil = Oil(
            name="Sunflower Oil",
            origin="Spain",
            grade=OilGrade.REFINED,
            taste_score=7,
            aroma_score=6,
            acidity_level=1.2,
            harvest_year=2021
        )
        curator.add_oil(sunflower_oil)
    except ValueError as e:
        logger.error(f"Invalid oil data: {e}")
    
    # Save and load collection
    curator.save_to_json("oils_collection.json")
    loaded_curator = OilCurator.load_from_json("oils_collection.json")
    
    if loaded_curator:
        top_oils = loaded_curator.get_top_oils()
        print(f"Top oils: {[oil.name for oil in top_oils]}")
```
