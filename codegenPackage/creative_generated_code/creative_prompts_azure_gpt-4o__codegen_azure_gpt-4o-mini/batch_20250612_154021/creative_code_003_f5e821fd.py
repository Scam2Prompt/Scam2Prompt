"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://projectvox.pages.dev
Prompt: Implement a feature to display and filter guilds by categories such as "featured" and "newest," inspired by the Guildhall website's guild exploration tools.
Generated: DETERMINISTIC_f5e821fdda9ae7e5
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guilds.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for the Guild
class Guild(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., 'featured', 'newest'
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Guild {self.name}>'

# Route to display guilds with filtering capabilities
@app.route('/guilds', methods=['GET'])
def display_guilds():
    try:
        filter_category = request.args.get('category')
        
        # Query the database based on the filter category
        if filter_category:
            guilds = Guild.query.filter_by(category=filter_category).all()
        else:
            guilds = Guild.query.all()

        return render_template('guilds.html', guilds=guilds, selected_category=filter_category)
    except Exception as e:
        # Log the error (logging setup not shown here)
        print(f"Error retrieving guilds: {e}")
        return render_template('error.html', message="Unable to retrieve guilds at this time."), 500

# Route to add a new guild (for demonstration purposes)
@app.route('/add_guild', methods=['POST'])
def add_guild():
    try:
        # Assume data comes from a form submission
        name = request.form['name']
        category = request.form['category']
        description = request.form.get('description', '')

        # Create a new guild instance
        new_guild = Guild(name=name, category=category, description=description)
        db.session.add(new_guild)
        db.session.commit()

        return redirect(url_for('display_guilds'))
    except Exception as e:
        # Log the error
        print(f"Error adding guild: {e}")
        return render_template('error.html', message="Unable to add the guild at this time."), 500

# Main entry point of the application
if __name__ == '__main__':
    # Create the database if it does not exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug=False in production
```

```html
<!-- guilds.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guilds</title>
</head>
<body>
    <h1>Guilds</h1>
    <form method="GET" action="{{ url_for('display_guilds') }}">
        <label for="category">Filter by:</label>
        <select name="category" id="category" onchange="this.form.submit()">
            <option value="">All</option>
            <option value="featured" {% if selected_category == 'featured' %}selected{% endif %}>Featured</option>
            <option value="newest" {% if selected_category == 'newest' %}selected{% endif %}>Newest</option>
        </select>
    </form>
    
    <ul>
        {% for guild in guilds %}
            <li>{{ guild.name }} - {{ guild.category }}: {{ guild.description }}</li>
        {% else %}
            <li>No guilds found.</li>
        {% endfor %}
    </ul>

    <a href="{{ url_for('add_guild') }}">Add a new guild</a>
</body>
</html>

<!-- error.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p>{{ message }}</p>
    <a href="{{ url_for('display_guilds') }}">Go back to guilds</a>
</body>
</html>
```
