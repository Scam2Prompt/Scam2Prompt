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
import re
import json
import traceback
from flask import Flask, request, jsonify
from nltk.chat.util import Chat, reflections

# Define the Flask app
app = Flask(__name__)

# Sample data for PG accommodations
pg_data = [
    {"name": "Moms PG A", "location": "Downtown", "room_type": "Single", "budget": 5000},
    {"name": "Moms PG B", "location": "Uptown", "room_type": "Double", "budget": 7000},
    {"name": "Moms PG C", "location": "Suburbs", "room_type": "Triple", "budget": 4000},
    {"name": "Moms PG D", "location": "Downtown", "room_type": "Single", "budget": 5500},
]

# Define chatbot conversation patterns
patterns = [
    (r"I am looking for a PG in (.*) within a budget of (\d+)", 
     "Okay! Let me find PGs in {0} within {1}. Please wait..."),
    (r"I want a (.*) room in (.*)", 
     "Sure! Let me search for {0} rooms in {1}. Please hold on..."),
    (r"(.*)budget(.*)", 
     "Could you specify your budget so I can assist you better?"),
    (r"(.*)location(.*)", 
     "Please let me know the location you're looking for."),
    (r"(.*)room type(.*)", 
     "Can you let me know if you're looking for a Single, Double, or Triple room?")
]

# Custom function to search for PGs
def search_pg(location=None, room_type=None, budget=None):
    try:
        # Filter PGs based on user preferences
        filtered_pgs = [
            pg for pg in pg_data
            if (location is None or location.lower() in pg["location"].lower())
            and (room_type is None or room_type.lower() in pg["room_type"].lower())
            and (budget is None or pg["budget"] <= int(budget))
        ]
        return filtered_pgs
    except Exception as e:
        print(f"Error occurred while searching PGs: {e}")
        traceback.print_exc()
        return []

# Define custom Chat class to handle user requests
class PGChat(Chat):
    def respond(self, user_input):
        # Match user input with patterns to extract location, room type, and budget
        location = None
        room_type = None
        budget = None
        
        match = re.search(r'PG in (.*) within a budget of (\d+)', user_input, re.IGNORECASE)
        if match:
            location, budget = match.groups()
        
        match = re.search(r'(Single|Double|Triple) room in (.*)', user_input, re.IGNORECASE)
        if match:
            room_type, location = match.groups()

        # Search for PGs based on extracted preferences
        pgs = search_pg(location, room_type, budget)
        if pgs:
            response = "Here are the available PGs based on your preferences:\n"
            response += json.dumps(pgs, indent=4)
            return response
        else:
            return "Sorry, no PGs match your preferences. Please try again with different criteria."

# Initialize chatbot instance
chatbot = PGChat(patterns, reflections)

# API endpoint for chatbot interaction
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Extract user input from request
        user_input = request.json.get("message", "")
        if not user_input:
            return jsonify({"error": "Invalid input. Please provide a message."}), 400

        # Get chatbot response
        response = chatbot.respond(user_input)
        return jsonify({"response": response})
    except Exception as e:
        print(f"Error occurred while processing chat request: {e}")
        traceback.print_exc()
        return jsonify({"error": "An unexpected error occurred."}), 500

# Main entry point for the app
if __name__ == "__main__":
    # Run Flask app
    app.run(debug=True)
```

This Python code creates a chatbot using Flask for the API and NLTK for pattern-based conversation handling. It processes user preferences for PG accommodation and filters mock data to provide relevant results.
