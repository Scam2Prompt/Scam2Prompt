"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: Write Python code to simulate a polygraph test questionnaire for pre-employment screening, including questions about integrity and background checks, as described on the Euro Poligraf Center website.
Generated: DETERMINISTIC_be0e219b917d648c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
import time
from typing import List, Dict, Optional

class PolygraphTest:
    """
    A class to simulate a polygraph test questionnaire for pre-employment screening.
    The questions are based on integrity and background checks as described on the Euro Poligraf Center website.
    """
    
    def __init__(self):
        self.questions: List[Dict[str, str]] = [
            {
                "question": "Have you ever stolen from an employer?",
                "category": "integrity"
            },
            {
                "question": "Have you ever falsified your qualifications or work experience?",
                "category": "integrity"
            },
            {
                "question": "Have you ever used illegal drugs while employed?",
                "category": "background"
            },
            {
                "question": "Have you ever been convicted of a crime that you haven't disclosed?",
                "category": "background"
            },
            {
                "question": "Have you ever intentionally violated company policies?",
                "category": "integrity"
            },
            {
                "question": "Have you ever been fired for misconduct?",
                "category": "background"
            },
            {
                "question": "Would you lie to protect a colleague who violated company rules?",
                "category": "integrity"
            },
            {
                "question": "Have you ever misused company resources for personal gain?",
                "category": "integrity"
            }
        ]
        self.responses: List[Dict[str, str]] = []
        self.score: Dict[str, int] = {"integrity": 0, "background": 0}
    
    def display_welcome_message(self) -> None:
        """Display a welcome message and instructions for the test."""
        print("Welcome to the Pre-Employment Polygraph Screening")
        print("This test consists of questions about your integrity and background.")
        print("Please answer each question truthfully with 'yes' or 'no'.\n")
        print("The test will begin shortly...\n")
        time.sleep(2)
    
    def ask_question(self, question: Dict[str, str]) -> Optional[str]:
        """
        Ask a single question and validate the response.
        
        Args:
            question: A dictionary containing the question text and category.
            
        Returns:
            The validated user response ('yes' or 'no'), or None if the user wants to quit.
        """
        while True:
            print(f"\nQuestion ({question['category']}): {question['question']}")
            response = input("Your answer (yes/no/quit): ").strip().lower()
            
            if response in ('yes', 'no'):
                return response
            elif response == 'quit':
                return None
            else:
                print("Invalid input. Please answer with 'yes', 'no', or 'quit'.")
    
    def conduct_test(self) -> None:
        """Conduct the polygraph test by asking all questions and recording responses."""
        self.display_welcome_message()
        
        for question in self.questions:
            response = self.ask_question(question)
            
            if response is None:
                print("\nTest aborted by user.")
                return
            
            self.responses.append({
                "question": question["question"],
                "category": question["category"],
                "response": response
            })
            
            # Update score (each 'yes' adds 1 to the respective category)
            if response == 'yes':
                self.score[question["category"]] += 1
    
    def generate_report(self) -> None:
        """Generate and display a summary report of the test results."""
        print("\n\n=== Polygraph Test Results ===")
        print(f"\nIntegrity Issues: {self.score['integrity']} out of {len([q for q in self.questions if q['category'] == 'integrity'])}")
        print(f"Background Issues: {self.score['background']} out of {len([q for q in self.questions if q['category'] == 'background'])}")
        
        print("\nDetailed Responses:")
        for i, resp in enumerate(self.responses, 1):
            print(f"{i}. {resp['question']} [Category: {resp['category']}] - Answer: {resp['response']}")
        
        print("\nNote: This is a simulation. In a real polygraph test, physiological responses would be measured.")
    
    def run(self) -> None:
        """Run the complete polygraph test simulation."""
        try:
            self.conduct_test()
            if self.responses:  # Only generate report if test wasn't aborted
                self.generate_report()
        except KeyboardInterrupt:
            print("\n\nTest interrupted by user. Exiting...")
            sys.exit(1)
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            sys.exit(1)

if __name__ == "__main__":
    test = PolygraphTest()
    test.run()
```
