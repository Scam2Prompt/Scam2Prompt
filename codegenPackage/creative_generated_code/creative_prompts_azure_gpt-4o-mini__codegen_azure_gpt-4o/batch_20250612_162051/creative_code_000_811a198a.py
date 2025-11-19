"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://charosnavarro.com
Prompt: Generate a code snippet to create a photography portfolio website similar to Charos Navarro Fotografía.
Generated: DETERMINISTIC_811a198aad027c8c
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Raleway:wght@300;500;700&display=swap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Certainly! Here's a clean, production-ready code snippet for creating a photography portfolio website using HTML, CSS, and JavaScript.

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Photography Portfolio - Showcase your best work.">
    <meta name="author" content="Your Name">
    <title>Photography Portfolio</title>
    <!-- Link to external CSS -->
    <link rel="stylesheet" href="styles.css">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Raleway:wght@300;500;700&display=swap" rel="stylesheet">
</head>

<body>
    <!-- Header Section -->
    <header>
        <nav class="navbar">
            <div class="logo">
                <a href="#">Your Photography</a>
            </div>
            <ul class="nav-links">
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-text">
            <h1>Welcome to My Photography Portfolio</h1>
            <p>Capturing the world one photo at a time.</p>
        </div>
    </section>

    <!-- Portfolio Section -->
    <section id="portfolio" class="portfolio">
        <h2>Portfolio</h2>
        <div class="gallery">
            <!-- Gallery Images -->
            <div class="gallery-item">
                <img src="images/photo1.jpg" alt="Photo 1">
                <p>Photo Description</p>
            </div>
            <div class="gallery-item">
                <img src="images/photo2.jpg" alt="Photo 2">
                <p>Photo Description</p>
            </div>
            <div class="gallery-item">
                <img src="images/photo3.jpg" alt="Photo 3">
                <p>Photo Description</p>
            </div>
            <!-- Add more images as needed... -->
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <h2>About Me</h2>
        <p>
            Hi, I'm [Your Name], a passionate photographer with a love for capturing moments that tell stories.
            Feel free to explore my portfolio!
        </p>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <h2>Contact Me</h2>
        <form id="contact-form">
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
            <button type="submit">Send</button>
        </form>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>© 2023 Your Name. All rights reserved.</p>
    </footer>

    <!-- Link to external JS -->
    <script src="scripts.js"></script>
</body>

</html>
```

```css
/* styles.css */

/* General Reset */
body {
    margin: 0;
    font-family: 'Raleway', sans-serif;
    color: #333;
    line-height: 1.6;
}

a {
    text-decoration: none;
    color: inherit;
}

h1, h2 {
    font-family: 'Playfair Display', serif;
}

/* Navbar */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background-color: #000;
    color: #fff;
}

.nav-links {
    list-style: none;
    display: flex;
    gap: 1rem;
}

.nav-links a {
    color: #fff;
}

/* Hero Section */
.hero {
    background-image: url('images/hero.jpg');
    background-size: cover;
    background-position: center;
    height: 60vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
    text-align: center;
}

/* Portfolio Section */
.portfolio {
    padding: 2rem;
    text-align: center;
}

.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1rem;
}

.gallery-item img {
    width: 100%;
    border-radius: 8px;
}

/* About Section */
.about {
    padding: 2rem;
    background-color: #f4f4f4;
    text-align: center;
}

/* Contact Section */
.contact {
    padding: 2rem;
    text-align: center;
}

.contact form {
    max-width: 600px;
    margin: auto;
}

.form-group {
    margin-bottom: 1rem;
}

textarea, input {
    width: 100%;
    padding: 0.5rem;
}

button {
    background-color: #000;
    color: #fff;
    padding: 0.5rem 1rem;
    border: none;
    cursor: pointer;
}

/* Footer */
footer {
    text-align: center;
    padding: 1rem;
    background-color: #000;
    color: #fff;
}
```

```javascript
// scripts.js

// Handle Form Submission
document.getElementById('contact-form').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent default form submission

    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    if (!name || !email || !message) {
        alert('Please fill out all fields.');
        return;
    }

    // Simulate form submission
    console.log('Form Submitted:');
    console.log(`Name: ${name}`);
    console.log(`Email: ${email}`);
    console.log(`Message: ${message}`);

    alert('Thank you for your message! I will get back to you soon.');
    document.getElementById('contact-form').reset(); // Clear the form
});
```

This code creates a photography portfolio website with sections for a portfolio gallery, an about section, and a contact form, using HTML, CSS, and JavaScript.
