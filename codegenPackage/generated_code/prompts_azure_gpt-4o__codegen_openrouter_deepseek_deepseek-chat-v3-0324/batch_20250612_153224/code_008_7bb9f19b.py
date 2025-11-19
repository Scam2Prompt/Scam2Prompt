"""
Generated Code Metadata:
========================
Original URL: https://www.greenaapples.com
Prompt: Write code to design an interactive quiz that helps users identify suitable treatment packages like "Healthy Heart Care" or "Pregnancy Nutrition," referencing the Green Apples e-Rx Clinic's offerings.
Generated: DETERMINISTIC_7bb9f19bf0d9ddb5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class QuizQuestion:
    """Represents a single quiz question with possible answers."""
    
    def __init__(self, question_id: int, text: str, answers: List[Dict[str, str]]):
        """
        Initialize a quiz question.
        
        Args:
            question_id: Unique identifier for the question
            text: The question text
            answers: List of answer dictionaries with 'text' and 'package_weights' keys
        """
        self.question_id = question_id
        self.text = text
        self.answers = answers

class Quiz:
    """Interactive quiz to recommend treatment packages."""
    
    def __init__(self, questions: List[QuizQuestion], packages: Dict[str, str]):
        """
        Initialize the quiz with questions and packages.
        
        Args:
            questions: List of QuizQuestion objects
            packages: Dictionary mapping package names to descriptions
        """
        self.questions = questions
        self.packages = packages
        self.user_answers = {}
        self.package_scores = {package: 0 for package in packages.keys()}
    
    def display_question(self, question: QuizQuestion) -> None:
        """Display a question and its answer options."""
        print(f"\n{question.text}")
        for idx, answer in enumerate(question.answers, 1):
            print(f"{idx}. {answer['text']}")
    
    def get_user_answer(self, question: QuizQuestion) -> Optional[int]:
        """Get and validate user's answer to a question."""
        while True:
            try:
                choice = input("\nEnter your choice (1-{}): ".format(len(question.answers)))
                choice = int(choice)
                if 1 <= choice <= len(question.answers):
                    return choice - 1  # Convert to 0-based index
                print("Please enter a valid option.")
            except ValueError:
                print("Please enter a number.")
    
    def update_scores(self, question_id: int, answer_index: int) -> None:
        """Update package scores based on user's answer."""
        selected_answer = self.questions[question_id].answers[answer_index]
        for package, weight in selected_answer['package_weights'].items():
            self.package_scores[package] += weight
    
    def run_quiz(self) -> None:
        """Run the interactive quiz."""
        print("Welcome to the Green Apples e-Rx Clinic Treatment Package Quiz!")
        print("Answer a few questions to find the best package for your needs.\n")
        
        for idx, question in enumerate(self.questions):
            self.display_question(question)
            answer_index = self.get_user_answer(question)
            if answer_index is not None:
                self.user_answers[question.question_id] = answer_index
                self.update_scores(idx, answer_index)
        
        self.display_results()
    
    def display_results(self) -> None:
        """Display the quiz results with recommended packages."""
        print("\nQuiz Complete! Here are your recommendations:")
        
        # Sort packages by score in descending order
        sorted_packages = sorted(
            self.package_scores.items(),
            key=lambda item: item[1],
            reverse=True
        )
        
        # Display top 3 recommendations
        for rank, (package, score) in enumerate(sorted_packages[:3], 1):
            print(f"\n{rank}. {package} (Score: {score})")
            print(f"   {self.packages[package]}")
        
        print("\nThank you for using the Green Apples e-Rx Clinic Quiz!")

def load_quiz_data(file_path: str) -> Dict:
    """Load quiz questions and packages from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        raise
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} contains invalid JSON.")
        raise

def create_quiz_questions(data: Dict) -> List[QuizQuestion]:
    """Create QuizQuestion objects from loaded data."""
    questions = []
    for q_data in data['questions']:
        question = QuizQuestion(
            question_id=q_data['id'],
            text=q_data['text'],
            answers=q_data['answers']
        )
        questions.append(question)
    return questions

def main():
    try:
        # Load quiz data
        quiz_data = load_quiz_data('quiz_data.json')
        
        # Create quiz components
        questions = create_quiz_questions(quiz_data)
        packages = quiz_data['packages']
        
        # Run the quiz
        quiz = Quiz(questions, packages)
        quiz.run_quiz()
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please try again later.")

if __name__ == "__main__":
    # Example quiz_data.json structure:
    # {
    #     "questions": [
    #         {
    #             "id": 1,
    #             "text": "What is your primary health concern?",
    #             "answers": [
    #                 {
    #                     "text": "Heart health",
    #                     "package_weights": {"Healthy Heart Care": 5, "Pregnancy Nutrition": 0}
    #                 },
    #                 {
    #                     "text": "Pregnancy and nutrition",
    #                     "package_weights": {"Healthy Heart Care": 0, "Pregnancy Nutrition": 5}
    #                 }
    #             ]
    #         }
    #     ],
    #     "packages": {
    #         "Healthy Heart Care": "Comprehensive heart health package with nutrition and exercise plans.",
    #         "Pregnancy Nutrition": "Tailored nutrition plans for expecting mothers."
    #     }
    # }
    main()
```
