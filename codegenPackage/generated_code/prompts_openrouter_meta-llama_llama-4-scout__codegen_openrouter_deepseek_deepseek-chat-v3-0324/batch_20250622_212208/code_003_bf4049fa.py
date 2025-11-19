"""
Generated Code Metadata:
========================
Original URL: https://refund-me.net
Prompt: Develop a basic chatbot dialogue flow to help users understand the Refund-me process, including the investigation, bank, and FOS stages.
Generated: DETERMINISTIC_bf4049faebd932a6
Batch ID: 20250622_212208
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

class Chatbot:
    """
    A simple chatbot to guide users through the Refund-me process.
    Handles dialogue flow for investigation, bank, and FOS stages.
    """
    
    def __init__(self):
        self.responses = self._load_responses()
        self.current_stage = "welcome"
        self.user_context = {}
    
    def _load_responses(self) -> Dict[str, Dict]:
        """Load predefined responses from a JSON structure."""
        return {
            "welcome": {
                "message": "Welcome to Refund-me assistance. How can I help you today?",
                "options": [
                    {"text": "Tell me about the refund process", "next_stage": "process_overview"},
                    {"text": "What is the investigation stage?", "next_stage": "investigation"},
                    {"text": "How does the bank handle my claim?", "next_stage": "bank_stage"},
                    {"text": "What if I disagree with the bank's decision?", "next_stage": "fos_stage"}
                ]
            },
            "process_overview": {
                "message": "The refund process has 3 main stages:\n1. Investigation - We gather evidence\n2. Bank Review - Your bank assesses the claim\n3. FOS - Financial Ombudsman if you're unhappy",
                "options": [
                    {"text": "Tell me about investigation", "next_stage": "investigation"},
                    {"text": "Tell me about bank review", "next_stage": "bank_stage"},
                    {"text": "Tell me about FOS", "next_stage": "fos_stage"},
                    {"text": "Back to main menu", "next_stage": "welcome"}
                ]
            },
            "investigation": {
                "message": "During investigation, we collect evidence like transaction records and communications. This typically takes 2-4 weeks.",
                "options": [
                    {"text": "What evidence is needed?", "next_stage": "investigation_evidence"},
                    {"text": "How long does it take?", "next_stage": "investigation_time"},
                    {"text": "Back to main menu", "next_stage": "welcome"}
                ]
            },
            "investigation_evidence": {
                "message": "We typically need:\n- Transaction details\n- Communication with the merchant\n- Proof of non-delivery/faulty goods",
                "options": [
                    {"text": "Back to investigation", "next_stage": "investigation"},
                    {"text": "Back to main menu", "next_stage": "welcome"}
                ]
            },
            "investigation_time": {
                "message": "The investigation usually takes 2-4 weeks depending on case complexity and response times.",
                "options": [
                    {"text": "Back to investigation", "next_stage": "investigation"},
                    {"text": "Back to main menu", "next_stage": "welcome"}
                ]
            },
            "bank_stage": {
                "message": "Your bank reviews our evidence and makes a decision. They have 8 weeks to respond under UK regulations.",
                "options": [
                    {"text": "What if they reject my claim?", "next_stage": "bank_rejection"},
                    {"text": "What's the time limit?", "next_stage": "bank_time"},
                    {"text": "Back to main menu", "next_stage": "welcome"}
                ]
            },
            "bank_rejection": {
                "message": "If rejected, you can escalate to the Financial Ombudsman Service (FOS) within 6 months.",
                "options": [
                    {"text": "Tell me about FOS", "next_stage": "fos_stage"},
                    {"text": "Back to bank stage", "next_stage": "bank_stage"},
                    {"text": "Back to main menu", "next_stage": "welcome"}
                ]
            },
            "bank_time": {
                "message": "Banks have up to 8 weeks to respond under UK regulations. Complex cases may take longer.",
                "options": [
                    {"text": "Back to bank stage", "next_stage": "bank_stage"},
                    {"text": "Back to main menu", "next_stage": "welcome"}
                ]
            },
            "fos_stage": {
                "message": "The Financial Ombudsman Service (FOS) is independent. They review cases within 3-6 months and their decision is binding on the bank.",
                "options": [
                    {"text": "How do I contact FOS?", "next_stage": "fos_contact"},
                    {"text": "Is there a time limit?", "next_stage": "fos_time"},
                    {"text": "Back to main menu", "next_stage": "welcome"}
                ]
            },
            "fos_contact": {
                "message": "You can contact FOS:\nPhone: 0800 023 4567\nWebsite: www.financial-ombudsman.org.uk",
                "options": [
                    {"text": "Back to FOS", "next_stage": "fos_stage"},
                    {"text": "Back to main menu", "next_stage": "welcome"}
                ]
            },
            "fos_time": {
                "message": "You must contact FOS within 6 months of your bank's final response.",
                "options": [
                    {"text": "Back to FOS", "next_stage": "fos_stage"},
                    {"text": "Back to main menu", "next_stage": "welcome"}
                ]
            }
        }
    
    def get_response(self, user_input: Optional[str] = None) -> Dict:
        """
        Get the chatbot's response based on current stage and optional user input.
        
        Args:
            user_input: Optional text input from user to select an option
            
        Returns:
            Dictionary containing message and options
        """
        try:
            if user_input and self.current_stage != "welcome":
                # Handle option selection
                current_options = self.responses[self.current_stage]["options"]
                selected_option = next(
                    (opt for opt in current_options if opt["text"].lower() == user_input.lower()),
                    None
                )
                if selected_option:
                    self.current_stage = selected_option["next_stage"]
            
            response = self.responses.get(self.current_stage, self.responses["welcome"])
            return {
                "message": response["message"],
                "options": [opt["text"] for opt in response["options"]]
            }
        
        except Exception as e:
            return {
                "message": "Sorry, something went wrong. Let's start again.",
                "options": [opt["text"] for opt in self.responses["welcome"]["options"]]
            }

# Example usage
if __name__ == "__main__":
    bot = Chatbot()
    print(bot.get_response()["message"])
    
    while True:
        options = bot.get_response()["options"]
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        try:
            choice = int(input("Select an option (number): "))
            if 1 <= choice <= len(options):
                user_input = options[choice-1]
                response = bot.get_response(user_input)
                print("\n" + response["message"] + "\n")
            else:
                print("Invalid option. Please try again.\n")
        except ValueError:
            print("Please enter a valid number.\n")
```
