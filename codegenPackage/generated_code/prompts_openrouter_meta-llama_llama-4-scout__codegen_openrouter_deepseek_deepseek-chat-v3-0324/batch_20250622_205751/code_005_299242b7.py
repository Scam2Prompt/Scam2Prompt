"""
Generated Code Metadata:
========================
Original URL: https://askcardiologist.in
Prompt: Develop a simple chatbot that answers frequently asked questions about heart health and cardiology, based on Dr. S Nagendra Boopathy's FAQs.
Generated: DETERMINISTIC_299242b773312b0c
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Optional

class HeartHealthChatbot:
    """
    A simple chatbot that answers frequently asked questions about heart health and cardiology.
    Based on Dr. S Nagendra Boopathy's FAQs.
    """
    
    def __init__(self, knowledge_base_path: str = "knowledge_base.json"):
        """
        Initialize the chatbot with a knowledge base.
        
        Args:
            knowledge_base_path: Path to the JSON file containing FAQ knowledge base.
        """
        self.knowledge_base = self._load_knowledge_base(knowledge_base_path)
    
    def _load_knowledge_base(self, file_path: str) -> Dict[str, str]:
        """
        Load the knowledge base from a JSON file.
        
        Args:
            file_path: Path to the JSON file.
            
        Returns:
            Dictionary containing question-answer pairs.
            
        Raises:
            FileNotFoundError: If the knowledge base file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Knowledge base file not found at {file_path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in knowledge base: {e.msg}", e.doc, e.pos)
    
    def get_answer(self, question: str) -> Optional[str]:
        """
        Get an answer for the given question.
        
        Args:
            question: User's question about heart health.
            
        Returns:
            Answer if found in knowledge base, None otherwise.
        """
        # Normalize the question for better matching
        normalized_question = question.lower().strip()
        
        # Try to find exact match first
        if normalized_question in self.knowledge_base:
            return self.knowledge_base[normalized_question]
        
        # Try to find partial matches
        for kb_question, answer in self.knowledge_base.items():
            if normalized_question in kb_question or kb_question in normalized_question:
                return answer
        
        return None
    
    def chat(self):
        """
        Start an interactive chat session with the user.
        """
        print("Heart Health Chatbot: Hello! I can answer questions about heart health.")
        print("Type 'quit' to end the conversation.\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() == 'quit':
                print("Heart Health Chatbot: Goodbye! Take care of your heart.")
                break
            
            answer = self.get_answer(user_input)
            
            if answer:
                print(f"Heart Health Chatbot: {answer}")
            else:
                print("Heart Health Chatbot: I'm sorry, I don't have an answer for that question.")
                print("Please consult with a cardiologist for more specific advice.")

# Sample knowledge base (would typically be in a separate JSON file)
SAMPLE_KNOWLEDGE_BASE = {
    "what are the symptoms of heart disease?": "Common symptoms include chest pain, shortness of breath, fatigue, irregular heartbeat, and swelling in legs.",
    "how can i prevent heart disease?": "Maintain a healthy diet, exercise regularly, avoid smoking, limit alcohol, and manage stress.",
    "what is a normal blood pressure?": "Normal blood pressure is typically around 120/80 mmHg. Consult your doctor for personalized advice.",
    "when should i see a cardiologist?": "You should see a cardiologist if you experience chest pain, shortness of breath, dizziness, or irregular heartbeats.",
    "what tests are done to check heart health?": "Common tests include ECG, stress test, echocardiogram, and blood tests for cholesterol and other markers."
}

def main():
    # Create a temporary knowledge base file for demonstration
    with open("knowledge_base.json", 'w', encoding='utf-8') as f:
        json.dump(SAMPLE_KNOWLEDGE_BASE, f)
    
    try:
        chatbot = HeartHealthChatbot()
        chatbot.chat()
    except Exception as e:
        print(f"Error initializing chatbot: {str(e)}")
    finally:
        # Clean up the temporary file
        import os
        if os.path.exists("knowledge_base.json"):
            os.remove("knowledge_base.json")

if __name__ == "__main__":
    main()
```
