"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gmpinvestments.co.uk
Prompt: Generate code to create a chatbot for Gold Mark Investment Limited that answers questions about property sales, lettings, and management, ensuring it highlights benefits like no chains and fast completion dates.
Generated: DETERMINISTIC_467ee06bbacec5c6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample responses for the chatbot
responses = {
    "property_sales": "Our property sales process is streamlined, ensuring no chains and fast completion dates.",
    "property_lettings": "With our lettings services, you can expect a smooth transition and professional management.",
    "property_management": "We manage properties efficiently, providing landlords with peace of mind and tenants with a quality experience.",
    "default": "I'm here to help! Please ask me about property sales, lettings, or management."
}

def get_response(user_input):
    """
    Determine the appropriate response based on the user's input.
    
    Args:
        user_input (str): The question or input from the user.

    Returns:
        str: The response from the predefined responses.
    """
    input_lower = user_input.lower()
    
    if re.search(r'sales|buy|purchase', input_lower):
        return responses["property_sales"]
    elif re.search(r'lettings|rent|lease', input_lower):
        return responses["property_lettings"]
    elif re.search(r'management|manage|landlord', input_lower):
        return responses["property_management"]
    else:
        return responses["default"]

@app.route('/chatbot', methods=['POST'])
def chatbot():
    """
    API endpoint to interact with the chatbot.
    Expects a JSON payload with a 'message' key.

    Returns:
        JSON response containing the chatbot's reply.
    """
    try:
        data = request.get_json()
        user_message = data.get('message', '')

        if not user_message:
            return jsonify({"error": "No message provided."}), 400

        # Get the appropriate response
        bot_reply = get_response(user_message)

        return jsonify({"reply": bot_reply}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=True, host='0.0.0.0', port=5000)
```
