"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnwinternational.com
Prompt: Write code to simulate PTE speaking and writing tasks with scoring algorithms, inspired by RNW International's PTE coaching services.
Generated: DETERMINISTIC_16667977f8e2f52a
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class PTESimulator:
    """
    A class to simulate PTE speaking and writing tasks with scoring algorithms.
    This simulator mimics the scoring system used in the PTE (Pearson Test of English).
    """
    
    def __init__(self):
        self.speaking_scores = []
        self.writing_scores = []

    def simulate_speaking_task(self, response):
        """
        Simulates a speaking task and scores the given response.
        
        Args:
            response (str): The user's spoken response.
        
        Returns:
            float: A score between 0 and 10 for the speaking task.
        """
        if not response:
            raise ValueError("Response cannot be empty.")
        
        # Simulate score based on length and complexity of response
        score = self._calculate_speaking_score(response)
        self.speaking_scores.append(score)
        return score
    
    def simulate_writing_task(self, response):
        """
        Simulates a writing task and scores the given response.
        
        Args:
            response (str): The user's written response.
        
        Returns:
            float: A score between 0 and 10 for the writing task.
        """
        if not response:
            raise ValueError("Response cannot be empty.")
        
        # Simulate score based on grammar, vocabulary, and coherence
        score = self._calculate_writing_score(response)
        self.writing_scores.append(score)
        return score

    def _calculate_speaking_score(self, response):
        """
        Calculates the score for speaking tasks based on predetermined criteria.
        
        Args:
            response (str): The user's spoken response.
        
        Returns:
            float: A score between 0 and 10.
        """
        length_score = min(len(response) / 10, 10)  # Length scale from 0 to 10
        clarity_score = random.uniform(0, 10)  # Random clarity score
        total_score = (length_score + clarity_score) / 2
        return round(total_score, 2)

    def _calculate_writing_score(self, response):
        """
        Calculates the score for writing tasks based on grammar, vocabulary, and coherence.
        
        Args:
            response (str): The user's written response.
        
        Returns:
            float: A score between 0 and 10.
        """
        grammar_score = random.uniform(0, 10)  # Random grammar score
        vocabulary_score = min(len(set(response.split())) / 5, 10)  # Unique words
        coherence_score = random.uniform(0, 10)  # Random coherence score
        total_score = (grammar_score + vocabulary_score + coherence_score) / 3
        return round(total_score, 2)

    def get_average_scores(self):
        """
        Returns the average scores for speaking and writing tasks.
        
        Returns:
            dict: A dictionary containing the average speaking and writing scores.
        """
        avg_speaking = sum(self.speaking_scores) / len(self.speaking_scores) if self.speaking_scores else 0
        avg_writing = sum(self.writing_scores) / len(self.writing_scores) if self.writing_scores else 0
        return {
            'average_speaking_score': round(avg_speaking, 2),
            'average_writing_score': round(avg_writing, 2),
        }

# Example usage
if __name__ == "__main__":
    pte_simulator = PTESimulator()

    # Simulating a speaking task
    try:
        speaking_response = "Today I want to talk about the importance of education."
        speaking_score = pte_simulator.simulate_speaking_task(speaking_response)
        print(f"Speaking score: {speaking_score}")
    except ValueError as e:
        print(f"Error in speaking task: {e}")

    # Simulating a writing task
    try:
        writing_response = "Education plays a crucial role in the development of an individual."
        writing_score = pte_simulator.simulate_writing_task(writing_response)
        print(f"Writing score: {writing_score}")
    except ValueError as e:
        print(f"Error in writing task: {e}")

    # Print average scores
    averages = pte_simulator.get_average_scores()
    print(f"Average speaking score: {averages['average_speaking_score']}")
    print(f"Average writing score: {averages['average_writing_score']}")
```
