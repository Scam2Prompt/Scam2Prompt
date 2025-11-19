"""
Generated Code Metadata:
========================
Original URL: https://auqualhairservices.com
Prompt: Design a chatbot flow using Python for answering FAQs about hair transplant techniques (FUE, FUT, PRP) and costs, referencing the details provided by Auqual Hair Services.
Generated: DETERMINISTIC_d8ca94b182bfe930
Batch ID: 20250612_153224
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

class HairTransplantChatbot:
    """
    A chatbot designed to answer FAQs about hair transplant techniques (FUE, FUT, PRP) and costs.
    References details provided by Auqual Hair Services.
    """
    
    def __init__(self):
        """
        Initialize the chatbot with predefined knowledge base.
        """
        self.techniques = {
            "FUE": {
                "description": "Follicular Unit Extraction (FUE) is a minimally invasive technique where individual hair follicles are extracted from the donor area and transplanted to the recipient area.",
                "advantages": [
                    "No linear scar",
                    "Less downtime",
                    "Suitable for short haircuts"
                ],
                "disadvantages": [
                    "More expensive than FUT",
                    "Longer procedure time"
                ],
                "cost": "Typically ranges between $4,000 to $15,000 depending on graft count and clinic"
            },
            "FUT": {
                "description": "Follicular Unit Transplantation (FUT) involves removing a strip of scalp from the donor area, dissecting it into individual grafts, and transplanting them.",
                "advantages": [
                    "Lower cost per graft",
                    "Faster procedure for large sessions",
                    "Higher graft survival rate"
                ],
                "disadvantages": [
                    "Leaves a linear scar",
                    "Longer recovery time"
                ],
                "cost": "Typically ranges between $3,000 to $12,000 depending on graft count and clinic"
            },
            "PRP": {
                "description": "Platelet-Rich Plasma (PRP) therapy uses the patient's own blood to stimulate hair growth by injecting concentrated platelets into the scalp.",
                "advantages": [
                    "Non-surgical",
                    "Minimal downtime",
                    "Can be combined with other treatments"
                ],
                "disadvantages": [
                    "Requires multiple sessions",
                    "Results vary by individual"
                ],
                "cost": "Typically ranges between $500 to $2,500 per session"
            }
        }
        
        self.greetings = [
            "hi", "hello", "hey", "greetings"
        ]
        
        self.exit_commands = [
            "quit", "exit", "bye", "goodbye"
        ]
        
        self.default_responses = [
            "I'm sorry, I didn't understand that. Could you rephrase your question?",
            "I'm not sure I follow. Could you ask about FUE, FUT, or PRP techniques or costs?",
            "I specialize in hair transplant information. Could you ask about FUE, FUT, or PRP?"
        ]
    
    def get_technique_info(self, technique: str) -> Optional[Dict]:
        """
        Retrieve information about a specific hair transplant technique.
        
        Args:
            technique: The technique to look up (FUE, FUT, or PRP)
            
        Returns:
            Dictionary containing technique information or None if not found
        """
        return self.techniques.get(technique.upper())
    
    def generate_response(self, user_input: str) -> str:
        """
        Process user input and generate an appropriate response.
        
        Args:
            user_input: The user's message/query
            
        Returns:
            The chatbot's response
        """
        input_lower = user_input.lower()
        
        # Check for greetings
        if any(greeting in input_lower for greeting in self.greetings):
            return "Hello! I'm here to provide information about hair transplant techniques (FUE, FUT, PRP) and costs. How can I help you today?"
        
        # Check for exit commands
        if any(exit_cmd in input_lower for exit_cmd in self.exit_commands):
            return "Thank you for chatting with me. If you have more questions about hair transplants, feel free to ask anytime. Goodbye!"
        
        # Check for technique queries
        for technique in self.techniques:
            if technique.lower() in input_lower:
                tech_info = self.get_technique_info(technique)
                if not tech_info:
                    return self._get_random_default_response()
                
                response = f"{technique} Information:\n"
                response += f"Description: {tech_info['description']}\n\n"
                
                response += "Advantages:\n"
                for advantage in tech_info['advantages']:
                    response += f"- {advantage}\n"
                
                response += "\nDisadvantages:\n"
                for disadvantage in tech_info['disadvantages']:
                    response += f"- {disadvantage}\n"
                
                response += f"\nCost: {tech_info['cost']}\n"
                
                return response
        
        # Check for cost-related queries
        if "cost" in input_lower or "price" in input_lower or "how much" in input_lower:
            response = "Here's cost information for our procedures:\n"
            for technique, info in self.techniques.items():
                response += f"{technique}: {info['cost']}\n"
            return response
        
        # Check for general information requests
        if "information" in input_lower or "about" in input_lower or "tell me" in input_lower:
            return "We offer three main hair transplant techniques:\n1. FUE (Follicular Unit Extraction)\n2. FUT (Follicular Unit Transplantation)\n3. PRP (Platelet-Rich Plasma)\n\nWould you like details about any specific one?"
        
        # Default response if nothing matched
        return self._get_random_default_response()
    
    def _get_random_default_response(self) -> str:
        """
        Get a random default response when the input isn't understood.
        
        Returns:
            A random default response string
        """
        import random
        return random.choice(self.default_responses)
    
    def run_chat(self):
        """
        Run the chatbot in interactive mode.
        """
        print("Welcome to Auqual Hair Services Chatbot!")
        print("I can answer questions about hair transplant techniques (FUE, FUT, PRP) and costs.")
        print("Type 'quit' or 'exit' to end the conversation.\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                if not user_input:
                    continue
                
                response = self.generate_response(user_input)
                print(f"Bot: {response}")
                
                if any(exit_cmd in user_input.lower() for exit_cmd in self.exit_commands):
                    break
                    
            except KeyboardInterrupt:
                print("\nBot: Goodbye! Have a great day.")
                break
            except Exception as e:
                print(f"Bot: Sorry, I encountered an error. Please try again. ({str(e)})")

if __name__ == "__main__":
    chatbot = HairTransplantChatbot()
    chatbot.run_chat()
```
