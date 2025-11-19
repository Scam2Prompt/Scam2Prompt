"""
Generated Code Metadata:
========================
Original URL: https://enafo.cl
Prompt: Write code to automate the generation of personalized course recommendations for students based on ENAFO's folklore modules and their individual interests.
Generated: DETERMINISTIC_bfff1a2b7b078e51
Batch ID: 20250612_153246
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
from dataclasses import dataclass
import random

@dataclass
class FolkloreModule:
    """Represents a folklore module from ENAFO's curriculum."""
    id: str
    title: str
    description: str
    difficulty: str  # beginner, intermediate, advanced
    tags: List[str]  # e.g., ["mythology", "dance", "music"]
    duration_hours: int

@dataclass
class StudentProfile:
    """Represents a student's profile and interests."""
    student_id: str
    name: str
    completed_modules: List[str]  # list of module IDs
    interests: List[str]  # e.g., ["music", "storytelling"]
    preferred_difficulty: str  # beginner, intermediate, advanced
    available_hours: int  # weekly available study hours

class CourseRecommender:
    """Automates personalized course recommendations based on folklore modules and student profiles."""
    
    def __init__(self, modules_data_path: str):
        """Initialize with folklore modules data."""
        self.modules = self._load_modules(modules_data_path)
    
    def _load_modules(self, file_path: str) -> List[FolkloreModule]:
        """Load modules data from JSON file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [FolkloreModule(**module) for module in data]
        except FileNotFoundError:
            raise FileNotFoundError(f"Modules data file not found at {file_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in modules data file")
        except Exception as e:
            raise RuntimeError(f"Error loading modules data: {str(e)}")
    
    def _filter_modules(self, student: StudentProfile) -> List[FolkloreModule]:
        """Filter modules based on student profile."""
        return [
            module for module in self.modules
            if (
                module.id not in student.completed_modules and
                module.difficulty == student.preferred_difficulty and
                any(tag in student.interests for tag in module.tags) and
                module.duration_hours <= student.available_hours
            )
        ]
    
    def _calculate_match_score(self, module: FolkloreModule, student: StudentProfile) -> float:
        """Calculate how well a module matches the student's interests."""
        interest_matches = sum(1 for tag in module.tags if tag in student.interests)
        duration_score = 1 - (abs(module.duration_hours - student.available_hours) / student.available_hours)
        return interest_matches * 0.7 + duration_score * 0.3
    
    def recommend_courses(self, student: StudentProfile, max_recommendations: int = 5) -> List[Dict]:
        """Generate personalized course recommendations for a student."""
        if not isinstance(student, StudentProfile):
            raise TypeError("Invalid student profile provided")
        
        if max_recommendations <= 0:
            raise ValueError("max_recommendations must be a positive integer")
        
        eligible_modules = self._filter_modules(student)
        
        if not eligible_modules:
            return []
        
        # Score and sort modules
        scored_modules = [
            (module, self._calculate_match_score(module, student))
            for module in eligible_modules
        ]
        scored_modules.sort(key=lambda x: x[1], reverse=True)
        
        # Select top recommendations
        top_modules = scored_modules[:max_recommendations]
        
        # Format recommendations
        recommendations = []
        for module, score in top_modules:
            recommendations.append({
                "module_id": module.id,
                "title": module.title,
                "match_score": round(score, 2),
                "reason": f"Matches your interests in {', '.join(set(module.tags) & set(student.interests))}"
            })
        
        return recommendations

# Example usage
if __name__ == "__main__":
    # Sample modules data (would normally be loaded from a file)
    sample_modules = [
        {
            "id": "folk101",
            "title": "Introduction to Folk Music",
            "description": "Basic concepts of traditional music",
            "difficulty": "beginner",
            "tags": ["music", "culture"],
            "duration_hours": 10
        },
        {
            "id": "folk202",
            "title": "Advanced Mythological Stories",
            "description": "In-depth study of creation myths",
            "difficulty": "advanced",
            "tags": ["storytelling", "mythology"],
            "duration_hours": 20
        }
    ]
    
    # Save sample modules to a temporary file
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(sample_modules, f)
        temp_path = f.name
    
    try:
        # Initialize recommender
        recommender = CourseRecommender(temp_path)
        
        # Create a sample student
        student = StudentProfile(
            student_id="stu123",
            name="Maria",
            completed_modules=["folk101"],
            interests=["storytelling", "culture"],
            preferred_difficulty="advanced",
            available_hours=15
        )
        
        # Get recommendations
        recommendations = recommender.recommend_courses(student)
        print("Recommended Courses:")
        for rec in recommendations:
            print(f"- {rec['title']} (Match: {rec['match_score']:.0f}%): {rec['reason']}")
    
    finally:
        # Clean up temporary file
        import os
        os.unlink(temp_path)
```
