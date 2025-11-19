"""
Generated Code Metadata:
========================
Original URL: https://springsinternational.org
Prompt: Create a chatbot using Python that answers questions about Springs International Ministries’ programs, such as “Where was Jesus on Saturday?” or details about Mission 2030.
Generated: DETERMINISTIC_b7ca9ed3814b2009
Batch ID: 20250612_151354
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

class SpringsChatbot:
    """
    A chatbot that provides information about Springs International Ministries' programs.
    """
    
    def __init__(self, knowledge_base_path: str = "knowledge_base.json"):
        """
        Initialize the chatbot with a knowledge base.
        
        Args:
            knowledge_base_path (str): Path to the JSON file containing the knowledge base.
        """
        self.knowledge_base = self._load_knowledge_base(knowledge_base_path)
    
    def _load_knowledge_base(self, path: str) -> Dict:
        """
        Load the knowledge base from a JSON file.
        
        Args:
            path (str): Path to the JSON file.
            
        Returns:
            Dict: The loaded knowledge base.
            
        Raises:
            FileNotFoundError: If the knowledge base file is not found.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Knowledge base file not found at {path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON format in knowledge base", doc=path, pos=0)
    
    def _find_best_match(self, user_question: str) -> Optional[str]:
        """
        Find the best matching question in the knowledge base.
        
        Args:
            user_question (str): The user's question.
            
        Returns:
            Optional[str]: The best matching question from the knowledge base, or None if no match found.
        """
        questions = [q.lower() for q in self.knowledge_base.keys()]
        user_question = user_question.lower()
        
        for question in questions:
            if question in user_question or user_question in question:
                return question
        return None
    
    def get_response(self, user_question: str) -> str:
        """
        Get a response to the user's question.
        
        Args:
            user_question (str): The user's question.
            
        Returns:
            str: The response to the question, or a default message if no answer is found.
        """
        best_match = self._find_best_match(user_question)
        
        if best_match:
            return self.knowledge_base[best_match]
        else:
            return "I'm sorry, I don't have information about that. Please ask about Springs International Ministries' programs."
    
    def run_chat(self):
        """
        Run the chatbot in interactive mode.
        """
        print("Welcome to Springs International Ministries Chatbot!")
        print("Ask me about our programs (e.g., 'Where was Jesus on Saturday?' or 'What is Mission 2030?')")
        print("Type 'quit' to exit.\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
                
            if not user_input:
                print("Please enter a question.")
                continue
                
            response = self.get_response(user_input)
            print(f"Bot: {response}\n")

# Sample knowledge base (would typically be in a separate JSON file)
sample_knowledge_base = {
    "Where was Jesus on Saturday?": "According to Christian tradition, Jesus was in the tomb on Saturday after his crucifixion on Friday and before his resurrection on Sunday.",
    "What is Mission 2030?": "Mission 2030 is Springs International Ministries' initiative to reach every nation with the gospel by the year 2030 through church planting, discipleship, and humanitarian aid.",
    "What programs does Springs International Ministries offer?": "We offer various programs including Bible studies, missionary training, humanitarian aid projects, and church planting initiatives.",
    "How can I get involved?": "You can get involved by volunteering, donating, or joining one of our mission trips. Visit our website for more information."
}

# Save sample knowledge base to a file (in a real application, this would be pre-existing)
with open("knowledge_base.json", 'w', encoding='utf-8') as file:
    json.dump(sample_knowledge_base, file, indent=2)

# Run the chatbot
if __name__ == "__main__":
    try:
        chatbot = SpringsChatbot()
        chatbot.run_chat()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
