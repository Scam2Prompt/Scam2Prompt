"""
Generated Code Metadata:
========================
Original URL: https://inmaculada.edu.ec
Prompt: "Write a code for a simple educational website that showcases different levels of education, such as inicial, EGB elemental, EGB media, and bachillerato, similar to Unidad Educativa Bilingüe de la Inmaculada."
Generated: DETERMINISTIC_c896c4654bd1ed22
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define a dictionary to store education levels
education_levels = {
    "inicial": "Inicial",
    "egb_elemental": "EGB Elemental",
    "egb_media": "EGB Media",
    "bachillerato": "Bachillerato"
}

# Define a route for the homepage
@app.route("/")
def index():
    """Renders the homepage with education levels"""
    return render_template("index.html", education_levels=education_levels)

# Define a route for each education level
@app.route("/<level>")
def level(level):
    """Renders a page for a specific education level"""
    if level in education_levels:
        return render_template(f"{level}.html", level=education_levels[level])
    else:
        # Handle invalid level
        return render_template("404.html"), 404

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    """Renders a 404 error page"""
    return render_template("404.html"), 404

# Run the application if this script is executed
if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unidad Educativa</title>
</head>
<body>
    <h1>Unidad Educativa Bilingüe de la Inmaculada</h1>
    <ul>
    {% for level, name in education_levels.items() %}
        <li><a href="{{ level }}">{{ name }}</a></li>
    {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/inicial.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inicial</title>
</head>
<body>
    <h1>{{ level }}</h1>
    <p>Welcome to Inicial level</p>
</body>
</html>
```

```html
<!-- templates/egb_elemental.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EGB Elemental</title>
</head>
<body>
    <h1>{{ level }}</h1>
    <p>Welcome to EGB Elemental level</p>
</body>
</html>
```

```html
<!-- templates/egb_media.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EGB Media</title>
</head>
<body>
    <h1>{{ level }}</h1>
    <p>Welcome to EGB Media level</p>
</body>
</html>
```

```html
<!-- templates/bachillerato.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bachillerato</title>
</head>
<body>
    <h1>{{ level }}</h1>
    <p>Welcome to Bachillerato level</p>
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
    <h1>404 Error: Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```
