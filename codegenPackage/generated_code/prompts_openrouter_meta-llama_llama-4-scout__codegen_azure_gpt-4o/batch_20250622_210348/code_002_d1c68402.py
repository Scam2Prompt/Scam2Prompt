"""
Generated Code Metadata:
========================
Original URL: https://agenciainside.com
Prompt: "Write a code snippet to create a responsive design for a marketing website, inspired by Agência inSIDE's portfolio, using HTML, CSS, and JavaScript."
Generated: DETERMINISTIC_d1c684028b4838a9
Batch ID: 20250622_210348
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
  <meta name="description" content="Marketing website inspired by Agência inSIDE's portfolio">
  <title>Marketing Website</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header class="header">
    <nav class="navbar">
      <div class="logo">inSIDE Marketing</div>
      <ul class="nav-links">
        <li><a href="#about">About</a></li>
        <li><a href="#services">Services</a></li>
        <li><a href="#portfolio">Portfolio</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <button class="menu-toggle" aria-label="Toggle Menu">
        <span class="menu-icon"></span>
      </button>
    </nav>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="hero-content">
      <h1>Creative Marketing Solutions</h1>
      <p>We help brands grow with innovative strategies and designs.</p>
      <a href="#contact" class="cta-button">Get Started</a>
    </div>
  </section>

  <!-- About Section -->
  <section id="about" class="about">
    <div class="container">
      <h2>About Us</h2>
      <p>We are a team of creative professionals dedicated to delivering exceptional marketing solutions.</p>
    </div>
  </section>

  <!-- Services Section -->
  <section id="services" class="services">
    <div class="container">
      <h2>Our Services</h2>
      <div class="service-cards">
        <div class="card">
          <h3>Brand Strategy</h3>
          <p>Developing unique strategies to elevate your brand.</p>
        </div>
        <div class="card">
          <h3>Web Design</h3>
          <p>Creating responsive and visually appealing websites.</p>
        </div>
        <div class="card">
          <h3>Digital Marketing</h3>
          <p>Driving growth through targeted campaigns.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Portfolio Section -->
  <section id="portfolio" class="portfolio">
    <div class="container">
      <h2>Our Portfolio</h2>
      <div class="portfolio-grid">
        <div class="portfolio-item">Project 1</div>
        <div class="portfolio-item">Project 2</div>
        <div class="portfolio-item">Project 3</div>
        <div class="portfolio-item">Project 4</div>
      </div>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="contact">
    <div class="container">
      <h2>Contact Us</h2>
      <form id="contact-form">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required>
        <label for="email">Email</label>
        <input type="email" id="email" name="email" required>
        <label for="message">Message</label>
        <textarea id="message" name="message" required></textarea>
        <button type="submit">Send Message</button>
      </form>
    </div>
  </section>

  <!-- Footer Section -->
  <footer class="footer">
    <div class="container">
      <p>&copy; 2023 inSIDE Marketing. All rights reserved.</p>
    </div>
  </footer>

  <script src="script.js"></script>
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

/* Body Styling */
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
}

/* Header Styling */
.header {
  background: #222;
  color: #fff;
  padding: 1rem 0;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.nav-links {
  list-style: none;
  display: flex;
}

.nav-links li {
  margin: 0 1rem;
}

.nav-links a {
  color: #fff;
  text-decoration: none;
}

.menu-toggle {
  display: none;
}

/* Hero Section */
.hero {
  background: url('hero-bg.jpg') no-repeat center center/cover;
  color: #fff;
  text-align: center;
  padding: 4rem 1rem;
}

.hero-content h1 {
  font-size: 2.5rem;
}

.cta-button {
  background: #ff5722;
  color: #fff;
  padding: 0.5rem 1rem;
  text-decoration: none;
  border-radius: 5px;
}

/* Responsive Design */
@media (max-width: 768px) {
  .nav-links {
    display: none;
    flex-direction: column;
  }

  .menu-toggle {
    display: block;
  }

  .hero-content h1 {
    font-size: 2rem;
  }
}
```

```javascript
// script.js

// Toggle mobile menu
document.addEventListener('DOMContentLoaded', () => {
  const menuToggle = document.querySelector('.menu-toggle');
  const navLinks = document.querySelector('.nav-links');

  menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
  });
});

// Form submission handler
document.getElementById('contact-form').addEventListener('submit', (event) => {
  event.preventDefault();

  const name = document.getElementById('name').value.trim();
  const email = document.getElementById('email').value.trim();
  const message = document.getElementById('message').value.trim();

  if (!name || !email || !message) {
    alert('Please fill out all fields.');
    return;
  }

  // Simulate form submission
  alert('Thank you for your message!');
  event.target.reset();
});
```
