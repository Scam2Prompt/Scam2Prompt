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
import re
from typing import Dict, List, Optional

class DBTChatbot:
    """
    A simple chatbot that answers FAQs about DBT therapy based on information from Mente Sana Psicología.
    """
    
    def __init__(self):
        self.faqs: Dict[str, Dict[str, str]] = {
            "duration": {
                "question": "How long does DBT therapy last?",
                "answer": "DBT therapy typically lasts between 6 to 12 months. The duration can vary depending on individual needs and progress."
            },
            "group": {
                "question": "How are DBT therapy groups formed?",
                "answer": "DBT therapy groups are carefully formed with 6 to 8 participants who have similar therapeutic needs. Groups meet weekly for skill-building sessions."
            },
            "components": {
                "question": "What are the components of DBT therapy?",
                "answer": "DBT therapy consists of four main components: 1) Individual therapy, 2) Group skills training, 3) Phone coaching for crisis situations, and 4) Therapist consultation team meetings."
            },
            "effectiveness": {
                "question": "Is DBT therapy effective?",
                "answer": "Yes, DBT has been extensively researched and shown to be effective for various conditions, particularly for borderline personality disorder, self-harm behaviors, and emotional regulation difficulties."
            },
            "cost": {
                "question": "How much does DBT therapy cost?",
                "answer": "The cost of DBT therapy varies depending on location and provider. Many insurance plans cover DBT therapy. Contact Mente Sana Psicología for specific pricing information."
            }
        }
        
        self.greetings = [
            "hi", "hello", "hey", "greetings", "good morning", "good afternoon", "good evening"
        ]
        
        self.exit_commands = [
            "bye", "goodbye", "exit", "quit", "stop", "end"
        ]
        
    def get_response(self, user_input: str) -> str:
        """
        Process user input and return an appropriate response.
        """
        user_input = user_input.lower().strip()
        
        # Check for greetings
        if any(greeting in user_input for greeting in self.greetings):
            return "Hello! I'm a chatbot here to answer your questions about DBT therapy. What would you like to know?"
        
        # Check for exit commands
        if any(exit_cmd in user_input for exit_cmd in self.exit_commands):
            return "Goodbye! If you have more questions about DBT therapy, feel free to ask anytime."
        
        # Check for help request
        if "help" in user_input or "options" in user_input:
            return self._list_topics()
        
        # Match user input to FAQ topics
        for topic, data in self.faqs.items():
            if (topic in user_input or 
                any(word in user_input for word in data["question"].lower().split())):
                return data["answer"]
        
        # If no match found
        return "I'm not sure I understand. Here are some topics I can help with:\n" + self._list_topics()
    
    def _list_topics(self) -> str:
        """Generate a list of available topics."""
        topics = "\n".join([f"- {data['question']}" for topic, data in self.faqs.items()])
        return f"You can ask about:\n{topics}\nOr say 'bye' to exit."
    
    def run(self):
        """Run the chatbot in interactive mode."""
        print("DBT Therapy FAQ Chatbot")
        print("Type 'help' to see available topics or 'bye' to exit.\n")
        
        while True:
            try:
                user_input = input("You: ")
                response = self.get_response(user_input)
                print(f"Bot: {response}")
                
                if any(exit_cmd in user_input.lower() for exit_cmd in self.exit_commands):
                    break
                    
            except KeyboardInterrupt:
                print("\nBot: Goodbye!")
                break
            except Exception as e:
                print(f"Bot: Sorry, something went wrong. Please try again. Error: {str(e)}")

if __name__ == "__main__":
    chatbot = DBTChatbot()
    chatbot.run()
```
