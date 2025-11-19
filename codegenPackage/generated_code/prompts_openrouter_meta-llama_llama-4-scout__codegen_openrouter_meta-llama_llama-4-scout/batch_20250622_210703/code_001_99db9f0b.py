"""
Generated Code Metadata:
========================
Original URL: https://cupomestudante.com.br
Prompt: "Write a Python code to create a quiz generator for Chemistry and Biology questions based on the ENEM exam pattern."
Generated: DETERMINISTIC_99db9f0b2e776a56
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json

# Define a base class for questions
class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

# Define a class for Chemistry questions
class ChemistryQuestion(Question):
    def __init__(self, question, options, correct_answer, topic):
        super().__init__(question, options, correct_answer)
        self.topic = topic

# Define a class for Biology questions
class BiologyQuestion(Question):
    def __init__(self, question, options, correct_answer, topic):
        super().__init__(question, options, correct_answer)
        self.topic = topic

# Load questions from JSON files
def load_questions(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return []
    except json.JSONDecodeError:
        print(f"Failed to parse JSON in file {file_name}.")
        return []

# Generate a quiz with the specified number of questions
def generate_quiz(questions, num_questions):
    if len(questions) < num_questions:
        print("Not enough questions available.")
        return []
    return random.sample(questions, num_questions)

# Save quiz to a JSON file
def save_quiz(quiz, file_name):
    try:
        with open(file_name, 'w') as file:
            json.dump([q.__dict__ for q in quiz], file, indent=4)
    except Exception as e:
        print(f"Failed to save quiz to file {file_name}: {str(e)}")

# Chemistry questions data
chemistry_questions_data = load_questions('chemistry_questions.json')

# Biology questions data
biology_questions_data = load_questions('biology_questions.json')

# Create Chemistry and Biology questions
chemistry_questions = []
for q in chemistry_questions_data:
    chemistry_questions.append(ChemistryQuestion(q['question'], q['options'], q['correct_answer'], q['topic']))

biology_questions = []
for q in biology_questions_data:
    biology_questions.append(BiologyQuestion(q['question'], q['options'], q['correct_answer'], q['topic']))

# Generate quizzes
num_questions = 5
chemistry_quiz = generate_quiz(chemistry_questions, num_questions)
biology_quiz = generate_quiz(biology_questions, num_questions)

# Save quizzes to files
save_quiz(chemistry_quiz, 'chemistry_quiz.json')
save_quiz(biology_quiz, 'biology_quiz.json')

# Function to start the quiz
def start_quiz(quiz):
    score = 0
    for i, q in enumerate(quiz):
        print(f"\nQuestion {i+1}: {q.question}")
        for j, option in enumerate(q.options):
            print(f"{j+1}. {option}")
        answer = input("Enter the number of your answer: ")
        if q.options[int(answer) - 1] == q.correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {q.correct_answer}.")
    print(f"\nQuiz finished. Your score is {score}/{len(quiz)}")

# Start the quizzes
print("Chemistry Quiz:")
start_quiz(chemistry_quiz)
print("\nBiology Quiz:")
start_quiz(biology_quiz)
```

**chemistry_questions.json**
```json
[
    {
        "question": "What is the atomic number of Hydrogen?",
        "options": ["1", "2", "3", "4"],
        "correct_answer": "1",
        "topic": "Atomic Structure"
    },
    {
        "question": "What is the molecular formula of water?",
        "options": ["H2O", "H3O", "HO2", "H2O2"],
        "correct_answer": "H2O",
        "topic": "Chemical Compounds"
    }
]
```

**biology_questions.json**
```json
[
    {
        "question": "What is the process by which plants make their own food?",
        "options": ["Respiration", "Photosynthesis", "Decomposition", "Fermentation"],
        "correct_answer": "Photosynthesis",
        "topic": "Plant Biology"
    },
    {
        "question": "What is the largest part of the human brain?",
        "options": ["Cerebrum", "Cerebellum", "Brainstem", "Spinal Cord"],
        "correct_answer": "Cerebrum",
        "topic": "Human Anatomy"
    }
]
```
