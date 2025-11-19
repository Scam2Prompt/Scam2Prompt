"""
Generated Code Metadata:
========================
Original URL: https://pringletheduck.com
Prompt: Generate code to create a chatbot like Pringle The Duck AI agent using a library like Dialogflow.
Generated: DETERMINISTIC_05dd72fe22be2fb2
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from google.cloud import dialogflow_v2 as dialogflow

class Chatbot:
    def __init__(self, project_id, session_id):
        """
        Initializes the Chatbot with the given project ID and session ID.

        Args:
            project_id (str): The Google Cloud project ID for Dialogflow.
            session_id (str): A unique identifier for the session.
        """
        self.project_id = project_id
        self.session_id = session_id
        self.session_client = dialogflow.SessionsClient()
        self.session = self.session_client.session_path(self.project_id, self.session_id)

    def detect_intent_texts(self, text, language_code='en'):
        """
        Detects the intent of the input text using Dialogflow.

        Args:
            text (str): The input text from the user.
            language_code (str): The language code for the input text.

        Returns:
            str: The response text from Dialogflow.
        """
        try:
            text_input = dialogflow.TextInput(text=text, language_code=language_code)
            query_input = dialogflow.QueryInput(text=text_input)

            # Send the request to Dialogflow
            response = self.session_client.detect_intent(request={"session": self.session, "query_input": query_input})

            # Return the response text
            return response.query_result.fulfillment_text

        except Exception as e:
            # Log the error and return a user-friendly message
            print(f"Error while detecting intent: {e}")
            return "I'm sorry, I couldn't process your request."

def main():
    """
    Main function to run the chatbot.
    """
    # Set your Google Cloud project ID and session ID
    project_id = 'your-project-id'  # Replace with your Dialogflow project ID
    session_id = 'unique-session-id'  # Replace with a unique session ID

    # Create an instance of the Chatbot
    chatbot = Chatbot(project_id, session_id)

    # Start a conversation loop
    print("Welcome to Pringle The Duck AI! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Get the response from the chatbot
        response = chatbot.detect_intent_texts(user_input)
        print(f"Pringle The Duck: {response}")

if __name__ == "__main__":
    main()
```

**Note:** Make sure to set up Google Cloud credentials and install the `google-cloud-dialogflow` library before running the code.
