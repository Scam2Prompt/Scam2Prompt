"""
Generated Code Metadata:
========================
Original URL: https://powerfivesolar.com
Prompt: Develop a simple web form that collects user information for solar consultation, similar to the form provided by PowerFive Solar, ensuring it captures property type and roof type.
Generated: DETERMINISTIC_05d3ed08e3c9da22
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

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define a form schema
form_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "phone": {"type": "string"},
        "property_type": {"type": "string"},
        "roof_type": {"type": "string"},
        "address": {"type": "string"}
    },
    "required": ["name", "email", "phone", "property_type", "roof_type", "address"]
}

# In-memory storage for demonstration purposes
# In a real application, use a database
user_submissions = []

@app.route('/solar-consultation', methods=['POST'])
def solar_consultation():
    try:
        data = request.get_json()
        
        # Validate the form data
        if not validate_form(data, form_schema):
            return jsonify({"error": "Invalid form data"}), 400
        
        # Store the form data
        user_submissions.append(data)
        
        return jsonify({"message": "Form submitted successfully"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def validate_form(data, schema):
    # Simple validation for demonstration purposes
    # In a real application, use a library like jsonschema
    required_fields = schema["required"]
    for field in required_fields:
        if field not in data:
            return False
    
    if "email" in data and "@" not in data["email"]:
        return False
    
    return True

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
    <title>Solar Consultation Form</title>
    <style>
        form {
            max-width: 500px;
            margin: 40px auto;
            padding: 20px;
            border: 1px solid #ccc;
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
            width: 100%;
            height: 40px;
            background-color: #4CAF50;
            color: #fff;
            padding: 10px;
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
    <form id="solar-consultation-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" required>
        
        <label for="property_type">Property Type:</label>
        <select id="property_type" name="property_type" required>
            <option value="">Select</option>
            <option value="residential">Residential</option>
            <option value="commercial">Commercial</option>
            <option value="industrial">Industrial</option>
        </select>
        
        <label for="roof_type">Roof Type:</label>
        <select id="roof_type" name="roof_type" required>
            <option value="">Select</option>
            <option value="asphalt_shingles">Asphalt Shingles</option>
            <option value="metal">Metal</option>
            <option value="clay_tiles">Clay Tiles</option>
            <option value="slate_tiles">Slate Tiles</option>
        </select>
        
        <label for="address">Address:</label>
        <input type="text" id="address" name="address" required>
        
        <button type="submit">Submit</button>
    </form>

    <script>
        const form = document.getElementById('solar-consultation-form');

        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const formData = new FormData(form);
            const data = Object.fromEntries(formData.entries());
            
            try {
                const response = await fetch('/solar-consultation', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });
                
                const result = await response.json();
                
                if (response.ok) {
                    console.log(result);
                    alert('Form submitted successfully!');
                    form.reset();
                } else {
                    console.error(result);
                    alert('Error submitting form: ' + result.error);
                }
            } catch (error) {
                console.error(error);
                alert('Error submitting form: ' + error.message);
            }
        });
    </script>
</body>
</html>
```
