"""
Generated Code Metadata:
========================
Original URL: https://digistrategy.in
Prompt: "Generate a homepage content for a digital agency that offers web design, development, and marketing services, including a brief about the team and their mission."
Generated: DETERMINISTIC_7d156f5485c866af
Batch ID: 20250622_210655
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
    <meta name="description" content="Digital agency specializing in web design, development, and marketing services.">
    <meta name="keywords" content="web design, web development, digital marketing, agency">
    <meta name="author" content="Your Digital Agency">
    <title>Your Digital Agency - Home</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file -->
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <h1>Your Digital Agency</h1>
            <p>Innovative solutions for web design, development, and marketing.</p>
        </div>
    </header>

    <!-- Navigation Bar -->
    <nav>
        <ul class="nav-menu">
            <li><a href="#services">Services</a></li>
            <li><a href="#about">About Us</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <!-- Main Content -->
    <main>
        <!-- Services Section -->
        <section id="services" class="services-section">
            <div class="container">
                <h2>Our Services</h2>
                <div class="service">
                    <h3>Web Design</h3>
                    <p>Crafting visually stunning and user-friendly designs tailored to your brand.</p>
                </div>
                <div class="service">
                    <h3>Web Development</h3>
                    <p>Building robust, scalable, and secure websites using the latest technologies.</p>
                </div>
                <div class="service">
                    <h3>Digital Marketing</h3>
                    <p>Driving growth through targeted campaigns and data-driven strategies.</p>
                </div>
            </div>
        </section>

        <!-- About Us Section -->
        <section id="about" class="about-section">
            <div class="container">
                <h2>About Us</h2>
                <p>We are a passionate team of designers, developers, and marketers dedicated to helping businesses succeed online.</p>
                <p><strong>Our Mission:</strong> To empower businesses with innovative digital solutions that drive results.</p>
            </div>
        </section>
    </main>

    <!-- Footer Section -->
    <footer>
        <div class="container">
            <p>&copy; 2023 Your Digital Agency. All rights reserved.</p>
            <p><a href="#contact">Contact Us</a> | <a href="#services">Our Services</a></p>
        </div>
    </footer>

    <!-- External JavaScript File -->
    <script src="scripts.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Styles */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Container */
.container {
    width: 80%;
    margin: 0 auto;
    max-width: 1200px;
}

/* Header */
header {
    background: #0073e6;
    color: #fff;
    padding: 20px 0;
    text-align: center;
}

header h1 {
    margin: 0;
    font-size: 2.5em;
}

header p {
    margin: 10px 0 0;
}

/* Navigation */
nav {
    background: #333;
    color: #fff;
}

.nav-menu {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    justify-content: center;
}

.nav-menu li {
    margin: 0 15px;
}

.nav-menu a {
    color: #fff;
    text-decoration: none;
    font-weight: bold;
}

.nav-menu a:hover {
    text-decoration: underline;
}

/* Services Section */
.services-section {
    padding: 20px 0;
    background: #fff;
}

.services-section h2 {
    text-align: center;
    margin-bottom: 20px;
}

.service {
    margin-bottom: 20px;
}

/* About Section */
.about-section {
    padding: 20px 0;
    background: #f1f1f1;
}

.about-section h2 {
    text-align: center;
    margin-bottom: 20px;
}

/* Footer */
footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
}

footer a {
    color: #0073e6;
    text-decoration: none;
}

footer a:hover {
    text-decoration: underline;
}
```

```javascript
// scripts.js

// Example JavaScript functionality for smooth scrolling
document.addEventListener('DOMContentLoaded', () => {
    const links = document.querySelectorAll('nav a');

    links.forEach(link => {
        link.addEventListener('click', event => {
            event.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});
```
