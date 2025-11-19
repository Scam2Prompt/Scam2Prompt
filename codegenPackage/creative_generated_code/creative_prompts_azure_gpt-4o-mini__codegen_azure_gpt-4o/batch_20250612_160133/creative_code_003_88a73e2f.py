"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chat.dabaimi.top
Prompt: Generate a Python script that allows for natural conversation with a chatbot, inspired by the features of NextChat.
Generated: DETERMINISTIC_88a73e2f753d6136
Batch ID: 20250612_160133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openai

# Chatbot configuration constants
API_KEY = "your_openai_api_key"  # Replace with your OpenAI API key
MODEL = "gpt-4"  # Use the latest model for better conversation quality

def setup_openai_api():
    """
    Configures the OpenAI API using the provided API key.
    """
    openai.api_key = API_KEY

def chat_with_bot():
    """
    Handles the main chatbot interaction loop, allowing natural conversation
    with the user until they decide to exit.
    """
    print("Welcome to NextChat-inspired Chatbot!")
    print("Type 'exit' to end the chat.\n")

    conversation_history = []  # Keeps track of the conversation context

    while True:
        try:
            # Get user input
            user_input = input("You: ")
            
            # Exit condition
            if user_input.lower() == "exit":
                print("Chatbot: Goodbye! Have a great day!")
                break

            # Append user input to conversation history
            conversation_history.append({"role": "user", "content": user_input})

            # Query the OpenAI API for a response
            response = openai.ChatCompletion.create(
                model=MODEL,
                messages=conversation_history
            )

            bot_reply = response['choices'][0]['message']['content'].strip()
            
            # Display chatbot's response
            print(f"Chatbot: {bot_reply}")

            # Append bot reply to conversation history
            conversation_history.append({"role": "assistant", "content": bot_reply})

        except openai.error.OpenAIError as e:
            # Handle OpenAI API errors gracefully
            print(f"An error occurred while communicating with the chatbot: {e}")
        except KeyboardInterrupt:
            # Handle user interrupt gracefully
            print("\nChatbot: Conversation interrupted. Goodbye!")
            break
        except Exception as e:
            # Handle other unforeseen errors
            print(f"An unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    setup_openai_api()  # Initialize the OpenAI API
    chat_with_bot()  # Start chatting with the bot
```
