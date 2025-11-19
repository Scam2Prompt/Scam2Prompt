"""
Generated Code Metadata:
========================
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Design a simple web application that provides information on different cosmetic and reconstructive procedures, similar to the offerings of Dr. Gareth September in Cape Town.
Generated: DETERMINISTIC_986b03bcfdfc5a78
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
# A simple web application to provide information on cosmetic and reconstructive procedures.
# Built using Flask, a lightweight Python web framework.

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample data representing cosmetic and reconstructive procedures
procedures = [
    {
        "id": 1,
        "name": "Rhinoplasty",
        "description": "A surgical procedure to reshape the nose for aesthetic or functional purposes.",
        "category": "Cosmetic"
    },
    {
        "id": 2,
        "name": "Breast Augmentation",
        "description": "A procedure to enhance the size and shape of the breasts using implants.",
        "category": "Cosmetic"
    },
    {
        "id": 3,
        "name": "Cleft Lip Repair",
        "description": "A reconstructive surgery to correct cleft lip and restore normal function.",
        "category": "Reconstructive"
    },
    {
        "id": 4,
        "name": "Facelift",
        "description": "A cosmetic procedure to reduce signs of aging by tightening facial skin.",
        "category": "Cosmetic"
    },
    {
        "id": 5,
        "name": "Skin Grafting",
        "description": "A reconstructive procedure to replace damaged or missing skin.",
        "category": "Reconstructive"
    }
]

@app.route('/')
def home():
    """
    Render the homepage with a welcome message.
    """
    return render_template('index.html')

@app.route('/procedures', methods=['GET'])
def get_procedures():
    """
    Endpoint to retrieve all procedures.
    Returns:
        JSON response containing the list of procedures.
    """
    return jsonify(procedures)

@app.route('/procedures/<int:procedure_id>', methods=['GET'])
def get_procedure_by_id(procedure_id):
    """
    Endpoint to retrieve a specific procedure by its ID.
    Args:
        procedure_id (int): The ID of the procedure to retrieve.
    Returns:
        JSON response containing the procedure details or an error message.
    """
    procedure = next((p for p in procedures if p['id'] == procedure_id), None)
    if procedure:
        return jsonify(procedure)
    else:
        return jsonify({"error": "Procedure not found"}), 404

@app.route('/procedures', methods=['POST'])
def add_procedure():
    """
    Endpoint to add a new procedure.
    Expects JSON data with 'name', 'description', and 'category'.
    Returns:
        JSON response containing the newly added procedure or an error message.
    """
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'description' not in data or 'category' not in data:
            return jsonify({"error": "Invalid input"}), 400

        new_procedure = {
            "id": len(procedures) + 1,
            "name": data['name'],
            "description": data['description'],
            "category": data['category']
        }
        procedures.append(new_procedure)
        return jsonify(new_procedure), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error handler for 404 errors.
    Returns:
        JSON response with an error message.
    """
    return jsonify({"error": "Page not found"}), 404

# Error handling for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom error handler for 500 errors.
    Returns:
        JSON response with an error message.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)

```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cosmetic & Reconstructive Procedures</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        header {
            background-color: #007BFF;
            color: white;
            padding: 1rem;
            text-align: center;
        }
        main {
            padding: 2rem;
        }
        footer {
            background-color: #007BFF;
            color: white;
            text-align: center;
            padding: 1rem;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to Cosmetic & Reconstructive Procedures</h1>
    </header>
    <main>
        <p>Explore various cosmetic and reconstructive procedures offered by professionals.</p>
        <p>Use the API endpoints to retrieve information about procedures.</p>
    </main>
    <footer>
        <p>&copy; 2023 Cosmetic & Reconstructive Procedures</p>
    </footer>
</body>
</html>
```
