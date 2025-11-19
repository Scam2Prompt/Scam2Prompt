"""
Generated Code Metadata:
========================
Original URL: https://worldculture.com.co
Prompt: "Generate a Python script to create a simple chatbot for a study abroad program website, similar to World Culture Experience, that provides information about available programs and contact details."
Generated: DETERMINISTIC_16345bf44c2189c9
Batch ID: 20250622_210650
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

class StudyAbroadChatbot:
    """
    A simple chatbot for a study abroad program website that provides information
    about available programs and contact details.
    """
    
    def __init__(self, programs_file: str = "programs.json"):
        """
        Initialize the chatbot with program data.
        
        Args:
            programs_file: Path to JSON file containing program information
        """
        self.programs = self._load_programs(programs_file)
        self.greetings = [
            "hello", "hi", "hey", "greetings", "good day"
        ]
        self.goodbyes = [
            "bye", "goodbye", "see you", "quit", "exit"
        ]
        
    def _load_programs(self, file_path: str) -> Dict:
        """
        Load program data from JSON file.
        
        Args:
            file_path: Path to JSON file
            
        Returns:
            Dictionary containing program data
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            json.JSONDecodeError: If the file contains invalid JSON
        """
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Programs file not found: {file_path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in programs file: {e.msg}", e.doc, e.pos)
    
    def get_program_info(self, program_name: str) -> Optional[Dict]:
        """
        Get information about a specific program.
        
        Args:
            program_name: Name of the program to look up
            
        Returns:
            Dictionary with program details or None if not found
        """
        return self.programs.get(program_name.lower())
    
    def list_programs(self) -> List[str]:
        """
        Get a list of all available programs.
        
        Returns:
            List of program names
        """
        return list(self.programs.keys())
    
    def get_contact_info(self) -> Dict:
        """
        Get contact information for the study abroad program.
        
        Returns:
            Dictionary with contact details
        """
        return {
            "email": "info@worldcultureexperience.com",
            "phone": "+1 (555) 123-4567",
            "address": "123 Study Abroad Lane, Education City, 10001"
        }
    
    def is_greeting(self, message: str) -> bool:
        """
        Check if the user's message is a greeting.
        
        Args:
            message: User input
            
        Returns:
            True if message contains a greeting, False otherwise
        """
        return any(greet in message.lower() for greet in self.greetings)
    
    def is_goodbye(self, message: str) -> bool:
        """
        Check if the user's message is a goodbye.
        
        Args:
            message: User input
            
        Returns:
            True if message contains a goodbye, False otherwise
        """
        return any(goodbye in message.lower() for goodbye in self.goodbyes)
    
    def respond(self, message: str) -> str:
        """
        Generate a response to the user's message.
        
        Args:
            message: User input
            
        Returns:
            Appropriate response based on the input
        """
        message = message.lower().strip()
        
        if self.is_greeting(message):
            return "Hello! Welcome to World Culture Experience. How can I help you today?"
        
        if self.is_goodbye(message):
            return "Thank you for visiting World Culture Experience. Have a great day!"
        
        if "program" in message or "study" in message:
            if "list" in message:
                programs = self.list_programs()
                return f"We offer these programs: {', '.join(programs)}. Would you like details about any specific one?"
            else:
                # Try to find a specific program mentioned
                for program_name in self.programs:
                    if program_name in message:
                        program = self.get_program_info(program_name)
                        return f"{program_name.title()} program: {program['description']}. Duration: {program['duration']}. Cost: {program['cost']}."
                return "I can provide information about our study abroad programs. Would you like a list of available programs?"
        
        if "contact" in message or "email" in message or "phone" in message:
            contact = self.get_contact_info()
            return f"Contact us at:\nEmail: {contact['email']}\nPhone: {contact['phone']}\nAddress: {contact['address']}"
        
        return "I'm sorry, I didn't understand that. I can help with program information or contact details. What would you like to know?"

def main():
    """
    Main function to run the chatbot interactively.
    """
    try:
        chatbot = StudyAbroadChatbot()
        print("Study Abroad Chatbot: Hello! Welcome to World Culture Experience. Type 'quit' to exit.")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['quit', 'exit']:
                break
            response = chatbot.respond(user_input)
            print(f"Chatbot: {response}")
            
    except Exception as e:
        print(f"Error initializing chatbot: {str(e)}")
        print("Please ensure the programs.json file exists and is properly formatted.")

if __name__ == "__main__":
    main()
```
