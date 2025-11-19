"""
Generated Code Metadata:
========================
Original URL: https://my-app-ej8.pages.dev
Prompt: Write a quiz on ether.fi Knowledge Test, using the Galxe OAT Quiz framework, and provide answers and explanations for the quiz questions.
Generated: DETERMINISTIC_b317346d3c3cd87b
Batch ID: 20250622_210033
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

class QuizQuestion:
    """
    Represents a single quiz question with its options, correct answer, and explanation.
    """
    def __init__(self, question: str, options: List[str], correct_answer: str, explanation: str):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.explanation = explanation

    def to_dict(self) -> Dict:
        """Convert the question to a dictionary for JSON serialization."""
        return {
            "question": self.question,
            "options": self.options,
            "correct_answer": self.correct_answer,
            "explanation": self.explanation
        }

class Quiz:
    """
    Represents a complete quiz with multiple questions.
    Uses the Galxe OAT Quiz framework structure.
    """
    def __init__(self, title: str, description: str, questions: List[QuizQuestion]):
        self.title = title
        self.description = description
        self.questions = questions

    def to_json(self) -> str:
        """Serialize the quiz to JSON format."""
        quiz_data = {
            "title": self.title,
            "description": self.description,
            "questions": [q.to_dict() for q in self.questions]
        }
        return json.dumps(quiz_data, indent=2)

    @classmethod
    def from_json(cls, json_str: str) -> 'Quiz':
        """Deserialize a quiz from JSON format."""
        try:
            data = json.loads(json_str)
            questions = [
                QuizQuestion(
                    question=q["question"],
                    options=q["options"],
                    correct_answer=q["correct_answer"],
                    explanation=q["explanation"]
                ) for q in data["questions"]
            ]
            return cls(
                title=data["title"],
                description=data["description"],
                questions=questions
            )
        except (json.JSONDecodeError, KeyError) as e:
            raise ValueError("Invalid quiz JSON format") from e

def create_etherfi_quiz() -> Quiz:
    """Create an ether.fi knowledge test quiz."""
    questions = [
        QuizQuestion(
            question="What is ether.fi's primary service?",
            options=[
                "Decentralized exchange",
                "Liquid staking protocol",
                "NFT marketplace",
                "Stablecoin issuer"
            ],
            correct_answer="Liquid staking protocol",
            explanation="ether.fi is a liquid staking protocol that allows users to stake ETH while maintaining liquidity."
        ),
        QuizQuestion(
            question="What token does ether.fi use to represent staked ETH?",
            options=[
                "eETH",
                "stETH",
                "ETH2",
                "fiETH"
            ],
            correct_answer="eETH",
            explanation="ether.fi issues eETH tokens to represent staked ETH, which can be used across DeFi."
        ),
        QuizQuestion(
            question="How does ether.fi differ from traditional staking?",
            options=[
                "It offers higher APY",
                "It provides liquidity while staking",
                "It doesn't require validators",
                "It's only for institutional investors"
            ],
            correct_answer="It provides liquidity while staking",
            explanation="ether.fi's liquid staking allows users to stake ETH while still having access to liquidity through eETH tokens."
        ),
        QuizQuestion(
            question="What is the minimum ETH required to stake on ether.fi?",
            options=[
                "0.1 ETH",
                "1 ETH",
                "No minimum",
                "32 ETH"
            ],
            correct_answer="No minimum",
            explanation="ether.fi allows staking any amount of ETH, unlike traditional staking which requires 32 ETH."
        ),
        QuizQuestion(
            question="Which of these is NOT a feature of ether.fi?",
            options=[
                "Non-custodial staking",
                "Automatic validator selection",
                "Instant unstaking",
                "Fixed-term staking contracts"
            ],
            correct_answer="Fixed-term staking contracts",
            explanation="ether.fi doesn't have fixed-term contracts; staking is flexible with no lock-up periods."
        )
    ]
    
    return Quiz(
        title="ether.fi Knowledge Test",
        description="Test your knowledge about the ether.fi liquid staking protocol",
        questions=questions
    )

def run_quiz(quiz: Quiz) -> None:
    """Run the quiz interactively in the console."""
    print(f"\n{quiz.title}")
    print(f"{quiz.description}\n")
    
    score = 0
    for i, question in enumerate(quiz.questions, 1):
        print(f"Question {i}: {question.question}")
        for j, option in enumerate(question.options, 1):
            print(f"  {j}. {option}")
        
        while True:
            try:
                answer = int(input("Your answer (1-4): ")) - 1
                if 0 <= answer < len(question.options):
                    break
                print("Please enter a number between 1 and 4")
            except ValueError:
                print("Please enter a valid number")
        
        selected = question.options[answer]
        if selected == question.correct_answer:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Incorrect!")
        
        print(f"Explanation: {question.explanation}\n")
    
    print(f"Quiz complete! Your score: {score}/{len(quiz.questions)}")

if __name__ == "__main__":
    try:
        quiz = create_etherfi_quiz()
        run_quiz(quiz)
        
        # Example of saving and loading the quiz
        json_data = quiz.to_json()
        print("\nQuiz JSON representation:")
        print(json_data)
        
        # Load from JSON (demonstration)
        loaded_quiz = Quiz.from_json(json_data)
        print("\nSuccessfully loaded quiz from JSON")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
