"""
Generated Code Metadata:
========================
Original URL: https://myneel.com
Prompt: Write a Python code snippet to implement a simple calorie counter with a daily checkup feature, similar to Neel's food tracking functionality.
Generated: DETERMINISTIC_4c405087cc523aab
Batch ID: 20250622_204925
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
from datetime import datetime, date

class CalorieCounter:
    """
    A simple calorie counter with daily tracking functionality.
    """
    
    def __init__(self, data_file='calorie_data.json'):
        """
        Initialize the calorie counter with a data file.
        """
        self.data_file = data_file
        self.today = date.today().isoformat()
        self.data = self._load_data()
        
    def _load_data(self):
        """
        Load data from file or initialize empty data structure.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")
        
        return {
            "daily_logs": {},
            "total_calories": 0,
            "last_updated": None
        }
    
    def _save_data(self):
        """
        Save data to file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_calories(self, food_name, calories):
        """
        Add calories consumed for today.
        """
        if not isinstance(calories, (int, float)) or calories < 0:
            raise ValueError("Calories must be a positive number")
            
        if not food_name or not isinstance(food_name, str):
            raise ValueError("Food name must be a non-empty string")
            
        if self.today not in self.data["daily_logs"]:
            self.data["daily_logs"][self.today] = {
                "foods": [],
                "total": 0
            }
            
        self.data["daily_logs"][self.today]["foods"].append({
            "name": food_name,
            "calories": calories,
            "timestamp": datetime.now().isoformat()
        })
        
        self.data["daily_logs"][self.today]["total"] += calories
        self.data["total_calories"] += calories
        self.data["last_updated"] = datetime.now().isoformat()
        
        self._save_data()
    
    def get_daily_summary(self, day=None):
        """
        Get summary for a specific day (defaults to today).
        """
        if day is None:
            day = self.today
            
        if day not in self.data["daily_logs"]:
            return None
            
        return self.data["daily_logs"][day]
    
    def get_total_calories(self):
        """
        Get total calories logged.
        """
        return self.data["total_calories"]
    
    def get_last_updated(self):
        """
        Get last updated timestamp.
        """
        return self.data["last_updated"]
    
    def reset_day(self, day=None):
        """
        Reset logs for a specific day (defaults to today).
        """
        if day is None:
            day = self.today
            
        if day in self.data["daily_logs"]:
            # Subtract day's calories from total before removing
            self.data["total_calories"] -= self.data["daily_logs"][day]["total"]
            del self.data["daily_logs"][day]
            self.data["last_updated"] = datetime.now().isoformat()
            self._save_data()
            return True
            
        return False


def main():
    """
    Example usage of the CalorieCounter class.
    """
    counter = CalorieCounter()
    
    while True:
        print("\nCalorie Counter Menu:")
        print("1. Add food entry")
        print("2. View today's summary")
        print("3. View total calories")
        print("4. Reset today's log")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        try:
            if choice == '1':
                food = input("Enter food name: ")
                calories = float(input("Enter calories: "))
                counter.add_calories(food, calories)
                print(f"Added {calories} calories for {food}")
                
            elif choice == '2':
                summary = counter.get_daily_summary()
                if summary:
                    print(f"\nToday's Summary ({counter.today}):")
                    print(f"Total Calories: {summary['total']}")
                    print("Foods Consumed:")
                    for food in summary['foods']:
                        print(f"- {food['name']}: {food['calories']} cal")
                else:
                    print("No entries for today.")
                    
            elif choice == '3':
                print(f"\nTotal Calories Logged: {counter.get_total_calories()}")
                
            elif choice == '4':
                if counter.reset_day():
                    print("Today's log has been reset.")
                else:
                    print("No entries to reset for today.")
                    
            elif choice == '5':
                print("Exiting...")
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
