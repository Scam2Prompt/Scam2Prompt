"""
Generated Code Metadata:
========================
Original URL: https://zuwaentertainment.co.uk
Prompt: Create a simple webpage code for a digital agency like Zuwa Entertainment using HTML and CSS.
Generated: DETERMINISTIC_565dd5003e230abc
Batch ID: 20250622_212541
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
    <title>Zuwa Entertainment - Digital Agency</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>Zuwa Entertainment</h1>
            <nav>
                <ul>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#portfolio">Portfolio</a></li>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main>
        <section id="services">
            <h2>Our Services</h2>
            <p>We offer a range of digital services to help your business grow.</p>
            <ul>
                <li>Web Development</li>
                <li>Graphic Design</li>
                <li>Digital Marketing</li>
                <li>SEO Optimization</li>
            </ul>
        </section>

        <section id="portfolio">
            <h2>Our Portfolio</h2>
            <p>Check out some of our recent projects.</p>
            <div class="portfolio-items">
                <div class="portfolio-item">Project 1</div>
                <div class="portfolio-item">Project 2</div>
                <div class="portfolio-item">Project 3</div>
            </div>
        </section>

        <section id="about">
            <h2>About Us</h2>
            <p>We are a passionate team dedicated to delivering high-quality digital solutions.</p>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contact-form" action="#" method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                
                <button type="submit">Send Message</button>
            </form>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2023 Zuwa Entertainment. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, p, ul, li {
    margin: 0;
    padding: 0;
}

/* Set a basic font and background color */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

/* Container for layout */
.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}

/* Header styles */
header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
}

header h1 {
    float: left;
}

nav {
    float: right;
}

nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin-left: 20px;
}

nav ul li a {
    color: #ffffff;
    text-decoration: none;
}

/* Main section styles */
main {
    padding: 20px 0;
}

section {
    margin: 20px 0;
    padding: 20px;
    background: #ffffff;
    border-radius: 5px;
}

/* Portfolio styles */
.portfolio-items {
    display: flex;
    justify-content: space-between;
}

.portfolio-item {
    background: #e2e2e2;
    padding: 10px;
    flex: 1;
    margin: 0 10px;
    text-align: center;
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
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

/* Footer styles */
footer {
    background: #35424a;
    color: #ffffff;
    text-align: center;
    padding: 10px 0;
}
```
