"""
Generated Code Metadata:
========================
Original URL: https://www.spanishupdate.com
Prompt: Write a Python script to recommend Spanish language classes for foreigners based on their proficiency level, using the structure described on the "Clases de Español para Extranjeros" page of SpanishUpdate.com.
Generated: DETERMINISTIC_a6f3296c7ad0a1e3
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, List, Optional

class ProficiencyLevel(Enum):
    """Enum representing Spanish language proficiency levels."""
    BEGINNER = "Beginner (A1)"
    ELEMENTARY = "Elementary (A2)"
    INTERMEDIATE = "Intermediate (B1)"
    UPPER_INTERMEDIATE = "Upper Intermediate (B2)"
    ADVANCED = "Advanced (C1)"
    PROFICIENCY = "Proficiency (C2)"

class SpanishClass:
    """Represents a Spanish language class with its details."""
    
    def __init__(
        self,
        name: str,
        level: ProficiencyLevel,
        description: str,
        duration: str,
        schedule: List[str],
        price: str,
        features: List[str]
    ):
        self.name = name
        self.level = level
        self.description = description
        self.duration = duration
        self.schedule = schedule
        self.price = price
        self.features = features
    
    def to_dict(self) -> Dict:
        """Convert class details to dictionary for easy serialization."""
        return {
            "name": self.name,
            "level": self.level.value,
            "description": self.description,
            "duration": self.duration,
            "schedule": self.schedule,
            "price": self.price,
            "features": self.features
        }

class SpanishClassRecommender:
    """Recommends Spanish classes based on user's proficiency level."""
    
    def __init__(self, classes_data_file: Optional[str] = None):
        """Initialize with optional data file path."""
        self.classes = []
        if classes_data_file:
            self.load_classes_from_file(classes_data_file)
        else:
            self.load_default_classes()
    
    def load_default_classes(self) -> None:
        """Load default set of Spanish classes."""
        self.classes = [
            SpanishClass(
                name="Spanish Basics",
                level=ProficiencyLevel.BEGINNER,
                description="Introduction to Spanish language and basic communication skills.",
                duration="8 weeks",
                schedule=["Mon/Wed 6-8pm", "Sat 10am-12pm"],
                price="$199",
                features=["Small groups", "Native teachers", "Interactive materials"]
            ),
            SpanishClass(
                name="Elementary Spanish",
                level=ProficiencyLevel.ELEMENTARY,
                description="Build on basic knowledge with more vocabulary and grammar.",
                duration="10 weeks",
                schedule=["Tue/Thu 6-8pm", "Sat 1-3pm"],
                price="$249",
                features=["Conversation practice", "Cultural insights", "Homework support"]
            ),
            SpanishClass(
                name="Intermediate Conversation",
                level=ProficiencyLevel.INTERMEDIATE,
                description="Improve fluency and confidence in everyday conversations.",
                duration="12 weeks",
                schedule=["Mon/Wed 7-9pm", "Sun 11am-1pm"],
                price="$299",
                features=["Role-playing", "Debates", "Media analysis"]
            ),
            SpanishClass(
                name="Advanced Grammar",
                level=ProficiencyLevel.UPPER_INTERMEDIATE,
                description="Master complex grammar structures and formal writing.",
                duration="10 weeks",
                schedule=["Tue/Thu 5-7pm"],
                price="$349",
                features=["Writing workshops", "Grammar drills", "Error correction"]
            ),
            SpanishClass(
                name="Business Spanish",
                level=ProficiencyLevel.ADVANCED,
                description="Specialized vocabulary for professional environments.",
                duration="8 weeks",
                schedule=["Mon/Fri 6-8pm"],
                price="$399",
                features=["Case studies", "Presentations", "Networking practice"]
            ),
            SpanishClass(
                name="Mastery Program",
                level=ProficiencyLevel.PROFICIENCY,
                description="Achieve native-like fluency in all contexts.",
                duration="16 weeks",
                schedule=["Flexible hours"],
                price="$599",
                features=["Personalized coaching", "Literature analysis", "Media production"]
            )
        ]
    
    def load_classes_from_file(self, file_path: str) -> None:
        """Load classes data from a JSON file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.classes = [
                    SpanishClass(
                        name=item["name"],
                        level=ProficiencyLevel(item["level"]),
                        description=item["description"],
                        duration=item["duration"],
                        schedule=item["schedule"],
                        price=item["price"],
                        features=item["features"]
                    ) for item in data
                ]
        except FileNotFoundError:
            print(f"Warning: File {file_path} not found. Loading default classes.")
            self.load_default_classes()
        except json.JSONDecodeError:
            print(f"Warning: Invalid JSON in {file_path}. Loading default classes.")
            self.load_default_classes()
        except KeyError as e:
            print(f"Warning: Missing required field {e} in data file. Loading default classes.")
            self.load_default_classes()
    
    def recommend_classes(self, level: ProficiencyLevel) -> List[Dict]:
        """Recommend classes for a given proficiency level."""
        recommended = [c for c in self.classes if c.level == level]
        if not recommended:
            print(f"No classes found for level {level.value}. Showing all available classes.")
            return [c.to_dict() for c in self.classes]
        return [c.to_dict() for c in recommended]
    
    def list_all_levels(self) -> List[str]:
        """List all available proficiency levels."""
        return [level.value for level in ProficiencyLevel]

def get_user_proficiency() -> ProficiencyLevel:
    """Prompt user to select their proficiency level."""
    print("Please select your Spanish proficiency level:")
    for i, level in enumerate(ProficiencyLevel, 1):
        print(f"{i}. {level.value}")
    
    while True:
        try:
            choice = int(input("Enter the number corresponding to your level: "))
            if 1 <= choice <= len(ProficiencyLevel):
                return list(ProficiencyLevel)[choice - 1]
            print("Invalid choice. Please enter a number between 1 and", len(ProficiencyLevel))
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main function to run the class recommender."""
    print("Welcome to Spanish Class Recommender!")
    print("We'll help you find the perfect Spanish class based on your level.\n")
    
    recommender = SpanishClassRecommender()
    user_level = get_user_proficiency()
    
    print(f"\nRecommended classes for {user_level.value} level:")
    recommended_classes = recommender.recommend_classes(user_level)
    
    for i, class_info in enumerate(recommended_classes, 1):
        print(f"\n{i}. {class_info['name']}")
        print(f"   Description: {class_info['description']}")
        print(f"   Duration: {class_info['duration']}")
        print(f"   Schedule: {', '.join(class_info['schedule'])}")
        print(f"   Price: {class_info['price']}")
        print(f"   Features: {', '.join(class_info['features'])}")

if __name__ == "__main__":
    main()
```
