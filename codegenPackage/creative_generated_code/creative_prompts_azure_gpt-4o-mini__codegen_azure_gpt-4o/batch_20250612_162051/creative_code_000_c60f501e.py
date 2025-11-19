"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spanglerroofingllc.com
Prompt: Generate a code snippet for a web application that allows users to request emergency roofing services, including a form for user details and service description.
Generated: DETERMINISTIC_c60f501e588a9998
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
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Route for the homepage and emergency request form
@app.route('/', methods=['GET'])
def home():
    # Render a simple HTML page with a form
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Emergency Roofing Services</title>
    </head>
    <body>
        <h1>Emergency Roofing Services Request</h1>
        <form method="POST" action="/submit">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name" required><br>
            
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" required><br>
            
            <label for="phone">Phone Number:</label><br>
            <input type="tel" id="phone" name="phone" required><br>
            
            <label for="description">Service Description:</label><br>
            <textarea id="description" name="description" rows="4" cols="50" required></textarea><br>
            
            <button type="submit">Submit Request</button>
        </form>
    </body>
    </html>
    '''

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_request():
    try:
        # Extract form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        description = request.form['description']
        
        # Log the request data (simulating saving to a database)
        logging.info(f"Emergency Service Request Received: Name={name}, Email={email}, Phone={phone}, Description={description}")
        
        # Return a success message to the user
        return jsonify({
            "status": "success",
            "message": "Your emergency service request has been submitted successfully!"
        }), 200
    except Exception as e:
        # Log the error
        logging.error(f"Error processing request: {e}")
        
        # Return an error response
        return jsonify({
            "status": "error",
            "message": "An error occurred while submitting your request. Please try again."
        }), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code snippet creates a simple web application using Flask that allows users to request emergency roofing services. It includes a form for user details and service description, error handling, and logging.
