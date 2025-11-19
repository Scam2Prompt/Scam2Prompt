"""
Generated Code Metadata:
========================
Original URL: https://meredithgastonmasnata.com
Prompt: Generate a Python script to create a basic website structure similar to Meredith Gaston Masnata's, featuring sections for Books, Art, Wellbeing, Speaking, Workshops, and Photography.
Generated: DETERMINISTIC_89e86637bf988a51
Batch ID: 20250622_205211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template

app = Flask(__name__)

# Define routes for each section of the website
@app.route('/')
def home():
    return render_template('index.html')  # Home page template

@app.route('/books')
def books():
    return render_template('books.html')  # Books section template

@app.route('/art')
def art():
    return render_template('art.html')  # Art section template

@app.route('/wellbeing')
def wellbeing():
    return render_template('wellbeing.html')  # Wellbeing section template

@app.route('/speaking')
def speaking():
    return render_template('speaking.html')  # Speaking section template

@app.route('/workshops')
def workshops():
    return render_template('workshops.html')  # Workshops section template

@app.route('/photography')
def photography():
    return render_template('photography.html')  # Photography section template

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404  # Custom 404 error page

# Main entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for development; use debug=False in production
```

### Directory Structure:
To make this script work, ensure the following directory structure exists:
```
project/
│
├── app.py                # The script above
├── templates/            # HTML templates folder
│   ├── index.html        # Home page
│   ├── books.html        # Books section
│   ├── art.html          # Art section
│   ├── wellbeing.html    # Wellbeing section
│   ├── speaking.html     # Speaking section
│   ├── workshops.html    # Workshops section
│   ├── photography.html  # Photography section
│   ├── 404.html          # Custom 404 error page
```

### Notes:
- Replace the content of each HTML file with the appropriate design and content for the respective sections.
- Use `debug=False` in production to avoid exposing sensitive information in case of errors.
- Install Flask using `pip install flask` if not already installed.
