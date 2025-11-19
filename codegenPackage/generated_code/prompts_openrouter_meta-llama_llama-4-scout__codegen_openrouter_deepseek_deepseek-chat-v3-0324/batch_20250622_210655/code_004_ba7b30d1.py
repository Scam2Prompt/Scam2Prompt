"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Develop a prompt for a chatbot that provides customer support for a cleaning services company like Maria HouseKeepers, including answers to frequently asked questions.
Generated: DETERMINISTIC_ba7b30d1c23ecd88
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class CleaningServiceChatbot:
    """
    A chatbot for customer support of a cleaning services company.
    Handles frequently asked questions and provides appropriate responses.
    """
    
    def __init__(self):
        self.faq_responses = self._load_faq_responses()
        self.greetings = [
            "hi", "hello", "hey", "greetings", "good morning", 
            "good afternoon", "good evening"
        ]
        self.goodbyes = [
            "bye", "goodbye", "see you", "farewell", "quit", "exit"
        ]
    
    def _load_faq_responses(self) -> Dict[str, Dict]:
        """Load FAQ responses from a JSON file."""
        try:
            with open('faq_responses.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "default": {
                    "response": "I'm sorry, I couldn't find the information you're looking for. Please contact our support team for assistance."
                }
            }
    
    def _get_response(self, intent: str) -> Optional[Dict]:
        """Get response for a specific intent."""
        return self.faq_responses.get(intent.lower(), self.faq_responses["default"])
    
    def _detect_intent(self, user_input: str) -> str:
        """Detect the intent from user input."""
        input_lower = user_input.lower()
        
        # Check for greetings
        if any(greeting in input_lower for greeting in self.greetings):
            return "greeting"
        
        # Check for goodbyes
        if any(goodbye in input_lower for goodbye in self.goodbyes):
            return "goodbye"
        
        # Check for FAQ intents
        for intent in self.faq_responses:
            if intent == "default":
                continue
            for keyword in self.faq_responses[intent]["keywords"]:
                if keyword in input_lower:
                    return intent
        
        return "unknown"
    
    def generate_response(self, user_input: str) -> str:
        """
        Generate a response based on user input.
        
        Args:
            user_input: The input text from the user.
            
        Returns:
            str: The generated response.
        """
        if not user_input.strip():
            return "Please type your question or concern."
            
        intent = self._detect_intent(user_input)
        
        if intent == "greeting":
            return "Hello! Welcome to Maria HouseKeepers. How can I assist you today?"
        elif intent == "goodbye":
            return "Thank you for contacting Maria HouseKeepers. Have a wonderful day!"
        elif intent == "unknown":
            return "I'm not sure I understand. Could you please rephrase your question?"
        
        response_data = self._get_response(intent)
        return response_data["response"]
    
    def get_suggested_questions(self) -> List[str]:
        """Get a list of suggested questions for the user."""
        return [
            "What services do you offer?",
            "How much does your cleaning service cost?",
            "Are your cleaners insured?",
            "Do I need to provide cleaning supplies?",
            "How do I schedule a cleaning?"
        ]


# Example FAQ responses JSON file content (would be in faq_responses.json)
"""
{
    "services": {
        "keywords": ["services", "offer", "provide", "do you clean"],
        "response": "We offer a variety of cleaning services including regular house cleaning, deep cleaning, move-in/move-out cleaning, and office cleaning. Would you like more details about any specific service?"
    },
    "pricing": {
        "keywords": ["cost", "price", "how much", "rate", "pricing"],
        "response": "Our pricing depends on the size of your space and the type of cleaning required. A standard cleaning for a 2-bedroom apartment typically starts at $120. Would you like a more accurate quote?"
    },
    "insurance": {
        "keywords": ["insured", "bonded", "liability", "damage"],
        "response": "Yes, all our cleaners are fully insured and bonded. Your property is protected in the rare case of any damage during cleaning."
    },
    "supplies": {
        "keywords": ["supplies", "equipment", "bring", "provide"],
        "response": "Our cleaners bring all necessary cleaning supplies and equipment. However, if you prefer us to use specific products you have, we're happy to accommodate that request."
    },
    "scheduling": {
        "keywords": ["schedule", "book", "appointment", "availability", "when"],
        "response": "You can schedule a cleaning by calling us at (555) 123-4567 or through our website. Our typical availability is Monday through Saturday from 8 AM to 6 PM."
    },
    "default": {
        "response": "I'm sorry, I couldn't find the information you're looking for. Please contact our support team at support@mariahousekeepers.com for assistance."
    }
}
"""
```
