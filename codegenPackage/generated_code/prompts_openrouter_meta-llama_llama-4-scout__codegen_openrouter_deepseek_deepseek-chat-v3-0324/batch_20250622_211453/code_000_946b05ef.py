"""
Generated Code Metadata:
========================
Original URL: https://amarparasanar.com.mx
Prompt: Write a Python script to create a simple chatbot that offers emotional support and connects users with therapists, incorporating the principles of Bioneuroemoción and EMDR therapy.
Generated: DETERMINISTIC_946b05ef1bf2edb1
Batch ID: 20250622_211453
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
import time
from typing import Dict, List, Optional

class Chatbot:
    """
    A simple chatbot that offers emotional support and connects users with therapists.
    Incorporates principles of Bioneuroemoción and EMDR therapy.
    """

    def __init__(self):
        """Initialize the chatbot with predefined responses and resources."""
        self.responses = self._load_responses()
        self.therapists = self._load_therapists()
        self.user_state: Dict[str, str] = {}

    def _load_responses(self) -> Dict[str, List[str]]:
        """Load predefined responses from a JSON file or default to built-in responses."""
        try:
            with open('responses.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "greeting": [
                    "Hello! I'm here to offer emotional support. How are you feeling today?",
                    "Hi there! I'm your emotional support chatbot. What's on your mind?"
                ],
                "support": [
                    "I hear you. It's okay to feel this way. Would you like to explore these emotions further?",
                    "That sounds challenging. Let's work through this together."
                ],
                "bioneuroemotion": [
                    "In Bioneuroemoción, we explore the emotional roots of physical symptoms. Can you describe any physical sensations you're experiencing?",
                    "This might be linked to an unconscious emotional conflict. Let's explore possible triggers."
                ],
                "emdr": [
                    "EMDR therapy can help process traumatic memories. Would you like to try a simple grounding exercise?",
                    "Let's focus on a safe place. Can you visualize a calming scene?"
                ],
                "therapist": [
                    "It might help to speak with a professional. Would you like me to connect you with a therapist?",
                    "I can provide a list of therapists specializing in your needs."
                ],
                "goodbye": [
                    "Take care of yourself. Remember, help is always available.",
                    "Wishing you peace. Don't hesitate to reach out again."
                ]
            }

    def _load_therapists(self) -> List[Dict[str, str]]:
        """Load therapist data from a JSON file or default to built-in list."""
        try:
            with open('therapists.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return [
                {
                    "name": "Dr. Jane Smith",
                    "specialty": "Bioneuroemoción",
                    "contact": "jane@therapy.com"
                },
                {
                    "name": "Dr. John Doe",
                    "specialty": "EMDR Therapy",
                    "contact": "john@therapy.com"
                }
            ]

    def get_response(self, user_input: str) -> str:
        """
        Generate a response based on user input and current state.
        
        Args:
            user_input: The user's message.
        
        Returns:
            A response string.
        """
        user_input = user_input.lower()

        if any(word in user_input for word in ["hello", "hi", "hey"]):
            return random.choice(self.responses["greeting"])
        
        elif any(word in user_input for word in ["sad", "anxious", "stressed", "upset"]):
            self.user_state["needs_support"] = "true"
            return random.choice(self.responses["support"])
        
        elif any(word in user_input for word in ["physical", "pain", "sensation"]):
            self.user_state["exploring_bioneuroemotion"] = "true"
            return random.choice(self.responses["bioneuroemotion"])
        
        elif any(word in user_input for word in ["trauma", "memory", "emdr"]):
            self.user_state["exploring_emdr"] = "true"
            return random.choice(self.responses["emdr"])
        
        elif any(word in user_input for word in ["therapist", "professional", "help"]):
            return self._handle_therapist_request()
        
        elif any(word in user_input for word in ["bye", "goodbye", "exit"]):
            return random.choice(self.responses["goodbye"])
        
        else:
            return "I'm here to listen. Can you tell me more about how you're feeling?"

    def _handle_therapist_request(self) -> str:
        """Generate therapist recommendations based on user state."""
        if "exploring_bioneuroemotion" in self.user_state:
            therapists = [t for t in self.therapists if t["specialty"] == "Bioneuroemoción"]
        elif "exploring_emdr" in self.user_state:
            therapists = [t for t in self.therapists if t["specialty"] == "EMDR Therapy"]
        else:
            therapists = self.therapists

        if not therapists:
            return "I couldn't find any therapists matching your needs. Please try again later."

        response = "Here are some therapists who might help:\n"
        for therapist in therapists[:3]:  # Limit to 3 recommendations
            response += f"- {therapist['name']} ({therapist['specialty']}): {therapist['contact']}\n"
        
        return response

    def run(self):
        """Run the chatbot interactively."""
        print("Chatbot: " + random.choice(self.responses["greeting"]))
        
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "bye", "goodbye"]:
                print("Chatbot: " + random.choice(self.responses["goodbye"]))
                break
            
            response = self.get_response(user_input)
            print("Chatbot: " + response)

            # Simulate typing delay for more natural interaction
            time.sleep(1)

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.run()
```
