"""
Generated Code Metadata:
========================
Original URL: https://pozymedia.com
Prompt: Write a code snippet for a website that integrates an event management system, focusing on features like vendor contract negotiation and program management, inspired by Pozy Media's services.
Generated: DETERMINISTIC_24af7e04db03e3fb
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database simulation
vendors = []
programs = []

# Error handling utility
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Vendor contract negotiation endpoint
@app.route('/vendors', methods=['POST'])
def add_vendor():
    """
    Add a new vendor to the system.
    Expected JSON payload:
    {
        "name": "Vendor Name",
        "contact": "Contact Information",
        "contract_terms": "Contract Terms"
    }
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ("name", "contact", "contract_terms")):
            return error_response("Invalid input. 'name', 'contact', and 'contract_terms' are required.")
        
        vendor = {
            "id": len(vendors) + 1,
            "name": data["name"],
            "contact": data["contact"],
            "contract_terms": data["contract_terms"],
            "created_at": datetime.utcnow()
        }
        vendors.append(vendor)
        return jsonify({"message": "Vendor added successfully", "vendor": vendor}), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Program management endpoint
@app.route('/programs', methods=['POST'])
def add_program():
    """
    Add a new program to the system.
    Expected JSON payload:
    {
        "title": "Program Title",
        "description": "Program Description",
        "date": "YYYY-MM-DD",
        "vendor_id": 1
    }
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ("title", "description", "date", "vendor_id")):
            return error_response("Invalid input. 'title', 'description', 'date', and 'vendor_id' are required.")
        
        # Validate vendor existence
        vendor = next((v for v in vendors if v["id"] == data["vendor_id"]), None)
        if not vendor:
            return error_response("Vendor not found.", 404)
        
        # Validate date format
        try:
            program_date = datetime.strptime(data["date"], "%Y-%m-%d")
        except ValueError:
            return error_response("Invalid date format. Use 'YYYY-MM-DD'.")
        
        program = {
            "id": len(programs) + 1,
            "title": data["title"],
            "description": data["description"],
            "date": program_date,
            "vendor_id": data["vendor_id"],
            "created_at": datetime.utcnow()
        }
        programs.append(program)
        return jsonify({"message": "Program added successfully", "program": program}), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Get all vendors
@app.route('/vendors', methods=['GET'])
def get_vendors():
    """
    Retrieve all vendors.
    """
    return jsonify({"vendors": vendors}), 200

# Get all programs
@app.route('/programs', methods=['GET'])
def get_programs():
    """
    Retrieve all programs.
    """
    return jsonify({"programs": programs}), 200

# Main entry point
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
