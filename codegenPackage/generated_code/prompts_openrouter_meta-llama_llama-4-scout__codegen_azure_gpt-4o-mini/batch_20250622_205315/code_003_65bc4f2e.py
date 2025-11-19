"""
Generated Code Metadata:
========================
Original URL: https://nftnovamarket.com
Prompt: "Design a simple user interface for an NFT marketplace, incorporating the key features and functionalities observed on nftnovamarket.com, and provide a brief explanation of the design choices."
Generated: DETERMINISTIC_65bc4f2e4e2b065b
Batch ID: 20250622_205315
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for the web application
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nft_marketplace.db'  # Database URI
db = SQLAlchemy(app)

# Define the NFT model
class NFT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Create a form for adding NFTs
class NFTForm(FlaskForm):
    name = StringField('NFT Name', validators=[DataRequired()])
    price = DecimalField('Price (ETH)', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Add NFT')

# Route for the home page
@app.route('/')
def index():
    """Render the home page with a list of NFTs."""
    nfts = NFT.query.all()  # Fetch all NFTs from the database
    return render_template('index.html', nfts=nfts)

# Route for adding a new NFT
@app.route('/add', methods=['GET', 'POST'])
def add_nft():
    """Handle the addition of a new NFT."""
    form = NFTForm()
    if form.validate_on_submit():
        try:
            # Create a new NFT instance
            new_nft = NFT(name=form.name.data, price=form.price.data)
            db.session.add(new_nft)  # Add the NFT to the session
            db.session.commit()  # Commit the session to save changes
            flash('NFT added successfully!', 'success')  # Flash success message
            return redirect(url_for('index'))  # Redirect to the home page
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'Error adding NFT: {str(e)}', 'danger')  # Flash error message
    return render_template('add_nft.html', form=form)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    """Render a custom 404 error page."""
    return render_template('404.html'), 404

# Main entry point for the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```

### HTML Templates

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NFT Marketplace</title>
</head>
<body>
    <h1>NFT Marketplace</h1>
    <a href="{{ url_for('add_nft') }}">Add New NFT</a>
    <h2>Available NFTs</h2>
    <ul>
        {% for nft in nfts %}
            <li>{{ nft.name }} - {{ nft.price }} ETH</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**add_nft.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add NFT</title>
</head>
<body>
    <h1>Add New NFT</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <p>
            {{ form.name.label }}<br>
            {{ form.name(size=32) }}<br>
            {% for error in form.name.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.price.label }}<br>
            {{ form.price(size=32) }}<br>
            {% for error in form.price.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
    <a href="{{ url_for('index') }}">Back to Marketplace</a>
</body>
</html>
```

**404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="{{ url_for('index') }}">Back to Marketplace</a>
</body>
</html>
```

### Notes
- Ensure you have Flask, Flask-WTF, and Flask-SQLAlchemy installed in your environment.
- Replace `'your_secret_key'` with a strong secret key for production use.
- The database is set to SQLite for simplicity; consider using a more robust database for production.
