"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aulacontable.com
Prompt: Develop a REST API endpoint that allows users to fetch details about the "Diplomado de Auditoria Gubernamental" course from AulaContable.
Generated: DETERMINISTIC_8ab7fa6b9f65683f
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aula_contable.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the Course object to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """Fetch details of a specific course by ID.

    Args:
        course_id (int): The ID of the course to fetch.

    Returns:
        JSON response with course details or an error message.
    """
    try:
        course = Course.query.get(course_id)
        if course is None:
            return jsonify({'error': 'Course not found'}), 404

        return jsonify(course.to_dict()), 200

    except SQLAlchemyError as e:
        # Log the error for debugging (in production, consider logging to a file or monitoring service)
        app.logger.error(f"Database error occurred: {str(e)}")
        return jsonify({'error': 'An internal error occurred'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
