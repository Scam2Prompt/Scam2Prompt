"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isiv.edu.ar
Prompt: How can I create a web application that displays the academic offerings, such as Turismo and Negocios Digitales, from ISIV's distance education platform?
Generated: DETERMINISTIC_cc947f6d1f297e50
Batch ID: 20250612_163506
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000/`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://127.0.0.1:5000/api/offerings`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is the code for creating a simple web application using Python's Flask framework that displays academic offerings. This assumes you have Python installed and will use Flask for a basic implementation. 

```python
# Import necessary libraries
from flask import Flask, jsonify, render_template

# Initialize the Flask application
app = Flask(__name__)

# Academic offerings data
# This would ideally come from a database in a production application.
ACADEMIC_OFFERINGS = [
    {"id": 1, "name": "Turismo", "description": "Learn about the tourism industry and its management."},
    {"id": 2, "name": "Negocios Digitales", "description": "Explore digital business models and strategies."}
]

# Route for the home page
@app.route('/')
def home():
    """
    Render the home page.
    """
    return render_template('index.html', offerings=ACADEMIC_OFFERINGS)

# Route to fetch academic offerings as JSON
@app.route('/api/offerings', methods=['GET'])
def get_offerings():
    """
    Return academic offerings as JSON data.
    """
    try:
        return jsonify({"success": True, "data": ACADEMIC_OFFERINGS})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors with a custom page.
    """
    return jsonify({"success": False, "error": "Page not found"}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors with a custom page.
    """
    return jsonify({"success": False, "error": "Internal server error"}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask app
    # Debugging is enabled for development purposes; disable in production.
    app.run(debug=True)
```

### HTML Template (`templates/index.html`):
Create a `templates` folder and add the following HTML file inside it.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ISIV Academic Offerings</title>
</head>
<body>
    <h1>ISIV Academic Offerings</h1>
    <ul>
        {% for offering in offerings %}
            <li>
                <h2>{{ offering.name }}</h2>
                <p>{{ offering.description }}</p>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Instructions:
1. Install Flask:
   ```
   pip install flask
   ```

2. Save the Python code to a file called `app.py`.

3. Create a folder named `templates` in the same directory as `app.py` and save the `index.html` file inside it.

4. Run the app:
   ```
   python app.py
   ```

5. Open a web browser and go to `http://127.0.0.1:5000/` to view the academic offerings.

6. To test the API endpoint, navigate to `http://127.0.0.1:5000/api/offerings`.

This code is production-ready but should be further refined for deployment, such as adding HTTPS, using a WSGI server like Gunicorn, and connecting to a database for dynamic data.
