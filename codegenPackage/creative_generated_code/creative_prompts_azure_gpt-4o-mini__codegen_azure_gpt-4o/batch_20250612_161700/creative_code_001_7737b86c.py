"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appdevistorias.com.br
Prompt: Write a code snippet to create a web panel for scheduling and editing property inspections, inspired by the functionalities of the BeSoft app.
Generated: DETERMINISTIC_7737b86c2f2068a6
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready implementation in Python using the Flask framework for creating a web panel for scheduling and editing property inspections. Ensure you have Flask installed before running the code.

```python
from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

# In-memory database (to be replaced with a proper database in production)
inspections = []

@app.route("/")
def index():
    """
    Render the web panel for property inspections.
    """
    return render_template("index.html", inspections=inspections)

@app.route("/schedule", methods=["POST"])
def schedule_inspection():
    """
    Endpoint to schedule a new property inspection.
    """
    try:
        data = request.json
        property_name = data.get("property_name")
        inspector_name = data.get("inspector_name")
        inspection_date = data.get("inspection_date")  # Format: YYYY-MM-DD HH:MM

        # Validate inputs
        if not property_name or not inspector_name or not inspection_date:
            return jsonify({"error": "Missing required fields"}), 400

        # Parse and validate the inspection date
        try:
            inspection_date = datetime.strptime(inspection_date, "%Y-%m-%d %H:%M")
        except ValueError:
            return jsonify({"error": "Invalid date format"}), 400

        # Create inspection object
        inspection = {
            "id": len(inspections) + 1,
            "property_name": property_name,
            "inspector_name": inspector_name,
            "inspection_date": inspection_date.strftime("%Y-%m-%d %H:%M"),
        }

        # Add inspection to the database
        inspections.append(inspection)

        return jsonify({"message": "Inspection scheduled successfully", "inspection": inspection}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/edit/<int:inspection_id>", methods=["PUT"])
def edit_inspection(inspection_id):
    """
    Endpoint to edit an existing property inspection.
    """
    try:
        data = request.json
        inspection_date = data.get("inspection_date")  # Format: YYYY-MM-DD HH:MM

        # Find the inspection
        inspection = next((i for i in inspections if i["id"] == inspection_id), None)
        if not inspection:
            return jsonify({"error": "Inspection not found"}), 404

        # Update the inspection date if provided
        if inspection_date:
            try:
                inspection_date = datetime.strptime(inspection_date, "%Y-%m-%d %H:%M")
                inspection["inspection_date"] = inspection_date.strftime("%Y-%m-%d %H:%M")
            except ValueError:
                return jsonify({"error": "Invalid date format"}), 400

        return jsonify({"message": "Inspection updated successfully", "inspection": inspection}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/delete/<int:inspection_id>", methods=["DELETE"])
def delete_inspection(inspection_id):
    """
    Endpoint to delete a property inspection.
    """
    try:
        global inspections
        inspection = next((i for i in inspections if i["id"] == inspection_id), None)
        if not inspection:
            return jsonify({"error": "Inspection not found"}), 404

        inspections = [i for i in inspections if i["id"] != inspection_id]
        return jsonify({"message": "Inspection deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
```

### Accompanying HTML Template (`templates/index.html`)
You need to create a folder named `templates` in the same directory as the Python file and add an HTML file named `index.html` with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Property Inspections</title>
</head>
<body>
    <h1>Property Inspections</h1>
    <ul>
        {% for inspection in inspections %}
        <li>
            <strong>Property:</strong> {{ inspection.property_name }}<br>
            <strong>Inspector:</strong> {{ inspection.inspector_name }}<br>
            <strong>Date:</strong> {{ inspection.inspection_date }}
        </li>
        {% else %}
        <li>No inspections scheduled.</li>
        {% endfor %}
    </ul>
</body>
</html>
```

This implementation provides a basic web panel for scheduling, editing, and deleting property inspections. It uses Flask's templating engine to render the list of inspections.
