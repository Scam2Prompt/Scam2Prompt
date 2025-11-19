"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: Develop a script to organize and display school achievements, such as sports medals and academic awards, similar to the "News & Events" section on the Deepti Convent Higher Secondary School website.
Generated: DETERMINISTIC_8cb37810a3223bc2
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from typing import List, Dict, Optional

class Achievement:
    """Class to represent a single achievement entry."""
    
    def __init__(self, title: str, description: str, date: str, category: str, image_path: Optional[str] = None):
        """
        Initialize an Achievement object.
        
        Args:
            title (str): Title of the achievement
            description (str): Description of the achievement
            date (str): Date of achievement in YYYY-MM-DD format
            category (str): Category (e.g., 'sports', 'academic')
            image_path (Optional[str]): Path to achievement image (optional)
        """
        self.title = title
        self.description = description
        self.date = date
        self.category = category
        self.image_path = image_path
        
    def to_dict(self) -> Dict:
        """Convert Achievement object to dictionary."""
        return {
            'title': self.title,
            'description': self.description,
            'date': self.date,
            'category': self.category,
            'image_path': self.image_path
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Achievement':
        """Create Achievement object from dictionary."""
        return cls(
            title=data['title'],
            description=data['description'],
            date=data['date'],
            category=data['category'],
            image_path=data.get('image_path')
        )

class AchievementManager:
    """Class to manage school achievements."""
    
    def __init__(self, storage_file: str = 'achievements.json'):
        """
        Initialize AchievementManager.
        
        Args:
            storage_file (str): Path to JSON file for storing achievements
        """
        self.storage_file = storage_file
        self.achievements: List[Achievement] = []
        self._load_achievements()
    
    def _load_achievements(self) -> None:
        """Load achievements from storage file."""
        try:
            if os.path.exists(self.storage_file):
                with open(self.storage_file, 'r') as f:
                    data = json.load(f)
                    self.achievements = [Achievement.from_dict(item) for item in data]
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading achievements: {e}")
            self.achievements = []
    
    def _save_achievements(self) -> None:
        """Save achievements to storage file."""
        try:
            with open(self.storage_file, 'w') as f:
                json.dump([a.to_dict() for a in self.achievements], f, indent=2)
        except IOError as e:
            print(f"Error saving achievements: {e}")
    
    def add_achievement(self, achievement: Achievement) -> None:
        """Add a new achievement."""
        try:
            # Validate date format
            datetime.strptime(achievement.date, '%Y-%m-%d')
            self.achievements.append(achievement)
            self._save_achievements()
        except ValueError as e:
            print(f"Invalid date format (YYYY-MM-DD required): {e}")
    
    def get_achievements(self, category: Optional[str] = None, limit: Optional[int] = None) -> List[Achievement]:
        """
        Get achievements, optionally filtered by category and limited in number.
        
        Args:
            category (Optional[str]): Filter by category (e.g., 'sports')
            limit (Optional[int]): Maximum number of achievements to return
            
        Returns:
            List[Achievement]: List of filtered achievements
        """
        achievements = self.achievements
        
        if category:
            achievements = [a for a in achievements if a.category.lower() == category.lower()]
        
        # Sort by date (newest first)
        achievements.sort(key=lambda x: x.date, reverse=True)
        
        if limit:
            achievements = achievements[:limit]
            
        return achievements
    
    def display_achievements(self, category: Optional[str] = None, limit: Optional[int] = 5) -> None:
        """Display achievements in a formatted way."""
        achievements = self.get_achievements(category, limit)
        
        if not achievements:
            print("No achievements found.")
            return
            
        print("\n=== School Achievements ===")
        if category:
            print(f"Category: {category.title()}")
        print("---------------------------")
        
        for achievement in achievements:
            print(f"\nTitle: {achievement.title}")
            print(f"Date: {achievement.date}")
            print(f"Category: {achievement.category.title()}")
            print(f"Description: {achievement.description}")
            if achievement.image_path:
                print(f"Image: {achievement.image_path}")
            print("---------------------------")

def main():
    """Main function to demonstrate the AchievementManager."""
    manager = AchievementManager()
    
    # Sample usage
    while True:
        print("\nSchool Achievements Management")
        print("1. Add New Achievement")
        print("2. View All Achievements")
        print("3. View Sports Achievements")
        print("4. View Academic Achievements")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            print("\nAdd New Achievement")
            title = input("Title: ")
            description = input("Description: ")
            date = input("Date (YYYY-MM-DD): ")
            category = input("Category (sports/academic/other): ")
            image_path = input("Image path (optional, press Enter to skip): ")
            
            if not image_path:
                image_path = None
                
            try:
                achievement = Achievement(title, description, date, category, image_path)
                manager.add_achievement(achievement)
                print("Achievement added successfully!")
            except Exception as e:
                print(f"Error adding achievement: {e}")
                
        elif choice == '2':
            manager.display_achievements()
            
        elif choice == '3':
            manager.display_achievements(category='sports')
            
        elif choice == '4':
            manager.display_achievements(category='academic')
            
        elif choice == '5':
            print("Exiting...")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
