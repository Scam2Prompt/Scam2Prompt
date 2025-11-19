"""
Generated Code Metadata:
========================
Original URL: https://nucleicinsights.com
Prompt: Write Python code to create a styled webpage that mimics the design elements described on Umama Shahid's portfolio, including sections for "About Me," "Professional Skills," and "Work Experience."
Generated: DETERMINISTIC_cf66171e5481bcd9
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import webbrowser
from jinja2 import Template

# Define HTML template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Umama Shahid Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#about">About Me</a></li>
                <li><a href="#skills">Professional Skills</a></li>
                <li><a href="#experience">Work Experience</a></li>
            </ul>
        </nav>
    </header>

    <!-- About Me Section -->
    <section id="about">
        <h1>About Me</h1>
        <p>Highly motivated and detail-oriented software developer with a passion for delivering high-quality solutions.</p>
    </section>

    <!-- Professional Skills Section -->
    <section id="skills">
        <h1>Professional Skills</h1>
        <ul>
            <li>Programming languages: Python, Java, JavaScript</li>
            <li>Development frameworks: Flask, Spring Boot, React</li>
            <li>Database management: MySQL, MongoDB</li>
        </ul>
    </section>

    <!-- Work Experience Section -->
    <section id="experience">
        <h1>Work Experience</h1>
        <ul>
            <li><b>Software Developer</b> - ABC Company (2020-Present)</li>
            <li><b>Junior Developer</b> - DEF Company (2018-2020)</li>
        </ul>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2024 Umama Shahid</p>
    </footer>
</body>
</html>
"""

# Define CSS template
css_template = """
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

header nav ul li {
    display: inline-block;
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

section {
    background-color: #f7f7f7;
    padding: 2em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    margin-top: 0;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
"""

# Write HTML and CSS to files
with open("index.html", "w") as f:
    f.write(html_template)

with open("styles.css", "w") as f:
    f.write(css_template)

# Open webpage in default browser
webbrowser.open("index.html")
```
