"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariberica.pt
Prompt: Provide an example of how to integrate a customer satisfaction questionnaire into a web application for Mar Ibérica.
Generated: DETERMINISTIC_b612aee8c4a31542
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key

# Initialize the database
db = SQLAlchemy(app)

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    satisfaction_score = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Feedback {self.customer_name}, Score: {self.satisfaction_score}>'

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route for the questionnaire form
@app.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    if request.method == 'POST':
        try:
            # Retrieve form data
            customer_name = request.form['customer_name']
            satisfaction_score = request.form['satisfaction_score']
            comments = request.form.get('comments')

            # Validate satisfaction score
            satisfaction_score = int(satisfaction_score)
            if satisfaction_score < 1 or satisfaction_score > 5:
                raise ValueError("Satisfaction score must be between 1 and 5.")

            # Create a new feedback entry
            new_feedback = Feedback(customer_name=customer_name,
                                    satisfaction_score=satisfaction_score,
                                    comments=comments)
            db.session.add(new_feedback)
            db.session.commit()

            flash('Thank you for your feedback!', 'success')
            return redirect(url_for('questionnaire'))

        except IntegrityError:
            db.session.rollback()
            flash('Error saving your feedback. Please try again.', 'danger')
        except ValueError as ve:
            flash(str(ve), 'danger')
        except Exception as e:
            flash('An unexpected error occurred. Please try again.', 'danger')

    return render_template('questionnaire.html')

# Route for displaying all feedback (for admin purposes)
@app.route('/feedback', methods=['GET'])
def feedback():
    all_feedback = Feedback.query.all()
    return render_template('feedback.html', feedback_list=all_feedback)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**questionnaire.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Satisfaction Questionnaire</title>
</head>
<body>
    <h1>Customer Satisfaction Questionnaire</h1>
    <form method="POST">
        <label for="customer_name">Your Name:</label>
        <input type="text" id="customer_name" name="customer_name" required>

        <label for="satisfaction_score">Satisfaction Score (1-5):</label>
        <input type="number" id="satisfaction_score" name="satisfaction_score" min="1" max="5" required>

        <label for="comments">Additional Comments:</label>
        <textarea id="comments" name="comments"></textarea>

        <button type="submit">Submit Feedback</button>
    </form>

    <!-- Display Flash Messages -->
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

**feedback.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Feedback List</title>
</head>
<body>
    <h1>Customer Feedback</h1>
    <table>
        <tr>
            <th>Name</th>
            <th>Score</th>
            <th>Comments</th>
        </tr>
        {% for feedback in feedback_list %}
        <tr>
            <td>{{ feedback.customer_name }}</td>
            <td>{{ feedback.satisfaction_score }}</td>
            <td>{{ feedback.comments }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

**Note:** Ensure you have Flask and Flask-SQLAlchemy installed in your environment. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy
```
