"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1o2.ir
Prompt: Generate a Python script that randomly selects a question from a list of interesting topics like music, food, and technology, similar to the questions found on dex.chat.
Generated: DETERMINISTIC_40ff460d8f650c2a
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import sys

def get_random_question():
    """Returns a randomly selected question from a predefined list of interesting topics."""
    
    questions = {
        "Music": [
            "What was the first concert you ever attended?",
            "If you could attend any music festival, which one would you choose?",
            "Who is your favorite artist and why?"
        ],
        "Food": [
            "What is your favorite dish to cook?",
            "If you could only eat one cuisine for the rest of your life, what would it be?",
            "What is the most unusual food you've ever tried?"
        ],
        "Technology": [
            "What piece of technology could you not live without?",
            "If you could invent one gadget, what would it be?",
            "How do you think technology will change in the next 10 years?"
        ]
    }

    try:
        # Select a random topic
        topic = random.choice(list(questions.keys()))
        # Select a random question from the chosen topic
        question = random.choice(questions[topic])
        return f"Topic: {topic}\nQuestion: {question}"
    except Exception as e:
        # Log the exception and return a user-friendly message
        print(f"An error occurred: {e}", file=sys.stderr)
        return "Unable to generate a question at this time."

if __name__ == "__main__":
    # Generate and print a random question
    print(get_random_question())
```
