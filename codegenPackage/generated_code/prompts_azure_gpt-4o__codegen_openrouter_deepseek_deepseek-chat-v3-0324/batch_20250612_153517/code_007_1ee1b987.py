"""
Generated Code Metadata:
========================
Original URL: https://otex.ae
Prompt: Create a chatbot that provides hearing aid support, including cleaning instructions and battery replacement guidance, inspired by Otex's support section.
Generated: DETERMINISTIC_1ee1b98765b80e56
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Any, Optional

class HearingAidChatbot:
    """
    A chatbot that provides hearing aid support, including cleaning instructions and battery replacement guidance.
    Inspired by Otex's support section.
    """

    def __init__(self):
        """
        Initialize the chatbot with predefined responses and knowledge base.
        """
        self.knowledge_base = self._load_knowledge_base()
        self.greetings = [
            "hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"
        ]
        self.exit_commands = [
            "exit", "quit", "bye", "goodbye", "stop", "end"
        ]

    def _load_knowledge_base(self) -> Dict[str, Any]:
        """
        Load the knowledge base from a JSON file or return default knowledge.

        Returns:
            Dict[str, Any]: The knowledge base containing responses.
        """
        try:
            with open('knowledge_base.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {
                "cleaning": {
                    "general": "To clean your hearing aid, use a soft, dry cloth. Avoid using water or cleaning solvents.",
                    "earwax": "For earwax removal, use the provided cleaning tool or a soft brush. Clean the microphone and receiver openings gently.",
                    "moisture": "If moisture is present, remove the battery and let the hearing aid dry overnight in a dry container."
                },
                "battery": {
                    "replacement": "To replace the battery, open the battery compartment and remove the old battery. Insert the new battery with the correct polarity.",
                    "lifespan": "Hearing aid batteries typically last 5-7 days, depending on usage.",
                    "storage": "Store batteries at room temperature and keep them in their original packaging until use."
                },
                "troubleshooting": {
                    "no_sound": "Check if the battery is inserted correctly and has charge. Ensure the hearing aid is turned on and the volume is adjusted.",
                    "feedback": "Feedback can occur if the hearing aid is not properly fitted. Try reinserting it or consult your audiologist.",
                    "distorted_sound": "This may be due to a low battery or earwax blockage. Try replacing the battery or cleaning the device."
                }
            }

    def get_response(self, user_input: str) -> Optional[str]:
        """
        Generate a response based on the user's input.

        Args:
            user_input (str): The user's input message.

        Returns:
            Optional[str]: The chatbot's response, or None if the user wants to exit.
        """
        user_input = user_input.lower().strip()

        if any(greeting in user_input for greeting in self.greetings):
            return "Hello! How can I assist you with your hearing aid today? You can ask about cleaning, battery replacement, or troubleshooting."

        if any(exit_command in user_input for exit_command in self.exit_commands):
            return None

        if "clean" in user_input or "cleaning" in user_input:
            if "earwax" in user_input:
                return self.knowledge_base["cleaning"]["earwax"]
            elif "moisture" in user_input:
                return self.knowledge_base["cleaning"]["moisture"]
            else:
                return self.knowledge_base["cleaning"]["general"]

        elif "battery" in user_input:
            if "replace" in user_input or "replacement" in user_input:
                return self.knowledge_base["battery"]["replacement"]
            elif "life" in user_input or "last" in user_input:
                return self.knowledge_base["battery"]["lifespan"]
            elif "store" in user_input or "storage" in user_input:
                return self.knowledge_base["battery"]["storage"]
            else:
                return "I can help with battery replacement, lifespan, or storage. Could you specify?"

        elif "troubleshoot" in user_input or "problem" in user_input or "issue" in user_input:
            if "no sound" in user_input or "not working" in user_input:
                return self.knowledge_base["troubleshooting"]["no_sound"]
            elif "feedback" in user_input or "whistling" in user_input:
                return self.knowledge_base["troubleshooting"]["feedback"]
            elif "distorted" in user_input or "unclear" in user_input:
                return self.knowledge_base["troubleshooting"]["distorted_sound"]
            else:
                return "I can help with common issues like no sound, feedback, or distorted sound. Could you specify?"

        else:
            return "I'm not sure I understand. You can ask about cleaning, battery replacement, or troubleshooting."

    def run(self):
        """
        Run the chatbot in an interactive loop.
        """
        print("Hearing Aid Support Chatbot: Hello! How can I assist you today? (Type 'exit' to quit)")

        while True:
            user_input = input("You: ")
            response = self.get_response(user_input)

            if response is None:
                print("Hearing Aid Support Chatbot: Goodbye! Have a great day.")
                break

            print(f"Hearing Aid Support Chatbot: {response}")

if __name__ == "__main__":
    chatbot = HearingAidChatbot()
    chatbot.run()
```
