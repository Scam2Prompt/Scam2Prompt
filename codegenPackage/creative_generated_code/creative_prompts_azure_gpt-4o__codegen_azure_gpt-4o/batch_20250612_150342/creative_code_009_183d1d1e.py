"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taiko-t.com
Prompt: Develop a web application for recruitment in the construction industry, tailored to companies like 株式会社タイコーテクノ, with features for job postings and applicant tracking.
Generated: DETERMINISTIC_183d1d1ea1785a73
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the implementation for a basic recruitment web application tailored to the construction industry. The example uses Python with the Flask framework on the backend and SQLite for the database.

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure value in production

DATABASE = 'recruitment.db'

# Utility function: Connect to the database
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

# Route: Home page
@app.route('/')
def index():
    conn = get_db_connection()
    if conn:
        jobs = conn.execute('SELECT * FROM job_postings').fetchall()
        conn.close()
        return render_template('index.html', jobs=jobs)
    flash('Failed to load jobs. Please try again later.')
    return render_template('index.html', jobs=[])

# Route: Create job posting
@app.route('/post-job', methods=['GET', 'POST'])
def post_job():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        company = request.form['company']
        
        if not title or not description or not company:
            flash('All fields are required.')
            return redirect(url_for('post_job'))
        
        conn = get_db_connection()
        if conn:
            conn.execute(
                'INSERT INTO job_postings (title, description, company) VALUES (?, ?, ?)',
                (title, description, company)
            )
            conn.commit()
            conn.close()
            flash('Job posted successfully!')
            return redirect(url_for('index'))
        flash('Failed to post the job. Please try again.')
        return redirect(url_for('post_job'))
    return render_template('post_job.html')

# Route: View applicants for a job
@app.route('/view-applicants/<int:job_id>', methods=['GET'])
def view_applicants(job_id):
    conn = get_db_connection()
    if conn:
        job = conn.execute('SELECT * FROM job_postings WHERE id = ?', (job_id,)).fetchone()
        applicants = conn.execute('SELECT * FROM applicants WHERE job_id = ?', (job_id,)).fetchall()
        conn.close()
        if job:
            return render_template('view_applicants.html', job=job, applicants=applicants)
    flash('Failed to load applicants.')
    return redirect(url_for('index'))

# Route: Apply for a job
@app.route('/apply/<int:job_id>', methods=['GET', 'POST'])
def apply(job_id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        resume = request.form['resume']
        
        if not name or not email or not resume:
            flash('All fields are required.')
            return redirect(url_for('apply', job_id=job_id))
        
        conn = get_db_connection()
        if conn:
            conn.execute(
                'INSERT INTO applicants (job_id, name, email, resume) VALUES (?, ?, ?, ?)',
                (job_id, name, email, resume)
            )
            conn.commit()
            conn.close()
            flash('Application submitted successfully!')
            return redirect(url_for('index'))
        flash('Failed to submit application. Please try again.')
        return redirect(url_for('apply', job_id=job_id))
    conn = get_db_connection()
    if conn:
        job = conn.execute('SELECT * FROM job_postings WHERE id = ?', (job_id,)).fetchone()
        conn.close()
        if job:
            return render_template('apply.html', job=job)
    flash('Job not found.')
    return redirect(url_for('index'))

# Endpoint: API to fetch job postings (JSON format)
@app.route('/api/jobs', methods=['GET'])
def api_jobs():
    conn = get_db_connection()
    if conn:
        jobs = conn.execute('SELECT * FROM job_postings').fetchall()
        conn.close()
        return jsonify([dict(job) for job in jobs])
    return jsonify({'error': 'Failed to fetch jobs.'}), 500

# Initialize the database
def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        conn.execute('''
            CREATE TABLE job_postings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                company TEXT NOT NULL
            )
        ''')
        conn.execute('''
            CREATE TABLE applicants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                resume TEXT NOT NULL,
                FOREIGN KEY (job_id) REFERENCES job_postings (id)
            )
        ''')
        conn.commit()
        conn.close()
        print("Database initialized.")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```

### HTML Templates
Save the following templates in a `templates` folder.

#### `index.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Job Postings</title>
</head>
<body>
    <h1>Job Postings</h1>
    <a href="/post-job">Post a New Job</a>
    <ul>
        {% for job in jobs %}
        <li>
            <h2>{{ job.title }}</h2>
            <p>{{ job.description }}</p>
            <p><strong>Company:</strong> {{ job.company }}</p>
            <a href="/apply/{{ job.id }}">Apply</a>
            <a href="/view-applicants/{{ job.id }}">View Applicants</a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `post_job.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Post a Job</title>
</head>
<body>
    <h1>Post a New Job</h1>
    <form method="POST" action="/post-job">
        <label>Title: <input type="text" name="title" required></label><br>
        <label>Description: <textarea name="description" required></textarea></label><br>
        <label>Company: <input type="text" name="company" required></label><br>
        <button type="submit">Post Job</button>
    </form>
</body>
</html>
```

#### `apply.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Apply for {{ job.title }}</title>
</head>
<body>
    <h1>Apply for {{ job.title }}</h1>
    <form method="POST" action="/apply/{{ job.id }}">
        <label>Name: <input type="text" name="name" required></label><br>
        <label>Email: <input type="email" name="email" required></label><br>
        <label>Resume: <textarea name="resume" required></textarea></label><br>
        <button type="submit">Submit Application</button>
    </form>
</body>
</html>
```

#### `view_applicants.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Applicants for {{ job.title }}</title>
</head>
<body>
    <h1>Applicants for {{ job.title }}</h1>
    <ul>
        {% for applicant in applicants %}
        <li>
            <p><strong>Name:</strong> {{ applicant.name }}</p>
            <p><strong>Email:</strong> {{ applicant.email }}</p>
            <p><strong>Resume:</strong> {{ applicant.resume }}</p>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Notes
- This is a basic implementation. For production, additional security measures (e.g., validating and sanitizing user input, using environment variables for secrets) should be applied.
- Styles (CSS) can be added for better appearance.
