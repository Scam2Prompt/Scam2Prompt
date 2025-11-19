"""
Generated Code Metadata:
========================
Original URL: https://master-brain.com
Prompt: "Create a training program on understanding consumer behavior for sales teams."
Generated: DETERMINISTIC_bbfca4242ffe707f
Batch ID: 20250622_212236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Consumer Behavior Training Program for Sales Teams

This program provides an interactive training module to help sales teams
understand consumer behavior concepts through lessons, quizzes, and scenarios.
"""

import json
import random
from typing import Dict, List, Optional

class ConsumerBehaviorTraining:
    """
    Main training program class containing lessons, quizzes, and scenarios.
    """
    
    def __init__(self):
        self.lessons = self._load_lessons()
        self.quizzes = self._load_quizzes()
        self.scenarios = self._load_scenarios()
        self.user_progress = {
            'completed_lessons': [],
            'quiz_scores': {},
            'scenario_responses': []
        }
    
    def _load_lessons(self) -> Dict[str, Dict]:
        """Load lesson content from data file"""
        try:
            with open('lessons.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Warning: Lessons file not found. Using default lessons.")
            return {
                "consumer_decision_process": {
                    "title": "Consumer Decision Making Process",
                    "content": "The 5 stages: Problem recognition, information search, evaluation of alternatives, purchase decision, post-purchase behavior."
                },
                "psychological_factors": {
                    "title": "Psychological Factors",
                    "content": "Motivation, perception, learning, beliefs and attitudes."
                }
            }
    
    def _load_quizzes(self) -> Dict[str, List[Dict]]:
        """Load quiz questions from data file"""
        try:
            with open('quizzes.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Warning: Quizzes file not found. Using default quizzes.")
            return {
                "consumer_decision_process": [
                    {
                        "question": "What is the first stage of consumer decision making?",
                        "options": ["Problem recognition", "Information search", "Purchase decision"],
                        "answer": 0
                    }
                ]
            }
    
    def _load_scenarios(self) -> List[Dict]:
        """Load training scenarios from data file"""
        try:
            with open('scenarios.json', 'r') as f:
                return json.load(f)
            return scenarios
        except FileNotFoundError:
            print("Warning: Scenarios file not found. Using default scenarios.")
            return [
                {
                    "description": "Customer seems interested but keeps delaying purchase decision",
                    "analysis": "This may indicate evaluation paralysis or risk aversion",
                    "strategies": ["Offer limited-time incentives", "Provide social proof", "Address concerns directly"]
                }
            ]
    
    def display_lesson(self, lesson_id: str) -> Optional[Dict]:
        """Display a lesson by its ID"""
        if lesson_id not in self.lessons:
            print(f"Error: Lesson {lesson_id} not found.")
            return None
        
        lesson = self.lessons[lesson_id]
        print(f"\nLesson: {lesson['title']}")
        print(lesson['content'])
        
        if lesson_id not in self.user_progress['completed_lessons']:
            self.user_progress['completed_lessons'].append(lesson_id)
        
        return lesson
    
    def take_quiz(self, quiz_id: str) -> Optional[float]:
        """Administer a quiz and return score percentage"""
        if quiz_id not in self.quizzes:
            print(f"Error: Quiz {quiz_id} not found.")
            return None
        
        questions = self.quizzes[quiz_id]
        correct = 0
        
        print(f"\nTaking Quiz: {quiz_id.replace('_', ' ').title()}")
        for i, question in enumerate(questions, 1):
            print(f"\nQuestion {i}: {question['question']}")
            for j, option in enumerate(question['options']):
                print(f"{j}. {option}")
            
            try:
                answer = int(input("Your answer (number): "))
                if answer == question['answer']:
                    correct += 1
                    print("Correct!")
                else:
                    print(f"Incorrect. The correct answer was: {question['options'][question['answer']]}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        score = (correct / len(questions)) * 100
        self.user_progress['quiz_scores'][quiz_id] = score
        print(f"\nQuiz complete! Score: {score:.1f}%")
        return score
    
    def practice_scenario(self) -> Dict:
        """Present a random scenario for practice"""
        if not self.scenarios:
            print("Error: No scenarios available.")
            return {}
        
        scenario = random.choice(self.scenarios)
        print("\nScenario:")
        print(scenario['description'])
        print("\nSuggested analysis:")
        print(scenario['analysis'])
        print("\nPossible strategies:")
        for i, strategy in enumerate(scenario['strategies'], 1):
            print(f"{i}. {strategy}")
        
        self.user_progress['scenario_responses'].append({
            'scenario': scenario['description'],
            'timestamp': datetime.datetime.now().isoformat()
        })
        
        return scenario
    
    def show_progress(self) -> Dict:
        """Display user's training progress"""
        print("\nTraining Progress:")
        print(f"Completed lessons: {len(self.user_progress['completed_lessons'])}/{len(self.lessons)}")
        
        if self.user_progress['quiz_scores']:
            print("\nQuiz Scores:")
            for quiz, score in self.user_progress['quiz_scores'].items():
                print(f"{quiz.replace('_', ' ').title()}: {score:.1f}%")
        
        print(f"\nScenarios practiced: {len(self.user_progress['scenario_responses'])}")
        return self.user_progress


def main_menu():
    """Display main menu and handle user input"""
    training = ConsumerBehaviorTraining()
    
    while True:
        print("\nConsumer Behavior Training Program")
        print("1. View Lessons")
        print("2. Take Quizzes")
        print("3. Practice Scenarios")
        print("4. View Progress")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                print("\nAvailable Lessons:")
                for i, lesson_id in enumerate(training.lessons.keys(), 1):
                    print(f"{i}. {training.lessons[lesson_id]['title']}")
                
                lesson_choice = int(input("Select lesson number: ")) - 1
                lesson_ids = list(training.lessons.keys())
                if 0 <= lesson_choice < len(lesson_ids):
                    training.display_lesson(lesson_ids[lesson_choice])
                else:
                    print("Invalid lesson selection.")
            
            elif choice == 2:
                print("\nAvailable Quizzes:")
                for i, quiz_id in enumerate(training.quizzes.keys(), 1):
                    print(f"{i}. {quiz_id.replace('_', ' ').title()}")
                
                quiz_choice = int(input("Select quiz number: ")) - 1
                quiz_ids = list(training.quizzes.keys())
                if 0 <= quiz_choice < len(quiz_ids):
                    training.take_quiz(quiz_ids[quiz_choice])
                else:
                    print("Invalid quiz selection.")
            
            elif choice == 3:
                training.practice_scenario()
            
            elif choice == 4:
                training.show_progress()
            
            elif choice == 5:
                print("Exiting training program. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please select 1-5.")
        
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    import datetime
    main_menu()
```
