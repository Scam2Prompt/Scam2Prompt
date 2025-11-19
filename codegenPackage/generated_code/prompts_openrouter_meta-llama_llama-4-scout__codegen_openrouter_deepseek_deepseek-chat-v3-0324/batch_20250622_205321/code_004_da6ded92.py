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
import json
from typing import Dict, Any

class BodhghhatChatbot:
    """
    A simple chatbot that provides information about the Bodhghhat project.
    """
    
    def __init__(self):
        """
        Initialize the chatbot with project data.
        """
        self.project_data = {
            "name": "Bodhghhat Project",
            "location": "Bodhghhat, India",
            "cost": "Approximately ₹200 crore",
            "status": "Under construction",
            "description": "A major infrastructure project aimed at improving transportation and connectivity."
        }
    
    def get_response(self, user_input: str) -> str:
        """
        Generate a response based on user input about the Bodhghhat project.
        
        Args:
            user_input (str): The user's query about the project.
            
        Returns:
            str: The chatbot's response.
        """
        user_input = user_input.lower().strip()
        
        if "cost" in user_input:
            return f"The estimated cost of the Bodhghhat project is {self.project_data['cost']}."
        elif "location" in user_input or "where" in user_input:
            return f"The Bodhghhat project is located in {self.project_data['location']}."
        elif "status" in user_input:
            return f"The current status of the Bodhghhat project is: {self.project_data['status']}."
        elif "info" in user_input or "about" in user_input:
            return self._format_project_info()
        else:
            return "I can provide information about the Bodhghhat project. Ask about its cost, location, or status."
    
    def _format_project_info(self) -> str:
        """
        Format all project information into a readable string.
        
        Returns:
            str: Formatted project information.
        """
        return (
            f"Project Name: {self.project_data['name']}\n"
            f"Location: {self.project_data['location']}\n"
            f"Estimated Cost: {self.project_data['cost']}\n"
            f"Current Status: {self.project_data['status']}\n"
            f"Description: {self.project_data['description']}"
        )

def main():
    """
    Main function to run the Bodhghhat chatbot.
    """
    chatbot = BodhghhatChatbot()
    print("Welcome to the Bodhghhat Project Information Chatbot!")
    print("Type 'exit' to quit the conversation.\n")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}\n")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Bot: Sorry, an error occurred. Please try again. Error: {str(e)}")

if __name__ == "__main__":
    main()
```
