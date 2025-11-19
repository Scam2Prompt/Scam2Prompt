"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milc-global.pages.dev
Prompt: Create a sample code snippet that demonstrates how to provide early audience feedback for video content within the MILC Community platform.
Generated: DETERMINISTIC_4a581774d482aaeb
Batch ID: 20250612_163419
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest, NotFound

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for sample purposes; change as needed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///milc_feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for storing video feedback
class VideoFeedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.String(50), nullable=False)
    feedback = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Feedback {self.id} for Video {self.video_id}>'

# Create database tables
with app.app_context():
    db.create_all()

# Route to submit feedback
@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """Submit feedback for a video."""
    try:
        data = request.json
        
        # Validate incoming data
        if not data or 'video_id' not in data or 'user_id' not in data or 'feedback' not in data:
            raise BadRequest("Missing required fields: video_id, user_id, feedback.")

        # Create and save a new feedback entry
        new_feedback = VideoFeedback(
            video_id=data['video_id'],
            user_id=data['user_id'],
            feedback=data['feedback']
        )
        db.session.add(new_feedback)
        db.session.commit()

        return jsonify({'message': 'Feedback submitted successfully!'}), 201

    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred while submitting feedback.'}), 500

# Route to get feedback for a specific video
@app.route('/feedback/<string:video_id>', methods=['GET'])
def get_feedback(video_id):
    """Retrieve all feedback for a specific video."""
    try:
        feedback_list = VideoFeedback.query.filter_by(video_id=video_id).all()
        if not feedback_list:
            raise NotFound("No feedback found for this video.")

        feedback_data = [{'user_id': feedback.user_id, 'feedback': feedback.feedback} for feedback in feedback_list]
        return jsonify(feedback_data), 200

    except NotFound as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving feedback.'}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
