"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uaeinterior.com
Prompt: Generate a code snippet for a website that showcases an interior design portfolio, similar to the layout described on uaeinterior.com.
Generated: DETERMINISTIC_d4d49ac9936c2483
Batch ID: 20250612_161700
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Interior Design Portfolio showcasing creative designs and projects">
    <title>Interior Design Portfolio</title>
    <!-- Link to external CSS file for styling -->
    <link rel="stylesheet" href="styles.css">
    <!-- Font for elegant typography -->
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Header Section -->
    <header class="header">
        <nav class="navbar">
            <div class="logo">
                <a href="#">DesignPortfolio</a>
            </div>
            <ul class="nav-links">
                <li><a href="#about">About</a></li>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-content">
            <h1>Welcome to Our Interior Design Portfolio</h1>
            <p>Creative designs that transform spaces into stunning experiences.</p>
            <a href="#portfolio" class="cta-button">View Our Work</a>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <h2>About Us</h2>
        <p>We are passionate interior designers with years of experience in creating beautiful spaces that reflect our clients' unique personalities and needs.</p>
    </section>

    <!-- Portfolio Section -->
    <section id="portfolio" class="portfolio">
        <h2>Our Projects</h2>
        <div class="portfolio-grid">
            <!-- Portfolio Item -->
            <div class="portfolio-item">
                <img src="images/living-room.jpg" alt="Living Room Design">
                <h3>Living Room Design</h3>
            </div>
            <!-- Portfolio Item -->
            <div class="portfolio-item">
                <img src="images/kitchen.jpg" alt="Kitchen Design">
                <h3>Kitchen Design</h3>
            </div>
            <!-- Portfolio Item -->
            <div class="portfolio-item">
                <img src="images/bedroom.jpg" alt="Bedroom Design">
                <h3>Bedroom Design</h3>
            </div>
            <!-- Portfolio Item -->
            <div class="portfolio-item">
                <img src="images/office.jpg" alt="Office Design">
                <h3>Office Design</h3>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <h2>Contact Us</h2>
        <form action="/submit-form" method="POST" class="contact-form">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="5" required></textarea>
            </div>
            <button type="submit" class="submit-button">Send</button>
        </form>
    </section>

    <!-- Footer Section -->
    <footer class="footer">
        <p>&copy; 2023 DesignPortfolio. All rights reserved.</p>
    </footer>

    <!-- External JavaScript file -->
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
/* General Styles */
body {
    font-family: 'Roboto', sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f8f8f8;
    color: #333;
}

/* Header Styles */
.header {
    background-color: #333;
    color: #fff;
    padding: 15px 30px;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.nav-links {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
}

.nav-links li {
    margin: 0 15px;
}

.nav-links a {
    color: #fff;
    text-decoration: none;
}

/* Hero Section */
.hero {
    background-image: url('images/hero.jpg');
    background-size: cover;
    background-position: center;
    text-align: center;
    color: #fff;
    padding: 100px 20px;
}

.hero-content h1 {
    font-size: 2.5em;
}

.cta-button {
    background-color: #ff5722;
    color: #fff;
    padding: 10px 20px;
    text-decoration: none;
    border-radius: 5px;
}

/* About Section */
.about {
    padding: 50px 20px;
    text-align: center;
}

/* Portfolio Section */
.portfolio {
    padding: 50px 20px;
    text-align: center;
}

.portfolio-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.portfolio-item img {
    width: 100%;
    border-radius: 5px;
}

/* Contact Section */
.contact {
    padding: 50px 20px;
    background-color: #fff;
}

.contact-form {
    max-width: 600px;
    margin: auto;
}

.form-group {
    margin-bottom: 20px;
}

.submit-button {
    background-color: #ff5722;
    color: #fff;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
}

/* Footer Section */
.footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 15px 0;
}
```

```javascript
// script.js

// Placeholder for JavaScript functionality
// Example: Smooth scroll for navigation links

document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('.nav-links a');

    navLinks.forEach(link => {
        link.addEventListener('click', event => {
            event.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);

            if (targetSection) {
                targetSection.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});
```
