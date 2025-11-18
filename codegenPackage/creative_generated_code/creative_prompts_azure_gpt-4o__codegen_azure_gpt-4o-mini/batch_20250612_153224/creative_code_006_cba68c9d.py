"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emareels.se
Prompt: Suggest a library or framework to create an interactive web interface for comparing fishing reel models, such as "Old School Brass 1 & 2" and "Trout 2," using the data from Emanuelson Reels.
Generated: DETERMINISTIC_cba68c9dde03830b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reels.db'  # Database URI
db = SQLAlchemy(app)

# Model for Fishing Reel
class FishingReel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(100), nullable=False)
    features = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<FishingReel {self.model_name}>"

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    # Fetch all reel models from the database
    reels = FishingReel.query.all()
    return render_template('index.html', reels=reels)

# Route for comparing two reels
@app.route('/compare', methods=['POST'])
def compare_reels():
    try:
        # Get model names from the request
        model1_name = request.json.get('model1')
        model2_name = request.json.get('model2')

        # Fetch reel models from the database
        model1 = FishingReel.query.filter_by(model_name=model1_name).first()
        model2 = FishingReel.query.filter_by(model_name=model2_name).first()

        # Check if both models exist
        if not model1 or not model2:
            return jsonify({'error': 'One or both reel models not found.'}), 404

        # Return the features of both reels for comparison
        return jsonify({
            'model1': {
                'name': model1.model_name,
                'features': model1.features
            },
            'model2': {
                'name': model2.model_name,
                'features': model2.features
            }
        })

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

# HTML Template (templates/index.html)
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fishing Reel Comparison</title>
</head>
<body>
    <h1>Compare Fishing Reels</h1>
    <form id="comparison-form">
        <label for="model1">Reel Model 1:</label>
        <input type="text" id="model1" required>
        <label for="model2">Reel Model 2:</label>
        <input type="text" id="model2" required>
        <button type="submit">Compare</button>
    </form>
    <div id="comparison-result"></div>

    <script>
        document.getElementById('comparison-form').addEventListener('submit', function(event) {
            event.preventDefault();
            const model1 = document.getElementById('model1').value;
            const model2 = document.getElementById('model2').value;

            fetch('/compare', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ model1, model2 })
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    document.getElementById('comparison-result').innerText = data.error;
                } else {
                    document.getElementById('comparison-result').innerHTML = `
                        <h2>Comparison Result</h2>
                        <h3>${data.model1.name}</h3>
                        <p>${data.model1.features}</p>
                        <h3>${data.model2.name}</h3>
                        <p>${data.model2.features}</p>
                    `;
                }
            })
            .catch(error => {
                document.getElementById('comparison-result').innerText = 'An error occurred while fetching comparison data.';
            });
        });
    </script>
</body>
</html>
'''
```
