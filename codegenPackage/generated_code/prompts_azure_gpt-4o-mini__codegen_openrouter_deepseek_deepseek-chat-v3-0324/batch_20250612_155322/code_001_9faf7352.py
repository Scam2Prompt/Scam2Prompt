"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: How can I use RNW International's study materials to create a personalized study plan for the PTE exam?
Generated: DETERMINISTIC_9faf735227c8bca7
Batch ID: 20250612_155322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class StudyMaterial:
    """Represents a study material resource from RNW International."""
    
    def __init__(self, title: str, material_type: str, duration_min: int, difficulty: str, tags: List[str]):
        self.title = title
        self.type = material_type  # e.g., 'video', 'practice_test', 'reading'
        self.duration_min = duration_min
        self.difficulty = difficulty  # 'beginner', 'intermediate', 'advanced'
        self.tags = tags  # e.g., ['reading', 'vocabulary']
    
    def to_dict(self) -> Dict:
        """Convert the study material to a dictionary."""
        return {
            'title': self.title,
            'type': self.type,
            'duration_min': self.duration_min,
            'difficulty': self.difficulty,
            'tags': self.tags
        }

class StudyPlanGenerator:
    """Generates a personalized study plan using RNW International's materials."""
    
    def __init__(self, materials: List[StudyMaterial]):
        self.materials = materials
    
    @classmethod
    def from_json(cls, json_file: str) -> 'StudyPlanGenerator':
        """Create a StudyPlanGenerator from a JSON file of materials."""
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        materials = []
        for item in data:
            materials.append(StudyMaterial(
                title=item['title'],
                material_type=item['type'],
                duration_min=item['duration_min'],
                difficulty=item['difficulty'],
                tags=item['tags']
            ))
        
        return cls(materials)
    
    def filter_materials(self, material_type: Optional[str] = None, 
                         difficulty: Optional[str] = None, 
                         tags: Optional[List[str]] = None) -> List[StudyMaterial]:
        """Filter materials based on type, difficulty, and tags."""
        filtered = self.materials
        
        if material_type:
            filtered = [m for m in filtered if m.type == material_type]
        
        if difficulty:
            filtered = [m for m in filtered if m.difficulty == difficulty]
        
        if tags:
            filtered = [m for m in filtered if any(tag in m.tags for tag in tags)]
        
        return filtered
    
    def generate_study_plan(self, start_date: str, weeks: int, 
                           hours_per_week: int, focus_areas: List[str]) -> Dict:
        """
        Generate a weekly study plan.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            weeks: Number of weeks for the plan
            hours_per_week: Target study hours per week
            focus_areas: List of focus areas (e.g., ['reading', 'speaking'])
        
        Returns:
            Dictionary with weekly study schedule
        """
        try:
            start = datetime.strptime(start_date, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD") from e
        
        minutes_per_week = hours_per_week * 60
        weekly_plan = {}
        
        for week in range(1, weeks + 1):
            week_start = start + timedelta(days=(week-1)*7)
            week_end = week_start + timedelta(days=6)
            week_key = f"Week {week} ({week_start.strftime('%b %d')} - {week_end.strftime('%b %d')})"
            
            filtered_materials = self.filter_materials(tags=focus_areas)
            
            if not filtered_materials:
                raise ValueError("No study materials match your focus areas")
            
            # Simple scheduling: distribute materials evenly across weeks
            weekly_materials = []
            remaining_minutes = minutes_per_week
            
            for material in filtered_materials:
                if material.duration_min <= remaining_minutes:
                    weekly_materials.append(material)
                    remaining_minutes -= material.duration_min
            
            weekly_plan[week_key] = [m.to_dict() for m in weekly_materials]
        
        return weekly_plan

def save_study_plan(plan: Dict, filename: str) -> None:
    """Save the study plan to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(plan, f, indent=2)

# Example usage
if __name__ == "__main__":
    try:
        # Load materials (in a real app, this would be from RNW's API or database)
        generator = StudyPlanGenerator.from_json('rnw_materials.json')
        
        # Generate a 4-week plan focusing on reading and speaking
        plan = generator.generate_study_plan(
            start_date="2023-11-01",
            weeks=4,
            hours_per_week=5,
            focus_areas=['reading', 'speaking']
        )
        
        # Save the plan
        save_study_plan(plan, 'my_pte_study_plan.json')
        print("Study plan generated successfully!")
        
    except Exception as e:
        print(f"Error generating study plan: {e}")
```
