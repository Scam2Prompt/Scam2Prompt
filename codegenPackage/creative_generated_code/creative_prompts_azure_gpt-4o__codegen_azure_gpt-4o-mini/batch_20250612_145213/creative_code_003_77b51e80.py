"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meetagreatamerican.com
Prompt: Suggest tools or frameworks for building a community-driven platform that highlights stories of accomplished individuals, as seen on "Meet A Great American."
Generated: DETERMINISTIC_77b51e80b2c08ea3
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for a web framework, database, and user authentication
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Set up configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community_stories.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Change this to a strong random key

# Initialize database and login manager
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


# Define the User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


# Define the Story model
class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relationship to link Story to User
    author = db.relationship('User', backref='stories')


# Load user function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Home route to display stories
@app.route('/')
def home():
    stories = Story.query.all()
    return render_template('home.html', stories=stories)


# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username=username, password=password)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except IntegrityError:
            db.session.rollback()
            return "Username already exists. Please choose a different one.", 400

    return render_template('register.html')


# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            return redirect(url_for('home'))
        return "Invalid username or password.", 401

    return render_template('login.html')


# Route to create a new story
@app.route('/story/new', methods=['GET', 'POST'])
@login_required
def create_story():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_story = Story(title=title, content=content, author_id=current_user.id)

        db.session.add(new_story)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('create_story.html')


# Route to log out
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return "Page not found", 404


# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug to False in production
```
