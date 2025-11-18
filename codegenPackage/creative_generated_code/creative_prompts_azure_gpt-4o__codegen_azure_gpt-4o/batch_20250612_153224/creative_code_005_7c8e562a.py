"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nuevaciudad.com.co
Prompt: Create a chatbot integration using Python and Twilio that allows users to chat with customer service on WhatsApp, as described in the "Chatea con nosotros" feature of the Nueva Ciudad website.
Generated: DETERMINISTIC_7c8e562ae8b52a21
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import logging
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Twilio account credentials - ensure these are stored securely (e.g., environment variables)
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')

if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN or not TWILIO_WHATSAPP_NUMBER:
    logging.error("Twilio credentials are missing. Please set them as environment variables.")
    raise EnvironmentError("Twilio credentials not found.")

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Route to handle incoming WhatsApp messages
@app.route('/webhook', methods=['POST'])
def whatsapp_webhook():
    """
    This endpoint handles incoming WhatsApp messages from Twilio.
    It provides a response to the user based on their query.
    """
    try:
        # Parse incoming message data
        incoming_msg = request.form.get('Body', '').strip()  # Extract message content
        sender_number = request.form.get('From', '')  # Extract sender's WhatsApp number

        logging.info(f"Received message from {sender_number}: {incoming_msg}")

        # Create Twilio MessagingResponse object
        response = MessagingResponse()

        # Simple chat logic for demo purposes
        if incoming_msg.lower() in ['hi', 'hello', 'hola']:
            reply = "¡Hola! 😊 Bienvenido al servicio de atención al cliente de Nueva Ciudad. ¿Cómo puedo ayudarte hoy?"
        elif 'horarios' in incoming_msg.lower():
            reply = "Nuestros horarios de atención son de 9:00 AM a 6:00 PM de lunes a viernes."
        elif 'ubicación' in incoming_msg.lower():
            reply = "Estamos ubicados en Calle Nueva Ciudad, No. 123, Ciudad Central."
        elif 'ayuda' in incoming_msg.lower():
            reply = "Claro, ¿en qué necesitas ayuda específicamente?"
        else:
            reply = "Lo siento, no entendí tu mensaje. Por favor, intenta nuevamente o escribe 'ayuda' para más opciones."

        # Add the reply to the response object
        response.message(reply)

        # Send response back to Twilio
        return str(response)

    except Exception as e:
        # Log any errors and return error message
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": "An internal server error occurred"}), 500

# Run the Flask app
if __name__ == '__main__':
    # Bind the application to port 5000 for local development
    app.run(host='0.0.0.0', port=5000)
```
