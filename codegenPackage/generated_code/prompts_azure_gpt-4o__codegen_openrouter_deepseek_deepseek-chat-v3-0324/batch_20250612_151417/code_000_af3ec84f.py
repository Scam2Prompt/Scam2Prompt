"""
Generated Code Metadata:
========================
Original URL: https://excelwithsmart.com
Prompt: Write Python code to simulate an aptitude test for placement training, incorporating modules for language skills, IT skills, and life skills, as described by SMART Training Resources.
Generated: DETERMINISTIC_af3ec84f5bb2c1db
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
import time
from typing import Dict, List, Optional, Tuple

class AptitudeTest:
    """
    A class to simulate an aptitude test with modules for language skills, IT skills, and life skills.
    """
    
    def __init__(self):
        """
        Initialize the test with questions and user data.
        """
        self.questions = {
            "language_skills": [
                {
                    "question": "Identify the grammatical error in the sentence: 'She go to school every day.'",
                    "options": ["She go", "to school", "every day", "No error"],
                    "answer": "She go"
                },
                {
                    "question": "Choose the correct synonym for 'Benevolent':",
                    "options": ["Kind", "Cruel", "Selfish", "Rude"],
                    "answer": "Kind"
                },
                {
                    "question": "Which of these is a complex sentence?",
                    "options": [
                        "I like coffee.",
                        "Although it was raining, we went out.",
                        "She ran quickly.",
                        "They laughed."
                    ],
                    "answer": "Although it was raining, we went out."
                }
            ],
            "it_skills": [
                {
                    "question": "What does SQL stand for?",
                    "options": [
                        "Structured Query Language",
                        "Simple Query Language",
                        "Standard Query Language",
                        "System Query Language"
                    ],
                    "answer": "Structured Query Language"
                },
                {
                    "question": "Which data structure uses LIFO principle?",
                    "options": ["Queue", "Stack", "Array", "Linked List"],
                    "answer": "Stack"
                },
                {
                    "question": "What is the time complexity of binary search?",
                    "options": ["O(n)", "O(n^2)", "O(log n)", "O(1)"],
                    "answer": "O(log n)"
                }
            ],
            "life_skills": [
                {
                    "question": "What is the first step in problem solving?",
                    "options": [
                        "Identify the problem",
                        "Implement solution",
                        "Evaluate alternatives",
                        "Define success criteria"
                    ],
                    "answer": "Identify the problem"
                },
                {
                    "question": "Which of these is NOT a good teamwork practice?",
                    "options": [
                        "Active listening",
                        "Blaming others",
                        "Sharing credit",
                        "Being punctual"
                    ],
                    "answer": "Blaming others"
                },
                {
                    "question": "When handling conflict, what is the most productive approach?",
                    "options": [
                        "Avoidance",
                        "Collaboration",
                        "Competition",
                        "Accommodation"
                    ],
                    "answer": "Collaboration"
                }
            ]
        }
        self.user_data = {
            "name": "",
            "scores": {
                "language_skills": 0,
                "it_skills": 0,
                "life_skills": 0
            },
            "responses": []
        }
    
    def display_welcome(self) -> None:
        """
        Display welcome message and instructions.
        """
        print("\n" + "="*50)
        print("SMART Training Resources - Aptitude Test".center(50))
        print("="*50)
        print("\nThis test consists of three modules:")
        print("1. Language Skills")
        print("2. IT Skills")
        print("3. Life Skills")
        print("\nEach module has 3 multiple-choice questions.")
        print("Select the correct option for each question.")
        print("="*50 + "\n")
    
    def get_user_info(self) -> None:
        """
        Get user's name and validate input.
        """
        while True:
            name = input("Enter your name: ").strip()
            if name:
                self.user_data["name"] = name
                break
            print("Error: Name cannot be empty. Please try again.")
    
    def shuffle_questions(self) -> None:
        """
        Shuffle questions within each module to randomize test order.
        """
        for module in self.questions.values():
            random.shuffle(module)
    
    def conduct_test(self) -> None:
        """
        Conduct the test by presenting questions and collecting responses.
        """
        self.shuffle_questions()
        
        for module_name, questions in self.questions.items():
            print(f"\n=== {module_name.replace('_', ' ').title()} ===")
            
            for i, question in enumerate(questions, 1):
                print(f"\nQuestion {i}: {question['question']}")
                for idx, option in enumerate(question['options'], 1):
                    print(f"{idx}. {option}")
                
                while True:
                    try:
                        choice = int(input("Your answer (1-4): "))
                        if 1 <= choice <= 4:
                            selected_option = question['options'][choice-1]
                            is_correct = selected_option == question['answer']
                            
                            self.user_data["responses"].append({
                                "module": module_name,
                                "question": question['question'],
                                "selected": selected_option,
                                "correct": question['answer'],
                                "is_correct": is_correct
                            })
                            
                            if is_correct:
                                self.user_data["scores"][module_name] += 1
                            break
                        print("Error: Please enter a number between 1 and 4.")
                    except ValueError:
                        print("Error: Invalid input. Please enter a number.")
    
    def calculate_results(self) -> Dict[str, float]:
        """
        Calculate and return the percentage scores for each module.
        """
        results = {}
        for module, score in self.user_data["scores"].items():
            total = len(self.questions[module])
            percentage = (score / total) * 100
            results[module] = round(percentage, 2)
        return results
    
    def display_results(self, results: Dict[str, float]) -> None:
        """
        Display the test results to the user.
        """
        print("\n" + "="*50)
        print("TEST RESULTS".center(50))
        print("="*50)
        print(f"\nCandidate: {self.user_data['name']}\n")
        
        for module, percentage in results.items():
            print(f"{module.replace('_', ' ').title()}: {percentage}%")
        
        overall = sum(results.values()) / len(results)
        print(f"\nOverall Score: {round(overall, 2)}%")
        
        if overall >= 70:
            print("\nPerformance: Excellent!")
        elif overall >= 50:
            print("\nPerformance: Good")
        else:
            print("\nPerformance: Needs Improvement")
        print("="*50 + "\n")
    
    def save_results(self, filename: str = "aptitude_test_results.json") -> None:
        """
        Save test results to a JSON file.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.user_data, f, indent=4)
            print(f"\nResults saved to {filename}")
        except IOError as e:
            print(f"\nError saving results: {e}")
    
    def run(self) -> None:
        """
        Run the complete aptitude test workflow.
        """
        try:
            self.display_welcome()
            self.get_user_info()
            
            print("\nStarting test in 3 seconds...")
            time.sleep(3)
            
            self.conduct_test()
            results = self.calculate_results()
            self.display_results(results)
            self.save_results()
            
        except KeyboardInterrupt:
            print("\n\nTest aborted by user.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    test = AptitudeTest()
    test.run()
```
