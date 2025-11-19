"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmaculada.edu.ec
Prompt: Generate a code snippet for a web application that displays information about the educational programs offered at Unidad Educativa Bilingüe de la Inmaculada in Quito, including details on English certification and extracurricular activities.
Generated: DETERMINISTIC_8f6c9d28cae3a7cb
Batch ID: 20250612_163728
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web development
from flask import Flask, render_template, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample data for educational programs
programs = [
    {
        "name": "English Language Program",
        "description": "Comprehensive English course aimed at achieving fluency.",
        "certification": "Cambridge English Certification",
        "extracurricular": [
            "Debate Club",
            "English Drama Society",
            "Book Club"
        ]
    },
    {
        "name": "Bilingual Education Program",
        "description": "Offers education in both English and Spanish.",
        "certification": "Bilingual Education Certificate",
        "extracurricular": [
            "Cultural Exchange Program",
            "Sports Activities",
            "Art and Craft Club"
        ]
    }
]

@app.route('/')
def index():
    """Render the main page with educational programs."""
    return render_template('index.html', programs=programs)

@app.route('/api/programs', methods=['GET'])
def get_programs():
    """API endpoint to get a list of educational programs."""
    try:
        return jsonify(programs), 200
    except Exception as e:
        # Log the error for debugging (using print for simplicity)
        print(f"Error retrieving programs: {e}")
        return jsonify({"error": "Unable to retrieve programs"}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Educational Programs - Unidad Educativa Bilingüe de la Inmaculada</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Educational Programs</h1>
        <div class="row">
            {% for program in programs %}
            <div class="col-md-4">
                <div class="card mb-4">
                    <div class="card-body">
                        <h5 class="card-title">{{ program.name }}</h5>
                        <p class="card-text">{{ program.description }}</p>
                        <p><strong>Certification:</strong> {{ program.certification }}</p>
                        <p><strong>Extracurricular Activities:</strong></p>
                        <ul>
                            {% for activity in program.extracurricular %}
                            <li>{{ activity }}</li>
                            {% endfor %}
                        </ul>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```
