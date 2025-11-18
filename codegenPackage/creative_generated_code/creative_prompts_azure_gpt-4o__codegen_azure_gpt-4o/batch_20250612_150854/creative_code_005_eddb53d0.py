"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.io
Prompt: Develop a web application using Flask or Django that replicates the Immediate Peak registration process and connects users to investment education companies.
Generated: DETERMINISTIC_eddb53d024ac358f
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application for Immediate Peak registration process
# and connecting users to investment education companies

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Used for session management and flash messages
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model for User Registration
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    investment_company = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'


@app.route('/')
def home():
    """
    Route to the homepage.
    """
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Route to handle user registration.
    """
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            investment_company = request.form['investment_company']

            # Validate form data
            if not name or not email or not phone or not investment_company:
                flash('All fields are required!', 'error')
                return redirect(url_for('register'))

            # Check for existing email
            if User.query.filter_by(email=email).first():
                flash('Email is already registered!', 'error')
                return redirect(url_for('register'))

            # Add user to the database
            new_user = User(
                name=name,
                email=email,
                phone=phone,
                investment_company=investment_company
            )
            db.session.add(new_user)
            db.session.commit()

            flash('Registration successful!', 'success')
            return redirect(url_for('home'))

        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
            return redirect(url_for('register'))

    return render_template('register.html')


@app.route('/users', methods=['GET'])
def users():
    """
    Route to display all registered users.
    """
    try:
        all_users = User.query.all()
        return render_template('users.html', users=all_users)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Error Handling
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors.
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    """
    Handle 500 errors.
    """
    return render_template('500.html'), 500


if __name__ == '__main__':
    # Create database and run the app
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Directory Structure
```
project/
├── app.py            # The main application script
├── templates/        # HTML files for rendering views
│   ├── home.html     # Home page template
│   ├── register.html # Registration page template
│   ├── users.html    # View registered users page
│   ├── 404.html      # Custom 404 error page
│   └── 500.html      # Custom 500 error page
├── static/           # CSS/JS/images (if needed)
└── users.db          # SQLite database (auto-generated)
```

You can extend the application as needed (e.g., adding authentication, connecting to external investment education APIs, etc.). Let me know if you'd like additional functionality!
