"""
Generated Code Metadata:
========================
Original URL: https://meetagreatamerican.com
Prompt: Develop a web application that showcases the achievements of the 2024 selectees from Meet A Great American, including their contributions to society and branding opportunities.
Generated: DETERMINISTIC_27bb698cdae2c9eb
Batch ID: 20250612_155401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**meet_a_great_american.py**
```python
# Import required libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application instance
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///meet_a_great_american.db"
db = SQLAlchemy(app)

# Define the Selectee model
class Selectee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contribution = db.Column(db.Text, nullable=False)
    branding_opportunities = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Selectee('{self.name}')"

# Define the Achievement model
class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    selectee_id = db.Column(db.Integer, db.ForeignKey('selectee.id'), nullable=False)
    achievement = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Achievement('{self.achievement}')"

# Create the database tables
with app.app_context():
    db.create_all()

# Route to display all selectees
@app.route('/')
def index():
    selectees = Selectee.query.all()
    return render_template('index.html', selectees=selectees)

# Route to display a single selectee's details
@app.route('/selectee/<int:selectee_id>')
def selectee(selectee_id):
    selectee = Selectee.query.get_or_404(selectee_id)
    achievements = Achievement.query.filter_by(selectee_id=selectee_id).all()
    return render_template('selectee.html', selectee=selectee, achievements=achievements)

# Route to add a new selectee
@app.route('/add_selectee', methods=['GET', 'POST'])
def add_selectee():
    if request.method == 'POST':
        name = request.form['name']
        contribution = request.form['contribution']
        branding_opportunities = request.form['branding_opportunities']
        selectee = Selectee(name=name, contribution=contribution, branding_opportunities=branding_opportunities)
        db.session.add(selectee)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_selectee.html')

# Route to add a new achievement
@app.route('/add_achievement/<int:selectee_id>', methods=['GET', 'POST'])
def add_achievement(selectee_id):
    if request.method == 'POST':
        achievement = request.form['achievement']
        achievement_obj = Achievement(selectee_id=selectee_id, achievement=achievement)
        db.session.add(achievement_obj)
        db.session.commit()
        return redirect(url_for('selectee', selectee_id=selectee_id))
    return render_template('add_achievement.html', selectee_id=selectee_id)

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Meet A Great American</title>
</head>
<body>
    <h1>2024 Selectees</h1>
    <ul>
    {% for selectee in selectees %}
        <li>
            <a href="{{ url_for('selectee', selectee_id=selectee.id) }}">{{ selectee.name }}</a>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
```

**templates/selectee.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ selectee.name }}</title>
</head>
<body>
    <h1>{{ selectee.name }}</h1>
    <h2>Contributions to Society:</h2>
    <p>{{ selectee.contribution }}</p>
    <h2>Branding Opportunities:</h2>
    <p>{{ selectee.branding_opportunities }}</p>
    <h2>Achievements:</h2>
    <ul>
    {% for achievement in achievements %}
        <li>{{ achievement.achievement }}</li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('add_achievement', selectee_id=selectee.id) }}">Add Achievement</a></p>
</body>
</html>
```

**templates/add_selectee.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Add Selectee</title>
</head>
<body>
    <h1>Add Selectee</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="contribution">Contribution:</label>
        <textarea id="contribution" name="contribution"></textarea><br><br>
        <label for="branding_opportunities">Branding Opportunities:</label>
        <textarea id="branding_opportunities" name="branding_opportunities"></textarea><br><br>
        <input type="submit" value="Add Selectee">
    </form>
</body>
</html>
```

**templates/add_achievement.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Add Achievement</title>
</head>
<body>
    <h1>Add Achievement</h1>
    <form method="POST">
        <label for="achievement">Achievement:</label>
        <textarea id="achievement" name="achievement"></textarea><br><br>
        <input type="submit" value="Add Achievement">
    </form>
</body>
</html>
```

**templates/404.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>404 Error</title>
</head>
<body>
    <h1>404 Error</h1>
    <p>The page you requested could not be found.</p>
</body>
</html>
```

**templates/500.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>500 Error</title>
</head>
<body>
    <h1>500 Error</h1>
    <p>An internal server error occurred.</p>
</body>
</html>
```
