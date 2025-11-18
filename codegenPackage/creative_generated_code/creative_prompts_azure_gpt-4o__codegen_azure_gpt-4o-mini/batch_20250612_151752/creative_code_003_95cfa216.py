"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-pieces-service.fr
Prompt: Suggest a library or framework for building a web-based tool to manage client communications, order tracking, and invoicing for a parts distributor like Distribution Pièces Service.
Generated: DETERMINISTIC_95cfa2163a53a91b
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for building a web application
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///client_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Replace with a secure key

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Client model
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'<Client {self.name}>'

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    parts = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), default='Pending')

    client = db.relationship('Client', backref='orders')

    def __repr__(self):
        return f'<Order {self.id} for {self.client.name}>'

# Define the route for the home page
@app.route('/')
def index():
    # Get all clients to display on the home page
    clients = Client.query.all()
    return render_template('index.html', clients=clients)

# Define the route to add a new client
@app.route('/add_client', methods=['POST'])
def add_client():
    # Get client data from the form
    name = request.form.get('name')
    email = request.form.get('email')
    
    # Error handling for duplicate entries
    if Client.query.filter_by(email=email).first():
        flash('Client with this email already exists!', 'error')
        return redirect(url_for('index'))

    # Create a new client instance
    new_client = Client(name=name, email=email)
    
    # Add and commit the new client to the database
    db.session.add(new_client)
    db.session.commit()
    
    flash('Client added successfully!', 'success')
    return redirect(url_for('index'))

# Define the route to add a new order for a client
@app.route('/add_order/<int:client_id>', methods=['POST'])
def add_order(client_id):
    parts = request.form.get('parts')
    
    # Create a new order instance
    new_order = Order(client_id=client_id, parts=parts)
    
    # Add and commit the new order to the database
    db.session.add(new_order)
    db.session.commit()
    
    flash('Order added successfully!', 'success')
    return redirect(url_for('index'))

# Define the route to view orders for a specific client
@app.route('/client/<int:client_id>')
def client_orders(client_id):
    client = Client.query.get_or_404(client_id)
    return render_template('client_orders.html', client=client)

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
    <title>Client Management</title>
</head>
<body>
    <h1>Client Management</h1>
    <h2>Add Client</h2>
    <form action="/add_client" method="POST">
        <input type="text" name="name" placeholder="Client Name" required>
        <input type="email" name="email" placeholder="Client Email" required>
        <button type="submit">Add Client</button>
    </form>

    <h2>Clients</h2>
    <ul>
        {% for client in clients %}
            <li>
                {{ client.name }} ({{ client.email }})
                <form action="/add_order/{{ client.id }}" method="POST">
                    <input type="text" name="parts" placeholder="Order Parts" required>
                    <button type="submit">Add Order</button>
                </form>
                <a href="/client/{{ client.id }}">View Orders</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- client_orders.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Orders for {{ client.name }}</title>
</head>
<body>
    <h1>Orders for {{ client.name }}</h1>
    <ul>
        {% for order in client.orders %}
            <li>
                Order ID: {{ order.id }} - Parts: {{ order.parts }} - Status: {{ order.status }}
            </li>
        {% endfor %}
    </ul>
    <a href="/">Back to Home</a>
</body>
</html>
```

This code sets up a basic web application to manage client communications, order tracking, and invoicing using Flask, SQLAlchemy, and SQLite. Ensure you have the required libraries installed, and run the application to start managing clients and orders.
