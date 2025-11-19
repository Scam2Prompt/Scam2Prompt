"""
Generated Code Metadata:
========================
Original URL: https://millymally.pl
Prompt: Develop a simple chatbot using a library like Dialogflow to provide customer support for an e-commerce store selling children's products, answering questions like "What is the price of Milly Mally Rowerek 5w1 Optimus Max?"
Generated: DETERMINISTIC_87259ccec895e691
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from google.cloud import dialogflow_v2 as dialogflow
import os

# Initialize Flask app
app = Flask(__name__)

# Set up Dialogflow credentials
# Ensure the environment variable GOOGLE_APPLICATION_CREDENTIALS is set to the path of your Dialogflow service account key JSON file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/dialogflow-service-account-key.json"

# Dialogflow project ID
DIALOGFLOW_PROJECT_ID = "your-dialogflow-project-id"
DIALOGFLOW_LANGUAGE_CODE = "en"

# Function to send user query to Dialogflow and get a response
def get_dialogflow_response(session_id, user_query):
    try:
        # Create a session client
        session_client = dialogflow.SessionsClient()
        
        # Define the session path
        session = session_client.session_path(DIALOGFLOW_PROJECT_ID, session_id)
        
        # Create the text input for Dialogflow
        text_input = dialogflow.TextInput(text=user_query, language_code=DIALOGFLOW_LANGUAGE_CODE)
        
        # Create the query input
        query_input = dialogflow.QueryInput(text=text_input)
        
        # Send the query to Dialogflow and get the response
        response = session_client.detect_intent(request={"session": session, "query_input": query_input})
        
        # Extract the fulfillment text (response message) from Dialogflow
        return response.query_result.fulfillment_text
    except Exception as e:
        # Handle errors gracefully
        return f"An error occurred while processing your request: {str(e)}"

# Define a route for the chatbot
@app.route("/chatbot", methods=["POST"])
def chatbot():
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        
        # Extract the user query and session ID
        user_query = data.get("query", "")
        session_id = data.get("session_id", "default_session")
        
        # Validate input
        if not user_query:
            return jsonify({"error": "Query is required"}), 400
        
        # Get the response from Dialogflow
        response_message = get_dialogflow_response(session_id, user_query)
        
        # Return the response as JSON
        return jsonify({"response": response_message})
    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run the Flask app
if __name__ == "__main__":
    # Use a production-ready server like Gunicorn in deployment
    app.run(host="0.0.0.0", port=5000, debug=False)
```

### Notes:
1. Replace `"path/to/your/dialogflow-service-account-key.json"` with the actual path to your Dialogflow service account key JSON file.
2. Replace `"your-dialogflow-project-id"` with your Dialogflow project ID.
3. Use a production-ready server like Gunicorn or similar when deploying this Flask app in a production environment.
