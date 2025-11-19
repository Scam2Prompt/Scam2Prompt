"""
Generated Code Metadata:
========================
Original URL: https://presale-app.com
Prompt: Recommend a simple web development setup for a presale application, including directory structure and initial webpage content.
Generated: DETERMINISTIC_3fa001c33ead4990
Batch ID: 20250622_211952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# File: app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- File: templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Presale Application</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <h1>Welcome to Our Presale</h1>
    </header>
    <main>
        <section>
            <p>Sign up to get early access to our product!</p>
            <form action="/submit" method="POST">
                <input type="email" name="email" placeholder="Enter your email" required>
                <button type="submit">Notify Me</button>
            </form>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Presale Application. All rights reserved.</p>
    </footer>
</body>
</html>
```

```html
<!-- File: templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <h1>404 - Page Not Found</h1>
    </header>
    <main>
        <p>The page you are looking for does not exist.</p>
        <a href="/">Return to Home</a>
    </main>
</body>
</html>
```

```css
/* File: static/css/style.css */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    color: #333;
}

header {
    background: #f4f4f4;
    padding: 1rem;
    text-align: center;
}

main {
    padding: 2rem;
    text-align: center;
}

input[type="email"] {
    padding: 0.5rem;
    width: 300px;
    margin-right: 0.5rem;
}

button {
    padding: 0.5rem 1rem;
    background: #333;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background: #555;
}

footer {
    text-align: center;
    padding: 1rem;
    background: #f4f4f4;
    position: fixed;
    bottom: 0;
    width: 100%;
}
```

```text
# Directory Structure
/presale-app
├── app.py
├── /templates
│   ├── index.html
│   └── 404.html
└── /static
    └── /css
        └── style.css
```

```python
# File: requirements.txt
Flask==2.0.1
```
