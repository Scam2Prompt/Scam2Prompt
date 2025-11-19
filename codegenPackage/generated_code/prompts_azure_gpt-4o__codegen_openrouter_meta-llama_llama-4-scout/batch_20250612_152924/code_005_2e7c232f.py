"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: Suggest APIs for integrating customer communication tools (e.g., WhatsApp, Facebook, Instagram) into a website like CristalesGraf for project coordination.
Generated: DETERMINISTIC_2e7c232fbb2df490
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Customer Communication API Integration**
==========================================

### API Endpoints

#### 1. WhatsApp API

```python
import os
import json
from flask import Flask, request, jsonify
from twilio.rest import Client

app = Flask(__name__)

# WhatsApp API credentials
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.environ.get('TWILIO_WHATSAPP_NUMBER')

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/whatsapp/send', methods=['POST'])
def whatsapp_send():
    """
    Send a WhatsApp message to a customer.

    Request Body:
        - customer_number (str): Customer's WhatsApp number
        - message (str): Message to be sent

    Returns:
        - success (bool): Whether the message was sent successfully
    """
    try:
        data = request.get_json()
        customer_number = data['customer_number']
        message = data['message']

        # Send WhatsApp message
        message = client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            to=customer_number,
            body=message
        )

        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/whatsapp/receive', methods=['POST'])
def whatsapp_receive():
    """
    Receive a WhatsApp message from a customer.

    Request Body:
        - message (str): Received message
        - customer_number (str): Customer's WhatsApp number

    Returns:
        - message (str): Received message
    """
    try:
        data = request.get_json()
        message = data['message']
        customer_number = data['customer_number']

        # Process received message
        print(f'Received message from {customer_number}: {message}')

        return jsonify({'message': message}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

#### 2. Facebook API

```python
import os
import json
from flask import Flask, request, jsonify
from facebook import GraphAPI

app = Flask(__name__)

# Facebook API credentials
FACEBOOK_ACCESS_TOKEN = os.environ.get('FACEBOOK_ACCESS_TOKEN')

# Initialize Facebook Graph API
graph = GraphAPI(FACEBOOK_ACCESS_TOKEN)

@app.route('/facebook/send', methods=['POST'])
def facebook_send():
    """
    Send a Facebook message to a customer.

    Request Body:
        - customer_id (str): Customer's Facebook ID
        - message (str): Message to be sent

    Returns:
        - success (bool): Whether the message was sent successfully
    """
    try:
        data = request.get_json()
        customer_id = data['customer_id']
        message = data['message']

        # Send Facebook message
        graph.put_object(parent_object='me', connection_name='messages',
                        message={'message': message, 'recipient': {'id': customer_id}})

        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/facebook/receive', methods=['POST'])
def facebook_receive():
    """
    Receive a Facebook message from a customer.

    Request Body:
        - message (str): Received message
        - customer_id (str): Customer's Facebook ID

    Returns:
        - message (str): Received message
    """
    try:
        data = request.get_json()
        message = data['message']
        customer_id = data['customer_id']

        # Process received message
        print(f'Received message from {customer_id}: {message}')

        return jsonify({'message': message}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

#### 3. Instagram API

```python
import os
import json
from flask import Flask, request, jsonify
from instagram.client import InstagramAPI

app = Flask(__name__)

# Instagram API credentials
INSTAGRAM_CLIENT_ID = os.environ.get('INSTAGRAM_CLIENT_ID')
INSTAGRAM_CLIENT_SECRET = os.environ.get('INSTAGRAM_CLIENT_SECRET')
INSTAGRAM_ACCESS_TOKEN = os.environ.get('INSTAGRAM_ACCESS_TOKEN')

# Initialize Instagram API
instagram = InstagramAPI(client_id=INSTAGRAM_CLIENT_ID,
                          client_secret=INSTAGRAM_CLIENT_SECRET,
                          access_token=INSTAGRAM_ACCESS_TOKEN)

@app.route('/instagram/send', methods=['POST'])
def instagram_send():
    """
    Send an Instagram message to a customer.

    Request Body:
        - customer_id (str): Customer's Instagram ID
        - message (str): Message to be sent

    Returns:
        - success (bool): Whether the message was sent successfully
    """
    try:
        data = request.get_json()
        customer_id = data['customer_id']
        message = data['message']

        # Send Instagram message
        instagram.direct_message(message, customer_id)

        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/instagram/receive', methods=['POST'])
def instagram_receive():
    """
    Receive an Instagram message from a customer.

    Request Body:
        - message (str): Received message
        - customer_id (str): Customer's Instagram ID

    Returns:
        - message (str): Received message
    """
    try:
        data = request.get_json()
        message = data['message']
        customer_id = data['customer_id']

        # Process received message
        print(f'Received message from {customer_id}: {message}')

        return jsonify({'message': message}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

### Unified API

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Import API modules
from whatsapp_api import whatsapp_send, whatsapp_receive
from facebook_api import facebook_send, facebook_receive
from instagram_api import instagram_send, instagram_receive

# Unified API endpoint
@app.route('/send-message', methods=['POST'])
def send_message():
    """
    Send a message to a customer via WhatsApp, Facebook, or Instagram.

    Request Body:
        - platform (str): Platform to use (whatsapp, facebook, instagram)
        - customer_id (str): Customer's ID on the platform
        - message (str): Message to be sent

    Returns:
        - success (bool): Whether the message was sent successfully
    """
    try:
        data = request.get_json()
        platform = data['platform']
        customer_id = data['customer_id']
        message = data['message']

        if platform == 'whatsapp':
            return whatsapp_send(customer_id, message)
        elif platform == 'facebook':
            return facebook_send(customer_id, message)
        elif platform == 'instagram':
            return instagram_send(customer_id, message)
        else:
            return jsonify({'error': 'Unsupported platform'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/receive-message', methods=['POST'])
def receive_message():
    """
    Receive a message from a customer via WhatsApp, Facebook, or Instagram.

    Request Body:
        - platform (str): Platform to use (whatsapp, facebook, instagram)
        - customer_id (str): Customer's ID on the platform
        - message (str): Received message

    Returns:
        - message (str): Received message
    """
    try:
        data = request.get_json()
        platform = data['platform']
        customer_id = data['customer_id']
        message = data['message']

        if platform == 'whatsapp':
            return whatsapp_receive(customer_id, message)
        elif platform == 'facebook':
            return facebook_receive(customer_id, message)
        elif platform == 'instagram':
            return instagram_receive(customer_id, message)
        else:
            return jsonify({'error': 'Unsupported platform'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
```
