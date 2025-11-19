"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Write a Python script to simulate a mock IELTS test based on the exam preparation techniques discussed on the RNW International website.
Generated: DETERMINISTIC_496bfd66a3d378c0
Batch ID: 20250612_155322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from collections import defaultdict

class IELTSTestSimulator:
    """
    A mock IELTS test simulator based on RNW International's exam preparation techniques.
    Simulates Listening, Reading, Writing, and Speaking sections with scoring.
    """
    
    def __init__(self):
        self.sections = {
            'Listening': self._simulate_listening,
            'Reading': self._simulate_reading,
            'Writing': self._simulate_writing,
            'Speaking': self._simulate_speaking
        }
        self.user_responses = defaultdict(dict)
        self.scores = {}
        self.band_score = 0.0
        
    def run_test(self):
        """Run the complete IELTS test simulation."""
        print("Welcome to the IELTS Test Simulator\n")
        print("This test includes 4 sections: Listening, Reading, Writing, and Speaking.\n")
        
        for section_name, section_func in self.sections.items():
            print(f"\n--- {section_name} Section ---")
            section_func()
            
        self._calculate_score()
        self._display_results()
        
    def _simulate_listening(self):
        """Simulate the Listening section with 4 parts and 40 questions."""
        print("\nYou will hear 4 recordings and answer 40 questions.")
        print("Each correct answer gives you 1 mark. No penalty for wrong answers.\n")
        
        questions = {
            'Part 1': 10,
            'Part 2': 10,
            'Part 3': 10,
            'Part 4': 10
        }
        
        correct_answers = 0
        
        for part, num_questions in questions.items():
            print(f"\n{part} - {num_questions} questions")
            for q in range(1, num_questions + 1):
                # Simulate user answering questions (random for simulation)
                user_answer = random.choice(['A', 'B', 'C', 'D', 'correct'])
                correct_answer = 'correct'
                
                self.user_responses['Listening'][f"{part}_Q{q}"] = user_answer
                
                if user_answer == correct_answer:
                    correct_answers += 1
                    
            time.sleep(1)  # Simulate time between parts
            
        self.scores['Listening'] = correct_answers
        print(f"\nListening section completed. You answered {correct_answers}/40 questions correctly.")
        
    def _simulate_reading(self):
        """Simulate the Reading section with 3 passages and 40 questions."""
        print("\nYou will read 3 passages and answer 40 questions.")
        print("Each correct answer gives you 1 mark. No penalty for wrong answers.\n")
        
        passages = {
            'Passage 1': 13,
            'Passage 2': 13,
            'Passage 3': 14
        }
        
        correct_answers = 0
        
        for passage, num_questions in passages.items():
            print(f"\n{passage} - {num_questions} questions")
            for q in range(1, num_questions + 1):
                # Simulate user answering questions (random for simulation)
                user_answer = random.choice(['A', 'B', 'C', 'D', 'True', 'False', 'Not Given', 'correct'])
                correct_answer = 'correct'
                
                self.user_responses['Reading'][f"{passage}_Q{q}"] = user_answer
                
                if user_answer == correct_answer:
                    correct_answers += 1
                    
            time.sleep(1)  # Simulate time between passages
            
        self.scores['Reading'] = correct_answers
        print(f"\nReading section completed. You answered {correct_answers}/40 questions correctly.")
        
    def _simulate_writing(self):
        """Simulate the Writing section with Task 1 and Task 2."""
        print("\nWriting Section has 2 tasks:")
        print("Task 1 (Academic): Describe a graph/chart/diagram (150 words minimum)")
        print("Task 2: Write an essay (250 words minimum)\n")
        
        # Simulate random scores for writing (4 criteria, each 0-9)
        task1_scores = {
            'Task Achievement': random.randint(4, 9),
            'Coherence and Cohesion': random.randint(4, 9),
            'Lexical Resource': random.randint(4, 9),
            'Grammatical Range and Accuracy': random.randint(4, 9)
        }
        
        task2_scores = {
            'Task Response': random.randint(4, 9),
            'Coherence and Cohesion': random.randint(4, 9),
            'Lexical Resource': random.randint(4, 9),
            'Grammatical Range and Accuracy': random.randint(4, 9)
        }
        
        self.user_responses['Writing'] = {
            'Task 1': task1_scores,
            'Task 2': task2_scores
        }
        
        # Calculate average scores
        task1_avg = sum(task1_scores.values()) / 4
        task2_avg = sum(task2_scores.values()) / 4
        
        # Writing score is weighted 1:2 for Task 1:Task 2
        writing_score = (task1_avg + task2_avg * 2) / 3
        self.scores['Writing'] = writing_score
        
        print("\nWriting section completed. Your responses have been evaluated.")
        
    def _simulate_speaking(self):
        """Simulate the Speaking section with 3 parts."""
        print("\nSpeaking Section has 3 parts:")
        print("Part 1: Introduction and interview (4-5 minutes)")
        print("Part 2: Long turn (3-4 minutes)")
        print("Part 3: Discussion (4-5 minutes)\n")
        
        # Simulate random scores for speaking (4 criteria, each 0-9)
        speaking_scores = {
            'Fluency and Coherence': random.randint(4, 9),
            'Lexical Resource': random.randint(4, 9),
            'Grammatical Range and Accuracy': random.randint(4, 9),
            'Pronunciation': random.randint(4, 9)
        }
        
        self.user_responses['Speaking'] = speaking_scores
        speaking_score = sum(speaking_scores.values()) / 4
        self.scores['Speaking'] = speaking_score
        
        print("\nSpeaking section completed. Your performance has been evaluated.")
        
    def _calculate_score(self):
        """Calculate the overall band score based on section scores."""
        # Convert Listening and Reading raw scores to band scores
        listening_raw = self.scores['Listening']
        reading_raw = self.scores['Reading']
        
        # Simplified conversion (real IELTS has more complex mapping)
        listening_band = min(9.0, max(1.0, listening_raw / 4.0))
        reading_band = min(9.0, max(1.0, reading_raw / 4.0))
        
        # Writing and Speaking are already in band score format
        writing_band = self.scores['Writing']
        speaking_band = self.scores['Speaking']
        
        # Calculate overall band score (average of all sections)
        self.band_score = round((listening_band + reading_band + writing_band + speaking_band) / 4, 1)
        
    def _display_results(self):
        """Display the test results to the user."""
        print("\n--- Test Results ---")
        print(f"\nListening: {self.scores['Listening']}/40 (Band: {min(9.0, max(1.0, self.scores['Listening'] / 4.0)):.1f})")
        print(f"Reading: {self.scores['Reading']}/40 (Band: {min(9.0, max(1.0, self.scores['Reading'] / 4.0)):.1f})")
        print(f"Writing: Band {self.scores['Writing']:.1f}")
        print(f"Speaking: Band {self.scores['Speaking']:.1f}")
        print(f"\nOverall Band Score: {self.band_score}")
        
        # Provide feedback based on score
        if self.band_score >= 7.0:
            print("\nExcellent! You're likely ready for the real IELTS test.")
        elif self.band_score >= 5.5:
            print("\nGood attempt! With more practice, you can improve further.")
        else:
            print("\nKeep practicing! Focus on your weaker areas to improve.")

if __name__ == "__main__":
    try:
        simulator = IELTSTestSimulator()
        simulator.run_test()
    except Exception as e:
        print(f"An error occurred during the test: {str(e)}")
        print("Please try again later.")
```
