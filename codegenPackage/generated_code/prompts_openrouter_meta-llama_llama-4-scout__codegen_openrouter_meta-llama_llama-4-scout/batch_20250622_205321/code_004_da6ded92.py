"""
Generated Code Metadata:
========================
Original URL: https://protsahitnews18.com
Prompt: Develop a simple chatbot that provides information on the Bodhghhat project, including its cost, location, and current status.
Generated: DETERMINISTIC_da6ded929f7d43f4
Batch ID: 20250622_205321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# chatbot.py

class BodhghhatProject:
    def __init__(self):
        self.cost = 2586.0  # in crores
        self.location = "Meghalaya, India"
        self.status = "Under construction"

    def get_cost(self):
        return f"The estimated cost of the Bodhghhat project is ₹{self.cost} crores."

    def get_location(self):
        return f"The Bodhghhat project is located in {self.location}."

    def get_status(self):
        return f"The current status of the Bodhghhat project is {self.status}."


class Chatbot:
    def __init__(self):
        self.project = BodhghhatProject()

    def start(self):
        print("Welcome to the Bodhghhat project chatbot!")
        while True:
            user_input = input("You: ").lower()
            if user_input in ["exit", "quit"]:
                print("Chatbot: Goodbye!")
                break
            elif user_input in ["cost", "project cost"]:
                print("Chatbot:", self.project.get_cost())
            elif user_input in ["location", "project location"]:
                print("Chatbot:", self.project.get_location())
            elif user_input in ["status", "project status"]:
                print("Chatbot:", self.project.get_status())
            else:
                print("Chatbot: Sorry, I didn't understand that. Please try again.")

def main():
    try:
        chatbot = Chatbot()
        chatbot.start()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

```python
# test_chatbot.py

import unittest
from chatbot import BodhghhatProject, Chatbot

class TestBodhghhatProject(unittest.TestCase):
    def test_get_cost(self):
        project = BodhghhatProject()
        self.assertEqual(project.get_cost(), "The estimated cost of the Bodhghhat project is ₹2586.0 crores.")

    def test_get_location(self):
        project = BodhghhatProject()
        self.assertEqual(project.get_location(), "The Bodhghhat project is located in Meghalaya, India.")

    def test_get_status(self):
        project = BodhghhatProject()
        self.assertEqual(project.get_status(), "The current status of the Bodhghhat project is Under construction.")

class TestChatbot(unittest.TestCase):
    def test_start(self):
        chatbot = Chatbot()
        # Test that the chatbot starts without errors
        try:
            chatbot.start()
        except Exception:
            self.fail("Chatbot failed to start")

if __name__ == "__main__":
    unittest.main()
```
