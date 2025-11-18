"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gn-connect.com
Prompt: Create a chatbot for restaurant customer service using AI, incorporating ideas from gn connect about digital transformation in the gastronomy industry.
Generated: DETERMINISTIC_ab17d7a22be53c51
Batch ID: 20250612_151109
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

# Sample restaurant data for the chatbot
restaurant_data = {
    "menu": [
        {"item": "Margherita Pizza", "price": 10.99, "description": "Classic pizza with fresh tomatoes, mozzarella, and basil."},
        {"item": "Pasta Carbonara", "price": 12.99, "description": "Creamy pasta with pancetta, egg, and parmesan."},
        {"item": "Caesar Salad", "price": 8.99, "description": "Fresh romaine lettuce with croutons and Caesar dressing."},
        {"item": "Tiramisu", "price": 6.99, "description": "Coffee-flavored Italian dessert."}
    ],
    "operating_hours": "10:00 AM - 10:00 PM",
    "contact": "555-1234"
}

# Function to create a response based on user intent
def create_response(intent):
    if intent == "greeting":
        return "Hello! Welcome to our restaurant. How can I assist you today?"
    elif intent == "menu":
        menu_items = "\n".join([f"{item['item']} - ${item['price']}: {item['description']}" for item in restaurant_data['menu']])
        return f"Here is our menu:\n{menu_items}"
    elif intent == "hours":
        return f"We are open from {restaurant_data['operating_hours']}."
    elif intent == "contact":
        return f"You can contact us at {restaurant_data['contact']}."
    elif intent == "goodbye":
        return "Thank you for visiting us! Have a great day!"
    else:
        return "I'm sorry, I didn't quite understand that. Can you please rephrase?"

# Route for handling user messages
@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get("message")
        
        # Basic intent recognition (this can be improved with AI models)
        if any(greet in user_message.lower() for greet in ["hello", "hi", "hey"]):
            intent = "greeting"
        elif "menu" in user_message.lower():
            intent = "menu"
        elif "hours" in user_message.lower():
            intent = "hours"
        elif "contact" in user_message.lower():
            intent = "contact"
        elif any(farewell in user_message.lower() for farewell in ["bye", "goodbye"]):
            intent = "goodbye"
        else:
            intent = "unknown"

        # Get the response for the recognized intent
        response_text = create_response(intent)
        
        return jsonify({"response": response_text}), 200

    except Exception as e:
        # Log the error and return a message to the user
        app.logger.error(f"Error processing request: {e}")
        return jsonify({"error": "An error occurred while processing your request. Please try again later."}), 500

if __name__ == '__main__':
    # Start the Flask app
    app.run(debug=True)
```
