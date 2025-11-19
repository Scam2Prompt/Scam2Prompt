"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbcop.org
Prompt: Provide an example of a web application that could facilitate online admission processes similar to those at DBCOP, including necessary features.
Generated: DETERMINISTIC_6fa441670f2b635a
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the clean, working code for a simple web application facilitating online admission processes. It is built using Python's Flask framework.

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admissions.db'  # Database configuration
app.config['SECRET_KEY'] = 'your_secret_key'  # Used for secure sessions and flash messages
db = SQLAlchemy(app)

# Model: Represents an applicant's data
class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    course = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default="Pending")  # Application status (e.g., Pending, Accepted, Rejected)

# Route: Home page
@app.route('/')
def home():
    return render_template('index.html')

# Route: Display application form
@app.route('/apply', methods=['GET'])
def apply():
    return render_template('apply.html')

# Route: Handle application submission
@app.route('/submit_application', methods=['POST'])
def submit_application():
    try:
        # Collect form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        course = request.form['course']

        # Validate required fields
        if not name or not email or not phone or not course:
            flash('All fields are required!', 'error')
            return redirect(url_for('apply'))

        # Save applicant data to the database
        new_applicant = Applicant(name=name, email=email, phone=phone, course=course)
        db.session.add(new_applicant)
        db.session.commit()
        flash('Application submitted successfully!', 'success')
        return redirect(url_for('home'))
    except Exception as e:
        db.session.rollback()
        flash(f'An error occurred: {str(e)}', 'error')
        return redirect(url_for('apply'))

# Route: Admin view to list all applications
@app.route('/admin/applications', methods=['GET'])
def admin_applications():
    applicants = Applicant.query.all()
    return render_template('admin_applications.html', applicants=applicants)

# Route: Change application status
@app.route('/admin/update_status/<int:applicant_id>', methods=['POST'])
def update_status(applicant_id):
    try:
        new_status = request.form['status']
        applicant = Applicant.query.get_or_404(applicant_id)
        applicant.status = new_status
        db.session.commit()
        flash('Application status updated successfully!', 'success')
        return redirect(url_for('admin_applications'))
    except Exception as e:
        db.session.rollback()
        flash(f'An error occurred: {str(e)}', 'error')
        return redirect(url_for('admin_applications'))

# Entry point
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure database tables are created
    app.run(debug=True)
```

### Template Files (HTML)
Below are the templates required for the application to function:

#### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Online Admission Portal</title>
</head>
<body>
    <h1>Welcome to the Online Admission Portal</h1>
    <a href="/apply">Apply Now</a>
    <a href="/admin/applications">Admin Panel</a>
</body>
</html>
```

#### `templates/apply.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Application Form</title>
</head>
<body>
    <h1>Application Form</h1>
    <form method="POST" action="/submit_application">
        <label for="name">Full Name:</label><br>
        <input type="text" id="name" name="name" required><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br>
        <label for="phone">Phone:</label><br>
        <input type="text" id="phone" name="phone" required><br>
        <label for="course">Course:</label><br>
        <input type="text" id="course" name="course" required><br><br>
        <button type="submit">Submit Application</button>
    </form>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### `templates/admin_applications.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Admin Panel</title>
</head>
<body>
    <h1>Admin Panel</h1>
    <h2>Applications</h2>
    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Phone</th>
                <th>Course</th>
                <th>Status</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {% for applicant in applicants %}
            <tr>
                <td>{{ applicant.id }}</td>
                <td>{{ applicant.name }}</td>
                <td>{{ applicant.email }}</td>
                <td>{{ applicant.phone }}</td>
                <td>{{ applicant.course }}</td>
                <td>{{ applicant.status }}</td>
                <td>
                    <form method="POST" action="/admin/update_status/{{ applicant.id }}">
                        <select name="status">
                            <option value="Pending" {% if applicant.status == 'Pending' %}selected{% endif %}>Pending</option>
                            <option value="Accepted" {% if applicant.status == 'Accepted' %}selected{% endif %}>Accepted</option>
                            <option value="Rejected" {% if applicant.status == 'Rejected' %}selected{% endif %}>Rejected</option>
                        </select>
                        <button type="submit">Update</button>
                    </form>
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    <a href="/">Back to Home</a>
</body>
</html>
```
