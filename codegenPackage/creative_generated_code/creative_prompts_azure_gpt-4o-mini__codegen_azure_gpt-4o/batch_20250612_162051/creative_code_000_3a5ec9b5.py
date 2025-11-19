"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kiddooplayway.com
Prompt: Write a code snippet for a web application that allows parents to enroll their children in a daycare program like Kiddoo Playway, focusing on features such as activity-based curriculum and parental webinars.
Generated: DETERMINISTIC_3a5ec9b501a1361a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database simulation for simplicity
enrollments = []
activities = ["Art & Craft", "Storytelling", "Outdoor Games", "Music & Dance"]
webinars = ["Parenting Tips", "Nutrition & Health", "Child Psychology"]

@app.route('/enroll', methods=['POST'])
def enroll_child():
    """
    Endpoint to enroll a child in the daycare program.
    Expects JSON payload with 'name', 'age', 'parent_name', and 'selected_activities'.
    """
    try:
        # Parse and validate request data
        data = request.json
        if not data or not all(k in data for k in ('name', 'age', 'parent_name', 'selected_activities')):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Validate selected activities
        selected_activities = data['selected_activities']
        if not all(activity in activities for activity in selected_activities):
            return jsonify({'error': 'Invalid activities selected'}), 400
        
        # Add enrollment to database
        enrollment = {
            'child_name': data['name'],
            'child_age': data['age'],
            'parent_name': data['parent_name'],
            'selected_activities': selected_activities
        }
        enrollments.append(enrollment)
        return jsonify({'message': 'Enrollment successful', 'enrollment': enrollment}), 201
    
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500


@app.route('/activities', methods=['GET'])
def get_activities():
    """
    Endpoint to retrieve available activities for the daycare program.
    """
    return jsonify({'activities': activities}), 200


@app.route('/webinars', methods=['GET'])
def get_webinars():
    """
    Endpoint to retrieve upcoming parental webinars.
    """
    return jsonify({'webinars': webinars}), 200


@app.route('/enrollments', methods=['GET'])
def get_enrollments():
    """
    Endpoint to retrieve all current enrollments.
    """
    return jsonify({'enrollments': enrollments}), 200


# Error handler for 404 (Not Found)
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Endpoint not found'}), 404


# Error handler for 405 (Method Not Allowed)
@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({'error': 'Method not allowed'}), 405


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
