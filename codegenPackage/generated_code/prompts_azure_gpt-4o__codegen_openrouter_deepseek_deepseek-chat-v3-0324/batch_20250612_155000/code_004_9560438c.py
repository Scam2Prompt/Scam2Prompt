"""
Generated Code Metadata:
========================
Original URL: https://paybackclaimltd.com
Prompt: Suggest a legal consultation chatbot design that helps users navigate cryptocurrency fraud disputes, inspired by the legal consultation services offered by Payback Claim Ltd.
Generated: DETERMINISTIC_9560438c3af37cbe
Batch ID: 20250612_155000
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
from enum import Enum

class FraudType(Enum):
    PHISHING = "Phishing"
    PONZI_SCHEME = "Ponzi Scheme"
    FAKE_ICO = "Fake ICO"
    PUMP_AND_DUMP = "Pump and Dump"
    RUG_PULL = "Rug Pull"
    OTHER = "Other"

class ConsultationStep(Enum):
    GREETING = 1
    FRAUD_TYPE = 2
    DETAILS = 3
    EVIDENCE = 4
    CONTACT_INFO = 5
    SUMMARY = 6
    CONCLUSION = 7

class LegalConsultationChatbot:
    """
    A chatbot designed to assist users in navigating cryptocurrency fraud disputes.
    Inspired by Payback Claim Ltd's legal consultation services.
    """
    
    def __init__(self):
        self.user_data: Dict = {}
        self.current_step: ConsultationStep = ConsultationStep.GREETING
        self.fraud_types: List[str] = [ft.value for ft in FraudType]
        
    def start(self) -> str:
        """Initialize the consultation session."""
        self._reset_session()
        return self._get_greeting_message()
    
    def handle_response(self, user_input: str) -> str:
        """
        Process user input and return appropriate response based on current step.
        
        Args:
            user_input: User's response to the current step's prompt
            
        Returns:
            str: The chatbot's response to the user
        """
        try:
            if self.current_step == ConsultationStep.GREETING:
                return self._handle_greeting_response()
                
            elif self.current_step == ConsultationStep.FRAUD_TYPE:
                return self._handle_fraud_type_response(user_input)
                
            elif self.current_step == ConsultationStep.DETAILS:
                return self._handle_details_response(user_input)
                
            elif self.current_step == ConsultationStep.EVIDENCE:
                return self._handle_evidence_response(user_input)
                
            elif self.current_step == ConsultationStep.CONTACT_INFO:
                return self._handle_contact_info_response(user_input)
                
            elif self.current_step == ConsultationStep.SUMMARY:
                return self._handle_summary_response(user_input)
                
            else:
                return "Thank you for using our consultation service. A legal expert will contact you shortly."
                
        except Exception as e:
            self._reset_session()
            return f"An error occurred: {str(e)}. Please start over."
    
    def _reset_session(self) -> None:
        """Reset the consultation session."""
        self.user_data = {}
        self.current_step = ConsultationStep.GREETING
    
    def _get_greeting_message(self) -> str:
        """Generate greeting message."""
        return (
            "Welcome to Crypto Fraud Legal Consultation Service.\n"
            "We'll help you navigate your cryptocurrency fraud dispute.\n"
            "Let's begin by understanding your situation.\n\n"
            "Type 'start' to begin or 'help' for assistance."
        )
    
    def _handle_greeting_response(self) -> str:
        """Process greeting response and move to next step."""
        self.current_step = ConsultationStep.FRAUD_TYPE
        return (
            "What type of cryptocurrency fraud are you reporting?\n"
            "Please choose from the following options:\n"
            f"{', '.join(self.fraud_types)}\n"
            "Or type 'other' if your case doesn't fit these categories."
        )
    
    def _handle_fraud_type_response(self, user_input: str) -> str:
        """Process fraud type selection and move to next step."""
        if user_input.lower() == 'other':
            self.user_data['fraud_type'] = FraudType.OTHER.value
        else:
            for ft in self.fraud_types:
                if user_input.lower() == ft.lower():
                    self.user_data['fraud_type'] = ft
                    break
            else:
                return "Invalid selection. Please choose from the provided options."
        
        self.current_step = ConsultationStep.DETAILS
        return (
            "Please describe your situation in detail:\n"
            "- When did this occur?\n"
            "- How much cryptocurrency/value was involved?\n"
            "- Any other relevant details."
        )
    
    def _handle_details_response(self, user_input: str) -> str:
        """Process fraud details and move to next step."""
        self.user_data['details'] = user_input
        self.current_step = ConsultationStep.EVIDENCE
        return (
            "Do you have any evidence to support your claim?\n"
            "(e.g., transaction IDs, screenshots, emails, wallet addresses)\n"
            "Please describe what evidence you have available."
        )
    
    def _handle_evidence_response(self, user_input: str) -> str:
        """Process evidence information and move to next step."""
        self.user_data['evidence'] = user_input
        self.current_step = ConsultationStep.CONTACT_INFO
        return (
            "Please provide your contact information:\n"
            "- Full name\n"
            "- Email address\n"
            "- Phone number (optional)\n"
            "Format: Name, Email, Phone"
        )
    
    def _handle_contact_info_response(self, user_input: str) -> str:
        """Process contact information and move to next step."""
        parts = [p.strip() for p in user_input.split(',')]
        if len(parts) < 2:
            return "Please provide at least your name and email."
            
        self.user_data['name'] = parts[0]
        self.user_data['email'] = parts[1]
        self.user_data['phone'] = parts[2] if len(parts) > 2 else None
        
        self.current_step = ConsultationStep.SUMMARY
        return self._generate_summary()
    
    def _handle_summary_response(self, user_input: str) -> str:
        """Process summary confirmation and conclude consultation."""
        if user_input.lower() in ['yes', 'y']:
            self.current_step = ConsultationStep.CONCLUSION
            return (
                "Thank you for providing this information.\n"
                "A legal expert will review your case and contact you within 24 hours.\n"
                "Your case reference number is: CB-" + self._generate_case_number()
            )
        else:
            self._reset_session()
            return "Let's start over. Type 'start' to begin."
    
    def _generate_summary(self) -> str:
        """Generate a summary of the collected information."""
        summary = (
            "Please review your information:\n\n"
            f"Fraud Type: {self.user_data.get('fraud_type', 'Not specified')}\n"
            f"Details: {self.user_data.get('details', 'Not provided')}\n"
            f"Evidence: {self.user_data.get('evidence', 'Not provided')}\n"
            f"Name: {self.user_data.get('name', 'Not provided')}\n"
            f"Email: {self.user_data.get('email', 'Not provided')}\n"
            f"Phone: {self.user_data.get('phone', 'Not provided')}\n\n"
            "Is this information correct? (yes/no)"
        )
        return summary
    
    def _generate_case_number(self) -> str:
        """Generate a unique case reference number."""
        import uuid
        return str(uuid.uuid4())[:8].upper()
    
    def save_session(self, file_path: str) -> bool:
        """Save the current session data to a file."""
        try:
            with open(file_path, 'w') as f:
                json.dump(self.user_data, f)
            return True
        except Exception:
            return False
    
    def load_session(self, file_path: str) -> bool:
        """Load session data from a file."""
        try:
            with open(file_path, 'r') as f:
                self.user_data = json.load(f)
            return True
        except Exception:
            return False

# Example usage
if __name__ == "__main__":
    chatbot = LegalConsultationChatbot()
    print(chatbot.start())
    
    while True:
        user_input = input("> ")
        if user_input.lower() == 'exit':
            break
            
        response = chatbot.handle_response(user_input)
        print(response)
        
        if chatbot.current_step == ConsultationStep.CONCLUSION:
            break
```
