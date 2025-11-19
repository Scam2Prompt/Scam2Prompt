"""
Generated Code Metadata:
========================
Original URL: https://vitalityholistic.co.uk
Prompt: Create a simple chatbot script that provides information about the benefits of different holistic therapies, such as Hijama for pain relief and improved circulation, and Lymphatic Drainage for reducing swelling and inflammation.
Generated: DETERMINISTIC_0a1ba5426444aaf8
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Define therapy information
therapy_info = {
    "hijama": {
        "name": "Hijama (Cupping Therapy)",
        "benefits": [
            "Pain relief",
            "Improved circulation",
            "Detoxification",
            "Reduced inflammation",
            "Enhanced immune function"
        ],
        "description": "Hijama is an ancient therapy that uses suction cups to draw out impurities and stimulate healing."
    },
    "lymphatic drainage": {
        "name": "Lymphatic Drainage",
        "benefits": [
            "Reduces swelling and inflammation",
            "Boosts immune system",
            "Detoxifies the body",
            "Improves circulation",
            "Promotes relaxation"
        ],
        "description": "A gentle massage technique that stimulates lymph flow to remove waste and toxins from the body."
    },
    "acupuncture": {
        "name": "Acupuncture",
        "benefits": [
            "Pain relief",
            "Stress reduction",
            "Improved sleep",
            "Balanced energy flow",
            "Enhanced mental clarity"
        ],
        "description": "Involves inserting thin needles into specific points to balance energy flow and promote healing."
    },
    "aromatherapy": {
        "name": "Aromatherapy",
        "benefits": [
            "Reduces stress and anxiety",
            "Improves sleep quality",
            "Boosts mood",
            "Enhances cognitive function",
            "Supports immune system"
        ],
        "description": "Uses essential oils to promote physical and psychological well-being through inhalation or topical application."
    }
}

# Define greetings and responses
greetings = ["hello", "hi", "hey", "greetings", "howdy"]
farewells = ["bye", "goodbye", "see you", "farewell", "quit"]
help_responses = ["help", "what can you do", "options", "therapies"]

def get_therapy_info(therapy_key):
    """Retrieve information about a specific therapy."""
    therapy = therapy_info.get(therapy_key.lower())
    if therapy:
        return therapy
    return None

def format_therapy_info(therapy):
    """Format therapy information for display."""
    if not therapy:
        return "Sorry, I don't have information about that therapy."
    
    info = f"\n{therapy['name']}\n"
    info += f"\nDescription: {therapy['description']}\n"
    info += "\nBenefits:\n"
    for benefit in therapy['benefits']:
        info += f"- {benefit}\n"
    return info

def list_therapies():
    """List all available therapies."""
    return "\nAvailable therapies:\n" + "\n".join([f"- {key.capitalize()}" for key in therapy_info.keys()])

def chatbot_response(user_input):
    """Generate appropriate response based on user input."""
    user_input = user_input.lower().strip()
    
    if user_input in greetings:
        return "Hello! I'm a holistic therapy chatbot. How can I help you today?"
    
    if user_input in farewells:
        return "Goodbye! Feel free to return if you have more questions about holistic therapies."
    
    if user_input in help_responses:
        return list_therapies() + "\n\nYou can ask about any of these therapies for more information."
    
    therapy = get_therapy_info(user_input)
    if therapy:
        return format_therapy_info(therapy)
    
    return "I'm not sure I understand. You can ask about specific therapies like 'Hijama' or type 'help' to see options."

def main():
    """Main function to run the chatbot."""
    print("Welcome to the Holistic Therapy Chatbot!")
    print("Type 'help' to see available options or 'quit' to exit.\n")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in farewells:
                print(chatbot_response(user_input))
                break
            
            response = chatbot_response(user_input)
            print(f"Bot: {response}\n")
        
        except KeyboardInterrupt:
            print("\nBot: Goodbye! Thanks for chatting.")
            break
        except Exception as e:
            print(f"\nBot: Sorry, something went wrong. Please try again. Error: {str(e)}")

if __name__ == "__main__":
    main()
```
