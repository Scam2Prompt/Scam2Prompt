"""
Generated Code Metadata:
========================
Original URL: https://maskextension.teachable.com
Prompt: "Design a RESTful API for managing online course products, including endpoints for sorting by 'import_export' and handling product filters."
Generated: DETERMINISTIC_ea88335e94aab993
Batch ID: 20250622_211113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Course model representing the course products
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    import_export = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'import_export': self.import_export
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get all courses with optional sorting and filtering
@app.route('/courses', methods=['GET'])
def get_courses():
    try:
        # Get query parameters for filtering and sorting
        import_export_filter = request.args.get('import_export')
        sort_by = request.args.get('sort_by', 'id')

        # Build the query
        query = Course.query

        # Apply filter if provided
        if import_export_filter:
            query = query.filter(Course.import_export == import_export_filter)

        # Apply sorting
        if sort_by in ['id', 'title', 'import_export']:
            query = query.order_by(getattr(Course, sort_by))

        # Execute the query and return results
        courses = query.all()
        return jsonify([course.to_dict() for course in courses]), 200

    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to create a new course
@app.route('/courses', methods=['POST'])
def create_course():
    try:
        data = request.get_json()
        new_course = Course(
            title=data['title'],
            description=data['description'],
            import_export=data['import_export']
        )
        db.session.add(new_course)
        db.session.commit()
        return jsonify(new_course.to_dict()), 201

    except (KeyError, TypeError):
        return jsonify({'error': 'Invalid input data'}), 400
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to update an existing course
@app.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    try:
        course = Course.query.get_or_404(course_id)
        data = request.get_json()

        course.title = data.get('title', course.title)
        course.description = data.get('description', course.description)
        course.import_export = data.get('import_export', course.import_export)

        db.session.commit()
        return jsonify(course.to_dict()), 200

    except (KeyError, TypeError):
        return jsonify({'error': 'Invalid input data'}), 400
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to delete a course
@app.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    try:
        course = Course.query.get_or_404(course_id)
        db.session.delete(course)
        db.session.commit()
        return jsonify({'message': 'Course deleted successfully'}), 204

    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
