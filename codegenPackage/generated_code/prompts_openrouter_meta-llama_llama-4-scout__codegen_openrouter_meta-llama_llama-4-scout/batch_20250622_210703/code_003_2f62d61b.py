"""
Generated Code Metadata:
========================
Original URL: https://aliahtirafia.com
Prompt: Create a simple chatbot using a library like Dialogflow to provide customer support for a company offering services like تركيب الستائر and نقل عفش بالاحساء.
Generated: DETERMINISTIC_2f62d61bded70ec0
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import logging
from google.cloud import dialogflow

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Dialogflow client settings
DIALOGFLOW_PROJECT_ID = 'your-dialogflow-project-id'
DIALOGFLOW_AGENT_ID = 'your-dialogflow-agent-id'
GOOGLE_APPLICATION_CREDENTIALS = 'path-to-your-service-account-key.json'

# Set up Dialogflow client
def create_dialogflow_client():
    try:
        credentials = os.environ.get(GOOGLE_APPLICATION_CREDENTIALS)
        if not credentials:
            logger.error("GOOGLE_APPLICATION_CREDENTIALS environment variable is not set.")
            return None
        session_client = dialogflow.SessionsClient()
        return session_client
    except Exception as e:
        logger.error(f"Error creating Dialogflow client: {e}")
        return None

# Define a function to handle customer support queries
def handle_customer_support(query):
    session_client = create_dialogflow_client()
    if not session_client:
        return "Failed to create Dialogflow client."

    # Create a session
    session_path = session_client.session_path(DIALOGFLOW_PROJECT_ID, DIALOGFLOW_AGENT_ID)
    session = dialogflow.types.Session(path=session_path)

    try:
        # Send the query to Dialogflow
        query_input = dialogflow.types.QueryInput(
            text=dialogflow.types.TextInput(text=query, language_code='ar')
        )
        response = session_client.detect_intent(session=session, query_input=query_input)

        # Get the response text
        response_text = response.query_result.fulfillment_text
        return response_text
    except Exception as e:
        logger.error(f"Error handling customer support query: {e}")
        return "Sorry, I didn't understand that."

# Define a function to provide services information
def provide_services_info(service):
    services = {
        "تركيب الستائر": "We provide installation services for curtains and blinds.",
        "نقل عفش بالاحساء": "We offer moving services in Al-Ahsa."
    }
    return services.get(service, "Sorry, we don't provide that service.")

# Main function to handle user queries
def chatbot(query):
    if query.startswith("تركيب الستائر") or query.startswith("نقل عفش بالاحساء"):
        return provide_services_info(query)
    else:
        return handle_customer_support(query)

# Test the chatbot
if __name__ == "__main__":
    query = input("Enter your query: ")
    response = chatbot(query)
    print(response)
```
