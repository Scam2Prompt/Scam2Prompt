"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shieldias.in
Prompt: Develop a code snippet that simulates a test series for UPSC aspirants, focusing on General Studies and CSAT, as outlined in the Shield IAS course offerings.
Generated: DETERMINISTIC_c215a2f16da8e8e6
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class TestSeries:
    """A class to simulate a test series for UPSC aspirants focusing on General Studies and CSAT."""

    def __init__(self):
        self.questions = {
            'General Studies': self.load_questions('general_studies_questions.txt'),
            'CSAT': self.load_questions('csat_questions.txt')
        }

    def load_questions(self, filename):
        """Load questions from a specified text file."""
        try:
            with open(filename, 'r') as file:
                questions = [line.strip() for line in file if line.strip()]
            return questions
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
            return []
        except Exception as e:
            print(f"An error occurred while loading questions: {e}")
            return []

    def conduct_test(self, subject, num_questions=5):
        """Conduct a test for the given subject and number of questions."""
        if subject not in self.questions:
            print(f"Error: Subject '{subject}' not found.")
            return

        selected_questions = random.sample(self.questions[subject], min(num_questions, len(self.questions[subject])))
        print(f"Conducting test for {subject}. Here are your questions:\n")
        
        for idx, question in enumerate(selected_questions, start=1):
            print(f"Q{idx}: {question}")

        print("\nTest completed. Thank you for participating!")

def main():
    """Main function to run the test series simulation."""
    test_series = TestSeries()
    
    # Example of conducting tests
    subjects = ['General Studies', 'CSAT']
    for subject in subjects:
        test_series.conduct_test(subject)

if __name__ == '__main__':
    main()
```

**Note:** Ensure you have two text files named `general_studies_questions.txt` and `csat_questions.txt` in the same directory as the script, containing the questions for the respective subjects. Each question should be on a new line.
