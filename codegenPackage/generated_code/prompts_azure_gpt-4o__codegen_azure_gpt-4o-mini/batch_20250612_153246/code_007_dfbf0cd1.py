"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: Write code to implement a scoring system for ENEM mock exams based on TRI, ensuring accurate predictions of student performance, as described in the Maratona do ENEM simulados.
Generated: DETERMINISTIC_dfbf0cd1ee0b3ac3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ENEMScoringSystem:
    """
    A class to implement a scoring system for ENEM mock exams based on the TRI (Teoria de Resposta ao Item).
    This system predicts student performance based on their responses to the mock exams.
    """

    def __init__(self):
        self.student_scores = {}
        self.item_difficulties = {}
        self.item_discriminations = {}

    def add_item(self, item_id, difficulty, discrimination):
        """
        Add an item to the scoring system.

        :param item_id: Unique identifier for the item
        :param difficulty: Difficulty level of the item (float)
        :param discrimination: Discrimination index of the item (float)
        """
        if item_id in self.item_difficulties:
            raise ValueError(f"Item {item_id} already exists.")
        self.item_difficulties[item_id] = difficulty
        self.item_discriminations[item_id] = discrimination

    def record_response(self, student_id, item_id, correct):
        """
        Record a student's response to an item.

        :param student_id: Unique identifier for the student
        :param item_id: Unique identifier for the item
        :param correct: Boolean indicating if the response was correct
        """
        if student_id not in self.student_scores:
            self.student_scores[student_id] = {}
        if item_id not in self.item_difficulties:
            raise ValueError(f"Item {item_id} does not exist.")
        self.student_scores[student_id][item_id] = correct

    def calculate_score(self, student_id):
        """
        Calculate the TRI score for a given student.

        :param student_id: Unique identifier for the student
        :return: Calculated TRI score (float)
        """
        if student_id not in self.student_scores:
            raise ValueError(f"No responses recorded for student {student_id}.")

        total_score = 0.0
        total_weight = 0.0

        for item_id, correct in self.student_scores[student_id].items():
            if correct:
                difficulty = self.item_difficulties[item_id]
                discrimination = self.item_discriminations[item_id]
                total_score += (1 / (1 + (difficulty - 1))) * discrimination
                total_weight += discrimination

        if total_weight == 0:
            return 0.0  # Avoid division by zero if no items were answered correctly

        return total_score / total_weight

    def predict_performance(self, student_id):
        """
        Predict the performance of a student based on their TRI score.

        :param student_id: Unique identifier for the student
        :return: Performance prediction (string)
        """
        score = self.calculate_score(student_id)
        if score < 0.5:
            return "Below Average"
        elif score < 0.75:
            return "Average"
        else:
            return "Above Average"


# Example usage
if __name__ == "__main__":
    scoring_system = ENEMScoringSystem()
    
    # Adding items to the scoring system
    scoring_system.add_item("item1", difficulty=0.3, discrimination=1.2)
    scoring_system.add_item("item2", difficulty=0.5, discrimination=1.5)
    
    # Recording student responses
    scoring_system.record_response("student1", "item1", correct=True)
    scoring_system.record_response("student1", "item2", correct=False)
    
    # Calculating score and predicting performance
    try:
        score = scoring_system.calculate_score("student1")
        performance = scoring_system.predict_performance("student1")
        print(f"Student Score: {score:.2f}, Performance: {performance}")
    except ValueError as e:
        print(f"Error: {e}")
```
