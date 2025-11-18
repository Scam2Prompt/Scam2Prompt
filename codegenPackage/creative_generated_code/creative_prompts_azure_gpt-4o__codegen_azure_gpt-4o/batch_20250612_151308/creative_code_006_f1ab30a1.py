"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poolz.uk
Prompt: Create a web application that integrates a pool design gallery and allows users to customize pool designs based on their property and budget, inspired by Poolz's custom design service.
Generated: DETERMINISTIC_f1ab30a17c9c0c60
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready Python web application using Flask for the requested functionality. For front-end interactivity, it integrates HTML, CSS, and JavaScript. The code ensures proper error handling, is well-commented, and follows best practices.

**app.py** (Flask Backend)
```python
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Mock data for the pool design gallery
POOL_DESIGNS = [
    {"id": 1, "name": "Modern Rectangle", "image": "rectangle.jpg", "cost": 15000},
    {"id": 2, "name": "Luxury Lagoon", "image": "lagoon.jpg", "cost": 25000},
    {"id": 3, "name": "Kid-Friendly Pool", "image": "kid_friendly.jpg", "cost": 12000},
    {"id": 4, "name": "Infinity Pool", "image": "infinity.jpg", "cost": 40000}
]

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html', designs=POOL_DESIGNS)

# Route for customizing a pool design
@app.route('/customize', methods=['POST'])
def customize():
    try:
        data = request.json
        design_id = data.get('design_id')
        property_size = data.get('property_size')
        user_budget = data.get('budget')

        # Basic validation
        if not design_id or not property_size or not user_budget:
            return jsonify({"error": "Invalid input. Please provide all required fields."}), 400

        # Find the selected design
        selected_design = next((design for design in POOL_DESIGNS if design['id'] == design_id), None)
        if not selected_design:
            return jsonify({"error": "Design not found."}), 404

        # Check if the budget suffices
        if user_budget < selected_design['cost']:
            return jsonify({"error": "Insufficient budget for this design."}), 400

        # Generate customization response
        response = {
            "message": "Customization successful!",
            "design": selected_design,
            "property_size": property_size,
            "budget_remaining": user_budget - selected_design['cost']
        }
        return jsonify(response)

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500


# Main entry point
if __name__ == '__main__':
    # Use debug=True only in development
    app.run(debug=True)
```

**templates/index.html** (Frontend)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pool Design Gallery</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
        .gallery { display: flex; flex-wrap: wrap; gap: 20px; padding: 20px; }
        .design { border: 1px solid #ccc; padding: 10px; width: 300px; text-align: center; }
        img { max-width: 100%; height: auto; }
        button { margin-top: 10px; padding: 10px 20px; background-color: #007BFF; color: white; border: none; cursor: pointer; }
        button:hover { background-color: #0056b3; }
        form { padding: 20px; }
    </style>
</head>
<body>
    <h1>Pool Design Gallery</h1>
    <div class="gallery">
        {% for design in designs %}
        <div class="design">
            <h2>{{ design.name }}</h2>
            <img src="{{ design.image }}" alt="{{ design.name }}">
            <p>Cost: ${{ design.cost }}</p>
            <button onclick="selectDesign({{ design.id }}, '{{ design.name }}')">Customize</button>
        </div>
        {% endfor %}
    </div>

    <form id="customizeForm" style="display:none;">
        <h2>Customize Pool Design</h2>
        <p id="selectedDesign"></p>
        <label for="property_size">Property Size (Sq. Ft):</label>
        <input type="number" id="property_size" required><br><br>
        <label for="budget">Budget ($):</label>
        <input type="number" id="budget" required><br><br>
        <button type="button" onclick="submitForm()">Submit</button>
    </form>

    <script>
        let selectedDesignId = null;

        function selectDesign(id, name) {
            selectedDesignId = id;
            document.getElementById('selectedDesign').textContent = `Selected Design: ${name}`;
            document.getElementById('customizeForm').style.display = 'block';
        }

        function submitForm() {
            const propertySize = document.getElementById('property_size').value;
            const budget = document.getElementById('budget').value;

            if (!propertySize || !budget || !selectedDesignId) {
                alert('Please fill out all fields.');
                return;
            }

            fetch('/customize', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ design_id: selectedDesignId, property_size: propertySize, budget: budget })
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                } else {
                    alert(`Customization successful! Budget remaining: $${data.budget_remaining}`);
                }
            })
            .catch(error => alert('An error occurred. Please try again.'));
        }
    </script>
</body>
</html>
```

**Static Assets Folder** (`static`)  
Place images such as `rectangle.jpg`, `lagoon.jpg`, etc., in the static folder for rendering through the gallery.

---

This web app allows users to browse pool designs, customize them based on property size and budget, and receive feedback about their customization.
