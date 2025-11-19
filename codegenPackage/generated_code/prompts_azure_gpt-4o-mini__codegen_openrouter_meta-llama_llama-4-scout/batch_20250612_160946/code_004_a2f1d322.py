"""
Generated Code Metadata:
========================
Original URL: https://coworkingcomercio.com.br
Prompt: Design a web form for users to inquire about coworking space availability, including fields for name, email, and desired space type, based on Coworking Comércio's services.
Generated: DETERMINISTIC_a2f1d32293da63cb
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define available coworking space types
space_types = ["private_office", "shared_desk", "meeting_room"]

# In-memory storage for inquiries (replace with a database in production)
inquiries = []

@app.route('/inquire', methods=['POST'])
def inquire():
    """
    Handle coworking space inquiry form submissions.

    Request Body:
        - name (str): User's name
        - email (str): User's email
        - space_type (str): Desired space type

    Returns:
        - JSON response with a success message or error details
    """
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Missing request data"}), 400

        name = data.get('name')
        email = data.get('email')
        space_type = data.get('space_type')

        if not all([name, email, space_type]):
            return jsonify({"error": "Please fill in all required fields"}), 400

        if space_type not in space_types:
            return jsonify({"error": f"Invalid space type. Available types: {', '.join(space_types)}"}), 400

        # Store inquiry (replace with database logic in production)
        inquiries.append({
            'name': name,
            'email': email,
            'space_type': space_type
        })

        return jsonify({"message": "Inquiry submitted successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coworking Comércio Inquiry Form</title>
    <style>
        form {
            max-width: 500px;
            margin: 40px auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        label {
            display: block;
            margin-bottom: 10px;
        }
        input, select {
            width: 100%;
            height: 40px;
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #ccc;
        }
        button[type="submit"] {
            background-color: #4CAF50;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button[type="submit"]:hover {
            background-color: #3e8e41;
        }
    </style>
</head>
<body>
    <form id="inquiry-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="space_type">Desired Space Type:</label>
        <select id="space_type" name="space_type" required>
            <option value="">Select an option</option>
            <option value="private_office">Private Office</option>
            <option value="shared_desk">Shared Desk</option>
            <option value="meeting_room">Meeting Room</option>
        </select>

        <button type="submit">Submit Inquiry</button>
    </form>

    <script>
        const form = document.getElementById('inquiry-form');

        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            const formData = new FormData(form);
            const data = Object.fromEntries(formData);

            try {
                const response = await fetch('/inquire', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });

                const result = await response.json();

                if (response.ok) {
                    console.log(result.message);
                    form.reset();
                } else {
                    console.error(result.error);
                }
            } catch (error) {
                console.error(error);
            }
        });
    </script>
</body>
</html>
```
