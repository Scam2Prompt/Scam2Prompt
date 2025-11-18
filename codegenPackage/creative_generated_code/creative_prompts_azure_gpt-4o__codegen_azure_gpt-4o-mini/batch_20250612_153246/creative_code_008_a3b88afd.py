"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rebelsatoshi-in.web.app
Prompt: Generate code for a leaderboard system to showcase the funniest Recusant memes submitted by users, integrating community voting functionality.
Generated: DETERMINISTIC_a3b88afdfbbebdb7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leaderboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Meme(db.Model):
    """Model representing a submitted meme."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    votes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Meme {self.title} - Votes: {self.votes}>"

class MemeSchema(Schema):
    """Schema for serializing Meme objects."""
    id = fields.Int()
    title = fields.Str(required=True)
    image_url = fields.Str(required=True)
    votes = fields.Int()

meme_schema = MemeSchema()
memes_schema = MemeSchema(many=True)

@app.route('/memes', methods=['POST'])
def submit_meme():
    """Endpoint to submit a new meme."""
    try:
        data = request.get_json()
        meme = meme_schema.load(data)
        new_meme = Meme(**meme)
        db.session.add(new_meme)
        db.session.commit()
        return meme_schema.dump(new_meme), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/memes', methods=['GET'])
def get_memes():
    """Endpoint to retrieve the leaderboard of memes sorted by votes."""
    memes = Meme.query.order_by(Meme.votes.desc()).all()
    return memes_schema.dump(memes), 200

@app.route('/vote/<int:meme_id>', methods=['POST'])
def vote_meme(meme_id):
    """Endpoint for voting on a meme."""
    try:
        meme = Meme.query.get_or_404(meme_id)
        meme.votes += 1
        db.session.commit()
        return meme_schema.dump(meme), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    """Render the leaderboard page."""
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
```

### Template: `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Leaderboard</title>
</head>
<body>
    <h1>Funniest Recusant Memes Leaderboard</h1>
    <div id="leaderboard"></div>

    <script>
        async function fetchMemes() {
            const response = await fetch('/memes');
            const memes = await response.json();
            const leaderboardDiv = document.getElementById('leaderboard');
            leaderboardDiv.innerHTML = '';
            memes.forEach(meme => {
                const memeDiv = document.createElement('div');
                memeDiv.innerHTML = `<h3>${meme.title} - Votes: ${meme.votes}</h3>
                                     <img src="${meme.image_url}" alt="${meme.title}" style="max-width: 200px;">
                                     <button onclick="vote(${meme.id})">Vote</button>`;
                leaderboardDiv.appendChild(memeDiv);
            });
        }

        async function vote(memeId) {
            const response = await fetch(`/vote/${memeId}`, { method: 'POST' });
            if (response.ok) {
                fetchMemes();  // Refresh the leaderboard after voting
            }
        }

        fetchMemes();  // Initial load
    </script>
</body>
</html>
```

### Note:
- Make sure to have Flask, Flask-SQLAlchemy, Flask-Migrate, and Marshmallow installed in your environment.
- Run the application with a valid Python environment and install the necessary packages.
- Create the database initially by running the application.
