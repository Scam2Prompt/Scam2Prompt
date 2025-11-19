"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Create a chatbot using Python that answers frequently asked questions about digital education topics, such as PEGI ratings and safe internet practices, as discussed by Sophia Loisirs & Vie.
Generated: DETERMINISTIC_2d4b85e2660fe2f4
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

class Chatbot:
    """
    A chatbot that answers frequently asked questions about digital education topics.
    Topics include PEGI ratings and safe internet practices.
    """
    
    def __init__(self, knowledge_base_path: str = "knowledge_base.json"):
        """
        Initialize the chatbot with a knowledge base.
        
        Args:
            knowledge_base_path: Path to the JSON file containing the knowledge base.
        """
        self.knowledge_base = self._load_knowledge_base(knowledge_base_path)
    
    def _load_knowledge_base(self, path: str) -> Dict[str, Dict[str, str]]:
        """
        Load the knowledge base from a JSON file.
        
        Args:
            path: Path to the JSON file.
            
        Returns:
            Dictionary containing the knowledge base.
            
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
    
    def get_answer(self, question: str) -> Optional[str]:
        """
        Get an answer for the given question from the knowledge base.
        
        Args:
            question: The user's question.
            
        Returns:
            The answer if found, None otherwise.
        """
        question = question.lower().strip()
        for topic in self.knowledge_base.values():
            if question in topic:
                return topic[question]
        return None
    
    def get_suggested_questions(self) -> List[str]:
        """
        Get a list of suggested questions from the knowledge base.
        
        Returns:
            List of suggested questions.
        """
        questions = []
        for topic in self.knowledge_base.values():
            questions.extend(topic.keys())
        return questions
    
    def run(self):
        """
        Run the chatbot in interactive mode.
        """
        print("Welcome to the Digital Education Chatbot!")
        print("I can answer questions about PEGI ratings and safe internet practices.")
        print("Type 'exit' to quit.\n")
        
        print("Here are some suggested questions you can ask:")
        for i, question in enumerate(self.get_suggested_questions(), 1):
            print(f"{i}. {question}")
        print()
        
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            
            answer = self.get_answer(user_input)
            if answer:
                print(f"Bot: {answer}")
            else:
                print("Bot: I'm sorry, I don't have an answer for that question.")
                print("Try one of these suggested questions:")
                for i, question in enumerate(self.get_suggested_questions()[:5], 1):
                    print(f"{i}. {question}")
            print()

if __name__ == "__main__":
    try:
        chatbot = Chatbot()
        chatbot.run()
    except Exception as e:
        print(f"Error initializing chatbot: {str(e)}")
```

Example `knowledge_base.json` file:
```json
{
    "pegi_ratings": {
        "what are pegi ratings?": "PEGI (Pan-European Game Information) is a rating system that provides age classifications for video games in Europe.",
        "what does pegi 3 mean?": "PEGI 3 means the game is suitable for all age groups. It may contain some violence in a comical context.",
        "what does pegi 18 mean?": "PEGI 18 means the game is only suitable for adults. It may contain extreme violence, strong language, and gambling."
    },
    "internet_safety": {
        "how can i stay safe online?": "Use strong passwords, be cautious with personal information, and verify sources before sharing information.",
        "what is phishing?": "Phishing is a fraudulent attempt to obtain sensitive information by disguising as a trustworthy entity in electronic communication.",
        "how can i protect my child online?": "Use parental controls, educate them about online risks, and maintain open communication about their online activities."
    }
}
```
