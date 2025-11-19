"""
Generated Code Metadata:
========================
Original URL: https://akaan.com.tr
Prompt: Generate a code snippet for a mobile-friendly website layout using HTML and CSS, inspired by Akaan's web design services.
Generated: DETERMINISTIC_1bc59ce0bfe1c62d
Batch ID: 20250612_162203
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
    <title>Akaan's Web Design Services</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Akaan's Web Design Services</h1>
        <nav>
            <ul>
                <li><a href="#services">Services</a></li>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="services">
            <h2>Our Services</h2>
            <div class="service">
                <h3>Web Design</h3>
                <p>Creating beautiful and functional websites tailored to your needs.</p>
            </div>
            <div class="service">
                <h3>SEO Optimization</h3>
                <p>Improving your website's visibility on search engines.</p>
            </div>
            <div class="service">
                <h3>Responsive Design</h3>
                <p>Ensuring your website looks great on all devices.</p>
            </div>
        </section>

        <section id="portfolio">
            <h2>Our Portfolio</h2>
            <div class="portfolio-item">
                <img src="project1.jpg" alt="Project 1">
                <h3>Project Title 1</h3>
                <p>Brief description of the project.</p>
            </div>
            <div class="portfolio-item">
                <img src="project2.jpg" alt="Project 2">
                <h3>Project Title 2</h3>
                <p>Brief description of the project.</p>
            </div>
            <div class="portfolio-item">
                <img src="project3.jpg" alt="Project 3">
                <h3>Project Title 3</h3>
                <p>Brief description of the project.</p>
            </div>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
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
    </main>

    <footer>
        <p>&copy; 2023 Akaan's Web Design Services. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, h3, p, ul, li {
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
    background: #007BFF;
    color: white;
    padding: 20px;
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
    color: white;
    text-decoration: none;
}

/* Main content styles */
main {
    padding: 20px;
}

/* Section styles */
section {
    margin-bottom: 40px;
}

.service, .portfolio-item {
    background: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 15px;
    margin: 10px 0;
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
    background: #007BFF;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

form button:hover {
    background: #0056b3;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 20px;
    background: #333;
    color: white;
}
```
