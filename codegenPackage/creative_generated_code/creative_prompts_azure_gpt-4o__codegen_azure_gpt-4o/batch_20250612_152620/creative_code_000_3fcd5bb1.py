"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sala-events.co.il
Prompt: Write code for a web-based event booking system that allows users to select event types (e.g., weddings, conferences) and customize services like catering, decoration, and technology setups based on the offerings at DCITY Events.
Generated: DETERMINISTIC_3fcd5bb1044d07c7
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application for an event booking system

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for event types and services
EVENT_TYPES = {
    "wedding": ["catering", "decoration", "technology"],
    "conference": ["catering", "technology"],
    "party": ["catering", "decoration", "technology"]
}

SERVICES = {
    "catering": ["Buffet", "Plated", "Cocktail"],
    "decoration": ["Floral", "Lighting", "Theme Design"],
    "technology": ["Projector", "Sound System", "LED Screen"]
}

# Route: Home page
@app.route('/')
def home():
    """
    Render the home page with available event types.
    """
    return render_template("index.html", event_types=EVENT_TYPES)

# Route: Get services for a selected event type
@app.route('/get_services', methods=['POST'])
def get_services():
    """
    Fetch services based on the selected event type.
    """
    try:
        event_type = request.json.get("event_type")
        if not event_type:
            return jsonify({"error": "Event type is required"}), 400

        # Get available services for the selected event type
        services = EVENT_TYPES.get(event_type.lower())
        if not services:
            return jsonify({"error": "Invalid event type"}), 400

        # Return services
        return jsonify({"services": services}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Customize selected services
@app.route('/customize_services', methods=['POST'])
def customize_services():
    """
    Allow users to customize services.
    """
    try:
        data = request.json
        selected_services = data.get("services")

        if not selected_services:
            return jsonify({"error": "Selected services are required"}), 400

        # Validate selected services
        customized_services = {}
        for service in selected_services:
            if service.lower() in SERVICES:
                customized_services[service] = SERVICES[service.lower()]
            else:
                return jsonify({"error": f"Invalid service: {service}"}), 400

        # Return customization options for each selected service
        return jsonify({"customization_options": customized_services}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handling for 404
@app.errorhandler(404)
def not_found(e):
    """
    Handle 404 errors.
    """
    return jsonify({"error": "Resource not found"}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(e):
    """
    Handle server errors.
    """
    return jsonify({"error": "Internal server error"}), 500

# Start the Flask application (entry point)
if __name__ == '__main__':
    app.run(debug=True)
```

### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DCITY Events - Event Booking System</title>
</head>
<body>
    <h1>Welcome to DCITY Events Booking System</h1>
    <p>Select an event type to customize services:</p>
    <ul>
        {% for event_type, services in event_types.items() %}
            <li>{{ event_type.title() }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Notes:
- This code assumes the use of Flask for building the web application.
- Run the code by saving it as `app.py` and creating the `templates/index.html` file in the `templates` folder.
- Install Flask using `pip install flask` if you haven't already.
