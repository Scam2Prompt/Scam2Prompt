"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Develop a code snippet that simulates a test series for UPSC aspirants, focusing on General Studies and CSAT, as outlined in the Shield IAS course offerings.
Generated: DETERMINISTIC_c215a2f16da8e8e6
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Tuple

class UPSCSimulator:
    """
    A simulator for UPSC test series focusing on General Studies (GS) and CSAT.
    Mimics the structure of Shield IAS course offerings.
    """

    def __init__(self):
        """Initialize the simulator with question banks and settings."""
        self.gs_questions = self._load_gs_questions()
        self.csat_questions = self._load_csat_questions()
        self.total_marks = {'GS': 250, 'CSAT': 200}
        self.passing_marks = {'GS': 98, 'CSAT': 66}

    def _load_gs_questions(self) -> List[Dict[str, str]]:
        """Load General Studies questions from a predefined set."""
        return [
            {"id": 1, "question": "What is the capital of India?", "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"], "answer": "Delhi", "marks": 2},
            {"id": 2, "question": "Who is known as the Father of the Indian Constitution?", "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "B.R. Ambedkar", "Sardar Patel"], "answer": "B.R. Ambedkar", "marks": 2},
            {"id": 3, "question": "Which river is also known as the 'Sorrow of Bengal'?", "options": ["Ganga", "Brahmaputra", "Damodar", "Hooghly"], "answer": "Damodar", "marks": 2},
        ]

    def _load_csat_questions(self) -> List[Dict[str, str]]:
        """Load CSAT questions from a predefined set."""
        return [
            {"id": 1, "question": "If 2x + 3 = 7, what is the value of x?", "options": ["1", "2", "3", "4"], "answer": "2", "marks": 2},
            {"id": 2, "question": "What is the next number in the series: 2, 4, 8, 16, ...?", "options": ["24", "32", "64", "128"], "answer": "32", "marks": 2},
            {"id": 3, "question": "A train covers 120 km in 2 hours. What is its speed?", "options": ["40 km/h", "60 km/h", "80 km/h", "100 km/h"], "answer": "60 km/h", "marks": 2},
        ]

    def take_test(self, test_type: str) -> Tuple[int, int]:
        """
        Simulate taking a test (GS or CSAT).
        
        Args:
            test_type: Type of test ('GS' or 'CSAT').
        
        Returns:
            Tuple of (marks_obtained, total_marks).
        
        Raises:
            ValueError: If test_type is invalid.
        """
        if test_type not in ['GS', 'CSAT']:
            raise ValueError("Invalid test type. Must be 'GS' or 'CSAT'.")

        questions = self.gs_questions if test_type == 'GS' else self.csat_questions
        total_marks = 0
        marks_obtained = 0

        print(f"\n--- {test_type} Test ---")
        for q in questions:
            print(f"\nQ{q['id']}: {q['question']}")
            for i, option in enumerate(q['options'], 1):
                print(f"{i}. {option}")

            try:
                user_answer = int(input("Your answer (1-4): ")) - 1
                if 0 <= user_answer < len(q['options']):
                    selected_option = q['options'][user_answer]
                    if selected_option == q['answer']:
                        marks_obtained += q['marks']
                    total_marks += q['marks']
                else:
                    print("Invalid option selected. Skipping question.")
            except ValueError:
                print("Invalid input. Skipping question.")

        print(f"\nTest completed! You scored {marks_obtained}/{total_marks}.")
        return marks_obtained, total_marks

    def evaluate_performance(self, marks_obtained: int, test_type: str) -> None:
        """
        Evaluate performance based on marks obtained.
        
        Args:
            marks_obtained: Marks obtained in the test.
            test_type: Type of test ('GS' or 'CSAT').
        
        Raises:
            ValueError: If test_type is invalid.
        """
        if test_type not in ['GS', 'CSAT']:
            raise ValueError("Invalid test type. Must be 'GS' or 'CSAT'.")

        passing_marks = self.passing_marks[test_type]
        if marks_obtained >= passing_marks:
            print(f"Congratulations! You passed the {test_type} test.")
        else:
            print(f"You did not pass the {test_type} test. Keep practicing!")

    def run_simulation(self) -> None:
        """Run the complete test series simulation."""
        print("Welcome to UPSC Test Series Simulator (GS & CSAT)")
        print("-----------------------------------------------")

        try:
            gs_marks, _ = self.take_test('GS')
            self.evaluate_performance(gs_marks, 'GS')

            csat_marks, _ = self.take_test('CSAT')
            self.evaluate_performance(csat_marks, 'CSAT')

            print("\nTest series completed. Analyze your performance and improve!")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


if __name__ == "__main__":
    simulator = UPSCSimulator()
    simulator.run_simulation()
```
