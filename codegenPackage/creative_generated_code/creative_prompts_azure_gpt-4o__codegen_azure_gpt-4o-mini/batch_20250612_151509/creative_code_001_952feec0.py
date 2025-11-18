"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://govssc.edu.bd
Prompt: Develop a web application using Flask that integrates with the Govt. Shah Sultan College's payment collection system for admission and session charges, ensuring users can download admit cards after payment.
Generated: DETERMINISTIC_952feec098d66ef7
Batch ID: 20250612_151509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for, send_file, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
import os
import pdfkit

# Initialize Flask application
app = Flask(__name__)

# Configuration settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///college.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this in production

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Models
class User(db.Model):
    """User model for storing user information."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

class Payment(db.Model):
    """Payment model for storing payment details."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)  # e.g., 'Pending', 'Completed'

# Routes
@app.route('/')
def index():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'], method='sha256')
        
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            flash('Login successful!', 'success')
            return redirect(url_for('payment'))
        else:
            flash('Login failed. Check your credentials.', 'danger')
    
    return render_template('login.html')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    """Handle payment processing."""
    if request.method == 'POST':
        amount = float(request.form['amount'])
        user_id = 1  # Replace with actual user session ID
        
        new_payment = Payment(user_id=user_id, amount=amount, status='Completed')
        db.session.add(new_payment)
        db.session.commit()
        
        flash('Payment successful!', 'success')
        return redirect(url_for('download_admit_card', payment_id=new_payment.id))
    
    return render_template('payment.html')

@app.route('/download_admit_card/<int:payment_id>')
def download_admit_card(payment_id):
    """Generate and download the admit card."""
    payment = Payment.query.get_or_404(payment_id)
    
    if payment.status != 'Completed':
        flash('Payment is not completed, cannot download admit card.', 'danger')
        return redirect(url_for('payment'))
    
    # Generate admit card as PDF
    admit_card_content = render_template('admit_card.html', payment=payment)
    pdf = pdfkit.from_string(admit_card_content, False)
    
    # Create a temporary file to hold the PDF
    pdf_filename = f'admit_card_{payment_id}.pdf'
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_filename)
    
    with open(pdf_path, 'wb') as f:
        f.write(pdf)
    
    return send_file(pdf_path, as_attachment=True)

# Error handling
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    # Create the uploads directory if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    # Run the app
    app.run(debug=True)
``` 

### Note:
- Ensure that you have the necessary HTML templates (`index.html`, `register.html`, `login.html`, `payment.html`, `admit_card.html`, `404.html`) in the `templates` folder.
- You need to install Flask, Flask-SQLAlchemy, Flask-Migrate, and pdfkit. Also, make sure to have wkhtmltopdf installed for pdfkit to work.
- Adjust the `SECRET_KEY` and database configuration as needed for production.
