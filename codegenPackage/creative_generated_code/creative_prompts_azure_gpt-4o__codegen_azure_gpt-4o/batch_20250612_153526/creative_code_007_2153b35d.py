"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kiberahamlets.org
Prompt: Create a chatbot using natural language processing that answers questions about Kibera Hamlets' programs, such as education initiatives ("Somesha") or environmental conservation efforts.
Generated: DETERMINISTIC_2153b35d7ed82cb0
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# chatbot_kibera.py

import nltk
from nltk.chat.util import Chat, reflections

# Ensure NLTK resources are downloaded
try:
    nltk.download('punkt', quiet=True)
except Exception as e:
    print(f"Error downloading NLTK resources: {e}")

# Define pairs for natural language processing
# These pairs map user inputs to chatbot responses
pairs = [
    # Education initiative: "Somesha"
    (r"(.*)Somesha(.*)", 
     ["Somesha is our education initiative that provides scholarships and support to children in Kibera. "
      "You can learn more at our website or contact us directly for more details."]),

    (r"What does Somesha do\?", 
     ["Somesha focuses on providing quality education opportunities to children in need."]),

    # Environmental conservation efforts
    (r"(.*)environmental conservation(.*)", 
     ["Our environmental conservation efforts focus on recycling, urban gardening, and community cleanup projects. "
      "Feel free to ask more about specific programs."]),

    (r"What projects do you have for the environment\?", 
     ["We have urban gardening initiatives, recycling programs, and regular community cleanup drives."]),

    # General greeting
    (r"(Hi|Hello|Hey)(.*)", 
     ["Hello! How can I assist you today regarding Kibera Hamlets' programs?"]),

    # Default response for unrecognized queries
    (r"(.*)", 
     ["I'm sorry, I didn't understand that. Can you please ask about our education or environmental programs?"])
]

# Define the chatbot function
def kibera_chatbot():
    """
    Starts a chatbot session to answer questions about Kibera Hamlets' programs.
    """
    print("Welcome to Kibera Hamlets Chatbot! Type 'quit' to exit.")
    print("You can ask about our education programs like 'Somesha' or environmental conservation efforts.")
    
    # Create a Chat instance with pairs and reflections
    chatbot = Chat(pairs, reflections)
    
    # Start the conversation loop
    while True:
        try:
            user_input = input("You: ").strip()
            
            # Check if the user wants to exit
            if user_input.lower() == 'quit':
                print("Chatbot: Thank you for chatting! Goodbye.")
                break
            
            # Generate a response using NLP
            response = chatbot.respond(user_input)
            print(f"Chatbot: {response}")
        
        except KeyboardInterrupt:
            print("\nChatbot: Session interrupted. Goodbye.")
            break
        
        except Exception as e:
            print(f"Error: {e}. Please try again.")

# Entry point for the chatbot
if __name__ == "__main__":
    kibera_chatbot()
```
