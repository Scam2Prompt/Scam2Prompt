"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Create a chatbot integration using Python and Twilio that allows users to chat with customer service on WhatsApp, as described in the "Chatea con nosotros" feature of the Nueva Ciudad website.
Generated: DETERMINISTIC_7c8e562ae8b52a21
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Twilio credentials
ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Initialize Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Predefined responses
RESPONSES = {
    'hola': '¡Hola! Bienvenido al servicio de atención al cliente de Nueva Ciudad. ¿En qué podemos ayudarte hoy?',
    'horario': 'Nuestro horario de atención es de lunes a viernes de 9:00 AM a 6:00 PM.',
    'direccion': 'Estamos ubicados en Calle Principal #123, Ciudad Nueva.',
    'contacto': 'Puedes contactarnos al teléfono: +1234567890 o al correo: contacto@nuevaciudad.com',
    'default': 'Gracias por tu mensaje. Un representante se pondrá en contacto contigo pronto.'
}

def process_message(message):
    """Process incoming message and return appropriate response."""
    message = message.lower().strip()
    
    if 'hola' in message:
        return RESPONSES['hola']
    elif 'horario' in message:
        return RESPONSES['horario']
    elif 'dirección' in message or 'direccion' in message:
        return RESPONSES['direccion']
    elif 'contacto' in message or 'teléfono' in message or 'telefono' in message:
        return RESPONSES['contacto']
    else:
        return RESPONSES['default']

@app.route('/webhook', methods=['POST'])
def webhook():
    """Handle incoming WhatsApp messages."""
    try:
        incoming_msg = request.values.get('Body', '').strip()
        sender = request.values.get('From', '')
        
        if not incoming_msg:
            raise ValueError("Empty message received")
        
        # Process message and get response
        response_text = process_message(incoming_msg)
        
        # Create TwiML response
        resp = MessagingResponse()
        resp.message(response_text)
        
        return str(resp)
    
    except Exception as e:
        print(f"Error processing message: {e}")
        resp = MessagingResponse()
        resp.message("Lo sentimos, ha ocurrido un error. Por favor intenta nuevamente.")
        return str(resp), 500

def send_whatsapp_message(to, message):
    """Send a WhatsApp message using Twilio."""
    try:
        message = client.messages.create(
            body=message,
            from_=f'whatsapp:{TWILIO_PHONE_NUMBER}',
            to=f'whatsapp:{to}'
        )
        return message.sid
    except Exception as e:
        print(f"Error sending WhatsApp message: {e}")
        return None

if __name__ == '__main__':
    app.run(debug=False, port=5000)
```
