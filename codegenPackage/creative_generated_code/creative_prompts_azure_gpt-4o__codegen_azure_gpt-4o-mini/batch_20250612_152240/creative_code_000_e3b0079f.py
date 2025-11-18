"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emfresh2o-digitalres-preprocessing1.netlify.app
Prompt: Write a code snippet using HTML5 and CSS to create a personal portfolio webpage similar to the structure described on EMFresh2o Digital Resume, including sections for "Home," "About," "Portfolio," and "Contact."
Generated: DETERMINISTIC_e3b0079f779a09ce
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file -->
</head>
<body>
    <header>
        <h1>My Portfolio</h1>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <section id="home">
        <h2>Welcome to My Portfolio</h2>
        <p>This is a brief introduction to my work and skills.</p>
    </section>

    <section id="about">
        <h2>About Me</h2>
        <p>Here you will find information about my background, experience, and skills.</p>
    </section>

    <section id="portfolio">
        <h2>My Work</h2>
        <div class="portfolio-item">
            <h3>Project Title 1</h3>
            <p>Description of project 1.</p>
        </div>
        <div class="portfolio-item">
            <h3>Project Title 2</h3>
            <p>Description of project 2.</p>
        </div>
        <!-- Add more portfolio items as needed -->
    </section>

    <section id="contact">
        <h2>Contact Me</h2>
        <form action="submit_form.php" method="POST"> <!-- Form submission handler -->
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
        <p>&copy; 2023 My Name. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, h3, p {
    margin: 0;
    padding: 0;
}

/* Set a basic font and background color */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styles */
header {
    background: #333;
    color: #fff;
    padding: 10px 0;
}

header h1 {
    text-align: center;
}

nav ul {
    list-style: none;
    padding: 0;
    text-align: center;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav a {
    color: #fff;
    text-decoration: none;
}

/* Section styles */
section {
    padding: 20px;
    margin: 20px 0;
    background: #fff;
    border-radius: 5px;
}

.portfolio-item {
    margin-bottom: 15px;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #333;
    color: #fff;
}
```
