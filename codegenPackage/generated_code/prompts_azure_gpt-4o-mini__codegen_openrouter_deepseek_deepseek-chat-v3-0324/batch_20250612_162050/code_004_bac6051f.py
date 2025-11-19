"""
Generated Code Metadata:
========================
Original URL: https://atvisaabogados.com
Prompt: Illustrate how to implement a chatbot that answers common questions about family petitions and special permits, based on the information from AT Visa Abogados.
Generated: DETERMINISTIC_bac6051fc470384a
Batch ID: 20250612_162050
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
    A chatbot that answers common questions about family petitions and special permits.
    The responses are based on the information from AT Visa Abogados.
    """
    
    def __init__(self, knowledge_base_path: str = "knowledge_base.json"):
        """
        Initialize the chatbot with a knowledge base.
        
        Args:
            knowledge_base_path (str): Path to the JSON file containing the knowledge base.
        """
        self.knowledge_base = self._load_knowledge_base(knowledge_base_path)
    
    def _load_knowledge_base(self, path: str) -> Dict[str, Dict[str, str]]:
        """
        Load the knowledge base from a JSON file.
        
        Args:
            path (str): Path to the JSON file.
            
        Returns:
            Dict[str, Dict[str, str]]: The loaded knowledge base.
            
        Raises:
            FileNotFoundError: If the knowledge base file is not found.
            json.JSONDecodeError: If the knowledge base file is not valid JSON.
        """
        try:
            with open(path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Knowledge base file not found: {path}") from e
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in knowledge base: {path}", e.doc, e.pos) from e
    
    def get_response(self, question: str) -> str:
        """
        Get a response to a user's question based on the knowledge base.
        
        Args:
            question (str): The user's question.
            
        Returns:
            str: The chatbot's response, or a default message if no answer is found.
        """
        question_lower = question.lower().strip()
        
        for category in self.knowledge_base.values():
            for q, a in category.items():
                if q.lower() in question_lower:
                    return a
        
        return "I'm sorry, I don't have information on that topic. Please contact AT Visa Abogados for more details."
    
    def get_categories(self) -> List[str]:
        """
        Get the list of available question categories.
        
        Returns:
            List[str]: The list of category names.
        """
        return list(self.knowledge_base.keys())
    
    def get_questions_in_category(self, category: str) -> Optional[List[str]]:
        """
        Get the list of questions in a specific category.
        
        Args:
            category (str): The category name.
            
        Returns:
            Optional[List[str]]: The list of questions, or None if the category doesn't exist.
        """
        return list(self.knowledge_base.get(category, {}).keys())

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the chatbot
        chatbot = Chatbot()
        
        # Example questions
        questions = [
            "What is a family petition?",
            "How do I apply for a special permit?",
            "What documents are needed for a visa application?",
            "What is the processing time for a work visa?"
        ]
        
        # Get responses
        for question in questions:
            response = chatbot.get_response(question)
            print(f"Q: {question}\nA: {response}\n")
        
        # Display available categories and questions
        print("Available categories:")
        for category in chatbot.get_categories():
            print(f"- {category}")
            questions = chatbot.get_questions_in_category(category)
            for q in questions:
                print(f"  • {q}")
                
    except Exception as e:
        print(f"An error occurred: {e}")
```

```json
{
    "family_petitions": {
        "What is a family petition?": "A family petition is a request filed by a U.S. citizen or lawful permanent resident to bring a family member to the United States. The process varies depending on the relationship.",
        "Who can file a family petition?": "U.S. citizens and lawful permanent residents (green card holders) can file family petitions for certain qualifying relatives.",
        "What are the categories of family-based visas?": "There are two main categories: Immediate Relative (unlimited visas) and Family Preference (limited visas)."
    },
    "special_permits": {
        "How do I apply for a special permit?": "Special permits typically require filing specific forms with USCIS, along with supporting documents. The exact process depends on the type of permit.",
        "What types of special permits are available?": "Common special permits include work permits (EAD), advance parole, and humanitarian parole.",
        "How long does it take to get a special permit?": "Processing times vary, but typically range from 3 to 6 months depending on the type of permit and current USCIS processing times."
    },
    "general_visa": {
        "What documents are needed for a visa application?": "Typically you need a valid passport, application forms, photos, supporting documents for your visa category, and fees.",
        "What is the processing time for a work visa?": "Work visa processing times vary by type (H-1B, L-1, etc.) and can range from a few weeks to several months."
    }
}
```
