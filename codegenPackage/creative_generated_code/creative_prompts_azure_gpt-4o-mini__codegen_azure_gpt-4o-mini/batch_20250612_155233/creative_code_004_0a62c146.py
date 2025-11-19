"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus-re.was-systems.com
Prompt: What libraries can I use to build a web form for collecting user recommendations, similar to the one on the Proximus site?
Generated: DETERMINISTIC_0a62c146667a852b
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web application development
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recommendations.db'  # Database configuration
app.config['SECRET_KEY'] = 'supersecretkey'  # Secret key for session management
db = SQLAlchemy(app)

# Define the Recommendation model
class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    user_name = db.Column(db.String(100), nullable=False)  # Name of the user
    recommendation_text = db.Column(db.Text, nullable=False)  # Text of the recommendation
    
    def __repr__(self):
        return f'<Recommendation {self.user_name}: {self.recommendation_text[:20]}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Define the route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form['user_name']
        recommendation_text = request.form['recommendation_text']
        
        # Create a new recommendation instance
        new_recommendation = Recommendation(user_name=user_name, recommendation_text=recommendation_text)
        
        try:
            db.session.add(new_recommendation)  # Add to the session
            db.session.commit()  # Commit the session
            flash('Recommendation submitted successfully!', 'success')  # Flash success message
            return redirect(url_for('index'))  # Redirect to the index page
        except IntegrityError:
            db.session.rollback()  # Rollback session on error
            flash('Error: Recommendation could not be saved. Please try again.', 'danger')  # Flash error message

    # Retrieve all recommendations for display
    recommendations = Recommendation.query.all() 
    return render_template('index.html', recommendations=recommendations)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development
```

```html
<!-- Templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Recommendations</title>
</head>
<body>
    <h1>User Recommendations</h1>
    
    <!-- Display flash messages -->
    {% with messages = get_flashed_messages(with_categories=True) %}
      {% if messages %}
        <ul>
        {% for category, message in messages %}
          <li class="{{ category }}">{{ message }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    
    <!-- Recommendation form -->
    <form action="" method="post">
        <label for="user_name">Your Name:</label>
        <input type="text" id="user_name" name="user_name" required>
        
        <label for="recommendation_text">Your Recommendation:</label>
        <textarea id="recommendation_text" name="recommendation_text" required></textarea>
        
        <button type="submit">Submit</button>
    </form>
    
    <h2>Previous Recommendations</h2>
    <ul>
        {% for recommendation in recommendations %}
            <li><strong>{{ recommendation.user_name }}:</strong> {{ recommendation.recommendation_text }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```
