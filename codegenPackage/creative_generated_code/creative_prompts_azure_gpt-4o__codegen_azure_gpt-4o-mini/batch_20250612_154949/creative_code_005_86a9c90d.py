"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lethmixedslowpitch.com
Prompt: Develop a web application feature that allows teams to report their own scores using a shortcode, as described in Slo-Pitch Central's platform functionality.
Generated: DETERMINISTIC_86a9c90daf7335ad
Batch ID: 20250612_154949
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
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scores.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Team Scores
class TeamScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    shortcode = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return f'<TeamScore {self.team_name}: {self.score}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/report_score', methods=['POST'])
def report_score():
    """
    Endpoint for teams to report their scores.
    Expects a JSON payload with 'team_name', 'score', and 'shortcode'.
    """
    try:
        data = request.get_json()

        # Validate incoming JSON data
        if not all(key in data for key in ('team_name', 'score', 'shortcode')):
            return jsonify({"error": "Missing required fields"}), 400

        team_name = data['team_name']
        score = data['score']
        shortcode = data['shortcode']

        # Ensure score is an integer
        if not isinstance(score, int):
            return jsonify({"error": "Score must be an integer"}), 400

        # Create new TeamScore entry
        new_score = TeamScore(team_name=team_name, score=score, shortcode=shortcode)
        db.session.add(new_score)

        # Commit the new score to the database
        db.session.commit()

        return jsonify({"message": "Score reported successfully", "data": {"team_name": team_name, "score": score}}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Shortcode already exists"}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/scores', methods=['GET'])
def get_scores():
    """
    Endpoint to retrieve all reported scores.
    Returns a JSON array of team scores.
    """
    try:
        scores = TeamScore.query.all()
        scores_list = [{"team_name": score.team_name, "score": score.score, "shortcode": score.shortcode} for score in scores]
        return jsonify(scores_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Use debug=False in production
```
