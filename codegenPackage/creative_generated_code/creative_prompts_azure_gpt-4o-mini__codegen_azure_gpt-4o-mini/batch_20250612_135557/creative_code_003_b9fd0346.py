"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boomchange.com
Prompt: Describe how to create a user-friendly interface for a crypto exchange that mimics the steps outlined on Boomchange, including selecting pairs and receiving crypto.
Generated: DETERMINISTIC_b9fd0346cd7c90ed
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, SelectField, SubmitField, validators

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crypto_exchange.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Database model for storing crypto pairs
class CryptoPair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<CryptoPair {self.name}>'

# Create a form for selecting crypto pairs
class PairSelectionForm(Form):
    pair = SelectField('Select Crypto Pair', coerce=int)
    submit = SubmitField('Exchange')

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    # Create the form instance
    form = PairSelectionForm(request.form)
    
    # Populate the pair selection dropdown
    form.pair.choices = [(pair.id, pair.name) for pair in CryptoPair.query.all()]

    if request.method == 'POST' and form.validate():
        selected_pair = CryptoPair.query.get(form.pair.data)
        if selected_pair:
            flash(f'You selected {selected_pair.name} for exchange.', 'success')
            return redirect(url_for('exchange', pair_id=selected_pair.id))
        else:
            flash('Error: Invalid selection.', 'danger')

    return render_template('index.html', form=form)

# Route for the exchange page
@app.route('/exchange/<int:pair_id>', methods=['GET', 'POST'])
def exchange(pair_id):
    # Fetch selected crypto pair from the database
    pair = CryptoPair.query.get_or_404(pair_id)
    return render_template('exchange.html', pair=pair)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Main function
if __name__ == '__main__':
    # Create the database if it doesn't exist
    with app.app_context():
        db.create_all()
    
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
1. The code assumes the presence of HTML templates named `index.html`, `exchange.html`, and `404.html` for rendering the pages.
2. Replace `'your_secret_key'` with a secure key to ensure session security.
3. Ensure that the SQLite database is appropriate for production or switch to a more robust database system as needed.
