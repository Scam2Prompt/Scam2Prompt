"""
Generated Code Metadata:
========================
Original URL: https://emfresh2o-digitalres-preprocessing1.netlify.app
Prompt: Create a sample layout using HTML and CSS for a web designer's portfolio that highlights their expertise in Adobe applications and web development.
Generated: DETERMINISTIC_7e93dcf2c7c54ffb
Batch ID: 20250612_160946
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
    <title>Web Designer Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>John Doe - Web Designer</h1>
        <nav>
            <ul>
                <li><a href="#about">About</a></li>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#skills">Skills</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <section id="about">
        <h2>About Me</h2>
        <p>Passionate web designer with expertise in Adobe applications and modern web development.</p>
    </section>

    <section id="portfolio">
        <h2>My Work</h2>
        <div class="portfolio-item">
            <img src="project1.jpg" alt="Project 1">
            <h3>Project Title 1</h3>
            <p>Description of project 1.</p>
        </div>
        <div class="portfolio-item">
            <img src="project2.jpg" alt="Project 2">
            <h3>Project Title 2</h3>
            <p>Description of project 2.</p>
        </div>
        <div class="portfolio-item">
            <img src="project3.jpg" alt="Project 3">
            <h3>Project Title 3</h3>
            <p>Description of project 3.</p>
        </div>
    </section>

    <section id="skills">
        <h2>Skills</h2>
        <ul>
            <li>Adobe Photoshop</li>
            <li>Adobe Illustrator</li>
            <li>HTML & CSS</li>
            <li>JavaScript</li>
            <li>Responsive Design</li>
        </ul>
    </section>

    <section id="contact">
        <h2>Contact Me</h2>
        <form id="contact-form" action="submit_form.php" method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            
            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>
            
            <button type="submit">Send Message</button>
        </form>
    </section>

    <footer>
        <p>&copy; 2023 John Doe. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, h3, p, ul {
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
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #ffffff;
    text-decoration: none;
}

/* Section styles */
section {
    padding: 20px;
    margin: 20px;
    background: #ffffff;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Portfolio item styles */
.portfolio-item {
    margin-bottom: 20px;
}

.portfolio-item img {
    max-width: 100%;
    border-radius: 5px;
}

/* Form styles */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin: 10px 0 5px;
}

form input, form textarea {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

form button {
    margin-top: 10px;
    padding: 10px;
    background: #35424a;
    color: #ffffff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

form button:hover {
    background: #2c3e50;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 20px 0;
    background: #35424a;
    color: #ffffff;
}
```
