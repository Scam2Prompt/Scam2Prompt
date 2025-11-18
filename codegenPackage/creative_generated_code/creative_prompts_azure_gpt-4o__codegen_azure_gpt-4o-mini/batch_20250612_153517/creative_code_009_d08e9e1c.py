"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchlawinc.com
Prompt: Suggest libraries or frameworks for building a responsive legal form platform with features like shopping cart and checkout, inspired by Launch Law's design.
Generated: DETERMINISTIC_d08e9e1c17a46b26
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Use a strong secret key in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///legal_forms.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and Bootstrap
db = SQLAlchemy(app)
Bootstrap(app)

# Database model for storing legal forms
class LegalForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Form class for user input
class FormPurchase(FlaskForm):
    form_id = SelectField('Legal Form', coerce=int, validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    submit = SubmitField('Add to Cart')

# Route to display legal forms
@app.route('/')
def index():
    """Render the homepage with a list of legal forms."""
    legal_forms = LegalForm.query.all()
    form = FormPurchase()
    form.form_id.choices = [(form.id, form.name) for form in legal_forms]
    return render_template('index.html', legal_forms=legal_forms, form=form)

# Route to handle form submission
@app.route('/checkout', methods=['POST'])
def checkout():
    """Handle the checkout process."""
    form = FormPurchase()
    # Validate form data
    if form.validate_on_submit():
        # Retrieve selected form and quantity
        selected_form = LegalForm.query.get(form.form_id.data)
        quantity = form.quantity.data
        total_price = selected_form.price * quantity
        
        # Store in session for checkout confirmation
        session['cart'] = {
            'form_name': selected_form.name,
            'quantity': quantity,
            'total_price': total_price
        }
        
        return redirect(url_for('confirm_checkout'))
    else:
        flash('Error in form submission!', 'danger')
        return redirect(url_for('index'))

# Route to confirm checkout
@app.route('/confirm')
def confirm_checkout():
    """Render the checkout confirmation page."""
    cart = session.get('cart')
    if cart:
        return render_template('confirm.html', cart=cart)
    else:
        flash('No items in cart!', 'warning')
        return redirect(url_for('index'))

# Error handling for 404
@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

# Main block to run the application
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set to False in production
```

### Note:
- You will need to create the corresponding HTML templates (`index.html`, `confirm.html`, and `404.html`) in a `templates` folder.
- Remember to install the required libraries using pip:

```bash
pip install Flask Flask-SQLAlchemy Flask-WTF Flask-Bootstrap
```
