"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://springsinternational.org
Prompt: Create a chatbot using Python that answers questions about Springs International Ministries’ programs, such as “Where was Jesus on Saturday?” or details about Mission 2030.
Generated: DETERMINISTIC_b7ca9ed3814b2009
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load program details (mock data for demonstration purposes)
PROGRAM_DETAILS = {
    "where_was_jesus_on_saturday": "According to biblical accounts, Jesus rested in the tomb on Saturday after His crucifixion.",
    "mission_2030": "Mission 2030 aims to spread the message of hope and love globally by 2030 through outreach programs, education, and community service.",
    "default": "I'm sorry, I don't have information about that topic. Please ask about 'Mission 2030' or 'Where was Jesus on Saturday?'"
}

# Function to handle user queries
def get_response(query):
    # Normalize query to lowercase
    normalized_query = query.lower()
    
    # Define responses for known queries
    if "where was jesus on saturday" in normalized_query:
        return PROGRAM_DETAILS["where_was_jesus_on_saturday"]
    elif "mission 2030" in normalized_query:
        return PROGRAM_DETAILS["mission_2030"]
    else:
        return PROGRAM_DETAILS["default"]

@app.route('/chat', methods=['POST'])
def chatbot():
    """
    Endpoint to handle chatbot interactions.
    Expects a JSON payload with a 'query' field.
    Returns a JSON response with chatbot's answer.
    """
    try:
        # Parse incoming JSON request
        data = request.get_json()
        if not data or 'query' not in data:
            return jsonify({"error": "Invalid request. Please provide a 'query' field."}), 400
        
        user_query = data['query']
        response = get_response(user_query)
        
        return jsonify({"response": response}), 200
    except Exception as e:
        # Catch and handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the chatbot server
    app.run(debug=True)
```

### Notes for Deployment:
- Install required dependencies before running (`pip install flask`).
- Replace mock `PROGRAM_DETAILS` data with real data.
- Disable debugging (`debug=False`) in production for better security.
