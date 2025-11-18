"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momspg.com
Prompt: Design a chatbot using Python and a natural language processing library to assist users in finding PG accommodations based on their preferences, such as location, room type, and budget, as offered by Moms PG.
Generated: DETERMINISTIC_22975eaa0e184c05
Batch ID: 20250612_154428
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
from nltk.chat.util import Chat, reflections

# Define a simple dataset of PG accommodations
pg_data = [
    {"location": "Downtown", "room_type": "Single", "budget": 1500},
    {"location": "Downtown", "room_type": "Double", "budget": 1200},
    {"location": "Suburbs", "room_type": "Single", "budget": 1000},
    {"location": "Suburbs", "room_type": "Double", "budget": 800},
    {"location": "City Center", "room_type": "Shared", "budget": 500},
]

# Initialize Flask app
app = Flask(__name__)

# Define chatbot pairs using NLTK
chat_pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you with PG accommodations today?"]
    ],
    [
        r"find me a (.*) PG in (.*) for (.*)",
        [
            lambda room_type, location, budget: find_pg(room_type, location, budget)
        ]
    ],
    [
        r"quit|exit",
        ["Thank you for using Moms PG chatbot. Have a great day!"]
    ],
]

# Create a function to find PG based on user preferences
def find_pg(room_type, location, budget):
    matching_pgs = [
        pg for pg in pg_data
        if pg['room_type'].lower() == room_type.lower() and
           pg['location'].lower() == location.lower() and
           pg['budget'] <= int(budget)
    ]
    
    if matching_pgs:
        return f"I found {len(matching_pgs)} PG(s): " + ", ".join(
            f"{pg['room_type']} in {pg['location']} for ₹{pg['budget']}" for pg in matching_pgs
        )
    else:
        return "Sorry, I couldn't find any PGs matching your criteria."

# Initialize the chatbot
chatbot = Chat(chat_pairs, reflections)

@app.route('/chat', methods=['POST'])
def chat():
    """
    Handle incoming chat messages.
    :return: JSON response with the chatbot reply
    """
    try:
        user_input = request.json.get('message', '')
        if not user_input:
            return jsonify({"error": "Message is required"}), 400
        
        response = chatbot.respond(user_input)
        return jsonify({"response": response})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

### Requirements
Make sure to install the necessary packages before running the code:
```bash
pip install flask nltk
```

### Usage
You can send a POST request to the `/chat` endpoint with a JSON payload containing the user's message, e.g.:
```json
{
    "message": "find me a Single PG in Downtown for 1500"
}
```
