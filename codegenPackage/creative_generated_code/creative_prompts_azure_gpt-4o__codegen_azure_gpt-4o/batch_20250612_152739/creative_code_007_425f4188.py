"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suzuki-capital.com
Prompt: Develop a chatbot using Python that provides information about Suzuki Capital Motors' 3S Workshop services, including repair, maintenance, and genuine parts availability.
Generated: DETERMINISTIC_425f4188302688d2
Batch ID: 20250612_152739
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

# Initialize the Flask application
app = Flask(__name__)

# Define the available services at Suzuki Capital Motors 3S Workshop
services = {
    "repair": "We offer comprehensive repair services for Suzuki vehicles.",
    "maintenance": "Our maintenance services include oil change, tire rotation, and more to keep your vehicle in top condition.",
    "genuine parts": "We provide genuine Suzuki parts to ensure your vehicle performs optimally."
}

# Function to handle user queries
def get_service_info(user_message):
    """
    Process the user's message and provide relevant information about 3S Workshop services.
    
    :param user_message: str: The input message from the user.
    :return: str: A response message.
    """
    user_message = user_message.lower()

    # Check for specific keywords related to services
    for keyword, info in services.items():
        if re.search(rf'\b{keyword}\b', user_message):
            return info

    # Default response if no keyword matches
    return "I'm sorry, I couldn't understand your request. Our services include repair, maintenance, and genuine parts availability. Please specify one for more details."

@app.route('/chat', methods=['POST'])
def chat():
    """
    API endpoint to handle chatbot messaging.
    Expects a JSON payload with a 'message' key.
    
    :return: JSON response with the chatbot's reply.
    """
    try:
        # Get the user's message from the POST request
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({"error": "Message field is required."}), 400

        # Generate the chatbot response based on the user's input
        response = get_service_info(user_message)

        return jsonify({"reply": response})
    
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
