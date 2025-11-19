"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agnedoveikaite.lt
Prompt: Generate a code snippet for a web application that integrates emotional intelligence training modules, inspired by Agne Doveikaite's approach to personal development.
Generated: DETERMINISTIC_da9a6c9010f38d64
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application to integrate emotional intelligence training modules
# Inspired by Agne Doveikaite's approach to personal development

from flask import Flask, render_template, request, jsonify
import logging

app = Flask(__name__)

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample emotional intelligence training modules (in a real-world app, these would be dynamic and database-driven)
TRAINING_MODULES = [
    {"id": 1, "title": "Self-Awareness Basics", "description": "Learn to identify your emotions and triggers."},
    {"id": 2, "title": "Empathy Building", "description": "Practice understanding the emotions of others."},
    {"id": 3, "title": "Resilience Techniques", "description": "Strengthen your ability to handle adversity calmly."},
]

@app.route('/')
def home():
    """
    Home route that displays available emotional intelligence training modules.
    """
    try:
        return render_template('index.html', modules=TRAINING_MODULES)
    except Exception as e:
        logging.error(f"Error rendering home page: {e}")
        return "An error occurred. Please try again later.", 500


@app.route('/module/<int:module_id>', methods=['GET'])
def view_module(module_id):
    """
    Route to display details of a specific training module.
    :param module_id: ID of the training module
    """
    try:
        module = next((mod for mod in TRAINING_MODULES if mod["id"] == module_id), None)
        if module:
            return render_template('module.html', module=module)
        else:
            logging.warning(f"Module with ID {module_id} not found.")
            return "Module not found.", 404
    except Exception as e:
        logging.error(f"Error loading module {module_id}: {e}")
        return "An error occurred. Please try again later.", 500


@app.route('/api/modules', methods=['GET'])
def api_modules():
    """
    API endpoint to retrieve all emotional intelligence training modules.
    """
    try:
        return jsonify(TRAINING_MODULES)
    except Exception as e:
        logging.error(f"Error fetching modules API: {e}")
        return jsonify({"error": "An error occurred. Please try again later."}), 500


@app.route('/api/module/<int:module_id>', methods=['GET'])
def api_view_module(module_id):
    """
    API endpoint to retrieve details of a specific training module.
    :param module_id: ID of the training module
    """
    try:
        module = next((mod for mod in TRAINING_MODULES if mod["id"] == module_id), None)
        if module:
            return jsonify(module)
        else:
            logging.warning(f"Module with ID {module_id} not found.")
            return jsonify({"error": "Module not found."}), 404
    except Exception as e:
        logging.error(f"Error fetching module API {module_id}: {e}")
        return jsonify({"error": "An error occurred. Please try again later."}), 500


if __name__ == '__main__':
    # Run the web application
    app.run(debug=True)
```

### Note:
- Ensure the `templates` directory contains `index.html` and `module.html` to render pages properly.
- Replace `TRAINING_MODULES` with database-driven content for a scalable production application.
- Disable `debug=True` in production environments and use a proper WSGI server like Gunicorn or uWSGI for deployment.
