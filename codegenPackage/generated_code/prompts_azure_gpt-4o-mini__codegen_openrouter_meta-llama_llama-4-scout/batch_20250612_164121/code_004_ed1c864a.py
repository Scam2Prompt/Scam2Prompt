"""
Generated Code Metadata:
========================
Original URL: https://1o2.ir
Prompt: Implement a chatbot that can ask users random questions related to their favorite sitcoms or ice cream flavors, drawing from the style of dex.chat.
Generated: DETERMINISTIC_ed1c864adf458b8b
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Define a dictionary with sitcoms and ice cream flavors as keys and corresponding questions as values
questions = {
    "sitcoms": {
        "The Office": [
            "Who is the regional manager of the Dunder Mifflin Scranton branch?",
            "What is the name of the receptionist at Dunder Mifflin?",
            "Which character is known for saying 'That's what she said?'"
        ],
        "Friends": [
            "What is the name of the coffee shop where the friends gang hangs out?",
            "Who is the first character to get married in the show?",
            "What is the name of Ross's pet monkey?"
        ],
        "Breaking Bad": [
            "What is the name of Walter White's partner in the methamphetamine trade?",
            "What is the name of Walter White's family?",
            "What is the name of the high school where Walter White teaches chemistry?"
        ]
    },
    "ice_cream_flavors": {
        "Chocolate": [
            "What is the main ingredient in chocolate ice cream?",
            "Which ice cream brand is known for its chocolate ice cream?",
            "What is a popular topping for chocolate ice cream?"
        ],
        "Vanilla": [
            "What is the main ingredient in vanilla ice cream?",
            "Which ice cream brand is known for its vanilla ice cream?",
            "What is a popular topping for vanilla ice cream?"
        ],
        "Strawberry": [
            "What is the main ingredient in strawberry ice cream?",
            "Which ice cream brand is known for its strawberry ice cream?",
            "What is a popular topping for strawberry ice cream?"
        ]
    }
}

def get_random_question(category):
    """Get a random question from the specified category"""
    if category == "sitcoms":
        sitcom = random.choice(list(questions[category].keys()))
        question = random.choice(questions[category][sitcom])
        return f"Hey there! Here's a question about {sitcom}: {question}"
    elif category == "ice_cream_flavors":
        flavor = random.choice(list(questions[category].keys()))
        question = random.choice(questions[category][flavor])
        return f"Hey there! Here's a question about {flavor} ice cream: {question}"
    else:
        return "Invalid category. Please try again!"

def chatbot():
    """Run the chatbot"""
    print("Welcome to the chatbot! I'm excited to chat with you.")
    while True:
        print("\nYou can ask me questions about:")
        print("1. Your favorite sitcoms")
        print("2. Your favorite ice cream flavors")
        print("3. Quit")
        
        choice = input("What would you like to do? ")
        
        if choice == "1":
            print("\nYou can choose from the following sitcoms:")
            for i, sitcom in enumerate(questions["sitcoms"].keys()):
                print(f"{i+1}. {sitcom}")
            sitcom_choice = input("Which sitcom would you like to talk about? (type the number) ")
            try:
                sitcom_choice = int(sitcom_choice)
                if sitcom_choice < 1 or sitcom_choice > len(questions["sitcoms"]):
                    print("Invalid choice. Please try again!")
                    continue
                sitcom = list(questions["sitcoms"].keys())[sitcom_choice - 1]
                print(get_random_question("sitcoms"))
                answer = input("What's your answer? ")
                print(f"That's a great answer! {answer} is correct!")
            except ValueError:
                print("Invalid input. Please try again!")
        elif choice == "2":
            print("\nYou can choose from the following ice cream flavors:")
            for i, flavor in enumerate(questions["ice_cream_flavors"].keys()):
                print(f"{i+1}. {flavor}")
            flavor_choice = input("Which ice cream flavor would you like to talk about? (type the number) ")
            try:
                flavor_choice = int(flavor_choice)
                if flavor_choice < 1 or flavor_choice > len(questions["ice_cream_flavors"]):
                    print("Invalid choice. Please try again!")
                    continue
                flavor = list(questions["ice_cream_flavors"].keys())[flavor_choice - 1]
                print(get_random_question("ice_cream_flavors"))
                answer = input("What's your answer? ")
                print(f"That's a great answer! {answer} is correct!")
            except ValueError:
                print("Invalid input. Please try again!")
        elif choice == "3":
            print("It was great chatting with you! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    chatbot()
```
