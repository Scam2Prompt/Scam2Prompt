"""
Generated Code Metadata:
========================
Original URL: https://collab.host
Prompt: Generate a sample code for a simple web page that showcases a UI designer's portfolio, including sections for projects, testimonials, and speaker bio, using HTML, CSS, and JavaScript.
Generated: DETERMINISTIC_9cdb40653ed58bf0
Batch ID: 20250622_212417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UI Designer Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Jane Doe - UI Designer</h1>
        <nav>
            <ul>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#testimonials">Testimonials</a></li>
                <li><a href="#bio">Bio</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="projects">
            <h2>Projects</h2>
            <div class="project">
                <h3>Project 1</h3>
                <p>Description of project 1.</p>
            </div>
            <div class="project">
                <h3>Project 2</h3>
                <p>Description of project 2.</p>
            </div>
            <div class="project">
                <h3>Project 3</h3>
                <p>Description of project 3.</p>
            </div>
        </section>

        <section id="testimonials">
            <h2>Testimonials</h2>
            <blockquote>
                <p>"Jane is an exceptional designer!" - Client A</p>
            </blockquote>
            <blockquote>
                <p>"Her work transformed our user experience." - Client B</p>
            </blockquote>
        </section>

        <section id="bio">
            <h2>Speaker Bio</h2>
            <p>Jane Doe is a UI designer with over 5 years of experience in creating user-friendly interfaces.</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Jane Doe. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, h3, p, blockquote {
    margin: 0;
    padding: 0;
}

/* Basic styling for the body */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styles */
header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
    text-align: center;
}

nav ul {
    list-style: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #ffffff;
    text-decoration: none;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Project styles */
.project {
    background: #ffffff;
    border: 1px solid #dddddd;
    margin: 10px 0;
    padding: 15px;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #35424a;
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

// This script can be expanded for future interactivity
document.addEventListener('DOMContentLoaded', () => {
    console.log("Document loaded and ready.");
    // Future JavaScript functionality can be added here
});
```
