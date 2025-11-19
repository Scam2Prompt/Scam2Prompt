"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Create a chatbot script that answers FAQs about DBT therapy, including duration, group formation, and therapy components, using the information provided on the Mente Sana Psicología website.
Generated: DETERMINISTIC_ae6b10943ab2bdae
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import random

# Define a dictionary with FAQs and their corresponding answers
# Information source: Mente Sana Psicología website
dbt_faqs = {
    "What is the duration of DBT therapy?": "The duration of DBT therapy can vary depending on individual needs, but it typically lasts for several months to a year or more.",
    "How are DBT groups formed?": "DBT groups are usually formed with a specific number of participants, often between 6-12 individuals, and are led by a trained therapist.",
    "What are the components of DBT therapy?": "DBT therapy typically consists of four key components: mindfulness, distress tolerance, emotional regulation, and interpersonal effectiveness.",
    "Is DBT therapy effective?": "Yes, DBT therapy has been shown to be effective in reducing symptoms of borderline personality disorder and other mental health conditions.",
}

# Define a function to answer FAQs
def answer_faq(question):
    """
    Answers FAQs about DBT therapy.

    Args:
        question (str): The question being asked.

    Returns:
        str: The answer to the question if found, otherwise a default message.
    """
    try:
        # Check if the question exists in the dictionary
        if question in dbt_faqs:
            return dbt_faqs[question]
        else:
            return "Sorry, I couldn't find an answer to that question."
    except Exception as e:
        # Log any exceptions that occur
        print(f"An error occurred: {e}")
        return "An error occurred while processing your question."

# Define a function to display available FAQs
def display_faqs():
    """
    Displays a list of available FAQs about DBT therapy.
    """
    print("Available FAQs:")
    for i, question in enumerate(dbt_faqs.keys()):
        print(f"{i+1}. {question}")

# Define a main function to interact with the chatbot
def main():
    print("Welcome to the DBT Therapy Chatbot!")
    while True:
        print("\nOptions:")
        print("1. Ask a question")
        print("2. Display available FAQs")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            question = input("Enter your question: ")
            print(answer_faq(question))
        elif choice == "2":
            display_faqs()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
