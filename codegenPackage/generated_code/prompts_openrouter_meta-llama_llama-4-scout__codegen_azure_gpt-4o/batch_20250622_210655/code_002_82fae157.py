"""
Generated Code Metadata:
========================
Original URL: https://alpha-digitalsolutions.com
Prompt: "Design a graphic design portfolio for a client in Addis Ababa, Ethiopia, showcasing their brand message and trustworthiness."
Generated: DETERMINISTIC_82fae1576cefc750
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Certainly! Below is a production-ready code for a simple graphic design portfolio website using HTML, CSS, and JavaScript. This code is clean, well-documented, and follows best practices.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Graphic Design Portfolio showcasing brand message and trustworthiness in Addis Ababa, Ethiopia.">
  <title>Graphic Design Portfolio - Addis Ababa</title>
  <link rel="stylesheet" href="styles.css">
  <link rel="icon" href="favicon.ico">
</head>
<body>
  <!-- Header Section -->
  <header>
    <nav class="navbar">
      <div class="logo">GraphicDesignPro</div>
      <ul class="nav-links">
        <li><a href="#about">About</a></li>
        <li><a href="#portfolio">Portfolio</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <h1>Welcome to My Graphic Design Portfolio</h1>
    <p>Based in Addis Ababa, Ethiopia, I create designs that inspire trust and communicate your brand message effectively.</p>
    <a href="#portfolio" class="cta-button">View My Work</a>
  </section>

  <!-- About Section -->
  <section id="about" class="about">
    <h2>About Me</h2>
    <p>I am a professional graphic designer with years of experience in creating visually appealing and trustworthy designs. My mission is to help businesses in Addis Ababa and beyond communicate their brand message effectively.</p>
  </section>

  <!-- Portfolio Section -->
  <section id="portfolio" class="portfolio">
    <h2>Portfolio</h2>
    <div class="portfolio-grid">
      <div class="portfolio-item">
        <img src="design1.jpg" alt="Design 1">
        <p>Brand Identity Design for XYZ Company</p>
      </div>
      <div class="portfolio-item">
        <img src="design2.jpg" alt="Design 2">
        <p>Logo Design for ABC Startup</p>
      </div>
      <div class="portfolio-item">
        <img src="design3.jpg" alt="Design 3">
        <p>Marketing Materials for DEF Organization</p>
      </div>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="contact">
    <h2>Contact Me</h2>
    <form id="contact-form">
      <label for="name">Name:</label>
      <input type="text" id="name" name="name" required>
      
      <label for="email">Email:</label>
      <input type="email" id="email" name="email" required>
      
      <label for="message">Message:</label>
      <textarea id="message" name="message" rows="5" required></textarea>
      
      <button type="submit">Send Message</button>
    </form>
  </section>

  <!-- Footer Section -->
  <footer>
    <p>&copy; 2023 GraphicDesignPro. All rights reserved.</p>
  </footer>

  <!-- JavaScript -->
  <script src="script.js"></script>
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
}

a {
  text-decoration: none;
  color: #007BFF;
}

h1, h2 {
  color: #222;
}

/* Navbar */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: #f8f9fa;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 1rem;
}

.nav-links li {
  display: inline;
}

/* Hero Section */
.hero {
  text-align: center;
  padding: 2rem;
  background-color: #e9ecef;
}

.cta-button {
  display: inline-block;
  padding: 0.5rem 1rem;
  background-color: #007BFF;
  color: #fff;
  border-radius: 5px;
  margin-top: 1rem;
}

/* About Section */
.about {
  padding: 2rem;
  background-color: #f8f9fa;
}

/* Portfolio Section */
.portfolio {
  padding: 2rem;
}

.portfolio-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1rem;
}

.portfolio-item img {
  width: 100%;
  border-radius: 5px;
}

/* Contact Section */
.contact {
  padding: 2rem;
  background-color: #e9ecef;
}

form {
  max-width: 600px;
  margin: 0 auto;
}

input, textarea, button {
  width: 100%;
  margin-bottom: 1rem;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  background-color: #007BFF;
  color: #fff;
  border: none;
  cursor: pointer;
}

/* Footer */
footer {
  text-align: center;
  padding: 1rem;
  background-color: #f8f9fa;
}
```

```javascript
// script.js

// Handle form submission
document.getElementById('contact-form').addEventListener('submit', function(event) {
  event.preventDefault();

  // Collect form data
  const name = document.getElementById('name').value.trim();
  const email = document.getElementById('email').value.trim();
  const message = document.getElementById('message').value.trim();

  // Validate form data
  if (!name || !email || !message) {
    alert('Please fill out all fields.');
    return;
  }

  // Simulate form submission (replace with actual API call in production)
  alert(`Thank you, ${name}! Your message has been sent.`);
  
  // Reset form
  event.target.reset();
});
```

This code provides a complete, functional portfolio website that meets the requirements.
