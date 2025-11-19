"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Develop a chatbot using Python that answers FAQs about roofing services, referencing King Roofing's FAQ section and service offerings.
Generated: DETERMINISTIC_4ca858720723daf5
Batch ID: 20250612_145114
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

class RoofingChatbot:
    """
    A chatbot that answers FAQs about roofing services for King Roofing.
    """
    
    def __init__(self, faq_file: str = "faqs.json"):
        """
        Initialize the chatbot with FAQs from a JSON file.
        
        Args:
            faq_file: Path to the JSON file containing FAQs.
        """
        self.faqs = self._load_faqs(faq_file)
        self.greetings = [
            "hi", "hello", "hey", "greetings", "good morning", "good afternoon", "good evening"
        ]
        self.exit_commands = [
            "quit", "exit", "bye", "goodbye", "stop", "end"
        ]
    
    def _load_faqs(self, file_path: str) -> Dict[str, str]:
        """
        Load FAQs from a JSON file.
        
        Args:
            file_path: Path to the JSON file.
            
        Returns:
            Dictionary of questions and answers.
            
        Raises:
            FileNotFoundError: If the FAQ file is not found.
            json.JSONDecodeError: If the FAQ file is not valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"FAQ file not found at {file_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON format in FAQ file", file_path, 0)
    
    def _find_best_match(self, user_input: str) -> Optional[str]:
        """
        Find the best matching FAQ for the user input.
        
        Args:
            user_input: The user's input/question.
            
        Returns:
            The best matching question from FAQs, or None if no match found.
        """
        user_input = user_input.lower()
        best_match = None
        max_similarity = 0
        
        for question in self.faqs.keys():
            similarity = self._calculate_similarity(user_input, question.lower())
            if similarity > max_similarity:
                max_similarity = similarity
                best_match = question
        
        return best_match if max_similarity > 0.5 else None
    
    def _calculate_similarity(self, input1: str, input2: str) -> float:
        """
        Calculate similarity between two strings using simple word overlap.
        
        Args:
            input1: First input string.
            input2: Second input string.
            
        Returns:
            Similarity score between 0 and 1.
        """
        words1 = set(input1.split())
        words2 = set(input2.split())
        common_words = words1.intersection(words2)
        return len(common_words) / max(len(words1), len(words2))
    
    def _is_greeting(self, user_input: str) -> bool:
        """
        Check if the user input is a greeting.
        
        Args:
            user_input: The user's input.
            
        Returns:
            True if the input is a greeting, False otherwise.
        """
        return any(greeting in user_input.lower() for greeting in self.greetings)
    
    def _is_exit_command(self, user_input: str) -> bool:
        """
        Check if the user input is an exit command.
        
        Args:
            user_input: The user's input.
            
        Returns:
            True if the input is an exit command, False otherwise.
        """
        return any(cmd in user_input.lower() for cmd in self.exit_commands)
    
    def get_response(self, user_input: str) -> str:
        """
        Get a response to the user's input.
        
        Args:
            user_input: The user's input/question.
            
        Returns:
            The chatbot's response.
        """
        if self._is_exit_command(user_input):
            return "Thank you for contacting King Roofing. Have a great day!"
        
        if self._is_greeting(user_input):
            return "Hello! Welcome to King Roofing's FAQ chatbot. How can I help you today?"
        
        best_match = self._find_best_match(user_input)
        
        if best_match:
            return self.faqs[best_match]
        else:
            return "I'm sorry, I couldn't find an answer to your question. Please contact King Roofing directly for more assistance."
    
    def run_chatbot(self):
        """
        Run the chatbot in interactive mode.
        """
        print("King Roofing FAQ Chatbot")
        print("Type 'quit', 'exit', or 'bye' to end the conversation.\n")
        
        while True:
            user_input = input("You: ")
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")
            
            if self._is_exit_command(user_input):
                break

if __name__ == "__main__":
    try:
        chatbot = RoofingChatbot()
        chatbot.run_chatbot()
    except Exception as e:
        print(f"Error initializing chatbot: {str(e)}")
```

Example `faqs.json` file:
```json
{
    "What roofing services do you offer?": "King Roofing offers a wide range of services including roof installation, roof repair, roof replacement, roof inspections, and emergency roofing services.",
    "How long does a roof replacement take?": "The duration of a roof replacement depends on the size and complexity of your roof, but most residential projects take between 1-3 days.",
    "What types of roofing materials do you work with?": "We work with various materials including asphalt shingles, metal roofing, tile roofing, slate, and flat roofing materials.",
    "Do you offer free estimates?": "Yes, King Roofing provides free, no-obligation estimates for all our roofing services.",
    "Are you licensed and insured?": "Yes, we are fully licensed and insured for your protection. We can provide proof of insurance upon request.",
    "What areas do you serve?": "We serve the entire metropolitan area and surrounding counties. Contact us to confirm if we service your specific location.",
    "How often should I have my roof inspected?": "We recommend having your roof professionally inspected at least once a year, and after any major storm events.",
    "What is your warranty policy?": "We offer manufacturer warranties on materials and workmanship warranties on our labor. Specific warranty terms depend on the product and service.",
    "How do I know if I need a roof repair or replacement?": "Signs you may need repairs include minor leaks or missing shingles. If your roof is over 20 years old or has widespread damage, replacement may be recommended. We can assess your roof's condition during a free inspection."
}
```
