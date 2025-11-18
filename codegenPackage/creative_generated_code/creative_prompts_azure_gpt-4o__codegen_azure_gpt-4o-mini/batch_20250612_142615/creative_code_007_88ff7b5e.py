"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabbi-apps.teachable.com
Prompt: Suggest methods for integrating privacy policy and terms of use pages into an online course platform, and provide example code.
Generated: DETERMINISTIC_88ff7b5ed245ca7b
Batch ID: 20250612_142615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Database model for Privacy Policy and Terms of Use
class Policy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Form for editing policy content
class PolicyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Update Policy')

@app.route('/policies', methods=['GET'])
def view_policies():
    """Render the Privacy Policy and Terms of Use pages."""
    privacy_policy = Policy.query.filter_by(title='Privacy Policy').first()
    terms_of_use = Policy.query.filter_by(title='Terms of Use').first()
    return render_template('policies.html', privacy_policy=privacy_policy, terms_of_use=terms_of_use)

@app.route('/policies/edit/<int:policy_id>', methods=['GET', 'POST'])
def edit_policy(policy_id):
    """Edit an existing policy."""
    policy = Policy.query.get_or_404(policy_id)
    form = PolicyForm(obj=policy)
    if form.validate_on_submit():
        policy.title = form.title.data
        policy.content = form.content.data
        db.session.commit()
        flash('Policy updated successfully!', 'success')
        return redirect(url_for('view_policies'))
    return render_template('edit_policy.html', form=form, policy=policy)

@app.route('/policies/create', methods=['GET', 'POST'])
def create_policy():
    """Create a new policy."""
    form = PolicyForm()
    if form.validate_on_submit():
        new_policy = Policy(title=form.title.data, content=form.content.data)
        db.session.add(new_policy)
        db.session.commit()
        flash('Policy created successfully!', 'success')
        return redirect(url_for('view_policies'))
    return render_template('create_policy.html', form=form)

if __name__ == '__main__':
    # Create database tables if they do not exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/policies.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Policies</title>
</head>
<body>
    <h1>Privacy Policy</h1>
    <div>{{ privacy_policy.content }}</div>
    <a href="{{ url_for('edit_policy', policy_id=privacy_policy.id) }}">Edit Privacy Policy</a>

    <h1>Terms of Use</h1>
    <div>{{ terms_of_use.content }}</div>
    <a href="{{ url_for('edit_policy', policy_id=terms_of_use.id) }}">Edit Terms of Use</a>
</body>
</html>
```

```html
<!-- templates/edit_policy.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Edit Policy</title>
</head>
<body>
    <h1>Edit {{ policy.title }}</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <p>
            {{ form.title.label }}<br>
            {{ form.title(size=32) }}<br>
            {% for error in form.title.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.content.label }}<br>
            {{ form.content(cols=40, rows=10) }}<br>
            {% for error in form.content.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
</body>
</html>
```

```html
<!-- templates/create_policy.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Create Policy</title>
</head>
<body>
    <h1>Create New Policy</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <p>
            {{ form.title.label }}<br>
            {{ form.title(size=32) }}<br>
            {% for error in form.title.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.content.label }}<br>
            {{ form.content(cols=40, rows=10) }}<br>
            {% for error in form.content.errors %}
                <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
</body>
</html>
```
