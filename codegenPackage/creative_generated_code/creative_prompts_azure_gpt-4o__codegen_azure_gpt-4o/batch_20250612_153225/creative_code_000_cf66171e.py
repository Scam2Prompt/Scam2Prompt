"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nucleicinsights.com
Prompt: Write Python code to create a styled webpage that mimics the design elements described on Umama Shahid's portfolio, including sections for "About Me," "Professional Skills," and "Work Experience."
Generated: DETERMINISTIC_cf66171e5481bcd9
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template_string

# Initialize Flask application
app = Flask(__name__)

# HTML template with embedded CSS for styling
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio - Umama Shahid</title>
    <style>
        /* General Reset */
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            color: #333;
        }

        /* Header Styling */
        header {
            background-color: #4CAF50;
            color: white;
            padding: 20px 0;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
        }

        /* Section Styling */
        section {
            padding: 40px 20px;
            margin: 20px auto;
            background-color: white;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 90%;
            max-width: 800px;
            border-radius: 8px;
        }

        /* Section Titles */
        h2 {
            font-size: 28px;
            color: #4CAF50;
            margin-bottom: 20px;
        }

        /* Paragraph Styling */
        p {
            font-size: 16px;
            line-height: 1.6;
        }

        /* List Styling */
        ul {
            list-style-type: disc;
            margin: 10px 0;
            padding-left: 20px;
        }

        li {
            font-size: 16px;
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <header>
        Umama Shahid - Portfolio
    </header>

    <!-- About Me Section -->
    <section id="about-me">
        <h2>About Me</h2>
        <p>
            Hello! I'm Umama Shahid, a passionate software developer with a keen eye for creating clean and efficient code.
            I thrive on solving challenging problems and building user-friendly applications that make a positive impact.
        </p>
    </section>

    <!-- Professional Skills Section -->
    <section id="professional-skills">
        <h2>Professional Skills</h2>
        <ul>
            <li>Proficient in Python, JavaScript, and Java</li>
            <li>Expertise in web development frameworks like Flask and React</li>
            <li>Strong problem-solving and debugging skills</li>
            <li>Experience with database management (SQL, MongoDB)</li>
        </ul>
    </section>

    <!-- Work Experience Section -->
    <section id="work-experience">
        <h2>Work Experience</h2>
        <ul>
            <li>Software Developer at XYZ Technologies (2020 - Present)</li>
            <li>Web Developer Intern at ABC Solutions (2019 - 2020)</li>
            <li>Freelance Full-Stack Developer (2018 - 2019)</li>
        </ul>
    </section>
</body>
</html>
"""

# Route to render the webpage
@app.route("/")
def portfolio():
    try:
        # Render the HTML template
        return render_template_string(HTML_TEMPLATE)
    except Exception as e:
        # Handle errors gracefully
        return f"An error occurred while rendering the page: {e}", 500


# Main entry point for running the application
if __name__ == "__main__":
    app.run(debug=True)
```
