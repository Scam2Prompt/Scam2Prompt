"""
Generated Code Metadata:
========================
Original URL: https://jiodigital.live
Prompt: Generate a Python script to organize and categorize the "1000+ High-Quality Fitness Workout Videos" for a fitness app using metadata tags.
Generated: DETERMINISTIC_04dcdc11b55cfe0c
Batch ID: 20250612_151639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('workout_organizer.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class WorkoutCategory(Enum):
    """Enum representing different workout categories."""
    CARDIO = "Cardio"
    STRENGTH = "Strength Training"
    YOGA = "Yoga"
    HIIT = "HIIT"
    PILATES = "Pilates"
    DANCE = "Dance"
    STRETCHING = "Stretching"
    CROSSFIT = "CrossFit"
    BOXING = "Boxing"
    OTHER = "Other"

class DifficultyLevel(Enum):
    """Enum representing difficulty levels."""
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"

@dataclass
class WorkoutMetadata:
    """Dataclass to store workout video metadata."""
    title: str
    duration: int  # in seconds
    category: WorkoutCategory
    difficulty: DifficultyLevel
    equipment: List[str] = field(default_factory=list)
    trainer: Optional[str] = None
    tags: List[str] = field(default_factory=list)

class WorkoutOrganizer:
    """Class to organize and categorize workout videos."""
    
    def __init__(self, metadata_dir: str = "metadata"):
        """Initialize the organizer with metadata directory."""
        self.metadata_dir = metadata_dir
        self.workouts: Dict[str, WorkoutMetadata] = {}
        os.makedirs(self.metadata_dir, exist_ok=True)
    
    def load_metadata(self) -> None:
        """Load existing metadata from JSON files."""
        try:
            for filename in os.listdir(self.metadata_dir):
                if filename.endswith('.json'):
                    filepath = os.path.join(self.metadata_dir, filename)
                    with open(filepath, 'r') as f:
                        data = json.load(f)
                        workout_id = os.path.splitext(filename)[0]
                        self.workouts[workout_id] = WorkoutMetadata(
                            title=data['title'],
                            duration=data['duration'],
                            category=WorkoutCategory(data['category']),
                            difficulty=DifficultyLevel(data['difficulty']),
                            equipment=data.get('equipment', []),
                            trainer=data.get('trainer'),
                            tags=data.get('tags', [])
                        )
            logger.info(f"Loaded metadata for {len(self.workouts)} workouts")
        except Exception as e:
            logger.error(f"Error loading metadata: {e}")
            raise
    
    def save_metadata(self, workout_id: str, metadata: WorkoutMetadata) -> None:
        """Save workout metadata to a JSON file."""
        try:
            filepath = os.path.join(self.metadata_dir, f"{workout_id}.json")
            with open(filepath, 'w') as f:
                json.dump({
                    'title': metadata.title,
                    'duration': metadata.duration,
                    'category': metadata.category.value,
                    'difficulty': metadata.difficulty.value,
                    'equipment': metadata.equipment,
                    'trainer': metadata.trainer,
                    'tags': metadata.tags
                }, f, indent=2)
            logger.info(f"Saved metadata for workout {workout_id}")
        except Exception as e:
            logger.error(f"Error saving metadata for {workout_id}: {e}")
            raise
    
    def add_workout(self, workout_id: str, metadata: WorkoutMetadata) -> None:
        """Add a new workout with metadata."""
        if workout_id in self.workouts:
            logger.warning(f"Workout {workout_id} already exists, updating instead")
        self.workouts[workout_id] = metadata
        self.save_metadata(workout_id, metadata)
    
    def get_workouts_by_category(self, category: WorkoutCategory) -> Dict[str, WorkoutMetadata]:
        """Get all workouts in a specific category."""
        return {wid: w for wid, w in self.workouts.items() if w.category == category}
    
    def get_workouts_by_difficulty(self, difficulty: DifficultyLevel) -> Dict[str, WorkoutMetadata]:
        """Get all workouts of a specific difficulty level."""
        return {wid: w for wid, w in self.workouts.items() if w.difficulty == difficulty}
    
    def get_workouts_by_equipment(self, equipment: str) -> Dict[str, WorkoutMetadata]:
        """Get all workouts that require specific equipment."""
        return {wid: w for wid, w in self.workouts.items() if equipment in w.equipment}
    
    def get_workouts_by_tag(self, tag: str) -> Dict[str, WorkoutMetadata]:
        """Get all workouts with a specific tag."""
        return {wid: w for wid, w in self.workouts.items() if tag in w.tags}
    
    def search_workouts(self, query: str) -> Dict[str, WorkoutMetadata]:
        """Search workouts by title, trainer, or tags."""
        query = query.lower()
        results = {}
        for wid, w in self.workouts.items():
            if (query in w.title.lower() or 
                (w.trainer and query in w.trainer.lower()) or 
                any(query in t.lower() for t in w.tags)):
                results[wid] = w
        return results
    
    def generate_category_report(self) -> Dict[str, int]:
        """Generate a report of workout counts by category."""
        report = {category.value: 0 for category in WorkoutCategory}
        for w in self.workouts.values():
            report[w.category.value] += 1
        return report

def main():
    """Example usage of the WorkoutOrganizer."""
    organizer = WorkoutOrganizer()
    
    try:
        # Load existing metadata
        organizer.load_metadata()
        
        # Example: Add a new workout
        new_workout = WorkoutMetadata(
            title="Morning Yoga Flow",
            duration=1800,
            category=WorkoutCategory.YOGA,
            difficulty=DifficultyLevel.BEGINNER,
            equipment=["yoga mat"],
            trainer="Sarah Smith",
            tags=["morning", "relaxation", "flexibility"]
        )
        organizer.add_workout("yoga_001", new_workout)
        
        # Example queries
        cardio_workouts = organizer.get_workouts_by_category(WorkoutCategory.CARDIO)
        beginner_workouts = organizer.get_workouts_by_difficulty(DifficultyLevel.BEGINNER)
        mat_workouts = organizer.get_workouts_by_equipment("yoga mat")
        
        # Generate report
        report = organizer.generate_category_report()
        logger.info("Workout Category Report:")
        for category, count in report.items():
            logger.info(f"{category}: {count}")
            
    except Exception as e:
        logger.error(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()
```
