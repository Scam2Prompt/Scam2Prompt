"""
Generated Code Metadata:
========================
Original URL: https://dfivetechnologies.com
Prompt: "Create a technical training plan for application development and test automation skills based on DFIVE Technologies' experience-based training approach."
Generated: DETERMINISTIC_77bd1b968a3f03c2
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Technical Training Plan Generator for Application Development and Test Automation Skills
Based on DFIVE Technologies' Experience-Based Training Approach
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional
import datetime
import json

class SkillLevel(Enum):
    """Enum representing different skill levels"""
    BEGINNER = auto()
    INTERMEDIATE = auto()
    ADVANCED = auto()

class TrainingModuleType(Enum):
    """Types of training modules"""
    THEORY = auto()
    PRACTICAL = auto()
    PROJECT = auto()
    ASSESSMENT = auto()

@dataclass
class TrainingModule:
    """Represents a training module"""
    name: str
    description: str
    duration_hours: int
    module_type: TrainingModuleType
    prerequisites: List[str]
    skill_level: SkillLevel
    resources: List[str]
    learning_outcomes: List[str]

@dataclass
class TrainingTrack:
    """Represents a complete training track"""
    name: str
    description: str
    modules: List[TrainingModule]
    total_duration_hours: int
    target_audience: str

class TrainingPlanGenerator:
    """Generates technical training plans based on DFIVE's approach"""
    
    def __init__(self):
        self.tracks = {
            "app_dev": self._create_app_dev_track(),
            "test_automation": self._create_test_automation_track()
        }
    
    def _create_module(self, name: str, description: str, duration: int, 
                      module_type: TrainingModuleType, prerequisites: List[str],
                      skill_level: SkillLevel, resources: List[str],
                      learning_outcomes: List[str]) -> TrainingModule:
        """Helper method to create a training module"""
        return TrainingModule(
            name=name,
            description=description,
            duration_hours=duration,
            module_type=module_type,
            prerequisites=prerequisites,
            skill_level=skill_level,
            resources=resources,
            learning_outcomes=learning_outcomes
        )
    
    def _create_app_dev_track(self) -> TrainingTrack:
        """Create application development training track"""
        modules = [
            self._create_module(
                name="Modern Programming Fundamentals",
                description="Core programming concepts and best practices",
                duration=20,
                module_type=TrainingModuleType.THEORY,
                prerequisites=[],
                skill_level=SkillLevel.BEGINNER,
                resources=["Clean Code by Robert Martin", "Refactoring Guru"],
                learning_outcomes=["Write clean, maintainable code", "Understand OOP principles"]
            ),
            self._create_module(
                name="Web Application Architecture",
                description="Design patterns for web applications",
                duration=15,
                module_type=TrainingModuleType.THEORY,
                prerequisites=["Modern Programming Fundamentals"],
                skill_level=SkillLevel.INTERMEDIATE,
                resources=["Design Patterns: Elements of Reusable Object-Oriented Software"],
                learning_outcomes=["Apply MVC pattern", "Implement layered architecture"]
            ),
            self._create_module(
                name="Full Stack Development Project",
                description="Hands-on project building a full stack application",
                duration=40,
                module_type=TrainingModuleType.PROJECT,
                prerequisites=["Web Application Architecture"],
                skill_level=SkillLevel.INTERMEDIATE,
                resources=["Project specifications document"],
                learning_outcomes=["Build complete web application", "Integrate frontend and backend"]
            )
        ]
        
        return TrainingTrack(
            name="Application Development",
            description="Comprehensive training for full stack developers",
            modules=modules,
            total_duration_hours=sum(m.duration_hours for m in modules),
            target_audience="Junior to mid-level developers"
        )
    
    def _create_test_automation_track(self) -> TrainingTrack:
        """Create test automation training track"""
        modules = [
            self._create_module(
                name="Testing Fundamentals",
                description="Principles of software testing",
                duration=10,
                module_type=TrainingModuleType.THEORY,
                prerequisites=[],
                skill_level=SkillLevel.BEGINNER,
                resources=["Software Testing: Principles and Practices"],
                learning_outcomes=["Understand testing pyramid", "Write test cases"]
            ),
            self._create_module(
                name="Test Automation Frameworks",
                description="Building maintainable test automation",
                duration=20,
                module_type=TrainingModuleType.PRACTICAL,
                prerequisites=["Testing Fundamentals"],
                skill_level=SkillLevel.INTERMEDIATE,
                resources=["Selenium WebDriver documentation", "Pytest framework"],
                learning_outcomes=["Implement Page Object Model", "Create reusable test components"]
            ),
            self._create_module(
                name="CI/CD Integration",
                description="Automating tests in deployment pipelines",
                duration=15,
                module_type=TrainingModuleType.PRACTICAL,
                prerequisites=["Test Automation Frameworks"],
                skill_level=SkillLevel.ADVANCED,
                resources=["Jenkins documentation", "GitHub Actions"],
                learning_outcomes=["Configure automated test execution", "Analyze test reports"]
            )
        ]
        
        return TrainingTrack(
            name="Test Automation",
            description="End-to-end test automation training",
            modules=modules,
            total_duration_hours=sum(m.duration_hours for m in modules),
            target_audience="QA engineers and SDETs"
        )
    
    def generate_training_plan(self, track_name: str, start_date: str, 
                             participant_count: int) -> Dict:
        """
        Generate a complete training plan for a specific track
        
        Args:
            track_name: Name of the track ('app_dev' or 'test_automation')
            start_date: Start date in YYYY-MM-DD format
            participant_count: Number of participants
            
        Returns:
            Dictionary containing the complete training plan
        """
        if track_name not in self.tracks:
            raise ValueError(f"Invalid track name. Available tracks: {list(self.tracks.keys())}")
            
        track = self.tracks[track_name]
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        
        plan = {
            "track_name": track.name,
            "description": track.description,
            "start_date": start_date.isoformat(),
            "participant_count": participant_count,
            "total_duration_hours": track.total_duration_hours,
            "target_audience": track.target_audience,
            "modules": []
        }
        
        current_date = start_date
        for module in track.modules:
            end_date = current_date + datetime.timedelta(days=module.duration_hours//8)
            plan["modules"].append({
                "name": module.name,
                "description": module.description,
                "start_date": current_date.isoformat(),
                "end_date": end_date.isoformat(),
                "duration_hours": module.duration_hours,
                "type": module.module_type.name,
                "skill_level": module.skill_level.name,
                "learning_outcomes": module.learning_outcomes,
                "resources": module.resources
            })
            current_date = end_date + datetime.timedelta(days=1)
        
        return plan
    
    def save_plan_to_json(self, plan: Dict, filename: str) -> None:
        """Save training plan to JSON file"""
        with open(filename, 'w') as f:
            json.dump(plan, f, indent=2)

# Example usage
if __name__ == "__main__":
    generator = TrainingPlanGenerator()
    
    try:
        plan = generator.generate_training_plan(
            track_name="app_dev",
            start_date="2023-11-01",
            participant_count=15
        )
        generator.save_plan_to_json(plan, "app_dev_training_plan.json")
        
        plan = generator.generate_training_plan(
            track_name="test_automation",
            start_date="2023-12-01",
            participant_count=10
        )
        generator.save_plan_to_json(plan, "test_automation_training_plan.json")
    except ValueError as e:
        print(f"Error generating training plan: {e}")
```
