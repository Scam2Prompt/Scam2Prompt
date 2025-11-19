"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: Develop a web application that showcases success stories of women leaders from Sauti Kenya, highlighting their contributions to community advocacy and sustainability.
Generated: DETERMINISTIC_2d141e24bd0b2184
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**sauti_kenya_app.py**
```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application instance
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sauti_kenya.db"
db = SQLAlchemy(app)

# Define the model for success stories
class SuccessStory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    story = db.Column(db.Text, nullable=False)
    contributions = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"SuccessStory('{self.name}', '{self.story}')"

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page
@app.route("/")
def index():
    try:
        stories = SuccessStory.query.all()
        return render_template("index.html", stories=stories)
    except Exception as e:
        return render_template("error.html", error=str(e))

# Route for adding a new success story
@app.route("/add_story", methods=["GET", "POST"])
def add_story():
    if request.method == "POST":
        try:
            story = SuccessStory(
                name=request.form["name"],
                story=request.form["story"],
                contributions=request.form["contributions"],
                image_url=request.form["image_url"],
            )
            db.session.add(story)
            db.session.commit()
            return redirect(url_for("index"))
        except Exception as e:
            return render_template("error.html", error=str(e))
    return render_template("add_story.html")

# Route for viewing a single success story
@app.route("/story/<int:story_id>")
def view_story(story_id):
    try:
        story = SuccessStory.query.get_or_404(story_id)
        return render_template("story.html", story=story)
    except Exception as e:
        return render_template("error.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sauti Kenya Success Stories</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Sauti Kenya Success Stories</h1>
    <div class="stories">
        {% for story in stories %}
            <div class="story">
                <h2>{{ story.name }}</h2>
                <p>{{ story.story }}</p>
                <p><strong>Contributions:</strong> {{ story.contributions }}</p>
                {% if story.image_url %}
                    <img src="{{ story.image_url }}" alt="{{ story.name }}">
                {% endif %}
            </div>
        {% endfor %}
    </div>
    <p><a href="{{ url_for('add_story') }}">Add a new success story</a></p>
</body>
</html>
```

**templates/add_story.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add a Success Story</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Add a Success Story</h1>
    <form method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="story">Story:</label>
        <textarea id="story" name="story"></textarea><br><br>
        <label for="contributions">Contributions:</label>
        <textarea id="contributions" name="contributions"></textarea><br><br>
        <label for="image_url">Image URL:</label>
        <input type="text" id="image_url" name="image_url"><br><br>
        <input type="submit" value="Add Story">
    </form>
</body>
</html>
```

**templates/story.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ story.name }}'s Success Story</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>{{ story.name }}'s Success Story</h1>
    <p>{{ story.story }}</p>
    <p><strong>Contributions:</strong> {{ story.contributions }}</p>
    {% if story.image_url %}
        <img src="{{ story.image_url }}" alt="{{ story.name }}">
    {% endif %}
</body>
</html>
```

**templates/error.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Error</h1>
    <p>{{ error }}</p>
</body>
</html>
```

**static/style.css**
```css
body {
    font-family: Arial, sans-serif;
}

.stories {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.story {
    margin: 20px;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.story img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}
```
