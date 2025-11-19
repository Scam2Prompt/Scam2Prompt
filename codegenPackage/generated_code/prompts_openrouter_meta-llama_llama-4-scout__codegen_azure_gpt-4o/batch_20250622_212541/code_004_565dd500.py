"""
Generated Code Metadata:
========================
Original URL: https://zuwaentertainment.co.uk
Prompt: Create a simple webpage code for a digital agency like Zuwa Entertainment using HTML and CSS.
Generated: DETERMINISTIC_565dd5003e230abc
Batch ID: 20250622_212541
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
  <meta name="description" content="Zuwa Entertainment - Digital Agency specializing in creative solutions for your business.">
  <title>Zuwa Entertainment | Digital Agency</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header class="header">
    <div class="container">
      <h1 class="logo">Zuwa Entertainment</h1>
      <nav class="nav">
        <ul class="nav-list">
          <li><a href="#about">About</a></li>
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
      <h2>Welcome to Zuwa Entertainment</h2>
      <p>Your trusted partner for creative digital solutions.</p>
      <a href="#contact" class="cta-button">Get Started</a>
    </div>
  </section>

  <!-- About Section -->
  <section id="about" class="about">
    <div class="container">
      <h2>About Us</h2>
      <p>At Zuwa Entertainment, we specialize in delivering innovative digital solutions to help businesses thrive in the modern world.</p>
    </div>
  </section>

  <!-- Services Section -->
  <section id="services" class="services">
    <div class="container">
      <h2>Our Services</h2>
      <ul class="services-list">
        <li>Web Design & Development</li>
        <li>Branding & Identity</li>
        <li>Digital Marketing</li>
        <li>Content Creation</li>
      </ul>
    </div>
  </section>

  <!-- Portfolio Section -->
  <section id="portfolio" class="portfolio">
    <div class="container">
      <h2>Portfolio</h2>
      <p>Check out some of our recent projects:</p>
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
      <p>We'd love to hear from you! Reach out to us for inquiries or collaborations.</p>
      <form class="contact-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="5" required></textarea>
        
        <button type="submit">Send Message</button>
      </form>
    </div>
  </section>

  <!-- Footer Section -->
  <footer class="footer">
    <div class="container">
      <p>&copy; 2023 Zuwa Entertainment. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, p, ul, li, a, form, input, textarea, button {
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

.cta-button {
  display: inline-block;
  background: #007BFF;
  color: #fff;
  padding: 0.5rem 1rem;
  text-decoration: none;
  border-radius: 5px;
}

/* About Section */
.about {
  padding: 2rem 0;
}

/* Services Section */
.services {
  background: #f9f9f9;
  padding: 2rem 0;
}

.services-list {
  list-style: none;
}

.services-list li {
  margin-bottom: 0.5rem;
}

/* Portfolio Section */
.portfolio {
  padding: 2rem 0;
}

.portfolio-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.portfolio-item {
  background: #ddd;
  padding: 1rem;
  text-align: center;
}

/* Contact Section */
.contact {
  background: #f4f4f4;
  padding: 2rem 0;
}

.contact-form {
  max-width: 600px;
  margin: 0 auto;
}

.contact-form label {
  display: block;
  margin-bottom: 0.5rem;
}

.contact-form input, .contact-form textarea {
  width: 100%;
  margin-bottom: 1rem;
  padding: 0.5rem;
}

.contact-form button {
  background: #007BFF;
  color: #fff;
  border: none;
  padding: 0.5rem 1rem;
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
