"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poolz.uk
Prompt: Create a web application that integrates a pool design gallery and allows users to customize pool designs based on their property and budget, inspired by Poolz's custom design service.
Generated: DETERMINISTIC_f1ab30a17c9c0c60
Batch ID: 20250612_151308
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://code.jquery.com/jquery-3.5.1.slim.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pools.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Pool model
class Pool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Pool {self.name}>'

# Create the database and add sample data
@app.before_first_request
def create_tables():
    db.create_all()
    if Pool.query.count() == 0:
        sample_pools = [
            Pool(name='Infinity Pool', description='A beautiful infinity pool.', image_url='url1.jpg', price=50000),
            Pool(name='Lap Pool', description='A long, narrow pool for swimming laps.', image_url='url2.jpg', price=30000),
            Pool(name='Kidney Pool', description='A kidney-shaped pool perfect for family fun.', image_url='url3.jpg', price=25000)
        ]
        db.session.bulk_save_objects(sample_pools)
        db.session.commit()

# Route for the home page
@app.route('/')
def index():
    pools = Pool.query.all()
    return render_template('index.html', pools=pools)

# Route to customize pool design
@app.route('/customize', methods=['POST'])
def customize_pool():
    try:
        data = request.get_json()

        # Validate input
        if 'pool_id' not in data or 'budget' not in data:
            return jsonify({'error': 'Invalid input!'}), 400

        pool = Pool.query.get(data['pool_id'])
        if pool is None:
            return jsonify({'error': 'Pool not found!'}), 404

        # Simple customization logic (placeholder)
        if pool.price > data['budget']:
            return jsonify({'error': 'Budget not sufficient for this design!'}), 400

        # Return customized pool details
        return jsonify({
            'success': True,
            'pool_name': pool.name,
            'pool_description': pool.description,
            'pool_price': pool.price,
            'custom_features': 'Customized features based on budget'
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pool Design Gallery</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="my-4">Pool Design Gallery</h1>
        <div class="row">
            {% for pool in pools %}
            <div class="col-md-4">
                <div class="card mb-4">
                    <img src="{{ pool.image_url }}" class="card-img-top" alt="{{ pool.name }}">
                    <div class="card-body">
                        <h5 class="card-title">{{ pool.name }}</h5>
                        <p class="card-text">{{ pool.description }}</p>
                        <p class="card-text"><strong>Price: ${{ pool.price }}</strong></p>
                        <button class="btn btn-primary customize-btn" data-id="{{ pool.id }}">Customize</button>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script>
        $(document).ready(function() {
            $('.customize-btn').click(function() {
                const poolId = $(this).data('id');
                const budget = prompt("Enter your budget:");

                if (budget) {
                    $.ajax({
                        url: '/customize',
                        method: 'POST',
                        contentType: 'application/json',
                        data: JSON.stringify({ pool_id: poolId, budget: parseFloat(budget) }),
                        success: function(response) {
                            alert('Customization successful! Features: ' + response.custom_features);
                        },
                        error: function(xhr) {
                            alert('Error: ' + xhr.responseJSON.error);
                        }
                    });
                }
            });
        });
    </script>
</body>
</html>
```

### Note:
1. Ensure you have Flask and SQLAlchemy installed. You can install them via pip:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```
2. Create a folder named `templates` in the same directory as `app.py` and place the HTML file within that folder.
3. You can run the application using:
   ```bash
   python app.py
   ```
