"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperswap.tech
Prompt: Generate a code snippet for a web application that allows users to request a quote for residential paving services, similar to the features on Hyperswap's Bedford Paving site.
Generated: DETERMINISTIC_252ddddc1ee016ff
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data storage for simplicity (in production, use a database like PostgreSQL or MongoDB)
requests_data = []

@app.route('/request-quote', methods=['POST'])
def request_quote():
    """
    Endpoint to handle quote requests for residential paving services.
    Accepts JSON input and stores it in the mock data storage.
    """
    try:
        # Parse incoming JSON request data
        data = request.get_json()

        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'address', 'project_details']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        # Store the data (in production, insert into a database)
        request_entry = {
            'name': data['name'],
            'email': data['email'],
            'phone': data['phone'],
            'address': data['address'],
            'project_details': data['project_details']
        }
        requests_data.append(request_entry)

        # Return success response
        return jsonify({'message': 'Quote request submitted successfully!', 'data': request_entry}), 201

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({'error': 'An error occurred while processing your request.', 'details': str(e)}), 500

@app.route('/view-requests', methods=['GET'])
def view_requests():
    """
    Endpoint to view all quote requests.
    For simplicity, retrieves the data from the mock storage.
    """
    try:
        return jsonify({'requests': requests_data}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving requests.', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application on localhost, port 5000
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Residential Paving Quote Request</title>
</head>
<body>
    <h1>Request a Quote</h1>
    <form id="quote-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>

        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" required><br>

        <label for="address">Address:</label>
        <input type="text" id="address" name="address" required><br>

        <label for="project_details">Project Details:</label><br>
        <textarea id="project_details" name="project_details" required></textarea><br>

        <button type="button" onclick="submitQuoteRequest()">Submit Request</button>
    </form>

    <script>
        // Function to handle form submission
        async function submitQuoteRequest() {
            const formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                phone: document.getElementById('phone').value,
                address: document.getElementById('address').value,
                project_details: document.getElementById('project_details').value
            };

            try {
                const response = await fetch('/request-quote', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formData)
                });

                const result = await response.json();

                if (response.ok) {
                    alert(result.message);
                } else {
                    alert(`Error: ${result.error}`);
                }
            } catch (error) {
                alert('An error occurred while submitting the request.');
                console.error(error);
            }
        }
    </script>
</body>
</html>
```

### Notes
1. Save the HTML file as `index.html` and run the Python script using `python app.py`. Ensure Flask is installed (`pip install flask`).
2. Host both files correctly (e.g., using Flask static routing or another web server) for production deployment.
3. Replace mock data storage with a database for persistent storage in production.
