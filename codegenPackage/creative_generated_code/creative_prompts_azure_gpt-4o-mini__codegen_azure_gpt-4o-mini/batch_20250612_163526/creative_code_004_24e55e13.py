"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://traceybaptiste.com
Prompt: Write a code example that implements a storytelling feature inspired by Tracey Baptiste's narrative style, allowing users to create their own fairy tales and family lore through a web interface.
Generated: DETERMINISTIC_24e55e13d2915657
Batch ID: 20250612_163526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://127.0.0.1:5000`": {
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
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, TextAreaField, SubmitField, validators

# Initialize the web application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stories.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Database model for storing stories
class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Story {self.title}>'

# WTForms form for story input
class StoryForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=200)])
    content = TextAreaField('Content', [validators.Length(min=1)])
    submit = SubmitField('Create Story')

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    form = StoryForm(request.form)

    if request.method == 'POST' and form.validate():
        try:
            # Create a new story instance
            new_story = Story(title=form.title.data, content=form.content.data)
            db.session.add(new_story)
            db.session.commit()
            flash('Story created successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'Error creating story: {str(e)}', 'danger')

    # Retrieve all stories for display
    stories = Story.query.all()
    return render_template('index.html', form=form, stories=stories)

# Route for displaying a specific story
@app.route('/story/<int:story_id>')
def story(story_id):
    story = Story.query.get_or_404(story_id)
    return render_template('story.html', story=story)

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main entry point
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fairy Tale Creator</title>
</head>
<body>
    <h1>Create Your Fairy Tale</h1>
    <form method="POST" action="/">
        {{ form.hidden_tag() }}
        <div>
            {{ form.title.label }}<br>
            {{ form.title(size=50) }}<br>
            {% for error in form.title.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.content.label }}<br>
            {{ form.content(cols=50, rows=10) }}<br>
            {% for error in form.content.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>

    <h2>Your Stories</h2>
    <ul>
        {% for story in stories %}
            <li><a href="{{ url_for('story', story_id=story.id) }}">{{ story.title }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

**HTML Template (story.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ story.title }}</title>
</head>
<body>
    <h1>{{ story.title }}</h1>
    <p>{{ story.content }}</p>
    <a href="{{ url_for('index') }}">Back to Story List</a>
</body>
</html>
```

**HTML Template (404.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="{{ url_for('index') }}">Return Home</a>
</body>
</html>
```

### Instructions:
1. Ensure you have Flask and Flask-WTF installed in your Python environment.
2. Create a `templates` directory and save the HTML files inside it.
3. Run the application with `python <filename>.py` and open `http://127.0.0.1:5000` in your web browser to use the storytelling feature.
