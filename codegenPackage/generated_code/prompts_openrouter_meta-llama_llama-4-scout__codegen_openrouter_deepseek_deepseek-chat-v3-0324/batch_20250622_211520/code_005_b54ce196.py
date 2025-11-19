"""
Generated Code Metadata:
========================
Original URL: https://meezaninteriorsolutions.com
Prompt: "Develop a chatbot script for an interior design firm's website, incorporating FAQs about services such as kitchen and bath design, custom furniture, and the process for a free consultation, based on Meezan Interior Solutions' offerings."
Generated: DETERMINISTIC_b54ce196297d69e1
Batch ID: 20250622_211520
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

class InteriorDesignChatbot:
    """
    A chatbot for Meezan Interior Solutions that handles FAQs about interior design services.
    """

    def __init__(self):
        """
        Initializes the chatbot with predefined FAQs and responses.
        """
        self.faqs = self._load_faqs()

    def _load_faqs(self) -> Dict[str, Dict[str, str]]:
        """
        Loads FAQs from a predefined dictionary (can be replaced with a database or file).

        Returns:
            Dict[str, Dict[str, str]]: A dictionary of FAQs categorized by service.
        """
        return {
            "general": {
                "What services do you offer?": "We offer kitchen design, bath design, custom furniture, and free consultations.",
                "How can I contact you?": "You can reach us via phone at (123) 456-7890 or email at info@meezaninteriors.com.",
                "Do you provide free consultations?": "Yes, we offer free initial consultations to discuss your project needs."
            },
            "kitchen_design": {
                "What is included in your kitchen design service?": "Our kitchen design service includes layout planning, material selection, and 3D renderings.",
                "How long does a kitchen design project take?": "Typically, it takes 4-6 weeks from design to completion."
            },
            "bath_design": {
                "What is included in your bath design service?": "We handle everything from layout to fixture selection and installation.",
                "Can you work with small bathrooms?": "Yes, we specialize in optimizing small spaces for functionality and style."
            },
            "custom_furniture": {
                "Do you design custom furniture?": "Yes, we create bespoke furniture tailored to your space and style.",
                "What materials do you use for custom furniture?": "We use high-quality wood, metal, and upholstery materials."
            },
            "consultation": {
                "How do I schedule a free consultation?": "Call us or fill out the form on our website to schedule a consultation.",
                "What should I prepare for the consultation?": "Bring your ideas, budget, and any inspiration images you have."
            }
        }

    def get_response(self, user_input: str) -> str:
        """
        Processes user input and returns the most relevant FAQ response.

        Args:
            user_input (str): The user's question or input.

        Returns:
            str: The chatbot's response or a default message if no match is found.
        """
        user_input = user_input.lower().strip()
        
        # Check each category for a matching question
        for category in self.faqs:
            for question in self.faqs[category]:
                if user_input in question.lower():
                    return self.faqs[category][question]
        
        return "I'm sorry, I couldn't find an answer to your question. Please contact us directly for more information."

    def get_categories(self) -> List[str]:
        """
        Returns a list of available FAQ categories.

        Returns:
            List[str]: List of category names.
        """
        return list(self.faqs.keys())

    def get_questions_by_category(self, category: str) -> Optional[Dict[str, str]]:
        """
        Returns all questions and answers for a specific category.

        Args:
            category (str): The category name.

        Returns:
            Optional[Dict[str, str]]: Dictionary of questions and answers, or None if category doesn't exist.
        """
        return self.faqs.get(category.lower(), None)


# Example usage
if __name__ == "__main__":
    chatbot = InteriorDesignChatbot()
    
    print("Welcome to Meezan Interior Solutions Chatbot!")
    print("Type 'exit' to end the conversation.\n")
    
    while True:
        user_input = input("How can I help you today? ")
        
        if user_input.lower() == 'exit':
            print("Thank you for chatting with us. Have a great day!")
            break
        
        response = chatbot.get_response(user_input)
        print(response)
```
