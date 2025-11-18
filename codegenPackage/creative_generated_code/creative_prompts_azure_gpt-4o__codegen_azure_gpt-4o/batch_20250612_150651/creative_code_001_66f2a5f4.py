"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notclosn.top
Prompt: Recommend APIs or libraries for creating a web-based personal branding portfolio, including tools for integrating client testimonials and project showcases, as outlined in the КарьераОнлайн module on building a personal brand.
Generated: DETERMINISTIC_66f2a5f4a0b39df2
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a Python example using Flask, SQLite, and Bootstrap for creating a web-based personal branding portfolio. It includes features for integrating client testimonials and project showcases:

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# Database file path
DATABASE = 'portfolio.db'

# Ensure database exists and create tables if needed
def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Create testimonials table
        cursor.execute('''
            CREATE TABLE testimonials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                testimonial TEXT NOT NULL
            )
        ''')

        # Create projects table
        cursor.execute('''
            CREATE TABLE projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                link TEXT
            )
        ''')

        conn.commit()
        conn.close()

# Home route displaying portfolio information
@app.route('/')
def home():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Fetch testimonials and projects
    cursor.execute('SELECT name, testimonial FROM testimonials')
    testimonials = cursor.fetchall()

    cursor.execute('SELECT title, description, link FROM projects')
    projects = cursor.fetchall()
    
    conn.close()
    
    # Render the homepage template
    return render_template('index.html', testimonials=testimonials, projects=projects)

# Add testimonial route
@app.route('/add_testimonial', methods=['GET', 'POST'])
def add_testimonial():
    if request.method == 'POST':
        name = request.form['name']
        testimonial = request.form['testimonial']
        
        if not name or not testimonial:
            flash('Both name and testimonial are required!', 'error')
        else:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO testimonials (name, testimonial) VALUES (?, ?)', (name, testimonial))
            conn.commit()
            conn.close()
            flash('Testimonial added successfully!', 'success')
            return redirect(url_for('home'))
    
    # Render form for adding testimonial
    return render_template('add_testimonial.html')

# Add project route
@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        link = request.form['link']
        
        if not title or not description:
            flash('Both title and description are required!', 'error')
        else:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO projects (title, description, link) VALUES (?, ?, ?)', (title, description, link))
            conn.commit()
            conn.close()
            flash('Project added successfully!', 'success')
            return redirect(url_for('home'))
    
    # Render form for adding project
    return render_template('add_project.html')

# Error handling for 404
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Main application entry point
if __name__ == '__main__':
    init_db()  # Initialize database if needed
    app.run(debug=True)
```

### Templates:
1. Create an `index.html` for the homepage showcasing testimonials and projects.
2. Create an `add_testimonial.html` for adding testimonials.
3. Create an `add_project.html` for adding projects.
4. Create a `404.html` for handling page not found errors.

### Folder Structure:
```
portfolio/
├── portfolio.db
├── app.py
├── templates/
│   ├── index.html
│   ├── add_testimonial.html
│   ├── add_project.html
│   ├── 404.html
└── static/
    └── css/
        └── styles.css
```

### Notes:
- Use Bootstrap for styling in the HTML templates (`index.html`, etc.).
- Include proper input validation in the HTML forms.
- Replace `your_secret_key` with a secure key for production use.
