"""
Generated Code Metadata:
========================
Original URL: https://okayvc.com
Prompt: "Create a simple website design using HTML and CSS that reflects Okay Visual Creations' user-friendly and aesthetically pleasing design principles."
Generated: DETERMINISTIC_d0191bb5d804ef26
Batch ID: 20250622_205411
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
    <title>Okay Visual Creations</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Okay Visual Creations</h1>
        <nav>
            <ul>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="about">
            <h2>About Us</h2>
            <p>At Okay Visual Creations, we believe in creating user-friendly and aesthetically pleasing designs that resonate with our clients' visions.</p>
        </section>

        <section id="services">
            <h2>Our Services</h2>
            <ul>
                <li>Web Design</li>
                <li>Graphic Design</li>
                <li>Branding</li>
                <li>Consultation</li>
            </ul>
        </section>

        <section id="portfolio">
            <h2>Our Portfolio</h2>
            <div class="portfolio-item">
                <img src="project1.jpg" alt="Project 1">
                <p>Project 1 Description</p>
            </div>
            <div class="portfolio-item">
                <img src="project2.jpg" alt="Project 2">
                <p>Project 2 Description</p>
            </div>
            <div class="portfolio-item">
                <img src="project3.jpg" alt="Project 3">
                <p>Project 3 Description</p>
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
        <p>&copy; 2023 Okay Visual Creations. All rights reserved.</p>
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

/* Header styles */
header {
    background: #007BFF;
    color: white;
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
    color: white;
    text-decoration: none;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Section styles */
section {
    margin-bottom: 40px;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Portfolio item styles */
.portfolio-item {
    margin-bottom: 20px;
}

.portfolio-item img {
    max-width: 100%;
    border-radius: 8px;
}

/* Form styles */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin-bottom: 5px;
}

form input, form textarea {
    margin-bottom: 15px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

form button {
    background: #007BFF;
    color: white;
    border: none;
    padding: 10px;
    border-radius: 4px;
    cursor: pointer;
}

form button:hover {
    background: #0056b3;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 20px 0;
    background: #007BFF;
    color: white;
}
```
