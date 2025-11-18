"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.slv-valbonne.fr
Prompt: Create a chatbot using Python that answers frequently asked questions about digital education topics, such as PEGI ratings and safe internet practices, as discussed by Sophia Loisirs & Vie.
Generated: DETERMINISTIC_2d4b85e2660fe2f4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Define a dictionary to store FAQs and their answers
FAQ_DATA = {
    "What are PEGI ratings?": (
        "PEGI ratings help parents make informed decisions about video games and apps "
        "based on age appropriateness and content descriptors."
    ),
    "How can I stay safe on the internet?": (
        "To stay safe, use strong passwords, be cautious with personal information, "
        "avoid suspicious links, and ensure websites are secure."
    ),
    "What is digital education?": (
        "Digital education focuses on teaching and learning using digital technologies "
        "to enhance knowledge and skills in a connected world."
    ),
    "Why is digital literacy important?": (
        "Digital literacy is crucial for navigating the modern world, enabling individuals "
        "to use technology responsibly, safely, and effectively."
    ),
}

def get_response(user_query):
    """
    Retrieve a response for the user's query.
    
    Args:
        user_query (str): The user's input question or statement.

    Returns:
        str: The chatbot's response.
    """
    # Normalize the user query (case insensitive matching)
    user_query = user_query.strip().lower()
    
    # Search for the best match in the FAQ_DATA
    for question, answer in FAQ_DATA.items():
        if user_query in question.lower():
            return answer
    
    # Fallback response for unrecognized queries
    return (
        "I'm sorry, I don't have information about that topic. "
        "Please ask another question related to digital education!"
    )

def main():
    """
    Main function to run the chatbot in an interactive loop.
    """
    print("Welcome to the Digital Education Chatbot! Ask me about digital education topics.")
    print("Type 'exit' to end the conversation.\n")
    
    while True:
        try:
            # Get input from the user
            user_input = input("You: ").strip()
            
            # Check if the user wants to exit
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for chatting! Stay safe online and have a great day!")
                break
            
            # Generate and display the chatbot's response
            response = get_response(user_input)
            print(f"Chatbot: {response}")
        
        except KeyboardInterrupt:
            # Graceful exit on Ctrl+C
            print("\nChatbot: Goodbye! Stay safe online!")
            break
        
        except Exception as e:
            # Catch-all error handling
            print(f"Chatbot: Oops, something went wrong! ({e})")

if __name__ == "__main__":
    main()
```
