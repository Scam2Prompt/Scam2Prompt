"""
Generated Code Metadata:
========================
Original URL: https://chanorodriguez.com
Prompt: Write a Python script to create a personalized fitness plan based on user input, similar to the services offered on ChanoRodriguez.com.
Generated: DETERMINISTIC_677205363d8f403e
Batch ID: 20250622_210655
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

class FitnessPlanGenerator:
    """Generates personalized fitness plans based on user input."""
    
    def __init__(self):
        self.exercise_db = self._load_exercise_database()
        self.plan_duration = 30  # Default plan duration in days
        
    def _load_exercise_database(self) -> Dict[str, List[Dict]]:
        """Load exercise database from JSON file."""
        try:
            with open('exercise_database.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("Exercise database file not found.")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in exercise database.")
    
    def _validate_user_input(self, user_data: Dict) -> bool:
        """Validate user input data."""
        required_fields = ['age', 'gender', 'weight', 'height', 'fitness_level', 'goals']
        for field in required_fields:
            if field not in user_data:
                raise ValueError(f"Missing required field: {field}")
            
        if not (18 <= user_data['age'] <= 100):
            raise ValueError("Age must be between 18 and 100.")
            
        if user_data['gender'].lower() not in ['male', 'female']:
            raise ValueError("Gender must be 'male' or 'female'.")
            
        if not (30 <= user_data['weight'] <= 300):  # kg
            raise ValueError("Weight must be between 30 and 300 kg.")
            
        if not (100 <= user_data['height'] <= 250):  # cm
            raise ValueError("Height must be between 100 and 250 cm.")
            
        if user_data['fitness_level'].lower() not in ['beginner', 'intermediate', 'advanced']:
            raise ValueError("Fitness level must be 'beginner', 'intermediate', or 'advanced'.")
            
        if not isinstance(user_data['goals'], list) or len(user_data['goals']) == 0:
            raise ValueError("Goals must be a non-empty list.")
            
        return True
    
    def _calculate_bmi(self, weight: float, height: float) -> float:
        """Calculate Body Mass Index (BMI)."""
        return weight / ((height / 100) ** 2)
    
    def _select_exercises(self, fitness_level: str, goals: List[str]) -> List[Dict]:
        """Select appropriate exercises based on fitness level and goals."""
        selected_exercises = []
        
        for goal in goals:
            if goal.lower() not in self.exercise_db:
                continue
                
            for exercise in self.exercise_db[goal.lower()]:
                if exercise['difficulty'].lower() == fitness_level.lower():
                    selected_exercises.append(exercise)
                    
        if not selected_exercises:
            raise ValueError("No exercises found matching the specified criteria.")
            
        return selected_exercises
    
    def _generate_weekly_schedule(self, exercises: List[Dict]) -> Dict[str, List[Dict]]:
        """Generate a weekly workout schedule."""
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        schedule = {day: [] for day in days}
        
        # Distribute exercises throughout the week
        for i, exercise in enumerate(exercises):
            day = days[i % len(days)]
            schedule[day].append(exercise)
            
        return schedule
    
    def _generate_meal_plan(self, bmi: float, goals: List[str]) -> Dict[str, List[str]]:
        """Generate a basic meal plan recommendation."""
        meal_plan = {
            'breakfast': [],
            'lunch': [],
            'dinner': [],
            'snacks': []
        }
        
        # Basic recommendations based on BMI and goals
        if bmi < 18.5:
            meal_plan['breakfast'].append("High-protein breakfast (e.g., eggs, Greek yogurt)")
            meal_plan['lunch'].append("Calorie-dense lunch (e.g., chicken with rice and vegetables)")
        elif bmi > 25:
            meal_plan['breakfast'].append("High-fiber breakfast (e.g., oatmeal with berries)")
            meal_plan['lunch'].append("Lean protein with vegetables (e.g., grilled fish with salad)")
        else:
            meal_plan['breakfast'].append("Balanced breakfast (e.g., whole grain toast with avocado)")
            meal_plan['lunch'].append("Balanced lunch (e.g., quinoa bowl with mixed vegetables)")
            
        if 'weight_loss' in [g.lower() for g in goals]:
            meal_plan['dinner'].append("Light dinner (e.g., vegetable soup or lean protein with greens)")
            meal_plan['snacks'].append("Healthy snacks (e.g., nuts, fruits)")
        elif 'muscle_gain' in [g.lower() for g in goals]:
            meal_plan['dinner'].append("Protein-rich dinner (e.g., steak with sweet potatoes)")
            meal_plan['snacks'].append("Protein snacks (e.g., protein shake, cottage cheese)")
        else:
            meal_plan['dinner'].append("Balanced dinner (e.g., chicken with roasted vegetables)")
            meal_plan['snacks'].append("Mixed snacks (e.g., hummus with veggies)")
            
        return meal_plan
    
    def generate_plan(self, user_data: Dict) -> Dict:
        """Generate a complete fitness plan based on user data."""
        try:
            self._validate_user_input(user_data)
            
            bmi = self._calculate_bmi(user_data['weight'], user_data['height'])
            exercises = self._select_exercises(user_data['fitness_level'], user_data['goals'])
            schedule = self._generate_weekly_schedule(exercises)
            meal_plan = self._generate_meal_plan(bmi, user_data['goals'])
            
            start_date = datetime.now().date()
            end_date = start_date + timedelta(days=self.plan_duration)
            
            return {
                'user_info': {
                    'name': user_data.get('name', 'User'),
                    'age': user_data['age'],
                    'gender': user_data['gender'],
                    'weight': user_data['weight'],
                    'height': user_data['height'],
                    'bmi': round(bmi, 1),
                    'fitness_level': user_data['fitness_level'],
                    'goals': user_data['goals']
                },
                'plan_duration': f"{self.plan_duration} days",
                'start_date': start_date.strftime('%Y-%m-%d'),
                'end_date': end_date.strftime('%Y-%m-%d'),
                'workout_schedule': schedule,
                'meal_plan': meal_plan,
                'recommendations': self._generate_recommendations(bmi, user_data['fitness_level'])
            }
        except Exception as e:
            raise RuntimeError(f"Failed to generate fitness plan: {str(e)}")
    
    def _generate_recommendations(self, bmi: float, fitness_level: str) -> List[str]:
        """Generate personalized recommendations."""
        recommendations = []
        
        if bmi < 18.5:
            recommendations.append("Consider increasing calorie intake for healthy weight gain.")
        elif bmi > 25:
            recommendations.append("Consider a calorie deficit for healthy weight loss.")
            
        if fitness_level.lower() == 'beginner':
            recommendations.append("Start with 3-4 workouts per week, focusing on form.")
        elif fitness_level.lower() == 'intermediate':
            recommendations.append("Aim for 4-5 workouts per week with progressive overload.")
        else:
            recommendations.append("Advanced training: 5-6 workouts per week with periodization.")
            
        recommendations.append("Stay hydrated and get at least 7-8 hours of sleep daily.")
        recommendations.append("Listen to your body and adjust intensity as needed.")
        
        return recommendations

def main():
    """Main function to demonstrate the fitness plan generator."""
    try:
        generator = FitnessPlanGenerator()
        
        # Example user data
        user_data = {
            'name': 'John Doe',
            'age': 30,
            'gender': 'male',
            'weight': 80,
            'height': 180,
            'fitness_level': 'intermediate',
            'goals': ['muscle_gain', 'strength']
        }
        
        plan = generator.generate_plan(user_data)
        print(json.dumps(plan, indent=2))
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
