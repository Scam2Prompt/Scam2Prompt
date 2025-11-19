"""
Generated Code Metadata:
========================
Original URL: https://officineimmagine.it
Prompt: Create a photography website template using HTML, CSS, and JavaScript, incorporating Officine dell'Immagine's style and services.
Generated: DETERMINISTIC_65835d16af6fbae4
Batch ID: 20250622_212148
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

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Photography website template for Officine dell'Immagine">
    <title>Officine dell'Immagine</title>
    <!-- Link to external CSS -->
    <link rel="stylesheet" href="styles.css">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <h1>Officine dell'Immagine</h1>
            <nav>
                <ul>
                    <li><a href="#about">About</a></li>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#portfolio">Portfolio</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- About Section -->
    <section id="about" class="section">
        <div class="container">
            <h2>About Us</h2>
            <p>Welcome to Officine dell'Immagine, where we capture moments that last a lifetime. Our team of professional photographers specializes in portrait, event, and commercial photography.</p>
        </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="section">
        <div class="container">
            <h2>Our Services</h2>
            <div class="service-list">
                <div class="service-item">
                    <h3>Portrait Photography</h3>
                    <p>High-quality portraits for individuals, families, and professionals.</p>
                </div>
                <div class="service-item">
                    <h3>Event Photography</h3>
                    <p>Capture the essence of your special events with our expert photographers.</p>
                </div>
                <div class="service-item">
                    <h3>Commercial Photography</h3>
                    <p>Professional images for your business, products, and marketing campaigns.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Portfolio Section -->
    <section id="portfolio" class="section">
        <div class="container">
            <h2>Portfolio</h2>
            <div class="portfolio-gallery">
                <img src="portfolio1.jpg" alt="Portfolio Image 1">
                <img src="portfolio2.jpg" alt="Portfolio Image 2">
                <img src="portfolio3.jpg" alt="Portfolio Image 3">
                <img src="portfolio4.jpg" alt="Portfolio Image 4">
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section">
        <div class="container">
            <h2>Contact Us</h2>
            <form id="contact-form">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                
                <button type="submit">Send Message</button>
            </form>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <div class="container">
            <p>&copy; 2023 Officine dell'Immagine. All rights reserved.</p>
        </div>
    </footer>

    <!-- Link to external JavaScript -->
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
    color: #333;
    background-color: #f9f9f9;
}

.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
}

/* Header Styles */
header {
    background-color: #222;
    color: #fff;
    padding: 20px 0;
}

header h1 {
    margin: 0;
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

nav ul li a {
    color: #fff;
    text-decoration: none;
    font-weight: bold;
}

/* Section Styles */
.section {
    padding: 50px 0;
}

.section h2 {
    text-align: center;
    margin-bottom: 20px;
}

/* Services Section */
.service-list {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
}

.service-item {
    width: 30%;
    margin: 10px 0;
    text-align: center;
}

/* Portfolio Section */
.portfolio-gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
}

.portfolio-gallery img {
    width: 45%;
    margin: 10px 0;
    border-radius: 5px;
}

/* Contact Section */
form {
    max-width: 600px;
    margin: 0 auto;
}

form label {
    display: block;
    margin: 10px 0 5px;
}

form input, form textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

form button {
    display: block;
    width: 100%;
    padding: 10px;
    background-color: #222;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

form button:hover {
    background-color: #444;
}

/* Footer Styles */
footer {
    background-color: #222;
    color: #fff;
    text-align: center;
    padding: 20px 0;
}
```

```javascript
// script.js

// Add event listener for the contact form submission
document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Collect form data
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    // Basic validation
    if (!name || !email || !message) {
        alert('Please fill out all fields.');
        return;
    }

    // Simulate form submission (replace with actual backend integration)
    alert(`Thank you, ${name}! Your message has been sent.`);
    
    // Clear the form
    document.getElementById('contact-form').reset();
});
```
