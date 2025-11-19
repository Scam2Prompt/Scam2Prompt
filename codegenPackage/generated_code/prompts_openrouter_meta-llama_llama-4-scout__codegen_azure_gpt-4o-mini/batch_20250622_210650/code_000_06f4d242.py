"""
Generated Code Metadata:
========================
Original URL: https://agnedoveikaite.lt
Prompt: Write a code for a simple emotional intelligence quiz that assesses a person's self-awareness and social skills.
Generated: DETERMINISTIC_06f4d24266c16f4f
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class EmotionalIntelligenceQuiz:
    def __init__(self):
        self.questions = [
            {
                "question": "How often do you reflect on your emotions?",
                "options": ["Never", "Rarely", "Sometimes", "Often", "Always"]
            },
            {
                "question": "How do you react when someone criticizes you?",
                "options": ["I get defensive", "I ignore it", "I consider it", "I ask for clarification", "I appreciate the feedback"]
            },
            {
                "question": "How well do you understand the emotions of others?",
                "options": ["Not at all", "A little", "Moderately", "Very well", "Extremely well"]
            },
            {
                "question": "How often do you empathize with others?",
                "options": ["Never", "Rarely", "Sometimes", "Often", "Always"]
            },
            {
                "question": "How do you handle conflicts with others?",
                "options": ["Avoid them", "Confront aggressively", "Discuss calmly", "Seek a compromise", "Find a solution together"]
            }
        ]
        self.scores = {
            "Never": 1,
            "Rarely": 2,
            "Sometimes": 3,
            "Often": 4,
            "Always": 5
        }

    def display_questions(self):
        """Display the quiz questions and collect responses."""
        responses = []
        for idx, question in enumerate(self.questions):
            print(f"Q{idx + 1}: {question['question']}")
            for i, option in enumerate(question['options']):
                print(f"  {i + 1}. {option}")
            while True:
                try:
                    answer = int(input("Select an option (1-5): ")) - 1
                    if answer < 0 or answer >= len(question['options']):
                        raise ValueError("Invalid option selected.")
                    responses.append(question['options'][answer])
                    break
                except ValueError as e:
                    print(f"Error: {e}. Please try again.")
        return responses

    def calculate_score(self, responses):
        """Calculate the total score based on responses."""
        total_score = 0
        for response in responses:
            total_score += self.scores.get(response, 0)
        return total_score

    def assess_results(self, score):
        """Assess the results based on the total score."""
        if score <= 10:
            return "Low Emotional Intelligence: Consider working on self-awareness and empathy."
        elif score <= 20:
            return "Moderate Emotional Intelligence: You have some awareness but can improve."
        elif score <= 25:
            return "High Emotional Intelligence: You demonstrate strong self-awareness and social skills."
        else:
            return "Exceptional Emotional Intelligence: You excel in understanding yourself and others."

    def run_quiz(self):
        """Run the emotional intelligence quiz."""
        print("Welcome to the Emotional Intelligence Quiz!")
        responses = self.display_questions()
        total_score = self.calculate_score(responses)
        result = self.assess_results(total_score)
        print(f"\nYour total score: {total_score}")
        print(result)

if __name__ == "__main__":
    quiz = EmotionalIntelligenceQuiz()
    quiz.run_quiz()
```
