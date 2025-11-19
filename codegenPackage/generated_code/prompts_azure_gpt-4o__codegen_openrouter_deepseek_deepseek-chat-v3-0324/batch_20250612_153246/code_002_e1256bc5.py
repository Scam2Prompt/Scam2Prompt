"""
Generated Code Metadata:
========================
Original URL: https://gkcritiques.com
Prompt: Develop a questionnaire for IT Decision Makers (ITDMs) to gather insights on technology adoption, leveraging the methodology described by GK Critique Services.
Generated: DETERMINISTIC_e1256bc56e4c1f56
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class Questionnaire:
    """
    A class to represent a questionnaire for IT Decision Makers (ITDMs) 
    to gather insights on technology adoption.
    Methodology inspired by GK Critique Services.
    """
    
    def __init__(self):
        self.questions = []
        self.responses = {}
        self.current_question_index = 0
        
    def add_question(self, question: str, question_type: str, options: Optional[List[str]] = None) -> None:
        """
        Add a question to the questionnaire.
        
        Args:
            question: The question text.
            question_type: Type of question ('text', 'single_choice', 'multiple_choice').
            options: List of options for choice-based questions.
        """
        if question_type not in ['text', 'single_choice', 'multiple_choice']:
            raise ValueError("Invalid question type. Must be 'text', 'single_choice', or 'multiple_choice'.")
            
        if question_type != 'text' and not options:
            raise ValueError("Choice-based questions must include options.")
            
        self.questions.append({
            'id': len(self.questions) + 1,
            'question': question,
            'type': question_type,
            'options': options
        })
    
    def start_questionnaire(self) -> None:
        """Initialize the questionnaire session."""
        self.current_question_index = 0
        self.responses = {}
        print("Welcome to the ITDM Technology Adoption Questionnaire")
        print("----------------------------------------------------")
        
    def display_current_question(self) -> None:
        """Display the current question to the user."""
        if self.current_question_index >= len(self.questions):
            print("Questionnaire completed. Thank you for your responses!")
            return
            
        question = self.questions[self.current_question_index]
        print(f"\nQuestion {question['id']}: {question['question']}")
        
        if question['type'] != 'text':
            for i, option in enumerate(question['options'], 1):
                print(f"{i}. {option}")
    
    def record_response(self, response: str) -> None:
        """
        Record the user's response to the current question.
        
        Args:
            response: The user's response to the current question.
        """
        if self.current_question_index >= len(self.questions):
            raise IndexError("No more questions to answer.")
            
        question = self.questions[self.current_question_index]
        question_id = question['id']
        
        # Validate response based on question type
        if question['type'] == 'text':
            if not response.strip():
                raise ValueError("Text response cannot be empty.")
            self.responses[question_id] = response
            
        elif question['type'] == 'single_choice':
            try:
                choice_index = int(response) - 1
                if choice_index < 0 or choice_index >= len(question['options']):
                    raise ValueError
                self.responses[question_id] = question['options'][choice_index]
            except (ValueError, IndexError):
                raise ValueError("Please enter a valid option number.")
                
        elif question['type'] == 'multiple_choice':
            try:
                choices = [int(c) - 1 for c in response.split(',')]
                for choice in choices:
                    if choice < 0 or choice >= len(question['options']):
                        raise ValueError
                self.responses[question_id] = [question['options'][c] for c in choices]
            except (ValueError, IndexError):
                raise ValueError("Please enter valid option numbers separated by commas.")
        
        self.current_question_index += 1
    
    def save_responses(self, filename: str) -> None:
        """
        Save the responses to a JSON file.
        
        Args:
            filename: The name of the file to save responses to.
        """
        with open(filename, 'w') as f:
            json.dump(self.responses, f, indent=4)
    
    def load_questionnaire(self, filename: str) -> None:
        """
        Load a questionnaire from a JSON file.
        
        Args:
            filename: The name of the file to load the questionnaire from.
        """
        with open(filename, 'r') as f:
            data = json.load(f)
            self.questions = data.get('questions', [])
    
    def save_questionnaire(self, filename: str) -> None:
        """
        Save the questionnaire to a JSON file.
        
        Args:
            filename: The name of the file to save the questionnaire to.
        """
        with open(filename, 'w') as f:
            json.dump({'questions': self.questions}, f, indent=4)

def create_default_questionnaire() -> Questionnaire:
    """
    Create a default questionnaire with standard questions for ITDMs.
    
    Returns:
        A Questionnaire object with predefined questions.
    """
    questionnaire = Questionnaire()
    
    # Technology Adoption Questions
    questionnaire.add_question(
        "What are the key factors driving technology adoption in your organization?",
        "multiple_choice",
        ["Competitive advantage", "Cost reduction", "Regulatory compliance", 
         "Customer demand", "Operational efficiency", "Other"]
    )
    
    questionnaire.add_question(
        "What is your organization's typical approach to adopting new technologies?",
        "single_choice",
        ["Early adopter", "Fast follower", "Wait for maturity", "Only when mandated"]
    )
    
    questionnaire.add_question(
        "What percentage of your IT budget is allocated to new technology adoption?",
        "single_choice",
        ["Less than 10%", "10-25%", "25-50%", "More than 50%"]
    )
    
    questionnaire.add_question(
        "What are the biggest challenges in adopting new technologies in your organization?",
        "multiple_choice",
        ["Budget constraints", "Lack of skilled personnel", "Integration with legacy systems",
         "Security concerns", "Organizational resistance to change", "Other"]
    )
    
    questionnaire.add_question(
        "How do you evaluate the success of technology adoption initiatives?",
        "multiple_choice",
        ["ROI metrics", "User adoption rates", "Operational KPIs", 
         "Customer satisfaction", "Strategic alignment", "Other"]
    )
    
    questionnaire.add_question(
        "What emerging technologies is your organization currently evaluating or piloting?",
        "text"
    )
    
    questionnaire.add_question(
        "What would make your organization more likely to adopt a new technology?",
        "text"
    )
    
    return questionnaire

def run_questionnaire(questionnaire: Questionnaire) -> None:
    """
    Run the questionnaire interactively in the console.
    
    Args:
        questionnaire: The Questionnaire object to run.
    """
    questionnaire.start_questionnaire()
    
    while questionnaire.current_question_index < len(questionnaire.questions):
        try:
            questionnaire.display_current_question()
            response = input("Your answer: ")
            questionnaire.record_response(response)
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break
    
    # Save responses
    try:
        questionnaire.save_responses("itdm_responses.json")
        print("\nYour responses have been saved to 'itdm_responses.json'")
    except Exception as e:
        print(f"Failed to save responses: {e}")

if __name__ == "__main__":
    # Create and run the questionnaire
    itdm_questionnaire = create_default_questionnaire()
    run_questionnaire(itdm_questionnaire)
```
