"""
Generated Code Metadata:
========================
Original URL: https://dentistasuzano.com.br
Prompt: Develop a chatbot script that answers common questions about dental implants, orthodontics, and aesthetic dentistry, based on the services offered by Odontoclinic Suzano.
Generated: DETERMINISTIC_4c79681b8f33420d
Batch ID: 20250622_210655
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

class DentalChatbot:
    """
    A chatbot that answers common questions about dental services offered by Odontoclinic Suzano.
    Services include dental implants, orthodontics, and aesthetic dentistry.
    """
    
    def __init__(self):
        self.knowledge_base = self._load_knowledge_base()
    
    def _load_knowledge_base(self) -> Dict[str, Dict[str, List[str]]]:
        """
        Load the knowledge base from a predefined dictionary.
        """
        return {
            "dental_implants": {
                "description": [
                    "Dental implants are artificial tooth roots that provide a permanent base for fixed or removable replacement teeth.",
                    "They are a popular and effective long-term solution for people who suffer from missing teeth."
                ],
                "procedure": [
                    "The implant procedure involves placing a titanium post into the jawbone, which fuses with the bone over time.",
                    "After healing, an abutment and crown are attached to complete the restoration."
                ],
                "benefits": [
                    "Improved appearance and confidence",
                    "Enhanced comfort and speech",
                    "Better oral health and easier eating",
                    "Durability and convenience"
                ],
                "faq": [
                    "Q: How long do dental implants last? A: With proper care, they can last a lifetime.",
                    "Q: Is the procedure painful? A: It's performed under anesthesia, so discomfort is minimal.",
                    "Q: Who is a good candidate? A: Anyone missing one or more teeth with adequate jawbone density."
                ]
            },
            "orthodontics": {
                "description": [
                    "Orthodontics focuses on diagnosing, preventing, and treating dental and facial irregularities.",
                    "Common treatments include braces and aligners to correct misaligned teeth and jaws."
                ],
                "types": [
                    "Traditional metal braces",
                    "Ceramic braces",
                    "Lingual braces",
                    "Clear aligners (e.g., Invisalign)"
                ],
                "benefits": [
                    "Improved bite and jaw alignment",
                    "Enhanced facial appearance",
                    "Better oral hygiene and easier cleaning",
                    "Reduced risk of tooth decay and gum disease"
                ],
                "faq": [
                    "Q: How long does treatment take? A: Typically 1-3 years depending on the case.",
                    "Q: Are braces painful? A: There may be initial discomfort, but it subsides quickly.",
                    "Q: Can adults get orthodontic treatment? A: Yes, age is not a limitation."
                ]
            },
            "aesthetic_dentistry": {
                "description": [
                    "Aesthetic dentistry focuses on improving the appearance of teeth, gums, and smile.",
                    "Procedures include teeth whitening, veneers, bonding, and gum contouring."
                ],
                "procedures": [
                    "Teeth whitening for a brighter smile",
                    "Veneers to correct chips, gaps, or discoloration",
                    "Dental bonding to repair minor imperfections",
                    "Gum contouring for a more balanced smile"
                ],
                "benefits": [
                    "Enhanced smile and self-confidence",
                    "Minimally invasive options available",
                    "Quick results with some procedures",
                    "Customized treatment plans"
                ],
                "faq": [
                    "Q: How long do veneers last? A: Typically 10-15 years with proper care.",
                    "Q: Is teeth whitening safe? A: Yes, when performed by a professional.",
                    "Q: Can aesthetic procedures damage teeth? A: No, they are designed to preserve tooth structure."
                ]
            }
        }
    
    def get_response(self, topic: str, subtopic: Optional[str] = None) -> str:
        """
        Generate a response based on the user's query.
        
        Args:
            topic: Main topic (dental_implants, orthodontics, aesthetic_dentistry)
            subtopic: Optional subtopic (description, procedure, benefits, faq, etc.)
            
        Returns:
            Formatted response string or error message if topic not found
        """
        if topic not in self.knowledge_base:
            return "Sorry, I don't have information on that topic. Please ask about dental implants, orthodontics, or aesthetic dentistry."
        
        if subtopic:
            if subtopic not in self.knowledge_base[topic]:
                return f"Sorry, I don't have information on '{subtopic}' for {topic}. Try asking about description, benefits, or faq."
            
            info = self.knowledge_base[topic][subtopic]
            response = f"Here's information about {topic} - {subtopic}:\n"
            response += "\n".join(info)
            return response
        
        # If no subtopic specified, return all available information
        response = f"Here's what I know about {topic}:\n\n"
        for subtopic, info in self.knowledge_base[topic].items():
            response += f"{subtopic.upper()}:\n"
            response += "\n".join(info) + "\n\n"
        return response.strip()
    
    def handle_user_input(self, user_input: str) -> str:
        """
        Process natural language input and return appropriate response.
        
        Args:
            user_input: User's question in natural language
            
        Returns:
            Appropriate response based on the knowledge base
        """
        user_input = user_input.lower().strip()
        
        # Check for greetings
        if any(word in user_input for word in ["hello", "hi", "greetings"]):
            return "Hello! I'm the Odontoclinic Suzano chatbot. How can I help you with dental implants, orthodontics, or aesthetic dentistry today?"
        
        # Check for thanks
        if any(word in user_input for word in ["thank", "thanks", "appreciate"]):
            return "You're welcome! Let me know if you have any other questions."
        
        # Check for topic and subtopic
        topic = None
        subtopic = None
        
        # Identify topic
        if "implant" in user_input:
            topic = "dental_implants"
        elif "orthodont" in user_input:
            topic = "orthodontics"
        elif "aesthetic" in user_input or "cosmetic" in user_input:
            topic = "aesthetic_dentistry"
        
        # Identify subtopic
        if "desc" in user_input or "what is" in user_input:
            subtopic = "description"
        elif "procedure" in user_input or "how it works" in user_input:
            subtopic = "procedure"
        elif "benefit" in user_input or "advantage" in user_input:
            subtopic = "benefits"
        elif "faq" in user_input or "question" in user_input:
            subtopic = "faq"
        elif "type" in user_input and topic == "orthodontics":
            subtopic = "types"
        elif "procedure" in user_input and topic == "aesthetic_dentistry":
            subtopic = "procedures"
        
        if topic:
            return self.get_response(topic, subtopic)
        else:
            return "I can answer questions about dental implants, orthodontics, and aesthetic dentistry. Could you be more specific about what you'd like to know?"


# Example usage
if __name__ == "__main__":
    chatbot = DentalChatbot()
    print("Welcome to Odontoclinic Suzano Chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            print("Goodbye! Have a great day.")
            break
        
        response = chatbot.handle_user_input(user_input)
        print(f"Bot: {response}")
```
