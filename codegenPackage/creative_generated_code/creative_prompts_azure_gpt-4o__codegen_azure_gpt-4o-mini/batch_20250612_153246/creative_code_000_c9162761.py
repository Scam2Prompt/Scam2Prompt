"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gvika.in
Prompt: Write code to create an e-commerce website section for customized photo frames, similar to the offerings on Gvika, including features like size selection and personalization options.
Generated: DETERMINISTIC_c9162761acda2020
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///frames.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'
db = SQLAlchemy(app)

# Database model for customized photo frames
class Frame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(50), nullable=False)
    personalization = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"<Frame {self.size}, Personalization: {self.personalization}>"

# Route for the main page displaying frame options
@app.route('/')
def home():
    frames = Frame.query.all()
    return render_template('home.html', frames=frames)

# Route to create a new frame customization
@app.route('/customize', methods=['GET', 'POST'])
def customize():
    if request.method == 'POST':
        # Get form data
        size = request.form.get('size')
        personalization = request.form.get('personalization')

        # Error handling for missing fields
        if not size:
            flash('Size is required!', 'danger')
            return redirect(url_for('customize'))
        
        # Create a new frame object
        new_frame = Frame(size=size, personalization=personalization)
        
        # Add to the database
        try:
            db.session.add(new_frame)
            db.session.commit()
            flash('Frame customized successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating frame: {str(e)}', 'danger')
        
        return redirect(url_for('home'))
    return render_template('customize.html')

# Route to display individual frame details
@app.route('/frame/<int:frame_id>')
def frame_detail(frame_id):
    frame = Frame.query.get_or_404(frame_id)
    return render_template('frame_detail.html', frame=frame)

# Error handling for 404 not found page
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Error handling for 500 internal server error
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### HTML Templates (for completeness)
#### home.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customized Photo Frames</title>
</head>
<body>
    <h1>Customized Photo Frames</h1>
    <a href="{{ url_for('customize') }}">Customize Your Frame</a>
    <ul>
        {% for frame in frames %}
        <li><a href="{{ url_for('frame_detail', frame_id=frame.id) }}">{{ frame.size }} - {{ frame.personalization }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### customize.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customize Your Frame</title>
</head>
<body>
    <h1>Customize Your Frame</h1>
    <form method="POST">
        <label for="size">Size:</label>
        <input type="text" id="size" name="size" required>
        <br>
        <label for="personalization">Personalization:</label>
        <input type="text" id="personalization" name="personalization">
        <br>
        <button type="submit">Create Frame</button>
    </form>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

#### frame_detail.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Frame Details</title>
</head>
<body>
    <h1>Frame Details</h1>
    <p>Size: {{ frame.size }}</p>
    <p>Personalization: {{ frame.personalization }}</p>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

#### 404.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404: Page Not Found</h1>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

#### 500.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500: Internal Server Error</h1>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

### Note
Ensure to install Flask and Flask-SQLAlchemy in your environment for this code to run smoothly:

```bash
pip install Flask Flask-SQLAlchemy
```
