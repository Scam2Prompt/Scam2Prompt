"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bplservicescenter.com
Prompt: Develop a chatbot using Python that can assist users in finding BPL service centers near them and booking repair services for appliances like refrigerators and washing machines.
Generated: DETERMINISTIC_c212657ed9c9f3cc
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import re
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample database of service centers
SERVICE_CENTERS = [
    {"id": 1, "name": "BPL Service Center - Downtown", "location": "Downtown", "contact": "123-456-7890"},
    {"id": 2, "name": "BPL Service Center - Uptown", "location": "Uptown", "contact": "987-654-3210"},
    {"id": 3, "name": "BPL Service Center - Suburbs", "location": "Suburbs", "contact": "456-789-0123"},
]

# Supported appliances
APPLIANCES = ["refrigerator", "washing machine"]

# Chatbot route
@app.route('/chatbot', methods=['POST'])
def chatbot():
    """
    Chatbot endpoint to handle user requests for finding service centers
    and booking repair services.
    """
    try:
        # Parse user input
        user_input = request.json.get("message", "").strip().lower()
        
        if not user_input:
            return jsonify({"response": "Please provide a valid input."})
        
        # Handle service center search
        if "service center near" in user_input:
            location_match = re.search(r"near (\w+)", user_input)
            if location_match:
                location = location_match.group(1).capitalize()
                centers = [center for center in SERVICE_CENTERS if center["location"] == location]
                if centers:
                    response = f"Found the following service center(s) in {location}:\n"
                    for center in centers:
                        response += f"- {center['name']} (Contact: {center['contact']})\n"
                else:
                    response = f"Sorry, no service centers found near {location}."
                return jsonify({"response": response})
            else:
                return jsonify({"response": "Please specify a location (e.g., 'service center near Downtown')."})

        # Handle repair service booking
        elif any(appliance in user_input for appliance in APPLIANCES):
            appliance_match = next((appliance for appliance in APPLIANCES if appliance in user_input), None)
            if appliance_match:
                response = f"You can book a repair service for your {appliance_match}. Please call one of our service centers:\n"
                for center in SERVICE_CENTERS:
                    response += f"- {center['name']} (Contact: {center['contact']})\n"
                return jsonify({"response": response})
            else:
                return jsonify({"response": "Please specify a valid appliance (e.g., 'repair my refrigerator')."})

        # Handle unknown requests
        else:
            return jsonify({"response": "I'm sorry, I didn't understand your request. You can ask about service centers or booking repair services for appliances."})

    except Exception as e:
        # Error handling
        return jsonify({"response": "An error occurred while processing your request.", "error": str(e)})


if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```
