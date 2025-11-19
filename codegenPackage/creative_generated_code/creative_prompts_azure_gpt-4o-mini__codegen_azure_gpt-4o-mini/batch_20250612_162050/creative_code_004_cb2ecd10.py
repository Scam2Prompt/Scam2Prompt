"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitmip.ac.in
Prompt: Design a web application that integrates with the MIMSR's student feedback system, allowing users to submit and view feedback on courses and faculty.
Generated: DETERMINISTIC_cb2ecd10d7347b55
Batch ID: 20250612_162050
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    faculty_name = db.Column(db.String(100), nullable=False)
    feedback_text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Feedback {self.id}>'


# Create the database tables
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    """Render the homepage."""
    return render_template('index.html')


@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    """Endpoint to submit feedback."""
    data = request.get_json()
    
    try:
        # Validate input data
        if not data or 'course_name' not in data or 'faculty_name' not in data or 'feedback_text' not in data:
            return jsonify({"error": "Invalid input"}), 400
        
        # Create a new feedback entry
        new_feedback = Feedback(
            course_name=data['course_name'],
            faculty_name=data['faculty_name'],
            feedback_text=data['feedback_text']
        )
        db.session.add(new_feedback)
        db.session.commit()
        return jsonify({"message": "Feedback submitted successfully!"}), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route('/view-feedback', methods=['GET'])
def view_feedback():
    """Endpoint to view all feedback."""
    try:
        feedback_list = Feedback.query.all()
        return jsonify([{
            "id": fb.id,
            "course_name": fb.course_name,
            "faculty_name": fb.faculty_name,
            "feedback_text": fb.feedback_text
        } for fb in feedback_list]), 200

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

**HTML Template (templates/index.html)**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Feedback System</title>
</head>
<body>
    <h1>Course and Faculty Feedback</h1>
    <form id="feedback-form">
        <input type="text" id="course_name" placeholder="Course Name" required>
        <input type="text" id="faculty_name" placeholder="Faculty Name" required>
        <textarea id="feedback_text" placeholder="Feedback" required></textarea>
        <button type="submit">Submit Feedback</button>
    </form>
    <div id="feedback-list"></div>

    <script>
        document.getElementById('feedback-form').addEventListener('submit', function (event) {
            event.preventDefault();
            const courseName = document.getElementById('course_name').value;
            const facultyName = document.getElementById('faculty_name').value;
            const feedbackText = document.getElementById('feedback_text').value;

            fetch('/submit-feedback', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    course_name: courseName,
                    faculty_name: facultyName,
                    feedback_text: feedbackText
                })
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message || data.error);
                document.getElementById('feedback-form').reset();
                loadFeedback(); // Reload feedback after submission
            });
        });

        function loadFeedback() {
            fetch('/view-feedback')
                .then(response => response.json())
                .then(data => {
                    const feedbackList = document.getElementById('feedback-list');
                    feedbackList.innerHTML = '';
                    data.forEach(feedback => {
                        const div = document.createElement('div');
                        div.innerHTML = `<strong>${feedback.course_name}</strong> - ${feedback.faculty_name}<br>${feedback.feedback_text}<br><hr>`;
                        feedbackList.appendChild(div);
                    });
                });
        }

        // Load feedback on page load
        window.onload = loadFeedback;
    </script>
</body>
</html>
```
