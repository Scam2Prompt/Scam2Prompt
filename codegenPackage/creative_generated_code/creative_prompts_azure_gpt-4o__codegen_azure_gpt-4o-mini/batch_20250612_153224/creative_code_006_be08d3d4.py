"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skyline-ia.com
Prompt: Suggest tools or frameworks for building a multilingual tourism website, ensuring support for languages like English, French, Turkish, German, and Italian, as seen on Skyline International Agent's site.
Generated: DETERMINISTIC_be08d3d4eeef66a9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# multilingual_tourism_website.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_babel import Babel, _

app = Flask(__name__)

# Configuration for Flask-Babel
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

babel = Babel(app)

# Supported languages
SUPPORTED_LANGUAGES = ['en', 'fr', 'tr', 'de', 'it']

@babel.localeselector
def get_locale():
    # Get the best matching language based on the user's preferences
    return request.accept_languages.best_match(SUPPORTED_LANGUAGES)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Basic validation
        if not name or not email or not message:
            flash(_('Please fill in all fields.'))
            return redirect(url_for('contact'))
        
        # Process the contact form (e.g., save to database or send an email)
        # This is a placeholder for actual processing logic
        flash(_('Your message has been sent!'))
        return redirect(url_for('home'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    # Run the app with debug mode off for production
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### Directory Structure
```
/your_project
│
├── multilingual_tourism_website.py
│
├── templates
│   ├── index.html
│   ├── services.html
│   └── contact.html
│
└── translations
    ├── fr
    │   └── LC_MESSAGES
    │       └── messages.po
    ├── tr
    │   └── LC_MESSAGES
    │       └── messages.po
    ├── de
    │   └── LC_MESSAGES
    │       └── messages.po
    └── it
        └── LC_MESSAGES
            └── messages.po
```

### Notes:
- Ensure to install Flask and Flask-Babel via pip:
  ```bash
  pip install Flask Flask-Babel
  ```
- You will need to create the necessary HTML templates (`index.html`, `services.html`, `contact.html`) and PO files for translations for different languages.
- The contact form currently includes basic error handling for empty fields. Adjust as necessary for your application's needs.
- This code is set to run on port 5000. You can change this based on your deployment configuration.
