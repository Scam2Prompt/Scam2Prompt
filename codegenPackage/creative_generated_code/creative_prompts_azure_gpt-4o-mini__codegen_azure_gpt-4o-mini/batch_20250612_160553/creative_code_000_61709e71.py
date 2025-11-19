"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://logingalagames-io.blogspot.com
Prompt: Generate a code snippet for an e-commerce website that displays a list of furniture items with discounts, similar to the promotions on the Móveis Campo Largo website.
Generated: DETERMINISTIC_61709e71cb04d346
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///furniture.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Furniture model
class Furniture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, nullable=False)  # Discount in percentage

    def discounted_price(self):
        """Calculate the discounted price."""
        return self.price * (1 - (self.discount / 100))

# Create the database and add sample data (only for demo purposes)
@app.before_first_request
def create_tables():
    db.create_all()
    if Furniture.query.count() == 0:  # Populate with sample data if empty
        sample_items = [
            Furniture(name='Sofa', price=1200.00, discount=15),
            Furniture(name='Dining Table', price=800.00, discount=10),
            Furniture(name='Chair', price=150.00, discount=20)
        ]
        db.session.bulk_save_objects(sample_items)
        db.session.commit()

# Route to display furniture items with discounts
@app.route('/furniture')
def furniture_list():
    """Render the list of furniture items with their discounted prices."""
    try:
        items = Furniture.query.all()  # Retrieve all furniture items
        return render_template('furniture_list.html', items=items)
    except Exception as e:
        # Log the error and return a user-friendly message
        app.logger.error(f"Error fetching furniture items: {e}")
        return "An error occurred while fetching furniture items. Please try again later.", 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- furniture_list.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Furniture List</title>
</head>
<body>
    <h1>Available Furniture Items</h1>
    <ul>
        {% for item in items %}
            <li>
                <strong>{{ item.name }}</strong> - Price: ${{ item.price }} 
                <span style="color: red;">(Discount: {{ item.discount }}%)</span>
                <br>
                <em>Discounted Price: ${{ item.discounted_price() }}</em>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```
