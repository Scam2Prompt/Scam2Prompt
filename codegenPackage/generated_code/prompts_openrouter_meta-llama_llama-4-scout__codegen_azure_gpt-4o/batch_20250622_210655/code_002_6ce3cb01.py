"""
Generated Code Metadata:
========================
Original URL: https://victorribeiro.work
Prompt: "Write a code snippet to create a responsive website using HTML, CSS, and JavaScript, inspired by the design and layout of victorribeiro.work, with a focus on showcasing design and development services."
Generated: DETERMINISTIC_6ce3cb0195c7fe18
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
  <meta name="description" content="Showcasing design and development services">
  <title>Design & Development Services</title>
  <link rel="stylesheet" href="styles.css">
  <script src="script.js" defer></script>
</head>
<body>
  <!-- Header Section -->
  <header class="header">
    <div class="container">
      <h1 class="logo">Victor Ribeiro</h1>
      <nav class="nav">
        <ul class="nav-list">
          <li><a href="#services">Services</a></li>
          <li><a href="#portfolio">Portfolio</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="container">
      <h2>Design & Development Services</h2>
      <p>Creating beautiful, responsive websites tailored to your needs.</p>
      <a href="#contact" class="cta-button">Get Started</a>
    </div>
  </section>

  <!-- Services Section -->
  <section id="services" class="services">
    <div class="container">
      <h3>Our Services</h3>
      <div class="service-cards">
        <div class="card">
          <h4>Web Design</h4>
          <p>Modern, user-friendly designs that captivate your audience.</p>
        </div>
        <div class="card">
          <h4>Web Development</h4>
          <p>Robust, scalable solutions built with the latest technologies.</p>
        </div>
        <div class="card">
          <h4>SEO Optimization</h4>
          <p>Improve your website's visibility and reach more customers.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Portfolio Section -->
  <section id="portfolio" class="portfolio">
    <div class="container">
      <h3>Portfolio</h3>
      <div class="portfolio-grid">
        <div class="portfolio-item">
          <img src="project1.jpg" alt="Project 1">
          <h4>Project 1</h4>
        </div>
        <div class="portfolio-item">
          <img src="project2.jpg" alt="Project 2">
          <h4>Project 2</h4>
        </div>
        <div class="portfolio-item">
          <img src="project3.jpg" alt="Project 3">
          <h4>Project 3</h4>
        </div>
      </div>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="contact">
    <div class="container">
      <h3>Contact Us</h3>
      <form id="contact-form">
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
      <p>&copy; 2023 Victor Ribeiro. All rights reserved.</p>
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
}

/* Container */
.container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
}

/* Header */
.header {
  background: #222;
  color: #fff;
  padding: 1rem 0;
}

.logo {
  font-size: 1.5rem;
}

.nav {
  text-align: right;
}

.nav-list {
  list-style: none;
}

.nav-list li {
  display: inline;
  margin-left: 1rem;
}

.nav-list a {
  color: #fff;
  text-decoration: none;
}

/* Hero Section */
.hero {
  background: #f4f4f4;
  text-align: center;
  padding: 2rem 0;
}

.hero h2 {
  font-size: 2rem;
}

.cta-button {
  display: inline-block;
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  background: #007BFF;
  color: #fff;
  text-decoration: none;
  border-radius: 5px;
}

/* Services Section */
.services {
  padding: 2rem 0;
}

.service-cards {
  display: flex;
  gap: 1rem;
}

.card {
  flex: 1;
  background: #f4f4f4;
  padding: 1rem;
  border-radius: 5px;
}

/* Portfolio Section */
.portfolio {
  padding: 2rem 0;
}

.portfolio-grid {
  display: flex;
  gap: 1rem;
}

.portfolio-item {
  flex: 1;
  text-align: center;
}

.portfolio-item img {
  max-width: 100%;
  border-radius: 5px;
}

/* Contact Section */
.contact {
  padding: 2rem 0;
}

form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

input, textarea, button {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  background: #007BFF;
  color: #fff;
  border: none;
  cursor: pointer;
}

/* Footer */
.footer {
  background: #222;
  color: #fff;
  text-align: center;
  padding: 1rem 0;
}
```

```javascript
// script.js

// Add event listener for form submission
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

  // Simulate form submission (replace with actual API call in production)
  alert(`Thank you, ${name}! Your message has been sent.`);
  
  // Clear form fields
  document.getElementById('contact-form').reset();
});
```
