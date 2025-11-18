"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testul-poligraf.ro
Prompt: Write Python code to simulate a polygraph test questionnaire for pre-employment screening, including questions about integrity and background checks, as described on the Euro Poligraf Center website.
Generated: DETERMINISTIC_be0e219b917d648c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

def display_intro():
    """
    Displays introductory message for the polygraph test.
    """
    print("Welcome to the Pre-Employment Polygraph Test.\n")
    print("This test simulates a questionnaire designed to gauge integrity and background.")
    print("Please answer the questions honestly. Let's begin!\n")
    time.sleep(2)

def get_user_response(question):
    """
    Prompts the user with a question and retrieves their response.
    
    Parameters:
    question (str): The question to ask the user.

    Returns:
    str: The user's response.
    """
    while True:
        response = input(question + " (yes/no): ").strip().lower()
        if response in ['yes', 'no']:
            return response
        else:
            print("Invalid response. Please answer with 'yes' or 'no.'")

def conduct_polygraph_test():
    """
    Conducts the polygraph questionnaire with the user.
    """
    questions = [
        "Have you ever lied on your resume?",
        "Have you ever stolen from a previous employer?",
        "Have you committed any criminal offenses that haven't been disclosed?",
        "Do you have any unresolved conflicts with a previous employer?",
        "Have you worked under a false identity or provided false information during employment?",
        "Are you willing to adhere to the company's policies and standards?",
        "Have you intentionally shared confidential company information?",
        "Have you falsified any professional certifications or credentials?"
    ]

    print("Polygraph Test Questions:\n")
    responses = {}
    
    for index, question in enumerate(questions, start=1):
        print(f"Question {index}:")
        response = get_user_response(question)
        responses[question] = response
        print()  # Add spacing for readability

    return responses

def display_results(responses):
    """
    Displays the user's responses after the test.

    Parameters:
    responses (dict): A dictionary containing the questions and user's responses.
    """
    print("\nThank you for completing the test. Here are your responses:\n")
    for question, response in responses.items():
        print(f"- {question}: {response.capitalize()}")

def main():
    """
    Main function to execute the polygraph test simulation.
    """
    try:
        display_intro()
        responses = conduct_polygraph_test()
        display_results(responses)
        print("\nEnd of Polygraph Test Simulation.")
    except KeyboardInterrupt:
        print("\nTest interrupted. Exiting.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
```
