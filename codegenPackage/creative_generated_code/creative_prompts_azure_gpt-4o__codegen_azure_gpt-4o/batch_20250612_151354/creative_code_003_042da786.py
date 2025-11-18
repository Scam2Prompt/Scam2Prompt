"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fondation.app
Prompt: Develop a REST API for managing beneficiaries, donors, and volunteers in a CRM system tailored for non-profits, incorporating multilingual support as described in CRM.f.
Generated: DETERMINISTIC_042da78685b7cfac
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_babel import Babel, _

app = Flask(__name__)

# Configuration for Babel (Multilingual support)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'es', 'fr']  # English, Spanish, French, etc.
babel = Babel(app)

# Sample database (in-memory, replace with actual DB in production)
database = {
    "beneficiaries": [],
    "donors": [],
    "volunteers": []
}

# Resource model validation
def validate_resource(data, required_fields):
    for field in required_fields:
        if field not in data:
            return False, _("Missing required field: {}").format(field)
    return True, None

# Error handler for 404
@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({"error": _("Resource not found")}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": _("An unexpected error occurred")}), 500

# Multilingual support selector
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

# Beneficiaries CRUD
@app.route('/beneficiaries', methods=['GET', 'POST'])
def manage_beneficiaries():
    if request.method == 'GET':
        return jsonify(database["beneficiaries"])

    if request.method == 'POST':
        data = request.json
        required_fields = ["name", "age", "needs"]
        valid, error_message = validate_resource(data, required_fields)
        if not valid:
            return jsonify({"error": error_message}), 400

        beneficiary = {
            "id": len(database["beneficiaries"]) + 1,
            "name": data["name"],
            "age": data["age"],
            "needs": data["needs"]
        }
        database["beneficiaries"].append(beneficiary)
        return jsonify(beneficiary), 201

# Donors CRUD
@app.route('/donors', methods=['GET', 'POST'])
def manage_donors():
    if request.method == 'GET':
        return jsonify(database["donors"])

    if request.method == 'POST':
        data = request.json
        required_fields = ["name", "donation_type", "amount"]
        valid, error_message = validate_resource(data, required_fields)
        if not valid:
            return jsonify({"error": error_message}), 400

        donor = {
            "id": len(database["donors"]) + 1,
            "name": data["name"],
            "donation_type": data["donation_type"],
            "amount": data["amount"]
        }
        database["donors"].append(donor)
        return jsonify(donor), 201

# Volunteers CRUD
@app.route('/volunteers', methods=['GET', 'POST'])
def manage_volunteers():
    if request.method == 'GET':
        return jsonify(database["volunteers"])

    if request.method == 'POST':
        data = request.json
        required_fields = ["name", "skills", "availability"]
        valid, error_message = validate_resource(data, required_fields)
        if not valid:
            return jsonify({"error": error_message}), 400

        volunteer = {
            "id": len(database["volunteers"]) + 1,
            "name": data["name"],
            "skills": data["skills"],
            "availability": data["availability"]
        }
        database["volunteers"].append(volunteer)
        return jsonify(volunteer), 201

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": _("Healthy")}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
