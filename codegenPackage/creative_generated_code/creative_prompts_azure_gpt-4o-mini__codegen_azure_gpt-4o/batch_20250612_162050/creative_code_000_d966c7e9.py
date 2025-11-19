"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tdkco.ir
Prompt: How can I implement a verification system for automotive parts like the authenticity system used by یاتاقان گلدن?
Generated: DETERMINISTIC_d966c7e9f0c7daa8
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the clean, well-documented, production-ready code for an automotive parts authenticity verification system. The example assumes a web-based API system using Python and Flask.

```python
from flask import Flask, request, jsonify
import hashlib
from datetime import datetime

app = Flask(__name__)

# Database mockup for storing part information and verification codes
# In production, use a proper database like PostgreSQL or MongoDB.
parts_database = {
    "ABC123": {"name": "Engine Bearing", "manufacturer": "Golden Bearings Co.", "verification_code": None},
    "XYZ789": {"name": "Transmission Gear", "manufacturer": "Golden Bearings Co.", "verification_code": None}
}

# Generate a unique verification code for a specific part
def generate_verification_code(part_id):
    try:
        # Create a unique hash based on part ID and current timestamp
        timestamp = datetime.utcnow().isoformat()
        unique_string = f"{part_id}-{timestamp}"
        hash_code = hashlib.sha256(unique_string.encode()).hexdigest()
        return hash_code
    except Exception as e:
        # Log error in a real-world application
        print(f"Error generating verification code: {e}")
        return None

@app.route('/generate_code/<part_id>', methods=['POST'])
def generate_code(part_id):
    """
    Endpoint to generate and store a verification code for a given part.
    """
    # Validate part ID
    if part_id not in parts_database:
        return jsonify({"error": "Invalid part ID"}), 404

    # Generate verification code
    verification_code = generate_verification_code(part_id)
    if verification_code is None:
        return jsonify({"error": "Failed to generate verification code"}), 500

    # Store the code in the database
    parts_database[part_id]["verification_code"] = verification_code

    return jsonify({"message": "Verification code generated successfully", "verification_code": verification_code}), 200

@app.route('/verify_code', methods=['POST'])
def verify_code():
    """
    Endpoint to verify the authenticity of a part using its verification code.
    """
    data = request.get_json()

    # Input validation
    if not data or "part_id" not in data or "verification_code" not in data:
        return jsonify({"error": "Invalid request data"}), 400

    part_id = data["part_id"]
    verification_code = data["verification_code"]

    # Check if the part exists
    if part_id not in parts_database:
        return jsonify({"error": "Part not found"}), 404

    # Check if the verification code matches
    stored_code = parts_database[part_id].get("verification_code")
    if stored_code is None or stored_code != verification_code:
        return jsonify({"error": "Verification failed"}), 401

    return jsonify({"message": "Part verified successfully", "part_details": parts_database[part_id]}), 200

@app.route('/parts', methods=['GET'])
def list_parts():
    """
    Endpoint to list all parts with their details (excluding verification codes).
    """
    parts_list = {part_id: {key: value for key, value in details.items() if key != "verification_code"} 
                  for part_id, details in parts_database.items()}
    return jsonify(parts_list), 200

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```

### Features of the code:
1. **Endpoints**:
   - `/generate_code/<part_id>`: Generates and stores a verification code for a given part.
   - `/verify_code`: Verifies the authenticity of a part using its verification code.
   - `/parts`: Lists all parts with their details.

2. **Error Handling**:
   - Invalid part ID handling.
   - JSON structure validation.
   - Verification code mismatch handling.

3. **Best Practices**:
   - Modular design with reusable functions.
   - Proper HTTP status codes for responses.
   - Security: Verification codes are generated using SHA-256 for uniqueness.

4. **Comments**:
   - Inline comments explain what each part of the code does.

To run this system, install Flask using `pip install flask`, save the code to a file (`app.py`), and execute it with `python app.py`.
