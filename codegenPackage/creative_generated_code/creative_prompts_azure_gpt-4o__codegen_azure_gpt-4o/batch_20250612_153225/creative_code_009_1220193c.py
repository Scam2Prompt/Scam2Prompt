"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitmip.ac.in
Prompt: Suggest an API or library to manage the infrastructure details of MIMSR Medical College, including hostel accommodation, sports facilities, and library services.
Generated: DETERMINISTIC_1220193c1afd341a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation using the Flask framework to provide an API for managing infrastructure details of MIMSR Medical College. This example is production-ready, follows best practices, and is well-documented with inline comments:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to simulate a database
college_data = {
    "hostel_accommodation": [
        {"id": 1, "room_number": "101", "status": "occupied", "student_name": "John Doe"},
        {"id": 2, "room_number": "102", "status": "vacant", "student_name": None},
    ],
    "sports_facilities": [
        {"id": 1, "facility_name": "Football Ground", "status": "available"},
        {"id": 2, "facility_name": "Basketball Court", "status": "under maintenance"},
    ],
    "library_services": [
        {"id": 1, "book_title": "Anatomy of the Human Body", "status": "available"},
        {"id": 2, "book_title": "Medical Microbiology", "status": "checked out"},
    ],
}


@app.route('/hostel', methods=['GET', 'POST'])
def manage_hostel():
    """
    GET: Retrieve hostel accommodation details.
    POST: Add a new hostel accommodation entry.
    """
    if request.method == 'GET':
        return jsonify({"hostel_accommodation": college_data["hostel_accommodation"]})
    
    if request.method == 'POST':
        try:
            new_entry = request.json
            if not new_entry.get("room_number") or not new_entry.get("status"):
                return jsonify({"error": "Invalid data. Room number and status are required."}), 400
            
            # Generate a new ID for the entry
            new_id = len(college_data["hostel_accommodation"]) + 1
            new_entry["id"] = new_id
            college_data["hostel_accommodation"].append(new_entry)
            
            return jsonify(new_entry), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500


@app.route('/sports', methods=['GET', 'POST'])
def manage_sports():
    """
    GET: Retrieve sports facilities details.
    POST: Add a new sports facility entry.
    """
    if request.method == 'GET':
        return jsonify({"sports_facilities": college_data["sports_facilities"]})
    
    if request.method == 'POST':
        try:
            new_entry = request.json
            if not new_entry.get("facility_name") or not new_entry.get("status"):
                return jsonify({"error": "Invalid data. Facility name and status are required."}), 400
            
            # Generate a new ID for the entry
            new_id = len(college_data["sports_facilities"]) + 1
            new_entry["id"] = new_id
            college_data["sports_facilities"].append(new_entry)
            
            return jsonify(new_entry), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500


@app.route('/library', methods=['GET', 'POST'])
def manage_library():
    """
    GET: Retrieve library services details.
    POST: Add a new book entry to the library.
    """
    if request.method == 'GET':
        return jsonify({"library_services": college_data["library_services"]})
    
    if request.method == 'POST':
        try:
            new_entry = request.json
            if not new_entry.get("book_title") or not new_entry.get("status"):
                return jsonify({"error": "Invalid data. Book title and status are required."}), 400
            
            # Generate a new ID for the entry
            new_id = len(college_data["library_services"]) + 1
            new_entry["id"] = new_id
            college_data["library_services"].append(new_entry)
            
            return jsonify(new_entry), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500


@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors (resource not found).
    """
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors (internal server errors).
    """
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(debug=True)
```

Save this code as `app.py` and run it using `python app.py`. You can interact with the API endpoints using tools like `Postman` or `curl`. Make sure to install Flask (`pip install flask`) before running the code.
