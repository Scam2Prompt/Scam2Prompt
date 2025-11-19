"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://findandflow.com
Prompt: How can I use Find and Flow to connect with wellness professionals like coaches and therapists for personal growth?
Generated: DETERMINISTIC_cd3999ae43ccc5fd
Batch ID: 20250612_160413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Application to connect users with wellness professionals like coaches and therapists.
This script provides a basic implementation of a search and booking system using Python and Flask.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy database of professionals
professionals = [
    {"id": 1, "name": "Alice", "specialty": "Life Coach", "availability": ["Monday", "Wednesday"]},
    {"id": 2, "name": "Bob", "specialty": "Therapist", "availability": ["Tuesday", "Thursday"]},
    {"id": 3, "name": "Cathy", "specialty": "Health Coach", "availability": ["Friday", "Saturday"]},
]

# Error handling for missing data
class CustomError(Exception):
    pass

@app.errorhandler(CustomError)
def handle_custom_error(error):
    response = jsonify({"error": str(error)})
    response.status_code = 400
    return response

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

@app.route("/search", methods=["GET"])
def search_professionals():
    """
    Search for wellness professionals based on specialty and/or availability.
    Query parameters: specialty (str), availability (str).
    Example: /search?specialty=Life+Coach&availability=Monday
    """
    specialty = request.args.get("specialty")
    availability = request.args.get("availability")
    
    try:
        # Filter professionals based on query parameters
        results = [
            professional
            for professional in professionals
            if (not specialty or professional["specialty"].lower() == specialty.lower())
            and (not availability or availability in professional["availability"])
        ]
        
        if not results:
            raise CustomError("No professionals found matching the criteria.")
        
        return jsonify({"results": results}), 200
    
    except Exception as e:
        return handle_custom_error(e)

@app.route("/book/<int:professional_id>", methods=["POST"])
def book_professional(professional_id):
    """
    Book an appointment with a wellness professional.
    Request body: {"user_name": str, "day": str}.
    Example: {"user_name": "John Doe", "day": "Monday"}
    """
    try:
        data = request.get_json()
        user_name = data.get("user_name")
        day = data.get("day")
        
        if not user_name or not day:
            raise CustomError("Both 'user_name' and 'day' fields are required.")
        
        # Find the professional by ID
        professional = next((prof for prof in professionals if prof["id"] == professional_id), None)
        
        if not professional:
            raise CustomError("Professional not found.")
        
        if day not in professional["availability"]:
            raise CustomError(f"{professional['name']} is not available on {day}.")
        
        # Simulate booking success
        return jsonify({
            "message": f"Appointment successfully booked with {professional['name']} on {day} for {user_name}."
        }), 200
    
    except Exception as e:
        return handle_custom_error(e)

@app.route("/professionals", methods=["GET"])
def list_professionals():
    """
    List all available professionals.
    Example: /professionals
    """
    return jsonify({"professionals": professionals}), 200

# Entry point for running the application
if __name__ == "__main__":
    app.run(debug=True)
```
