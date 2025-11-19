"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Develop a Python script to automate the delivery of personalized workout plans via an exclusive app, ensuring the plans are generated within 4 days after a physical evaluation.
Generated: DETERMINISTIC_57372dd1add4798b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional

# Constants
WORKOUT_PLANS_DIR = "workout_plans"
EVALUATION_DATA_FILE = "evaluation_data.json"
MAX_DAYS_TO_GENERATE = 4

class WorkoutPlanGenerator:
    """
    A class to generate and deliver personalized workout plans based on physical evaluations.
    """

    def __init__(self):
        """
        Initialize the WorkoutPlanGenerator with necessary directories and files.
        """
        self._ensure_directory_exists(WORKOUT_PLANS_DIR)
        self.evaluation_data = self._load_evaluation_data()

    def _ensure_directory_exists(self, directory: str) -> None:
        """
        Ensure the specified directory exists, create it if it doesn't.
        
        Args:
            directory (str): Path to the directory to check/create.
        """
        if not os.path.exists(directory):
            os.makedirs(directory)

    def _load_evaluation_data(self) -> Dict:
        """
        Load evaluation data from the JSON file.
        
        Returns:
            Dict: Evaluation data loaded from file.
        
        Raises:
            FileNotFoundError: If evaluation data file doesn't exist.
            json.JSONDecodeError: If file contains invalid JSON.
        """
        try:
            with open(EVALUATION_DATA_FILE, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Evaluation data file '{EVALUATION_DATA_FILE}' not found.")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in evaluation data file: {e}", e.doc, e.pos)

    def _generate_workout_plan(self, user_id: str, evaluation: Dict) -> Dict:
        """
        Generate a personalized workout plan based on evaluation data.
        
        Args:
            user_id (str): ID of the user.
            evaluation (Dict): Evaluation data for the user.
            
        Returns:
            Dict: Generated workout plan.
        """
        # This is a simplified example - in production, this would use more complex logic
        # based on evaluation data to generate personalized plans
        return {
            "user_id": user_id,
            "generated_on": datetime.datetime.now().isoformat(),
            "plan": {
                "cardio": {
                    "type": "running" if evaluation.get("fitness_level", 0) > 5 else "walking",
                    "duration": "30 minutes"
                },
                "strength": {
                    "exercises": ["squats", "push-ups", "lunges"],
                    "sets": 3,
                    "reps": 10
                },
                "flexibility": "10 minutes stretching"
            }
        }

    def _save_workout_plan(self, user_id: str, plan: Dict) -> None:
        """
        Save the generated workout plan to a file.
        
        Args:
            user_id (str): ID of the user.
            plan (Dict): Workout plan to save.
        """
        filename = os.path.join(WORKOUT_PLANS_DIR, f"{user_id}_workout_plan.json")
        with open(filename, 'w') as file:
            json.dump(plan, file, indent=4)

    def _is_within_deadline(self, evaluation_date: str) -> bool:
        """
        Check if the evaluation date is within the 4-day generation deadline.
        
        Args:
            evaluation_date (str): ISO format date string of the evaluation.
            
        Returns:
            bool: True if within deadline, False otherwise.
        """
        eval_date = datetime.datetime.fromisoformat(evaluation_date)
        current_date = datetime.datetime.now()
        delta = current_date - eval_date
        return delta.days <= MAX_DAYS_TO_GENERATE

    def generate_plans_for_pending_evaluations(self) -> List[str]:
        """
        Generate workout plans for all pending evaluations within the deadline.
        
        Returns:
            List[str]: List of user IDs for whom plans were generated.
            
        Raises:
            ValueError: If evaluation data is invalid.
        """
        generated_plans = []
        
        if not isinstance(self.evaluation_data, dict):
            raise ValueError("Invalid evaluation data format. Expected a dictionary.")
            
        for user_id, evaluation in self.evaluation_data.items():
            try:
                if not self._is_within_deadline(evaluation["evaluation_date"]):
                    continue
                    
                plan = self._generate_workout_plan(user_id, evaluation)
                self._save_workout_plan(user_id, plan)
                generated_plans.append(user_id)
                
            except KeyError as e:
                print(f"Skipping user {user_id}: Missing evaluation data - {str(e)}")
            except Exception as e:
                print(f"Error generating plan for user {user_id}: {str(e)}")
                
        return generated_plans

    def deliver_plans(self, user_ids: List[str]) -> None:
        """
        Simulate delivering plans to users (in production, this would integrate with the app).
        
        Args:
            user_ids (List[str]): List of user IDs to deliver plans to.
        """
        for user_id in user_ids:
            print(f"Delivered workout plan to user {user_id}")

def main():
    """
    Main function to execute the workout plan generation and delivery process.
    """
    try:
        generator = WorkoutPlanGenerator()
        generated_user_ids = generator.generate_plans_for_pending_evaluations()
        
        if generated_user_ids:
            print(f"Generated workout plans for users: {', '.join(generated_user_ids)}")
            generator.deliver_plans(generated_user_ids)
        else:
            print("No workout plans to generate at this time.")
            
    except Exception as e:
        print(f"Error in workout plan generation: {str(e)}")

if __name__ == "__main__":
    main()
```
