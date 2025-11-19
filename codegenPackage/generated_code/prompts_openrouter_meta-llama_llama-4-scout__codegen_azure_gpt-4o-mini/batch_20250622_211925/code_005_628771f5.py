"""
Generated Code Metadata:
========================
Original URL: https://deafah.in
Prompt: Develop a chatbot script that provides premium hospitality services for pilgrims and guests, similar to Deafah International Group's offerings, using a library like Dialogflow.
Generated: DETERMINISTIC_628771f58583bfe7
Batch ID: 20250622_211925
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

class HospitalityChatbot:
    def __init__(self, project_id, session_id):
        """
        Initializes the chatbot with the given project ID and session ID.

        Args:
            project_id (str): Google Cloud project ID for Dialogflow.
            session_id (str): Unique session ID for the conversation.
        """
        self.project_id = project_id
        self.session_id = session_id
        self.session_client = dialogflow.SessionsClient()
        self.session = self.session_client.session_path(self.project_id, self.session_id)

    def detect_intent_texts(self, text, language_code='en'):
        """
        Detects the intent of the user's text input.

        Args:
            text (str): The text input from the user.
            language_code (str): The language code for the input text.

        Returns:
            str: The response text from Dialogflow.
        """
        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)

        try:
            response = self.session_client.detect_intent(request={"session": self.session, "query_input": query_input})
            return response.query_result.fulfillment_text
        except Exception as e:
            print(f"Error detecting intent: {e}")
            return "I'm sorry, I couldn't process your request at the moment."

    def run_chatbot(self):
        """
        Runs the chatbot, allowing user interaction in a loop until 'exit' is typed.
        """
        print("Welcome to the Hospitality Chatbot! Type 'exit' to end the conversation.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for using our service. Goodbye!")
                break
            
            response = self.detect_intent_texts(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    # Set your Google Cloud project ID and session ID
    PROJECT_ID = os.getenv('DIALOGFLOW_PROJECT_ID')  # Ensure this environment variable is set
    SESSION_ID = 'unique_session_id'  # This can be any unique identifier for the session

    # Create an instance of the HospitalityChatbot and run it
    chatbot = HospitalityChatbot(PROJECT_ID, SESSION_ID)
    chatbot.run_chatbot()
```

### Requirements:
- Ensure you have the `google-cloud-dialogflow` library installed. You can install it using:
  ```bash
  pip install google-cloud-dialogflow
  ```
- Set the environment variable `DIALOGFLOW_PROJECT_ID` to your Dialogflow project ID before running the script.
