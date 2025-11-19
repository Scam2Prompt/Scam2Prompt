"""
Generated Code Metadata:
========================
Original URL: https://alpha-digitalsolutions.com
Prompt: Create a sample HTML and CSS layout for a graphic design portfolio that reflects the innovative design concepts used by Alpha Digital Solutions.
Generated: DETERMINISTIC_e3af8e1f751941a4
Batch ID: 20250612_162051
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
    <meta name="description" content="Graphic Design Portfolio for Alpha Digital Solutions">
    <title>Alpha Digital Solutions - Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header class="header">
        <div class="container">
            <h1 class="logo">Alpha Digital Solutions</h1>
            <nav class="nav">
                <ul>
                    <li><a href="#about">About</a></li>
                    <li><a href="#portfolio">Portfolio</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h2>Innovative Design Concepts</h2>
            <p>Transforming ideas into stunning visuals.</p>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <h2>About Us</h2>
            <p>Alpha Digital Solutions specializes in creating cutting-edge graphic designs that captivate and inspire. Our team of experts is dedicated to delivering innovative solutions tailored to your needs.</p>
        </div>
    </section>

    <!-- Portfolio Section -->
    <section id="portfolio" class="portfolio">
        <div class="container">
            <h2>Our Work</h2>
            <div class="portfolio-grid">
                <div class="portfolio-item">
                    <img src="project1.jpg" alt="Project 1">
                    <h3>Project 1</h3>
                </div>
                <div class="portfolio-item">
                    <img src="project2.jpg" alt="Project 2">
                    <h3>Project 2</h3>
                </div>
                <div class="portfolio-item">
                    <img src="project3.jpg" alt="Project 3">
                    <h3>Project 3</h3>
                </div>
                <div class="portfolio-item">
                    <img src="project4.jpg" alt="Project 4">
                    <h3>Project 4</h3>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <h2>Contact Us</h2>
            <form action="#" method="POST" class="contact-form">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message</label>
                <textarea id="message" name="message" rows="5" required></textarea>
                
                <button type="submit">Send Message</button>
            </form>
        </div>
    </section>

    <!-- Footer Section -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2023 Alpha Digital Solutions. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Container */
.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
}

/* Header */
.header {
    background: #333;
    color: #fff;
    padding: 1rem 0;
}

.header .logo {
    font-size: 1.5rem;
    font-weight: bold;
}

.nav ul {
    list-style: none;
    display: flex;
    justify-content: flex-end;
}

.nav ul li {
    margin-left: 20px;
}

.nav ul li a {
    color: #fff;
    text-decoration: none;
    font-weight: bold;
}

.nav ul li a:hover {
    text-decoration: underline;
}

/* Hero Section */
.hero {
    background: url('hero-bg.jpg') no-repeat center center/cover;
    color: #fff;
    text-align: center;
    padding: 5rem 0;
}

.hero h2 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

.hero p {
    font-size: 1.2rem;
}

/* About Section */
.about {
    padding: 2rem 0;
    background: #fff;
    text-align: center;
}

.about h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
}

/* Portfolio Section */
.portfolio {
    padding: 2rem 0;
    background: #f4f4f4;
}

.portfolio h2 {
    text-align: center;
    margin-bottom: 2rem;
}

.portfolio-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
}

.portfolio-item {
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    overflow: hidden;
    text-align: center;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.portfolio-item img {
    width: 100%;
    height: auto;
}

.portfolio-item h3 {
    padding: 1rem;
    font-size: 1.2rem;
}

/* Contact Section */
.contact {
    padding: 2rem 0;
    background: #fff;
}

.contact h2 {
    text-align: center;
    margin-bottom: 1.5rem;
}

.contact-form {
    max-width: 600px;
    margin: 0 auto;
}

.contact-form label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
}

.contact-form input,
.contact-form textarea {
    width: 100%;
    padding: 0.5rem;
    margin-bottom: 1rem;
    border: 1px solid #ddd;
    border-radius: 5px;
}

.contact-form button {
    display: block;
    width: 100%;
    padding: 0.7rem;
    background: #333;
    color: #fff;
    border: none;
    border-radius: 5px;
    font-size: 1rem;
    cursor: pointer;
}

.contact-form button:hover {
    background: #555;
}

/* Footer */
.footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 1rem 0;
    margin-top: 2rem;
}
```
