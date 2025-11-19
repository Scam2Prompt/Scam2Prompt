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
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///daycare.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Daycare Enrollment
class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    child_name = db.Column(db.String(100), nullable=False)
    parent_email = db.Column(db.String(120), nullable=False, unique=True)
    curriculum_type = db.Column(db.String(50), nullable=False)
    webinar_preference = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Enrollment {self.child_name}>'

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for enrolling children in the daycare program
@app.route('/enroll', methods=['POST'])
def enroll():
    data = request.get_json()
    
    try:
        # Validate input data
        if not all(key in data for key in ('child_name', 'parent_email', 'curriculum_type')):
            return jsonify({'error': 'Missing required fields!'}), 400

        # Create new enrollment
        new_enrollment = Enrollment(
            child_name=data['child_name'],
            parent_email=data['parent_email'],
            curriculum_type=data['curriculum_type'],
            webinar_preference=data.get('webinar_preference', False)
        )

        # Add enrollment to the database
        db.session.add(new_enrollment)
        db.session.commit()
        return jsonify({'message': 'Enrollment successful!'}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email already in use!'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run application
if __name__ == '__main__':
    with app.app_context():
        # Create database tables
        db.create_all()
    app.run(debug=True)

# HTML Template (index.html)
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Daycare Enrollment</title>
# </head>
# <body>
#     <h1>Enroll Your Child in Our Daycare Program</h1>
#     <form id="enrollmentForm">
#         <label for="child_name">Child's Name:</label>
#         <input type="text" id="child_name" name="child_name" required>
#         <label for="parent_email">Parent's Email:</label>
#         <input type="email" id="parent_email" name="parent_email" required>
#         <label for="curriculum_type">Curriculum Type:</label>
#         <select id="curriculum_type" name="curriculum_type" required>
#             <option value="activity_based">Activity-Based</option>
#             <option value="academic">Academic</option>
#         </select>
#         <label>
#             <input type="checkbox" name="webinar_preference"> Interested in parental webinars
#         </label>
#         <button type="submit">Enroll</button>
#     </form>
#     <script>
#         document.getElementById('enrollmentForm').addEventListener('submit', function (event) {
#             event.preventDefault();
#             const formData = new FormData(event.target);
#             const data = Object.fromEntries(formData.entries());

#             fetch('/enroll', {
#                 method: 'POST',
#                 headers: {
#                     'Content-Type': 'application/json',
#                 },
#                 body: JSON.stringify(data),
#             })
#             .then(response => response.json())
#             .then(data => {
#                 alert(data.message || data.error);
#             })
#             .catch((error) => {
#                 console.error('Error:', error);
#             });
#         });
#     </script>
# </body>
# </html>
```
