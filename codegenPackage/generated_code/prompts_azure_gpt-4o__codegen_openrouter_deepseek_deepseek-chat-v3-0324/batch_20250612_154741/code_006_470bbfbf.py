"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: Generate a Python script that simulates the open-book Guardianship and Conservatorship Pre-appointment Test, pulling answers from the Utah Courts website.
Generated: DETERMINISTIC_470bbfbf346db487
Batch ID: 20250612_154741
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.utcourts.gov": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from bs4 import BeautifulSoup
import random
import time
from typing import Dict, List, Optional, Tuple

class GuardianshipTestSimulator:
    """
    A simulator for the open-book Guardianship and Conservatorship Pre-appointment Test.
    Pulls questions and answers from the Utah Courts website.
    """
    
    def __init__(self):
        self.base_url = "https://www.utcourts.gov"
        self.test_url = f"{self.base_url}/howto/guardian/conservator-test/"
        self.questions: List[Dict[str, str]] = []
        self.answers: Dict[str, str] = {}
        self.user_score = 0
        self.total_questions = 0
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def fetch_test_content(self) -> bool:
        """
        Fetch the test content from Utah Courts website.
        Returns True if successful, False otherwise.
        """
        try:
            response = self.session.get(self.test_url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            main_content = soup.find('div', {'class': 'content'})
            
            if not main_content:
                print("Error: Could not find test content on the page.")
                return False
            
            # Extract questions and answers
            self._parse_questions_and_answers(main_content)
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching test content: {e}")
            return False

    def _parse_questions_and_answers(self, content) -> None:
        """
        Parse questions and answers from the HTML content.
        """
        # Find all question blocks (assuming each question is in a <p> tag)
        paragraphs = content.find_all('p')
        
        current_question = None
        for p in paragraphs:
            text = p.get_text().strip()
            if not text:
                continue
                
            # Check if this is a question (starts with number)
            if text[0].isdigit() and '.' in text:
                if current_question:
                    self.questions.append(current_question)
                question_parts = text.split('?', 1)
                if len(question_parts) == 2:
                    question_text = question_parts[0] + '?'
                    answer_hint = question_parts[1].strip()
                else:
                    question_text = text
                    answer_hint = ""
                    
                current_question = {
                    'text': question_text,
                    'hint': answer_hint,
                    'options': []
                }
            elif current_question:
                # Check if this is an option (starts with a letter)
                if len(text) > 2 and text[1] == ')':
                    current_question['options'].append(text)
                # Check if this is the correct answer
                if 'correct answer is' in text.lower():
                    self.answers[current_question['text']] = text.split(':')[-1].strip()
        
        # Add the last question if exists
        if current_question:
            self.questions.append(current_question)
            
        self.total_questions = len(self.questions)

    def display_question(self, question_num: int) -> Optional[Dict[str, str]]:
        """
        Display a question by its number (1-based index).
        Returns the question data if successful, None otherwise.
        """
        if question_num < 1 or question_num > len(self.questions):
            print("Invalid question number.")
            return None
            
        question = self.questions[question_num - 1]
        print(f"\nQuestion {question_num}: {question['text']}")
        if question['hint']:
            print(f"Hint: {question['hint']}")
            
        for i, option in enumerate(question['options'], 1):
            print(f"{i}. {option}")
            
        return question

    def check_answer(self, question_num: int, user_answer: str) -> Tuple[bool, str]:
        """
        Check if the user's answer is correct.
        Returns a tuple of (is_correct, correct_answer).
        """
        if question_num < 1 or question_num > len(self.questions):
            return (False, "Invalid question number")
            
        question = self.questions[question_num - 1]
        correct_answer = self.answers.get(question['text'], "")
        
        # Simple comparison (could be enhanced)
        is_correct = user_answer.lower() in correct_answer.lower()
        return (is_correct, correct_answer)

    def run_test(self) -> None:
        """
        Run the test simulation.
        """
        print("\n=== Guardianship and Conservatorship Pre-appointment Test Simulator ===")
        print("Pulling questions from Utah Courts website...\n")
        
        if not self.fetch_test_content():
            print("Failed to fetch test content. Please check your internet connection.")
            return
            
        print(f"Loaded {self.total_questions} questions from the Utah Courts website.")
        print("This is an open-book test. You may refer to the website for answers.")
        print("Type 'quit' at any time to exit.\n")
        
        # Shuffle questions for variety
        random.shuffle(self.questions)
        
        for i, question in enumerate(self.questions, 1):
            print(f"\nQuestion {i} of {self.total_questions}")
            print("=" * 50)
            print(question['text'])
            if question['hint']:
                print(f"\nHint: {question['hint']}")
                
            for j, option in enumerate(question['options'], 1):
                print(f"{j}. {option}")
                
            while True:
                user_input = input("\nYour answer (enter option number or 'skip'): ").strip().lower()
                
                if user_input == 'quit':
                    print("\nTest aborted by user.")
                    self._display_score()
                    return
                elif user_input == 'skip':
                    print("Question skipped.")
                    break
                
                try:
                    option_num = int(user_input)
                    if 1 <= option_num <= len(question['options']):
                        selected_option = question['options'][option_num - 1]
                        is_correct, correct_answer = self.check_answer(i, selected_option)
                        
                        if is_correct:
                            print("\n✅ Correct!")
                            self.user_score += 1
                        else:
                            print(f"\n❌ Incorrect. The correct answer is: {correct_answer}")
                        break
                    else:
                        print(f"Please enter a number between 1 and {len(question['options'])}")
                except ValueError:
                    print("Please enter a valid option number or 'skip'")
        
        self._display_score()

    def _display_score(self) -> None:
        """
        Display the user's final score.
        """
        print("\n" + "=" * 50)
        print(f"Test completed. Your score: {self.user_score}/{self.total_questions}")
        passing_score = int(self.total_questions * 0.8)  # Assuming 80% is passing
        if self.user_score >= passing_score:
            print("Congratulations! You passed the test.")
        else:
            print(f"You need at least {passing_score} correct answers to pass. Please try again.")
        print("=" * 50)

    def __del__(self):
        """Clean up resources."""
        self.session.close()

if __name__ == "__main__":
    simulator = GuardianshipTestSimulator()
    try:
        simulator.run_test()
    except KeyboardInterrupt:
        print("\nTest interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
