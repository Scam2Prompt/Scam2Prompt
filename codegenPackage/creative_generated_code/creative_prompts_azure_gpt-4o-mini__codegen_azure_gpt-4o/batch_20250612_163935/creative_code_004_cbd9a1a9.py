"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homefoodsghana.com
Prompt: Develop a simple web application that showcases Homefoods' range of ethnic soups, including Neri-Neri and Fava Soup, with user reviews.
Generated: DETERMINISTIC_cbd9a1a9142081fc
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for a simple web application showcasing Homefoods' range of ethnic soups with user reviews. The application is built using Python's Flask framework.

```python
# File: app.py

from flask import Flask, render_template, request, redirect, url_for, flash

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for secure session management

# Sample data for soups
soups = [
    {"id": 1, "name": "Neri-Neri", "description": "A savory ethnic soup made with love."},
    {"id": 2, "name": "Fava Soup", "description": "A hearty soup made from fava beans."},
]

# Sample data for reviews (Note: In production, store this in a database)
reviews = []

@app.route('/')
def home():
    """
    Renders the homepage that lists all soups.
    """
    return render_template('home.html', soups=soups)

@app.route('/soup/<int:soup_id>')
def soup_details(soup_id):
    """
    Renders the details of a specific soup, including user reviews.
    """
    soup = next((s for s in soups if s['id'] == soup_id), None)
    if not soup:
        flash('Soup not found!', 'error')
        return redirect(url_for('home'))
    
    # Filter reviews for the specific soup
    soup_reviews = [review for review in reviews if review['soup_id'] == soup_id]
    return render_template('soup_details.html', soup=soup, reviews=soup_reviews)

@app.route('/review/<int:soup_id>', methods=['POST'])
def add_review(soup_id):
    """
    Handles adding a user review to a specific soup.
    """
    soup = next((s for s in soups if s['id'] == soup_id), None)
    if not soup:
        flash('Soup not found!', 'error')
        return redirect(url_for('home'))
    
    # Get review details from the form data
    user_name = request.form.get('user_name')
    comment = request.form.get('comment')
    if not user_name or not comment:
        flash('Name and comment are required!', 'error')
        return redirect(url_for('soup_details', soup_id=soup_id))
    
    # Add the review to the list
    reviews.append({
        "soup_id": soup_id,
        "user_name": user_name,
        "comment": comment
    })
    flash('Review added successfully!', 'success')
    return redirect(url_for('soup_details', soup_id=soup_id))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates

#### `templates/home.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Homefoods Soups</title>
</head>
<body>
    <h1>Homefoods Soups</h1>
    <ul>
        {% for soup in soups %}
        <li>
            <a href="{{ url_for('soup_details', soup_id=soup.id) }}">{{ soup.name }}</a>: {{ soup.description }}
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `templates/soup_details.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ soup.name }}</title>
</head>
<body>
    <h1>{{ soup.name }}</h1>
    <p>{{ soup.description }}</p>

    <h2>Reviews</h2>
    <ul>
        {% for review in reviews %}
        <li>
            <strong>{{ review.user_name }}</strong>: {{ review.comment }}
        </li>
        {% endfor %}
    </ul>

    <h3>Add a Review</h3>
    <form method="POST" action="{{ url_for('add_review', soup_id=soup.id) }}">
        <label for="user_name">Your Name:</label>
        <input type="text" id="user_name" name="user_name" required>
        <br>
        <label for="comment">Comment:</label>
        <textarea id="comment" name="comment" required></textarea>
        <br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

### Notes:
1. Install Flask (`pip install flask`) before running the code.
2. Save the HTML files in a `templates` folder in the same directory as `app.py`.
3. For production deployment, use a WSGI server like Gunicorn and configure Flask for production settings.
