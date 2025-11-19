"""
Generated Code Metadata:
========================
Original URL: https://jkpcrnica.rs
Prompt: Generate a Python script to create a simple website structure similar to jkpcrnica.rs, including sections for ПОЧЕТНА, О НАМА, and КОНТАКТ.
Generated: DETERMINISTIC_427effd7b01436e5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define routes for the website
@app.route('/')
def home():
    """
    Route for the home page (ПОЧЕТНА).
    """
    return render_template('home.html')

@app.route('/about')
def about():
    """
    Route for the about page (О НАМА).
    """
    return render_template('about.html')

@app.route('/contact')
def contact():
    """
    Route for the contact page (КОНТАКТ).
    """
    return render_template('contact.html')

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error handler for 404 errors.
    """
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

# Directory structure:
# templates/
# ├── home.html
# ├── about.html
# ├── contact.html
# └── 404.html

# Example HTML templates:
# home.html:
# <!DOCTYPE html>
# <html lang="sr">
# <head>
#     <meta charset="UTF-8">
#     <title>ПОЧЕТНА</title>
# </head>
# <body>
#     <h1>Добродошли на нашу веб страницу!</h1>
#     <nav>
#         <a href="/">ПОЧЕТНА</a> | <a href="/about">О НАМА</a> | <a href="/contact">КОНТАКТ</a>
#     </nav>
# </body>
# </html>

# about.html:
# <!DOCTYPE html>
# <html lang="sr">
# <head>
#     <meta charset="UTF-8">
#     <title>О НАМА</title>
# </head>
# <body>
#     <h1>О НАМА</h1>
#     <p>Ово је страница о нама.</p>
#     <nav>
#         <a href="/">ПОЧЕТНА</a> | <a href="/about">О НАМА</a> | <a href="/contact">КОНТАКТ</a>
#     </nav>
# </body>
# </html>

# contact.html:
# <!DOCTYPE html>
# <html lang="sr">
# <head>
#     <meta charset="UTF-8">
#     <title>КОНТАКТ</title>
# </head>
# <body>
#     <h1>КОНТАКТ</h1>
#     <p>Контактирајте нас путем е-поште или телефона.</p>
#     <nav>
#         <a href="/">ПОЧЕТНА</a> | <a href="/about">О НАМА</a> | <a href="/contact">КОНТАКТ</a>
#     </nav>
# </body>
# </html>

# 404.html:
# <!DOCTYPE html>
# <html lang="sr">
# <head>
#     <meta charset="UTF-8">
#     <title>Грешка 404</title>
# </head>
# <body>
#     <h1>Страница није пронађена</h1>
#     <p>Извините, страница коју тражите не постоји.</p>
#     <nav>
#         <a href="/">ПОЧЕТНА</a> | <a href="/about">О НАМА</a> | <a href="/contact">КОНТАКТ</a>
#     </nav>
# </body>
# </html>
```
