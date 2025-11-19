"""
Generated Code Metadata:
========================
Original URL: https://kraken.media
Prompt: Write code to create a custom e-learning video series with interactive quizzes and progress tracking, inspired by Kraken Media’s approach to engaging training modules.
Generated: DETERMINISTIC_f4ccc8cffe48d30a
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e_learning_platform.py

from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///e_learning.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    url = db.Column(db.String(300), nullable=False)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), nullable=False)
    question = db.Column(db.String(300), nullable=False)
    correct_answer = db.Column(db.String(150), nullable=False)
    options = db.Column(db.String(500), nullable=False)  # Comma-separated options

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), nullable=False)
    completed = db.Column(db.Boolean, default=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    videos = Video.query.all()
    return render_template('index.html', videos=videos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/video/<int:video_id>', methods=['GET', 'POST'])
@login_required
def video(video_id):
    video = Video.query.get_or_404(video_id)
    if request.method == 'POST':
        # Handle quiz submission
        selected_answer = request.form.get('answer')
        quiz = Quiz.query.filter_by(video_id=video_id).first()
        if selected_answer == quiz.correct_answer:
            progress = Progress(user_id=current_user.id, video_id=video_id, completed=True)
            db.session.add(progress)
            db.session.commit()
            flash('Quiz completed successfully!')
        else:
            flash('Incorrect answer, please try again.')
    quizzes = Quiz.query.filter_by(video_id=video_id).all()
    return render_template('video.html', video=video, quizzes=quizzes)

@app.route('/progress')
@login_required
def progress():
    user_progress = Progress.query.filter_by(user_id=current_user.id).all()
    return render_template('progress.html', progress=user_progress)

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug=False in production
```

### Note:
- Ensure you have the necessary HTML templates (`index.html`, `login.html`, `video.html`, `progress.html`, `404.html`, `500.html`) in a `templates` directory.
- Install required packages using `pip install Flask Flask-SQLAlchemy Flask-Login`.
- Replace `'your_secret_key'` with a secure key for production use.
