"""
Generated Code Metadata:
========================
Original URL: https://happyscholarsacademy.com
Prompt: Develop a library function that generates a list of activities for preschool-aged children, focusing on educational and social development, based on the curriculum at Happy Scholars Academy.
Generated: DETERMINISTIC_488d22442f0f4c08
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Optional

class ActivityGenerator:
    """
    A library to generate educational and social development activities for preschool-aged children.
    Based on the curriculum at Happy Scholars Academy.
    """
    
    def __init__(self):
        """
        Initialize the activity generator with predefined activity categories and examples.
        """
        self.categories = {
            'language_development': [
                "Storytelling with picture cards",
                "Alphabet matching game",
                "Rhyming word bingo",
                "Name writing practice",
                "Vocabulary scavenger hunt"
            ],
            'math_concepts': [
                "Counting with blocks",
                "Shape sorting activity",
                "Pattern recognition with beads",
                "Number hopscotch",
                "Simple measuring with non-standard units"
            ],
            'social_skills': [
                "Role-playing different community helpers",
                "Turn-taking board games",
                "Emotion charades",
                "Collaborative art project",
                "Group storytelling"
            ],
            'science_exploration': [
                "Sink or float experiment",
                "Nature walk with observation journal",
                "Planting seeds and tracking growth",
                "Magnet exploration",
                "Weather charting"
            ],
            'fine_motor': [
                "Playdough letter formation",
                "Bead threading",
                "Scissor skills practice",
                "Puzzle solving",
                "Tweezer transfer activities"
            ],
            'gross_motor': [
                "Obstacle course",
                "Dance freeze game",
                "Balloon volleyball",
                "Animal movement imitation",
                "Balance beam walking"
            ]
        }
        
        self.difficulty_levels = {
            'easy': 1,
            'medium': 2,
            'hard': 3
        }
    
    def generate_activities(
        self,
        category: Optional[str] = None,
        difficulty: Optional[str] = None,
        num_activities: int = 5
    ) -> List[Dict[str, str]]:
        """
        Generate a list of activities based on specified criteria.
        
        Args:
            category: The developmental category (e.g., 'language_development')
            difficulty: The difficulty level ('easy', 'medium', 'hard')
            num_activities: Number of activities to generate (default: 5)
            
        Returns:
            List of dictionaries containing activity details
            
        Raises:
            ValueError: If invalid category or difficulty is provided
        """
        # Validate inputs
        if category and category not in self.categories:
            raise ValueError(f"Invalid category. Must be one of: {list(self.categories.keys())}")
            
        if difficulty and difficulty not in self.difficulty_levels:
            raise ValueError(f"Invalid difficulty. Must be one of: {list(self.difficulty_levels.keys())}")
            
        if num_activities <= 0:
            raise ValueError("Number of activities must be positive")
        
        # Select activities from specified category or all categories
        pool = []
        if category:
            pool = self.categories[category]
        else:
            for activities in self.categories.values():
                pool.extend(activities)
        
        # Randomly sample activities
        selected_activities = random.sample(pool, min(num_activities, len(pool)))
        
        # Prepare result with metadata
        result = []
        for activity in selected_activities:
            activity_data = {
                'activity': activity,
                'category': self._determine_category(activity),
                'difficulty': difficulty if difficulty else self._assign_random_difficulty()
            }
            result.append(activity_data)
            
        return result
    
    def _determine_category(self, activity: str) -> str:
        """
        Determine which category an activity belongs to.
        
        Args:
            activity: The activity name
            
        Returns:
            The category name
        """
        for category, activities in self.categories.items():
            if activity in activities:
                return category
        return 'unknown'
    
    def _assign_random_difficulty(self) -> str:
        """
        Randomly assign a difficulty level to an activity.
        
        Returns:
            Random difficulty level ('easy', 'medium', or 'hard')
        """
        return random.choice(list(self.difficulty_levels.keys()))
    
    def get_activity_categories(self) -> List[str]:
        """
        Get the list of available activity categories.
        
        Returns:
            List of category names
        """
        return list(self.categories.keys())
    
    def get_difficulty_levels(self) -> List[str]:
        """
        Get the list of available difficulty levels.
        
        Returns:
            List of difficulty levels
        """
        return list(self.difficulty_levels.keys())

# Example usage
if __name__ == "__main__":
    generator = ActivityGenerator()
    
    # Generate 3 random activities from all categories
    print("Random activities:")
    for activity in generator.generate_activities(num_activities=3):
        print(f"- {activity['activity']} ({activity['category']}, {activity['difficulty']})")
    
    # Generate 2 language development activities
    print("\nLanguage development activities:")
    for activity in generator.generate_activities(category='language_development', num_activities=2):
        print(f"- {activity['activity']} ({activity['difficulty']})")
```
