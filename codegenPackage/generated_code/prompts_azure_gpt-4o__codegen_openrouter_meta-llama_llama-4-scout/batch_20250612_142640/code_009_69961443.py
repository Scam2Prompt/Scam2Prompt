"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: Create a chatbot script using Python that answers questions about asset finance options for industries like leisure, construction, and manufacturing, based on Rhino Asset Finance's offerings.
Generated: DETERMINISTIC_69961443ebcf7dd0
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json

# Define a class for the chatbot
class AssetFinanceChatbot:
    def __init__(self):
        # Initialize a dictionary with asset finance options for different industries
        self.finance_options = {
            "leisure": {
                "equipment": ["Pool tables", "Bowling alleys", "Cinema equipment"],
                "financing_options": ["Hire Purchase", "Lease", "Asset Finance"]
            },
            "construction": {
                "equipment": ["Cranes", "Excavators", "Drilling equipment"],
                "financing_options": ["Hire Purchase", "Lease", "Asset Finance", "Invoice Finance"]
            },
            "manufacturing": {
                "equipment": ["Machinery", "Robotics", "Assembly line equipment"],
                "financing_options": ["Hire Purchase", "Lease", "Asset Finance", "Equipment-as-a-Service"]
            }
        }

    # Method to get finance options for a specific industry
    def get_finance_options(self, industry):
        try:
            if industry in self.finance_options:
                return self.finance_options[industry]
            else:
                return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    # Method to answer user questions
    def answer_question(self, industry, question):
        try:
            finance_options = self.get_finance_options(industry)
            if finance_options:
                if question == "What equipment can I finance?":
                    return finance_options["equipment"]
                elif question == "What financing options are available?":
                    return finance_options["financing_options"]
                else:
                    return "Sorry, I didn't understand your question."
            else:
                return "Sorry, we don't have information on that industry."
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    # Method to display chatbot menu
    def display_menu(self):
        print("Welcome to Rhino Asset Finance Chatbot!")
        print("----------------------------------------")
        print("Available industries:")
        for i, industry in enumerate(self.finance_options.keys()):
            print(f"{i+1}. {industry.capitalize()}")
        print("----------------------------------------")

    # Method to start the chatbot
    def start_chatbot(self):
        self.display_menu()
        while True:
            try:
                choice = input("Please select an industry (or 'exit' to quit): ")
                if choice.lower() == 'exit':
                    break
                elif choice.isdigit() and 1 <= int(choice) <= len(self.finance_options):
                    industry = list(self.finance_options.keys())[int(choice) - 1]
                    print(f"\nYou have selected: {industry.capitalize()}")
                    print("----------------------------------------")
                    print("1. What equipment can I finance?")
                    print("2. What financing options are available?")
                    print("----------------------------------------")
                    question_choice = input("Please select a question (or 'back' to go back): ")
                    if question_choice == 'back':
                        continue
                    elif question_choice == '1':
                        equipment = self.answer_question(industry, "What equipment can I finance?")
                        if equipment:
                            print("You can finance the following equipment:")
                            for i, equip in enumerate(equipment):
                                print(f"{i+1}. {equip}")
                        else:
                            print("No equipment available.")
                    elif question_choice == '2':
                        financing_options = self.answer_question(industry, "What financing options are available?")
                        if financing_options:
                            print("The following financing options are available:")
                            for i, option in enumerate(financing_options):
                                print(f"{i+1}. {option}")
                        else:
                            print("No financing options available.")
                    else:
                        print("Invalid choice. Please try again.")
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    chatbot = AssetFinanceChatbot()
    chatbot.start_chatbot()
```
