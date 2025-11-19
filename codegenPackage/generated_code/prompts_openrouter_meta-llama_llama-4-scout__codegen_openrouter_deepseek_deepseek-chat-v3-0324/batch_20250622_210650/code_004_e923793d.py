"""
Generated Code Metadata:
========================
Original URL: https://934ummfm.com
Prompt: Design a basic chatbot that provides information about UMM FM's programs and events, using a library like Dialogflow.
Generated: DETERMINISTIC_e923793d7af0afaf
Batch ID: 20250622_210650
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
from dialogflow_fulfillment import WebhookClient, QuickReplies, Text

app = Flask(__name__)

# Environment variables for configuration
DIALOGFLOW_PROJECT_ID = os.getenv('DIALOGFLOW_PROJECT_ID', 'your-project-id')
PORT = os.getenv('PORT', 8080)

@app.route('/webhook', methods=['POST'])
def webhook():
    """Handle webhook requests from Dialogflow."""
    try:
        request_json = request.get_json(silent=True, force=True)
        agent = WebhookClient(request_json)
        
        intent_name = agent.intent
        
        if intent_name == 'Welcome':
            handle_welcome(agent)
        elif intent_name == 'ProgramSchedule':
            handle_program_schedule(agent)
        elif intent_name == 'UpcomingEvents':
            handle_upcoming_events(agent)
        elif intent_name == 'ContactInfo':
            handle_contact_info(agent)
        else:
            handle_unknown_intent(agent)
            
        return jsonify(agent.response)
    
    except Exception as e:
        print(f"Error processing webhook: {str(e)}")
        return jsonify({"fulfillmentText": "Sorry, I encountered an error processing your request."}), 500

def handle_welcome(agent):
    """Handle welcome intent."""
    welcome_text = "Welcome to UMM FM! How can I help you today?"
    quick_replies = QuickReplies(
        quick_replies=[
            "Program Schedule",
            "Upcoming Events",
            "Contact Information"
        ]
    )
    agent.add(Text(welcome_text))
    agent.add(quick_replies)

def handle_program_schedule(agent):
    """Handle program schedule intent."""
    schedule = {
        "Monday": "Morning Show (6-9 AM), Afternoon Jazz (2-5 PM)",
        "Tuesday": "News Hour (12-1 PM), Evening Rock (7-10 PM)",
        "Wednesday": "Classical Hour (1-2 PM), Indie Night (8-11 PM)",
        "Thursday": "Talk Show (10 AM-12 PM), Electronic Beats (6-9 PM)",
        "Friday": "Weekend Warmup (5-8 PM)",
        "Saturday": "Saturday Specials (10 AM-4 PM)",
        "Sunday": "Sunday Chill (12-6 PM)"
    }
    
    response = "Here's our weekly program schedule:\n"
    for day, programs in schedule.items():
        response += f"{day}: {programs}\n"
    
    agent.add(Text(response))

def handle_upcoming_events(agent):
    """Handle upcoming events intent."""
    events = [
        "Live Concert: Local Band Night - June 15th, 7 PM",
        "Radio Drama Premiere: 'The Midnight Hour' - June 20th, 8 PM",
        "Fundraiser Marathon - June 25th, all day"
    ]
    
    response = "Upcoming events at UMM FM:\n" + "\n".join(events)
    agent.add(Text(response))

def handle_contact_info(agent):
    """Handle contact information intent."""
    contact_info = """
    You can contact UMM FM at:
    Phone: (555) 123-4567
    Email: contact@ummfm.edu
    Address: 123 University Ave, Morris, MN 56267
    """
    agent.add(Text(contact_info))

def handle_unknown_intent(agent):
    """Handle unknown or unmatched intents."""
    agent.add(Text("I'm not sure how to help with that. Can you try asking something else?"))

if __name__ == '__main__':
    app.run(port=PORT)
```
