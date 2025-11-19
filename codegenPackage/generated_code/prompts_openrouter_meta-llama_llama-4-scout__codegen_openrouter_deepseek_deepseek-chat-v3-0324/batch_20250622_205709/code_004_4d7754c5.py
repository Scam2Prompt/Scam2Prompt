"""
Generated Code Metadata:
========================
Original URL: https://jardinesdeprovenza.com.gt
Prompt: Develop a simple chatbot using a library like Dialogflow to provide customer support for a tourist destination like Jardines de Provenza, handling queries about events and accommodations.
Generated: DETERMINISTIC_4d7754c5a08970fe
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from flask import Flask, request, jsonify
from dialogflow_fulfillment import WebhookClient

app = Flask(__name__)

def handle_dialogflow_webhook(request):
    """Handle webhook requests from Dialogflow."""
    try:
        req = request.get_json(silent=True, force=True)
        agent = WebhookClient(req)
        
        intent_name = agent.intent
        
        if intent_name == 'Welcome Intent':
            welcome_response(agent)
        elif intent_name == 'Events Query':
            events_response(agent)
        elif intent_name == 'Accommodations Query':
            accommodations_response(agent)
        else:
            fallback_response(agent)
            
        return agent.response
    except Exception as e:
        print(f"Error handling webhook: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

def welcome_response(agent):
    """Handle welcome intent."""
    agent.add("Welcome to Jardines de Provenza! How can I help you today? You can ask about events or accommodations.")

def events_response(agent):
    """Handle events query."""
    current_events = [
        "Annual Flower Festival: March 15-20",
        "Summer Concert Series: Every Friday in July",
        "Provenza Food Fair: August 5-7"
    ]
    agent.add("Here are the upcoming events at Jardines de Provenza:")
    for event in current_events:
        agent.add(event)

def accommodations_response(agent):
    """Handle accommodations query."""
    nearby_accommodations = [
        "Provenza Grand Hotel (0.5 miles away)",
        "Garden View Inn (0.2 miles away)",
        "Rosewood Bed & Breakfast (0.3 miles away)"
    ]
    agent.add("Here are some nearby accommodations:")
    for accommodation in nearby_accommodations:
        agent.add(accommodation)

def fallback_response(agent):
    """Handle unknown intents."""
    agent.add("I didn't understand that. Can you please rephrase? You can ask about events or accommodations.")

@app.route('/webhook', methods=['POST'])
def webhook():
    """Handle Dialogflow webhook requests."""
    return handle_dialogflow_webhook(request)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
```
