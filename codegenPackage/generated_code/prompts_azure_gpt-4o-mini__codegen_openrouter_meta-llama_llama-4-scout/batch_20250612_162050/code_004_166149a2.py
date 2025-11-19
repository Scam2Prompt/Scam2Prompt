"""
Generated Code Metadata:
========================
Original URL: https://openmindsinstituto.com.br
Prompt: Construct a code example that demonstrates how to implement a feedback form for participants of the Open Minds forums and symposia.
Generated: DETERMINISTIC_166149a28681d3f6
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# feedback_form.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, TextAreaField, validators

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SECRET_KEY'] = 'secret_key_here'
db = SQLAlchemy(app)


class Feedback(db.Model):
    """Feedback model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    feedback = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Feedback('{self.name}', '{self.email}')"


class FeedbackForm(Form):
    """Feedback form"""
    name = StringField('Name', [validators.Length(min=4, max=100)])
    email = StringField('Email Address', [validators.Length(min=6, max=100), validators.Email()])
    feedback = TextAreaField('Feedback', [validators.Length(min=10)])


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    """Feedback form view"""
    form = FeedbackForm()
    if request.method == 'POST':
        if form.validate():
            feedback = Feedback(name=form.name.data, email=form.email.data, feedback=form.feedback.data)
            db.session.add(feedback)
            db.session.commit()
            return redirect(url_for('success'))
        else:
            return render_template('feedback.html', form=form, errors=form.errors)
    return render_template('feedback.html', form=form)


@app.route('/success')
def success():
    """Success view"""
    return render_template('success.html')


@app.errorhandler(404)
def not_found(error):
    """404 error handler"""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """500 error handler"""
    db.session.rollback()
    return render_template('500.html'), 500


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/feedback.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Feedback Form</title>
</head>
<body>
    <h1>Feedback Form</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.name.label }} {{ form.name() }}
        {% for error in form.name.errors %}
            <span style="color: red;">[{{ error }}]</span>
        {% endfor %}
        <br>
        {{ form.email.label }} {{ form.email() }}
        {% for error in form.email.errors %}
            <span style="color: red;">[{{ error }}]</span>
        {% endfor %}
        <br>
        {{ form.feedback.label }} {{ form.feedback() }}
        {% for error in form.feedback.errors %}
            <span style="color: red;">[{{ error }}]</span>
        {% endfor %}
        <br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

```html
<!-- templates/success.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success</title>
</head>
<body>
    <h1>Thank you for your feedback!</h1>
</body>
</html>
```

```html
<!-- templates/404.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Error</title>
</head>
<body>
    <h1>404 Error: Page not found</h1>
</body>
</html>
```

```html
<!-- templates/500.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>500 Error</title>
</head>
<body>
    <h1>500 Error: Internal server error</h1>
</body>
</html>
```
