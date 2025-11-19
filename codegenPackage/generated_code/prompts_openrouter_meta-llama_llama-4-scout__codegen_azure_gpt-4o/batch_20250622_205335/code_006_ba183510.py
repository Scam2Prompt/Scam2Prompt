"""
Generated Code Metadata:
========================
Original URL: https://soulart.hu
Prompt: Develop a simple web application using a library like Flask or Django to share and track Mediterranean diet meal plans.
Generated: DETERMINISTIC_ba18351043182503
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
"""
A simple web application using Flask to share and track Mediterranean diet meal plans.
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure key in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meal_plans.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the MealPlan model
class MealPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<MealPlan {self.title}>"

# Route: Home page displaying all meal plans
@app.route('/')
def index():
    meal_plans = MealPlan.query.order_by(MealPlan.date_created.desc()).all()
    return render_template('index.html', meal_plans=meal_plans)

# Route: Add a new meal plan
@app.route('/add', methods=['GET', 'POST'])
def add_meal_plan():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')

        if not title or not description:
            flash('Title and description are required!', 'error')
            return redirect(url_for('add_meal_plan'))

        new_meal_plan = MealPlan(title=title, description=description)
        try:
            db.session.add(new_meal_plan)
            db.session.commit()
            flash('Meal plan added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error adding meal plan: {str(e)}', 'error')
            return redirect(url_for('add_meal_plan'))

    return render_template('add_meal_plan.html')

# Route: Delete a meal plan
@app.route('/delete/<int:id>')
def delete_meal_plan(id):
    meal_plan = MealPlan.query.get_or_404(id)
    try:
        db.session.delete(meal_plan)
        db.session.commit()
        flash('Meal plan deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting meal plan: {str(e)}', 'error')
    return redirect(url_for('index'))

# Route: Edit a meal plan
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_meal_plan(id):
    meal_plan = MealPlan.query.get_or_404(id)
    if request.method == 'POST':
        meal_plan.title = request.form.get('title')
        meal_plan.description = request.form.get('description')

        if not meal_plan.title or not meal_plan.description:
            flash('Title and description are required!', 'error')
            return redirect(url_for('edit_meal_plan', id=id))

        try:
            db.session.commit()
            flash('Meal plan updated successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error updating meal plan: {str(e)}', 'error')
            return redirect(url_for('edit_meal_plan', id=id))

    return render_template('edit_meal_plan.html', meal_plan=meal_plan)

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mediterranean Diet Meal Plans</title>
</head>
<body>
    <h1>Mediterranean Diet Meal Plans</h1>
    <a href="/add">Add New Meal Plan</a>
    <ul>
        {% for meal_plan in meal_plans %}
            <li>
                <h2>{{ meal_plan.title }}</h2>
                <p>{{ meal_plan.description }}</p>
                <a href="/edit/{{ meal_plan.id }}">Edit</a>
                <a href="/delete/{{ meal_plan.id }}" onclick="return confirm('Are you sure?');">Delete</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/add_meal_plan.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Meal Plan</title>
</head>
<body>
    <h1>Add New Meal Plan</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea>
        <br>
        <button type="submit">Add Meal Plan</button>
    </form>
    <a href="/">Back to Home</a>
</body>
</html>
```

```html
<!-- templates/edit_meal_plan.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Meal Plan</title>
</head>
<body>
    <h1>Edit Meal Plan</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" value="{{ meal_plan.title }}" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description" required>{{ meal_plan.description }}</textarea>
        <br>
        <button type="submit">Update Meal Plan</button>
    </form>
    <a href="/">Back to Home</a>
</body>
</html>
```
