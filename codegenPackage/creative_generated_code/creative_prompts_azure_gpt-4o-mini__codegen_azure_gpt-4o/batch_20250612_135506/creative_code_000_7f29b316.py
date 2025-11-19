"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://regency-towel.com
Prompt: Generate a code snippet for an online inquiry form that captures customer details for towel orders, similar to the inquiry process at Regency Towel.
Generated: DETERMINISTIC_7f29b31635f391ba
Batch ID: 20250612_135506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to display a sample form (in production, this would be replaced with a full web page)
@app.route('/inquiry-form', methods=['GET'])
def inquiry_form():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Towel Order Inquiry Form</title>
    </head>
    <body>
        <h1>Inquiry Form for Towel Orders</h1>
        <form action="/submit-inquiry" method="POST">
            <label for="name">Full Name:</label><br>
            <input type="text" id="name" name="name" required><br><br>
            
            <label for="email">Email Address:</label><br>
            <input type="email" id="email" name="email" required><br><br>
            
            <label for="phone">Phone Number:</label><br>
            <input type="tel" id="phone" name="phone" required><br><br>
            
            <label for="quantity">Number of Towels:</label><br>
            <input type="number" id="quantity" name="quantity" min="1" required><br><br>
            
            <label for="comments">Additional Comments:</label><br>
            <textarea id="comments" name="comments"></textarea><br><br>
            
            <button type="submit">Submit Inquiry</button>
        </form>
    </body>
    </html>
    '''

# Route to handle form submission
@app.route('/submit-inquiry', methods=['POST'])
def submit_inquiry():
    try:
        # Capture form data
        customer_details = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "phone": request.form.get("phone"),
            "quantity": request.form.get("quantity"),
            "comments": request.form.get("comments")
        }
        
        # Validate required fields
        if not all([customer_details["name"], customer_details["email"], customer_details["phone"], customer_details["quantity"]]):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Log or process the inquiry (this is where you might save to a database)
        # For demonstration purposes, we simply return the captured data
        return jsonify({
            "message": "Inquiry submitted successfully",
            "data": customer_details
        }), 200
    
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred while processing the inquiry", "details": str(e)}), 500

# Run the app (development environment only; use a production-ready server like Gunicorn for deployment)
if __name__ == '__main__':
    app.run(debug=True)
```
