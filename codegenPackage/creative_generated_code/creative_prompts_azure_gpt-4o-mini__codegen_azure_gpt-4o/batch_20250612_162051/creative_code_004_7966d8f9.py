"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.izikard.com
Prompt: Create a sample code for a web application that allows users to design and order personalized NFC business cards like those from Izikard.
Generated: DETERMINISTIC_7966d8f9f3b06f99
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
import uuid
import os

app = Flask(__name__)

# Placeholder directory for storing card designs (in production, use a database)
CARD_DESIGN_DIR = "card_designs"
os.makedirs(CARD_DESIGN_DIR, exist_ok=True)

@app.route('/')
def home():
    """
    Renders the homepage for designing and ordering NFC business cards.
    """
    return render_template('index.html')  # Assume 'index.html' contains the frontend UI

@app.route('/design', methods=['POST'])
def design_card():
    """
    Endpoint for designing a personalized NFC business card.
    Accepts user input via POST request and saves the design.
    """
    try:
        # Parse input data from the request
        data = request.json
        full_name = data.get('full_name')
        contact_info = data.get('contact_info')
        company_name = data.get('company_name')
        design_template = data.get('design_template')

        # Validate input
        if not full_name or not contact_info or not company_name or not design_template:
            return jsonify({'error': 'All fields are required'}), 400

        # Generate a unique ID for the card design
        card_id = str(uuid.uuid4())
        card_data = {
            'card_id': card_id,
            'full_name': full_name,
            'contact_info': contact_info,
            'company_name': company_name,
            'design_template': design_template
        }

        # Save card design to a file (in production, save to a database)
        card_file_path = os.path.join(CARD_DESIGN_DIR, f"{card_id}.json")
        with open(card_file_path, 'w') as card_file:
            card_file.write(str(card_data))  # Save the card details

        return jsonify({'message': 'Card design saved successfully', 'card_id': card_id}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

@app.route('/order/<card_id>', methods=['POST'])
def order_card(card_id):
    """
    Endpoint to order a previously designed NFC business card.
    """
    try:
        # Check if the card design exists
        card_file_path = os.path.join(CARD_DESIGN_DIR, f"{card_id}.json")
        if not os.path.exists(card_file_path):
            return jsonify({'error': 'Card design not found'}), 404

        # Simulate ordering process (in production, integrate with payment gateway and order system)
        return jsonify({'message': f"Order for card ID {card_id} placed successfully"}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** Ensure you have Flask installed (`pip install flask`) and create a basic `index.html` file for the UI in the same directory. In production, replace file-based storage with a database and add authentication & payment processing.
