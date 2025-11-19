"""
Generated Code Metadata:
========================
Original URL: https://skees.ir
Prompt: Develop a program to generate sample exam questions for vocational school subjects, using predefined templates and randomization techniques to ensure variety.
Generated: DETERMINISTIC_71d59c6e58989c9d
Batch ID: 20250612_151446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Tuple

# Predefined templates for different question types
QUESTION_TEMPLATES = {
    "multiple_choice": [
        "What is the correct answer to the following: {question}?\n{a}\n{b}\n{c}\n{d}",
        "Which of these options best describes {concept}?\n{a}\n{b}\n{c}\n{d}",
        "Select the most accurate statement about {topic}:\n{a}\n{b}\n{c}\n{d}"
    ],
    "true_false": [
        "True or False: {statement}",
        "Is the following statement correct? {statement}",
        "Mark as True or False: {statement}"
    ],
    "short_answer": [
        "Explain briefly: {question}",
        "Describe in your own words: {concept}",
        "What is the purpose of {item}?"
    ],
    "fill_in_the_blank": [
        "Complete the sentence: {sentence_start} _____ {sentence_end}",
        "Fill in the blank: {blank_text}",
        "The term for {definition} is _____."
    ]
}

# Sample data for different vocational subjects
SUBJECT_DATA = {
    "automotive": {
        "concepts": ["engine", "transmission", "brake system", "suspension"],
        "topics": ["oil change", "tire rotation", "engine diagnostics"],
        "items": ["carburetor", "spark plug", "alternator"],
        "definitions": {
            "ABS": "Anti-lock Braking System",
            "OBD": "On-Board Diagnostics",
            "MPG": "Miles Per Gallon"
        }
    },
    "culinary": {
        "concepts": ["mise en place", "knife skills", "food safety"],
        "topics": ["sautéing", "baking", "plating"],
        "items": ["chef's knife", "mandoline", "immersion blender"],
        "definitions": {
            "al dente": "cooked to be firm to the bite",
            "julienne": "cut into thin strips",
            "deglaze": "adding liquid to a pan to loosen browned bits"
        }
    },
    "electrical": {
        "concepts": ["circuit", "voltage", "resistance"],
        "topics": ["wiring", "safety protocols", "troubleshooting"],
        "items": ["multimeter", "wire stripper", "circuit breaker"],
        "definitions": {
            "AC": "Alternating Current",
            "DC": "Direct Current",
            "GFCI": "Ground Fault Circuit Interrupter"
        }
    }
}

def generate_multiple_choice(subject: str) -> Tuple[str, List[str], str]:
    """Generate a multiple choice question with options and correct answer."""
    data = SUBJECT_DATA[subject]
    template = random.choice(QUESTION_TEMPLATES["multiple_choice"])
    
    # Generate question content
    question_content = {
        "question": f"how to perform {random.choice(data['topics'])}",
        "concept": random.choice(data["concepts"]),
        "topic": random.choice(data["topics"])
    }
    
    # Generate options (3 wrong, 1 correct)
    correct = random.choice(data["items"])
    options = random.sample(data["items"], 3)
    while correct in options:
        options = random.sample(data["items"], 3)
    options.append(correct)
    random.shuffle(options)
    
    # Map options to a, b, c, d
    option_map = {
        "a": options[0],
        "b": options[1],
        "c": options[2],
        "d": options[3]
    }
    
    question_content.update(option_map)
    question = template.format(**question_content)
    
    return question, options, correct

def generate_true_false(subject: str) -> Tuple[str, str]:
    """Generate a true/false question with correct answer."""
    data = SUBJECT_DATA[subject]
    template = random.choice(QUESTION_TEMPLATES["true_false"])
    
    # Generate statement (50% chance of being true)
    is_true = random.choice([True, False])
    if is_true:
        statement = f"{random.choice(data['concepts'])} is important for {random.choice(data['topics'])}"
    else:
        wrong_concept = random.choice(list(SUBJECT_DATA.keys()))
        while wrong_concept == subject:
            wrong_concept = random.choice(list(SUBJECT_DATA.keys()))
        statement = f"{random.choice(SUBJECT_DATA[wrong_concept]['concepts'])} is used in {random.choice(data['topics'])}"
    
    question = template.format(statement=statement)
    answer = "True" if is_true else "False"
    
    return question, answer

def generate_short_answer(subject: str) -> str:
    """Generate a short answer question."""
    data = SUBJECT_DATA[subject]
    template = random.choice(QUESTION_TEMPLATES["short_answer"])
    
    content = {
        "question": f"the process of {random.choice(data['topics'])}",
        "concept": random.choice(data["concepts"]),
        "item": random.choice(data["items"])
    }
    
    return template.format(**content)

def generate_fill_in_the_blank(subject: str) -> Tuple[str, str]:
    """Generate a fill-in-the-blank question with correct answer."""
    data = SUBJECT_DATA[subject]
    template = random.choice(QUESTION_TEMPLATES["fill_in_the_blank"])
    
    # Choose a random definition
    term, definition = random.choice(list(data["definitions"].items()))
    
    content = {
        "sentence_start": f"In {subject}, the abbreviation",
        "sentence_end": f"stands for {definition}",
        "blank_text": f"The term '{definition}' refers to _____",
        "definition": definition
    }
    
    question = template.format(**content)
    return question, term

def generate_exam_questions(subject: str, num_questions: int = 10) -> List[Dict]:
    """Generate a set of exam questions for a given subject."""
    if subject not in SUBJECT_DATA:
        raise ValueError(f"Invalid subject. Available subjects: {list(SUBJECT_DATA.keys())}")
    
    questions = []
    question_types = [
        generate_multiple_choice,
        generate_true_false,
        generate_short_answer,
        generate_fill_in_the_blank
    ]
    
    for _ in range(num_questions):
        generator = random.choice(question_types)
        if generator == generate_multiple_choice:
            question, options, answer = generator(subject)
            questions.append({
                "type": "multiple_choice",
                "question": question,
                "options": options,
                "answer": answer
            })
        elif generator == generate_true_false:
            question, answer = generator(subject)
            questions.append({
                "type": "true_false",
                "question": question,
                "answer": answer
            })
        elif generator == generate_short_answer:
            question = generator(subject)
            questions.append({
                "type": "short_answer",
                "question": question
            })
        elif generator == generate_fill_in_the_blank:
            question, answer = generator(subject)
            questions.append({
                "type": "fill_in_the_blank",
                "question": question,
                "answer": answer
            })
    
    return questions

def print_questions(questions: List[Dict]):
    """Print generated questions in a readable format."""
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['type'].replace('_', ' ').title()}")
        print(q["question"])
        if q["type"] == "multiple_choice":
            for opt in q["options"]:
                print(f"- {opt}")
        if "answer" in q:
            print(f"\nAnswer: {q['answer']}")

if __name__ == "__main__":
    try:
        subject = input("Enter subject (automotive, culinary, electrical): ").lower()
        num_questions = int(input("Number of questions to generate (default 10): ") or 10)
        
        questions = generate_exam_questions(subject, num_questions)
        print("\n" + "="*50)
        print(f"Generated {num_questions} questions for {subject}:")
        print("="*50)
        print_questions(questions)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
