"""
Generated Code Metadata:
========================
Original URL: https://1o2.ir
Prompt: What are some interesting questions to ask about TV and movies, and can you suggest a few based on popular sitcoms?
Generated: DETERMINISTIC_37c393654a7922fc
Batch ID: 20250622_211811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class MovieTVQuestions:
    """
    A class to generate interesting questions about TV shows and movies,
    particularly focusing on popular sitcoms.
    """

    def __init__(self):
        """
        Initializes the class with a list of popular sitcoms and their related questions.
        """
        self.sitcoms = {
            "Friends": [
                "What is your favorite episode of Friends and why?",
                "Which character do you relate to the most?",
                "If you could have dinner with any character from Friends, who would it be?"
            ],
            "The Office": [
                "Who is your favorite character from The Office and what makes them special?",
                "What is the most memorable quote from The Office?",
                "If you could work at Dunder Mifflin, which department would you want to be in?"
            ],
            "Parks and Recreation": [
                "Which Parks and Recreation character do you think has the best character development?",
                "What is your favorite moment from Parks and Recreation?",
                "If you could be any character from Parks and Recreation for a day, who would it be?"
            ],
            "Brooklyn Nine-Nine": [
                "What is your favorite cold open from Brooklyn Nine-Nine?",
                "Which character's storyline did you find the most compelling?",
                "If you could solve a case with any character from Brooklyn Nine-Nine, who would it be?"
            ]
        }

    def get_random_question(self, sitcom):
        """
        Returns a random question from the specified sitcom.

        Args:
            sitcom (str): The name of the sitcom to get a question from.

        Returns:
            str: A random question related to the specified sitcom.

        Raises:
            ValueError: If the sitcom is not found in the list.
        """
        if sitcom not in self.sitcoms:
            raise ValueError(f"Sitcom '{sitcom}' not found. Please choose from: {', '.join(self.sitcoms.keys())}")

        return random.choice(self.sitcoms[sitcom])

    def get_all_questions(self):
        """
        Returns a dictionary of all questions for each sitcom.

        Returns:
            dict: A dictionary containing sitcoms as keys and their questions as values.
        """
        return self.sitcoms

def main():
    """
    Main function to demonstrate the usage of the MovieTVQuestions class.
    """
    try:
        questions_generator = MovieTVQuestions()
        
        # Example usage: Get a random question from a specific sitcom
        sitcom = "Friends"
        question = questions_generator.get_random_question(sitcom)
        print(f"Random question from {sitcom}: {question}")

        # Display all questions for a specific sitcom
        all_questions = questions_generator.get_all_questions()
        print("\nAll questions by sitcom:")
        for sitcom_name, questions in all_questions.items():
            print(f"{sitcom_name}:")
            for q in questions:
                print(f" - {q}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
