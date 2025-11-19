"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.web.app
Prompt: Create a sample application questionnaire for the Sui Foundation's Developer Grants Program, ensuring it emphasizes the project's impact on decentralization.
Generated: DETERMINISTIC_756add81d3aca771
Batch ID: 20250612_162311
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

class SuiGrantApplication:
    """
    A sample application questionnaire for the Sui Foundation's Developer Grants Program.
    This class handles the application form, validation, and submission.
    """

    def __init__(self):
        self.questions = {
            "project_name": "Project Name",
            "team_name": "Team Name",
            "contact_email": "Contact Email",
            "project_description": "Brief Project Description (max 500 chars)",
            "decentralization_impact": "How does your project contribute to decentralization in the Sui ecosystem? (max 1000 chars)",
            "technical_implementation": "Technical Implementation Details (max 1000 chars)",
            "roadmap": "Project Roadmap (max 1000 chars)",
            "funding_request": "Funding Request (in USD)",
            "additional_notes": "Additional Notes (optional, max 500 chars)"
        }
        self.responses: Dict[str, str] = {}
        self.max_lengths = {
            "project_description": 500,
            "decentralization_impact": 1000,
            "technical_implementation": 1000,
            "roadmap": 1000,
            "additional_notes": 500
        }

    def validate_response(self, question_id: str, response: str) -> bool:
        """
        Validate a response based on question requirements.
        
        Args:
            question_id: The ID of the question being validated
            response: The user's response to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        if question_id not in self.questions:
            return False
            
        if question_id in ["project_name", "team_name", "contact_email"]:
            if not response.strip():
                return False
            if question_id == "contact_email" and "@" not in response:
                return False
            return True
            
        if question_id in self.max_lengths:
            return len(response) <= self.max_lengths[question_id]
            
        if question_id == "funding_request":
            try:
                amount = float(response)
                return amount > 0
            except ValueError:
                return False
                
        return True

    def add_response(self, question_id: str, response: str) -> bool:
        """
        Add a validated response to the application.
        
        Args:
            question_id: The ID of the question
            response: The user's response
            
        Returns:
            bool: True if successfully added, False if validation failed
        """
        if not self.validate_response(question_id, response):
            return False
            
        self.responses[question_id] = response
        return True

    def is_complete(self) -> bool:
        """
        Check if all required questions have been answered.
        
        Returns:
            bool: True if application is complete, False otherwise
        """
        required_fields = set(self.questions.keys()) - {"additional_notes"}
        return required_fields.issubset(self.responses.keys())

    def generate_application_json(self) -> Optional[str]:
        """
        Generate a JSON representation of the completed application.
        
        Returns:
            Optional[str]: JSON string if application is complete, None otherwise
        """
        if not self.is_complete():
            return None
            
        return json.dumps(self.responses, indent=2)

    def display_questions(self) -> List[str]:
        """
        Get a list of all questions in the application.
        
        Returns:
            List[str]: List of formatted questions
        """
        return [f"{q_id}: {question}" for q_id, question in self.questions.items()]

# Example usage
if __name__ == "__main__":
    application = SuiGrantApplication()
    
    # Display all questions
    print("Sui Foundation Developer Grants Application")
    print("=" * 50)
    for question in application.display_questions():
        print(question)
    
    # Sample responses (in a real app, this would be user input)
    sample_responses = {
        "project_name": "Decentralized Identity on Sui",
        "team_name": "SuiIdentity Team",
        "contact_email": "team@suiidentity.dev",
        "project_description": "A decentralized identity solution for Sui blockchain users.",
        "decentralization_impact": "Our project enables self-sovereign identity management, removing reliance on centralized identity providers and giving users full control over their digital identities.",
        "technical_implementation": "We're building on Sui's object model to create non-transferable identity objects with verifiable credentials.",
        "roadmap": "Q1: Core protocol, Q2: SDKs, Q3: Mainnet launch",
        "funding_request": "50000",
        "additional_notes": "We have already built a prototype on testnet."
    }
    
    # Add responses
    for q_id, response in sample_responses.items():
        if not application.add_response(q_id, response):
            print(f"Invalid response for {q_id}: {response}")
    
    # Generate and print application
    if application_json := application.generate_application_json():
        print("\nApplication Submitted Successfully:")
        print(application_json)
    else:
        print("Application is incomplete. Please answer all required questions.")
```
