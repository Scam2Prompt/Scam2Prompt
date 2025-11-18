"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prize-beam.net
Prompt: Create a chatbot using HubSpot's Free Chatbot Builder that integrates with the Service Hub's omni-channel help desk for customer support.
Generated: DETERMINISTIC_ba5e318c3c0c1211
Batch ID: 20250612_152109
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hubapi.com/conversations/v3/inboxes/messages": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Unfortunately, HubSpot's Free Chatbot Builder does not allow direct code integration as it is a no-code tool that relies on a visual interface for chatbot creation. Instead, it integrates with HubSpot Service Hub and other tools directly through its platform.

If you want to programmatically achieve similar functionality, you would need to use HubSpot's APIs or webhook integrations in combination with your own chatbot framework. Here’s sample Python code to create a chatbot using Flask and integrate it with HubSpot APIs for customer support.

```python
import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set HubSpot API key (use environment variables in production for security)
HUBSPOT_API_KEY = os.getenv("HUBSPOT_API_KEY")  # Replace with your HubSpot API key

# Function to send a message to HubSpot Service Hub
def send_to_hubspot(contact_id, message):
    """
    Sends a message to HubSpot Service Hub using Conversations API.
    Args:
        contact_id (str): The HubSpot contact ID.
        message (str): The message to send.
    Returns:
        dict: Response from HubSpot API.
    """
    url = f"https://api.hubapi.com/conversations/v3/inboxes/messages"
    headers = {
        "Authorization": f"Bearer {HUBSPOT_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "sender": {
            "id": contact_id,
            "type": "CONTACT"
        },
        "message": {
            "text": message
        }
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Endpoint for chatbot messages. This simulates receiving a message from the user
    and forwarding it to HubSpot Service Hub.
    """
    data = request.json
    
    # Validate input data
    if not data or 'contact_id' not in data or 'message' not in data:
        return jsonify({"error": "Invalid request payload"}), 400
    
    contact_id = data['contact_id']
    message = data['message']
    
    # Forward the message to HubSpot
    response = send_to_hubspot(contact_id, message)
    
    return jsonify(response)

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint.
    """
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```

### Key Points:
1. **HubSpot API Key:** Replace `os.getenv("HUBSPOT_API_KEY")` with your HubSpot API key or configure it as an environment variable for better security.
2. **Error Handling:** Includes error handling for invalid requests and API failures.
3. **Endpoints:** 
   - `/webhook` is the main endpoint to receive chatbot messages and forward them to HubSpot Service Hub.
   - `/health` is a simple health check endpoint.
4. **Production Considerations:** Use HTTPS for secure communication in production. Implement proper rate-limiting and logging for scalability.

Integrate this with your chatbot platform, and ensure you have configured HubSpot Service Hub to receive conversation messages.
