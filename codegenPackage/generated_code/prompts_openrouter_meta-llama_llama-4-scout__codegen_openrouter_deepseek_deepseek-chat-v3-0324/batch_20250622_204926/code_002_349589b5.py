"""
Generated Code Metadata:
========================
Original URL: https://comestim.com.co
Prompt: "Write a survey script for customer satisfaction regarding edible print services, incorporating a rating system from 1 to 5."
Generated: DETERMINISTIC_349589b53510d413
Batch ID: 20250622_204926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Dict, List, Optional

class SurveyQuestion:
    """Represents a single survey question with its options."""
    
    def __init__(self, question_text: str, options: List[str]):
        self.question_text = question_text
        self.options = options
    
    def display(self) -> None:
        """Displays the question and its options."""
        print(f"\n{self.question_text}")
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

class Survey:
    """Represents a customer satisfaction survey."""
    
    def __init__(self, title: str, questions: List[SurveyQuestion]):
        self.title = title
        self.questions = questions
        self.responses: List[Dict[int, int]] = []
    
    def display_welcome(self) -> None:
        """Displays the welcome message and instructions."""
        print(f"\n{'=' * 50}")
        print(f"Welcome to the {self.title} Survey!")
        print("Please rate your experience from 1 to 5, where:")
        print("1 = Very Dissatisfied, 5 = Very Satisfied")
        print(f"{'=' * 50}\n")
    
    def conduct_survey(self) -> None:
        """Conducts the survey by asking each question and collecting responses."""
        self.display_welcome()
        response: Dict[int, int] = {}
        
        for i, question in enumerate(self.questions, start=1):
            while True:
                try:
                    question.display()
                    answer = int(input("Your rating (1-5): "))
                    if 1 <= answer <= 5:
                        response[i] = answer
                        break
                    else:
                        print("Error: Please enter a number between 1 and 5.")
                except ValueError:
                    print("Error: Please enter a valid number.")
        
        self.responses.append(response)
        print("\nThank you for completing the survey!")
    
    def get_summary(self) -> Dict[int, float]:
        """Calculates the average rating for each question.
        
        Returns:
            Dict[int, float]: A dictionary with question numbers as keys and average ratings as values.
        """
        if not self.responses:
            return {}
        
        summary: Dict[int, float] = {}
        num_responses = len(self.responses)
        
        for question_num in range(1, len(self.questions) + 1):
            total = sum(response[question_num] for response in self.responses)
            summary[question_num] = total / num_responses
        
        return summary

def main() -> None:
    """Main function to run the survey."""
    # Define survey questions
    questions = [
        SurveyQuestion(
            "How satisfied are you with the quality of the edible prints?",
            ["Very Dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very Satisfied"]
        ),
        SurveyQuestion(
            "How satisfied are you with the variety of designs available?",
            ["Very Dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very Satisfied"]
        ),
        SurveyQuestion(
            "How satisfied are you with the delivery time?",
            ["Very Dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very Satisfied"]
        ),
        SurveyQuestion(
            "How satisfied are you with the customer service?",
            ["Very Dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very Satisfied"]
        ),
        SurveyQuestion(
            "How likely are you to recommend our edible print services to others?",
            ["Very Unlikely", "Unlikely", "Neutral", "Likely", "Very Likely"]
        )
    ]
    
    # Create and conduct the survey
    survey = Survey("Edible Print Services Customer Satisfaction", questions)
    
    try:
        while True:
            survey.conduct_survey()
            another = input("\nWould you like to submit another response? (yes/no): ").strip().lower()
            if another != 'yes':
                break
        
        # Display summary if there are responses
        if survey.responses:
            print("\nSurvey Summary:")
            summary = survey.get_summary()
            for q_num, avg_rating in summary.items():
                print(f"Question {q_num}: Average Rating = {avg_rating:.2f}")
    
    except KeyboardInterrupt:
        print("\n\nSurvey interrupted. Exiting...")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
