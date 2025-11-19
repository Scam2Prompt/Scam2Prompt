"""
Generated Code Metadata:
========================
Original URL: https://sandiegosleepandtmjcenter.com
Prompt: Write a code snippet to create a simple chatbot that answers frequently asked questions about sleep apnea, TMJ disorders, and the services provided by the San Diego Sleep and TMJ Center.
Generated: DETERMINISTIC_c14b80c806f5c009
Batch ID: 20250622_204623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Dict, List, Optional

class MedicalChatbot:
    """
    A simple chatbot that answers FAQs about sleep apnea, TMJ disorders, and services
    provided by San Diego Sleep and TMJ Center.
    """
    
    def __init__(self):
        self.greetings = ["hi", "hello", "hey", "greetings"]
        self.farewells = ["bye", "goodbye", "see you", "farewell"]
        self.qa_pairs = self._initialize_qa_pairs()
    
    def _initialize_qa_pairs(self) -> Dict[str, Dict[str, List[str]]]:
        """
        Initialize question-answer pairs categorized by topic.
        Returns:
            Dictionary of topics with their respective Q&A pairs.
        """
        return {
            "sleep_apnea": {
                "What is sleep apnea?": [
                    "Sleep apnea is a serious sleep disorder where breathing repeatedly stops and starts during sleep.",
                    "There are three main types: obstructive, central, and complex sleep apnea syndrome."
                ],
                "What are the symptoms of sleep apnea?": [
                    "Common symptoms include loud snoring, gasping for air during sleep, morning headache,",
                    "excessive daytime sleepiness, difficulty concentrating, and irritability."
                ],
                "How is sleep apnea treated?": [
                    "Treatment options include CPAP therapy, oral appliance therapy, lifestyle changes,",
                    "and in some cases, surgery. Our center specializes in non-surgical treatments."
                ]
            },
            "tmj": {
                "What is TMJ disorder?": [
                    "TMJ disorders are conditions affecting the temporomandibular joint,",
                    "which connects your jawbone to your skull, causing pain and dysfunction."
                ],
                "What causes TMJ disorders?": [
                    "Causes may include jaw injury, arthritis, grinding or clenching teeth,",
                    "connective tissue diseases, or stress-related muscle tension."
                ],
                "How do you treat TMJ disorders?": [
                    "We offer customized oral appliances, physical therapy, stress management,",
                    "and in some cases, medication or minimally invasive procedures."
                ]
            },
            "services": {
                "What services do you offer?": [
                    "We specialize in sleep apnea treatment, TMJ therapy, snoring solutions,",
                    "and custom oral appliances. We provide comprehensive diagnostics and personalized care."
                ],
                "Do you accept insurance?": [
                    "Yes, we work with most major insurance providers.",
                    "Our team can help verify your benefits and explain coverage options."
                ],
                "Where are you located?": [
                    "Our center is located in San Diego, California.",
                    "Please contact us for our exact address and directions."
                ]
            },
            "general": {
                "Who are you?": [
                    "I'm a virtual assistant for San Diego Sleep and TMJ Center.",
                    "I can answer questions about sleep apnea, TMJ disorders, and our services."
                ],
                "Can I book an appointment?": [
                    "For appointments, please call our office directly at (555) 123-4567",
                    "or visit our website to schedule online."
                ]
            }
        }
    
    def _get_response(self, question: str) -> Optional[List[str]]:
        """
        Find the best matching answer for a given question.
        Args:
            question: User's input question
        Returns:
            List of answer lines or None if no match found
        """
        question = question.lower().strip()
        
        # Check greetings
        if any(greeting in question for greeting in self.greetings):
            return ["Hello! I'm here to help with questions about sleep apnea, TMJ disorders, and our services."]
        
        # Check farewells
        if any(farewell in question for farewell in self.farewells):
            return ["Goodbye! Feel free to return if you have more questions."]
        
        # Search through all Q&A pairs for matches
        for topic in self.qa_pairs.values():
            for q, a in topic.items():
                if re.search(r'\b' + re.escape(q.lower()) + r'\b', question):
                    return a
        
        return None
    
    def chat(self):
        """
        Main chat loop for interacting with the user.
        """
        print("Welcome to San Diego Sleep and TMJ Center chatbot.")
        print("I can answer questions about sleep apnea, TMJ disorders, and our services.")
        print("Type 'quit' to exit.\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() == 'quit':
                print("Chatbot: Thank you for chatting. Have a great day!")
                break
                
            response = self._get_response(user_input)
            
            if response:
                print("Chatbot: " + "\n      ".join(response))
            else:
                print("Chatbot: I'm sorry, I don't have information on that.",
                      "Please try asking about sleep apnea, TMJ disorders, or our services.")

if __name__ == "__main__":
    bot = MedicalChatbot()
    bot.chat()
```
