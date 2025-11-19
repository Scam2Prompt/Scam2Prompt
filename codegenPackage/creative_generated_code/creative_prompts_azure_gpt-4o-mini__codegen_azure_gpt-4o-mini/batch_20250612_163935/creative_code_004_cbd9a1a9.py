"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homefoodsghana.com
Prompt: Develop a simple web application that showcases Homefoods' range of ethnic soups, including Neri-Neri and Fava Soup, with user reviews.
Generated: DETERMINISTIC_cbd9a1a9142081fc
Batch ID: 20250612_163935
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///soup_reviews.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'
db = SQLAlchemy(app)

# Define the Review model for the database
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    soup_name = db.Column(db.String(100), nullable=False)
    review_text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Review {self.soup_name}>'


# Route for the home page displaying soups and reviews
@app.route('/')
def home():
    soups = ['Neri-Neri', 'Fava Soup']
    reviews = Review.query.all()
    return render_template('home.html', soups=soups, reviews=reviews)


# Route for adding a new review
@app.route('/add_review', methods=['POST'])
def add_review():
    try:
        soup_name = request.form.get('soup_name')
        review_text = request.form.get('review_text')
        if not soup_name or not review_text:
            flash('Both soup name and review text are required!', 'danger')
            return redirect(url_for('home'))

        new_review = Review(soup_name=soup_name, review_text=review_text)
        db.session.add(new_review)
        db.session.commit()
        flash('Review added successfully!', 'success')
        return redirect(url_for('home'))
    except Exception as e:
        db.session.rollback()
        flash(f'An error occurred: {e}', 'danger')
        return redirect(url_for('home'))


# Create the database tables
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**home.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Homefoods Ethnic Soups</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Welcome to Homefoods Ethnic Soups</h1>
        <h2>Our Soups</h2>
        <ul>
            {% for soup in soups %}
                <li>{{ soup }}</li>
            {% endfor %}
        </ul>

        <h2>User Reviews</h2>
        <ul>
            {% for review in reviews %}
                <li><strong>{{ review.soup_name }}:</strong> {{ review.review_text }}</li>
            {% endfor %}
        </ul>

        <h2>Add Your Review</h2>
        <form action="{{ url_for('add_review') }}" method="POST">
            <div class="form-group">
                <label for="soup_name">Soup Name:</label>
                <input type="text" class="form-control" id="soup_name" name="soup_name" required>
            </div>
            <div class="form-group">
                <label for="review_text">Your Review:</label>
                <textarea class="form-control" id="review_text" name="review_text" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Submit Review</button>
        </form>
        
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <div class="mt-3">
                    {% for category, message in messages %}
                        <div class="alert alert-{{ category }}">{{ message }}</div>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}
    </div>
</body>
</html>
```

**Instructions:**
- Ensure you have Flask and Flask-SQLAlchemy installed (`pip install Flask Flask-SQLAlchemy`).
- Save the Python code in a file named `app.py` and the HTML code in a `templates` folder as `home.html`.
- Run the application with the command `python app.py`.
