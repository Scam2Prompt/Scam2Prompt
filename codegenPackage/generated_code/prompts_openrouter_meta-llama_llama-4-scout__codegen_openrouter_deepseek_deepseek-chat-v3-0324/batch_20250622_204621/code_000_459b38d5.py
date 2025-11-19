"""
Generated Code Metadata:
========================
Original URL: https://simonscat.pages.dev
Prompt: Write a Python script to create a simple quiz that determines which Simon's Cat character a user is, based on a few easy questions.
Generated: DETERMINISTIC_459b38d53889add9
Batch ID: 20250622_204621
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

# Quiz questions and possible answers
questions = [
    {
        "question": "What's your favorite activity?",
        "answers": {
            "a": "Sleeping",
            "b": "Eating",
            "c": "Causing mischief",
            "d": "Being pampered"
        }
    },
    {
        "question": "How do you react when hungry?",
        "answers": {
            "a": "Patiently wait for food",
            "b": "Demand food loudly",
            "c": "Steal food when no one's looking",
            "d": "Refuse to eat unless it's gourmet"
        }
    },
    {
        "question": "What's your relationship with your owner?",
        "answers": {
            "a": "They're my servant",
            "b": "We're best friends",
            "c": "I tolerate them",
            "d": "I'm the actual owner"
        }
    },
    {
        "question": "Choose a color:",
        "answers": {
            "a": "Black",
            "b": "Ginger",
            "c": "White",
            "d": "Gray"
        }
    }
]

# Character mappings based on answers
characters = {
    "Simon's Cat": {
        "description": "You're Simon's Cat - mischievous, playful, and always hungry!",
        "answers": ["b", "b", "a", "a"]
    },
    "Kitten": {
        "description": "You're the Kitten - full of energy and always getting into trouble!",
        "answers": ["c", "c", "b", "d"]
    },
    "Chloe": {
        "description": "You're Chloe - elegant, sophisticated, and a bit demanding!",
        "answers": ["d", "d", "d", "c"]
    },
    "Jazz": {
        "description": "You're Jazz - laid back, wise, and always relaxed!",
        "answers": ["a", "a", "c", "b"]
    }
}

def run_quiz():
    """Run the Simon's Cat character quiz."""
    print("Welcome to the Simon's Cat Character Quiz!")
    print("Answer a few questions to find out which character you are!\n")
    
    user_answers = []
    
    try:
        for i, question in enumerate(questions, 1):
            print(f"Question {i}: {question['question']}")
            for option, answer in question['answers'].items():
                print(f"{option}) {answer}")
            
            while True:
                answer = input("Your answer (a/b/c/d): ").lower().strip()
                if answer in ['a', 'b', 'c', 'd']:
                    user_answers.append(answer)
                    print()
                    break
                else:
                    print("Invalid input. Please enter a, b, c, or d.")
        
        determine_character(user_answers)
    except KeyboardInterrupt:
        print("\n\nQuiz aborted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)

def determine_character(user_answers):
    """Determine which Simon's Cat character matches the user's answers."""
    best_match = None
    highest_score = 0
    
    for char_name, char_data in characters.items():
        score = sum(1 for i, answer in enumerate(char_data['answers']) 
                   if i < len(user_answers) and answer == user_answers[i])
        
        if score > highest_score:
            highest_score = score
            best_match = char_name
    
    if best_match:
        print("\nResults:")
        print(f"You are most like {best_match}!")
        print(characters[best_match]['description'])
    else:
        print("\nHmm... we couldn't determine your character. Maybe you're unique!")

if __name__ == "__main__":
    run_quiz()
```
