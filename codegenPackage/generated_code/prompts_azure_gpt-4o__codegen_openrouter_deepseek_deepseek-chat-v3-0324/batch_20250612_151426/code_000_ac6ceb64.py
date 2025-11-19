"""
Generated Code Metadata:
========================
Original URL: https://myneel.com
Prompt: Write Python code to simulate a calorie tracking system similar to the one described on Neel's AI weight loss assistant website. Include features like food input, calorie calculation, and daily summaries.
Generated: DETERMINISTIC_ac6ceb64442f15c8
Batch ID: 20250612_151426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import List, Dict, Optional

class FoodItem:
    """Represents a food item with its nutritional information."""
    
    def __init__(self, name: str, calories: float, protein: float = 0, carbs: float = 0, fat: float = 0):
        """
        Initialize a food item.
        
        Args:
            name: Name of the food item
            calories: Calories per serving
            protein: Protein in grams per serving (optional)
            carbs: Carbohydrates in grams per serving (optional)
            fat: Fat in grams per serving (optional)
        """
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
    
    def to_dict(self) -> Dict:
        """Convert food item to dictionary for serialization."""
        return {
            'name': self.name,
            'calories': self.calories,
            'protein': self.protein,
            'carbs': self.carbs,
            'fat': self.fat
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'FoodItem':
        """Create food item from dictionary."""
        return cls(
            name=data['name'],
            calories=data['calories'],
            protein=data.get('protein', 0),
            carbs=data.get('carbs', 0),
            fat=data.get('fat', 0)
        )

class MealEntry:
    """Represents a meal entry containing multiple food items."""
    
    def __init__(self, name: str, food_items: List[FoodItem] = None):
        """
        Initialize a meal entry.
        
        Args:
            name: Name of the meal (e.g., 'Breakfast', 'Lunch')
            food_items: List of food items in the meal (optional)
        """
        self.name = name
        self.food_items = food_items if food_items else []
    
    def add_food_item(self, food_item: FoodItem) -> None:
        """Add a food item to the meal."""
        self.food_items.append(food_item)
    
    def total_nutrition(self) -> Dict[str, float]:
        """Calculate total nutrition for the meal."""
        totals = {
            'calories': 0,
            'protein': 0,
            'carbs': 0,
            'fat': 0
        }
        
        for item in self.food_items:
            totals['calories'] += item.calories
            totals['protein'] += item.protein
            totals['carbs'] += item.carbs
            totals['fat'] += item.fat
        
        return totals
    
    def to_dict(self) -> Dict:
        """Convert meal entry to dictionary for serialization."""
        return {
            'name': self.name,
            'food_items': [item.to_dict() for item in self.food_items]
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'MealEntry':
        """Create meal entry from dictionary."""
        return cls(
            name=data['name'],
            food_items=[FoodItem.from_dict(item) for item in data['food_items']]
        )

class DailyLog:
    """Represents a day's worth of food consumption."""
    
    def __init__(self, date: datetime.date = None, meals: List[MealEntry] = None):
        """
        Initialize a daily log.
        
        Args:
            date: Date of the log (defaults to today)
            meals: List of meal entries (optional)
        """
        self.date = date if date else datetime.date.today()
        self.meals = meals if meals else []
    
    def add_meal(self, meal: MealEntry) -> None:
        """Add a meal to the daily log."""
        self.meals.append(meal)
    
    def total_nutrition(self) -> Dict[str, float]:
        """Calculate total nutrition for the day."""
        totals = {
            'calories': 0,
            'protein': 0,
            'carbs': 0,
            'fat': 0
        }
        
        for meal in self.meals:
            meal_totals = meal.total_nutrition()
            for key in totals:
                totals[key] += meal_totals[key]
        
        return totals
    
    def to_dict(self) -> Dict:
        """Convert daily log to dictionary for serialization."""
        return {
            'date': self.date.isoformat(),
            'meals': [meal.to_dict() for meal in self.meals]
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'DailyLog':
        """Create daily log from dictionary."""
        return cls(
            date=datetime.date.fromisoformat(data['date']),
            meals=[MealEntry.from_dict(meal) for meal in data['meals']]
        )

class CalorieTracker:
    """Main class for the calorie tracking system."""
    
    def __init__(self, data_file: str = 'calorie_tracker_data.json'):
        """
        Initialize the calorie tracker.
        
        Args:
            data_file: Path to the data file for persistence (optional)
        """
        self.data_file = data_file
        self.daily_logs: Dict[str, DailyLog] = {}  # key: ISO date string
        self.load_data()
    
    def add_food_to_meal(self, date: datetime.date, meal_name: str, food_item: FoodItem) -> None:
        """
        Add a food item to a specific meal on a specific date.
        
        Args:
            date: Date of the meal
            meal_name: Name of the meal (e.g., 'Breakfast')
            food_item: Food item to add
        """
        date_str = date.isoformat()
        
        if date_str not in self.daily_logs:
            self.daily_logs[date_str] = DailyLog(date)
        
        daily_log = self.daily_logs[date_str]
        
        # Find existing meal or create new one
        meal = next((m for m in daily_log.meals if m.name == meal_name), None)
        if not meal:
            meal = MealEntry(meal_name)
            daily_log.add_meal(meal)
        
        meal.add_food_item(food_item)
        self.save_data()
    
    def get_daily_summary(self, date: datetime.date) -> Dict:
        """
        Get a summary of nutrition for a specific day.
        
        Args:
            date: Date to get summary for
            
        Returns:
            Dictionary containing date and nutrition totals
        """
        date_str = date.isoformat()
        if date_str not in self.daily_logs:
            return {
                'date': date_str,
                'calories': 0,
                'protein': 0,
                'carbs': 0,
                'fat': 0,
                'meals': []
            }
        
        daily_log = self.daily_logs[date_str]
        totals = daily_log.total_nutrition()
        
        return {
            'date': date_str,
            'calories': totals['calories'],
            'protein': totals['protein'],
            'carbs': totals['carbs'],
            'fat': totals['fat'],
            'meals': [meal.to_dict() for meal in daily_log.meals]
        }
    
    def save_data(self) -> None:
        """Save all data to the data file."""
        data = {
            'daily_logs': {
                date: log.to_dict() for date, log in self.daily_logs.items()
            }
        }
        
        try:
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def load_data(self) -> None:
        """Load data from the data file."""
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.daily_logs = {
                    date: DailyLog.from_dict(log_data)
                    for date, log_data in data['daily_logs'].items()
                }
        except FileNotFoundError:
            # First run - no data file exists yet
            self.daily_logs = {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            self.daily_logs = {}

# Example usage
if __name__ == "__main__":
    tracker = CalorieTracker()
    
    # Add some food items
    today = datetime.date.today()
    apple = FoodItem("Apple", 95, 0.5, 25, 0.3)
    chicken_breast = FoodItem("Chicken Breast", 165, 31, 0, 3.6)
    rice = FoodItem("White Rice", 205, 4.3, 44, 0.4)
    
    # Add to meals
    tracker.add_food_to_meal(today, "Breakfast", apple)
    tracker.add_food_to_meal(today, "Lunch", chicken_breast)
    tracker.add_food_to_meal(today, "Lunch", rice)
    
    # Get summary
    summary = tracker.get_daily_summary(today
