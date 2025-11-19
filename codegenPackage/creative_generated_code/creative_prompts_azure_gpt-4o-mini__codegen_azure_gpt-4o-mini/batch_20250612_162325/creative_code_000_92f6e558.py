"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Generate a code snippet for a web application that allows users to create their own cosmetic brand using the full-service project model described by Fabricare Cosméticos.
Generated: DETERMINISTIC_92f6e558e446265f
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cosmetic_brands.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing cosmetic brands
class CosmeticBrand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    owner_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<CosmeticBrand {self.name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new cosmetic brand
@app.route('/create_brand', methods=['POST'])
def create_brand():
    try:
        # Extract data from the request
        data = request.get_json()
        brand_name = data.get('name')
        owner_name = data.get('owner_name')
        description = data.get('description', '')

        # Validate input data
        if not brand_name or not owner_name:
            raise BadRequest("Brand name and owner name are required.")

        # Create and add a new cosmetic brand to the database
        new_brand = CosmeticBrand(name=brand_name, owner_name=owner_name, description=description)
        db.session.add(new_brand)
        db.session.commit()

        return jsonify({"message": "Brand created successfully!", "brand": new_brand.name}), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while creating the brand."}), 500

# Route to get all cosmetic brands
@app.route('/brands', methods=['GET'])
def get_brands():
    try:
        brands = CosmeticBrand.query.all()
        return jsonify([{"id": brand.id, "name": brand.name, "owner": brand.owner_name, "description": brand.description} for brand in brands]), 200
    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving brands."}), 500

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Run the application
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
    <title>Create Cosmetic Brand</title>
</head>
<body>
    <h1>Create Your Own Cosmetic Brand</h1>
    <form id="brandForm">
        <label for="name">Brand Name:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="owner_name">Owner Name:</label>
        <input type="text" id="owner_name" name="owner_name" required><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br>
        <button type="submit">Create Brand</button>
    </form>
    <div id="message"></div>

    <script>
        // Handle form submission
        document.getElementById('brandForm').addEventListener('submit', async function(event) {
            event.preventDefault();
            const formData = new FormData(this);
            const data = Object.fromEntries(formData.entries());

            try {
                const response = await fetch('/create_brand', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });

                const result = await response.json();
                document.getElementById('message').innerText = result.message || result.error;
                if (response.status === 201) {
                    this.reset();  // Reset the form
                }
            } catch (error) {
                document.getElementById('message').innerText = "An error occurred.";
            }
        });
    </script>
</body>
</html>
```
