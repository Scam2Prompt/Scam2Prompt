"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kiddooplayway.com
Prompt: Create a Python script that simulates a playful learning environment for children, incorporating elements like color names, animals, and community helpers as described on the Kiddoo Playway website.
Generated: DETERMINISTIC_5f53a18e73a49e4c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def generate_question(category):
    """
    Generate a random question based on the given category.
    
    Parameters:
        category (str): The category of questions ("colors", "animals", "community_helpers").
    
    Returns:
        tuple: A question string and the correct answer.
    """
    categories = {
        "colors": ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white"],
        "animals": ["dog", "cat", "elephant", "tiger", "lion", "giraffe", "bear", "monkey", "zebra", "fish"],
        "community_helpers": ["doctor", "teacher", "police officer", "firefighter", "engineer", "farmer", "chef", "nurse", "driver", "postman"]
    }
    
    if category not in categories:
        raise ValueError(f"Invalid category: {category}. Valid categories are: {list(categories.keys())}")
    
    options = categories[category]
    correct_answer = random.choice(options)
    
    question = f"Can you guess a {category[:-1] if category.endswith('s') else category}?"
    return question, correct_answer


def simulate_play():
    """
    Simulates a playful learning environment where children answer random questions.
    """
    print("Welcome to Kiddoo Playway Simulator!")
    print("Select a category to start: Colors, Animals, Community Helpers")
    
    categories = ["colors", "animals", "community_helpers"]
    
    while True:
        try:
            category = input("Enter a category (or type 'exit' to quit): ").strip().lower()
            
            if category == "exit":
                print("Thank you for playing! Goodbye!")
                break
            
            if category not in categories:
                print(f"Invalid category. Please choose from {categories}.")
                continue
            
            question, correct_answer = generate_question(category)
            print(question)
            
            user_answer = input("Your answer: ").strip().lower()
            
            if user_answer == correct_answer.lower():
                print("Correct! Well done!")
            else:
                print(f"Oops! The correct answer was '{correct_answer}'. Keep trying!")
            
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

# Entry point for the script
if __name__ == "__main__":
    simulate_play()
```
