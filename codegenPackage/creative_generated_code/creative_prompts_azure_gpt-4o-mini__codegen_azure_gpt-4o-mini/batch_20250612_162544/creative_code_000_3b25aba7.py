"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aydinspirate.com
Prompt: Generate a code snippet for a web application that allows users to customize and order motorized blinds from a selection of styles like Sheer Elegance and Honeycell.
Generated: DETERMINISTIC_3b25aba74d765532
Batch ID: 20250612_162544
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

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blinds.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for Blinds
class Blind(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    style = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Blind {self.style} - {self.color}>'

# Route for the home page to display available blinds
@app.route('/')
def index():
    blinds = Blind.query.all()
    return render_template('index.html', blinds=blinds)

# Route to handle customization and order submission
@app.route('/order', methods=['POST'])
def order_blind():
    try:
        # Get data from the request
        style = request.form.get('style')
        color = request.form.get('color')
        quantity = int(request.form.get('quantity'))
        
        # Validate input
        if not style or not color or quantity <= 0:
            return jsonify({'error': 'Invalid input!'}), 400
        
        # Find the selected blind
        blind = Blind.query.filter_by(style=style, color=color).first()
        if not blind:
            return jsonify({'error': 'Blind not found!'}), 404
        
        # Calculate total price
        total_price = blind.price * quantity
        
        # Respond with order confirmation
        return jsonify({'message': 'Order placed successfully!', 'total_price': total_price}), 200
        
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred!'}), 500

# Initialize the database and create tables
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customize Motorized Blinds</title>
</head>
<body>
    <h1>Customize Your Motorized Blinds</h1>
    <form id="orderForm" method="POST" action="/order">
        <label for="style">Select Style:</label>
        <select name="style" id="style" required>
            {% for blind in blinds %}
                <option value="{{ blind.style }}">{{ blind.style }} - {{ blind.color }} (${{ blind.price }})</option>
            {% endfor %}
        </select>
        
        <label for="color">Select Color:</label>
        <input type="text" name="color" id="color" required>
        
        <label for="quantity">Quantity:</label>
        <input type="number" name="quantity" id="quantity" min="1" required>
        
        <button type="submit">Order Now</button>
    </form>
    
    <div id="response"></div>

    <script>
        // Handle form submission
        document.getElementById('orderForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            const formData = new FormData(this);
            fetch('/order', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                const responseDiv = document.getElementById('response');
                if (data.error) {
                    responseDiv.innerHTML = `<p>Error: ${data.error}</p>`;
                } else {
                    responseDiv.innerHTML = `<p>${data.message} Total Price: $${data.total_price}</p>`;
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    </script>
</body>
</html>
```
