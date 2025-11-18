"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.emerginggifts.com
Prompt: Develop a chatbot prototype for nonprofit organizations in emerging economies to assist with digital-first fundraising, inspired by Emerging Gifts' approach.
Generated: DETERMINISTIC_c0697813a6a591e1
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openai
import logging

# Set up logging for debugging and monitoring
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# *** Chatbot Prototype for Nonprofit Fundraising ***

# Function to initialize OpenAI GPT API
def initialize_openai_api(api_key: str):
    """
    Initializes OpenAI API with the provided API key.

    :param api_key: OpenAI API key
    """
    openai.api_key = api_key
    logging.info("OpenAI API initialized successfully.")

# Function to generate a chatbot response
def generate_response(prompt: str) -> str:
    """
    Generates a chatbot response using OpenAI GPT-4.

    :param prompt: User input to the chatbot
    :return: Chatbot response string
    """
    try:
        # Send the request to OpenAI and get the response
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful chatbot designed to assist nonprofit organizations with fundraising strategies."},
                {"role": "user", "content": prompt}
            ]
        )
        # Extract and return the response text
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        # Log and return a safe error message
        logging.error(f"Error generating response: {e}")
        return "I'm sorry, but I encountered an error while processing your request. Please try again."

# Main function to run the chatbot prototype
def main():
    """
    Entry point for running the chatbot prototype.
    """
    # Replace with your OpenAI API key
    api_key = "your_openai_api_key_here"
    initialize_openai_api(api_key)

    logging.info("Starting chatbot prototype...")

    print("Welcome to the Nonprofit Fundraising Assistant! Type 'exit' to end the conversation.")
    
    # Chat loop
    while True:
        user_input = input("\nYou: ").strip()
        
        # Exit condition
        if user_input.lower() == 'exit':
            print("Thank you for using the Nonprofit Fundraising Assistant. Goodbye!")
            break
        
        # Generate and display response
        response = generate_response(user_input)
        print("\nChatbot:", response)

# Check if the script is run directly
if __name__ == "__main__":
    main()
```
