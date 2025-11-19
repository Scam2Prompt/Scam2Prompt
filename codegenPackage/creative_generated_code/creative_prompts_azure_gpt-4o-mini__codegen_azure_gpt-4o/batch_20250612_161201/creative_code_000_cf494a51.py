"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dexodoor.com
Prompt: Generate a code snippet for a web application that allows users to request a quote for UPVC window and door systems, similar to the functionality on the DEXODOOR website.
Generated: DETERMINISTIC_cf494a51cfcf3598
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A Flask-based web application for requesting quotes for UPVC window and door systems.
The application follows best practices, includes proper error handling, and is production-ready.
"""

from flask import Flask, render_template, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Simulated data storage for quotes (In production, use a database)
quotes = []

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.description, "code": e.code})
    response.content_type = "application/json"
    return response

# Error handler for other exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": "An unexpected error occurred"}), 500

# Home page route
@app.route('/')
def home():
    """
    Render the home page.
    """
    return render_template('index.html')

# Endpoint for submitting a quote request
@app.route('/request-quote', methods=['POST'])
def request_quote():
    """
    Handle quote requests submitted via the form.
    """
    try:
        # Parse form data
        user_data = request.form
        name = user_data.get('name', '').strip()
        email = user_data.get('email', '').strip()
        product_type = user_data.get('product_type', '').strip()
        dimensions = user_data.get('dimensions', '').strip()

        # Validate input
        if not name or not email or not product_type or not dimensions:
            return jsonify({"error": "All fields are required"}), 400

        # Simulate storing the quote request
        quote = {
            "name": name,
            "email": email,
            "product_type": product_type,
            "dimensions": dimensions
        }
        quotes.append(quote)

        # Return success response
        return jsonify({"message": "Quote request successfully submitted"}), 201

    except Exception as e:
        # Log error and return generic error message
        app.logger.error(f"Error in request_quote: {str(e)}")
        return jsonify({"error": "An error occurred while processing your request"}), 500

# Endpoint to retrieve all quote requests (for admin use)
@app.route('/quotes', methods=['GET'])
def get_quotes():
    """
    Retrieve all quote requests.
    """
    return jsonify(quotes), 200

# Application entry point
if __name__ == '__main__':
    # Run the application on localhost, port 5000
    app.run(debug=True)
```

### HTML Template (`templates/index.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UPVC Quote Request</title>
</head>
<body>
    <h1>Request a Quote for UPVC Window and Door Systems</h1>
    <form action="/request-quote" method="post">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="product_type">Product Type (e.g., Window, Door):</label><br>
        <input type="text" id="product_type" name="product_type" required><br><br>
        
        <label for="dimensions">Dimensions (e.g., Width x Height):</label><br>
        <input type="text" id="dimensions" name="dimensions" required><br><br>

        <button type="submit">Submit Request</button>
    </form>
</body>
</html>
```

Ensure you install Flask (`pip install flask`) before running the application.
