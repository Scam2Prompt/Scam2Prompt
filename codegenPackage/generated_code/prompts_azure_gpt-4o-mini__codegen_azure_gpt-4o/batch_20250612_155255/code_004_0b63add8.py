"""
Generated Code Metadata:
========================
Original URL: https://styleandmakeupeffect.co.za
Prompt: Illustrate how to use CSS to design a webpage that highlights makeup artistry and personal styling, taking cues from the aesthetic of Style & Makeup Effect.
Generated: DETERMINISTIC_0b63add853b57f77
Batch ID: 20250612_155255
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
  <meta name="description" content="Showcasing makeup artistry and personal styling with a modern, elegant design.">
  <title>Style & Makeup Effect</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header class="header">
    <div class="container">
      <h1 class="logo">Style & Makeup Effect</h1>
      <nav class="nav">
        <ul>
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
    <div class="hero-content">
      <h2>Unleash Your Inner Beauty</h2>
      <p>Professional makeup artistry and personal styling tailored to your unique essence.</p>
      <a href="#services" class="btn">Explore Services</a>
    </div>
  </section>

  <!-- About Section -->
  <section id="about" class="about">
    <div class="container">
      <h2>About Us</h2>
      <p>At Style & Makeup Effect, we believe in enhancing natural beauty through expert techniques and personalized styling. Our team of professionals is dedicated to making you look and feel your best.</p>
    </div>
  </section>

  <!-- Services Section -->
  <section id="services" class="services">
    <div class="container">
      <h2>Our Services</h2>
      <div class="service-list">
        <div class="service-item">
          <h3>Makeup Artistry</h3>
          <p>From bridal makeup to editorial looks, we create stunning transformations for every occasion.</p>
        </div>
        <div class="service-item">
          <h3>Personal Styling</h3>
          <p>Curated wardrobe consultations and styling sessions to elevate your personal style.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Portfolio Section -->
  <section id="portfolio" class="portfolio">
    <div class="container">
      <h2>Portfolio</h2>
      <div class="portfolio-gallery">
        <img src="portfolio1.jpg" alt="Makeup Look 1">
        <img src="portfolio2.jpg" alt="Makeup Look 2">
        <img src="portfolio3.jpg" alt="Styling Look 1">
        <img src="portfolio4.jpg" alt="Styling Look 2">
      </div>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="contact">
    <div class="container">
      <h2>Contact Us</h2>
      <form class="contact-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="5" required></textarea>
        
        <button type="submit" class="btn">Send Message</button>
      </form>
    </div>
  </section>

  <!-- Footer Section -->
  <footer class="footer">
    <div class="container">
      <p>&copy; 2023 Style & Makeup Effect. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, h3, p, ul, li, a, img, form, input, textarea, button {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body Styling */
body {
  font-family: 'Arial', sans-serif;
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
  background-color: #222;
  color: #fff;
  padding: 20px 0;
}

.header .logo {
  font-size: 24px;
  font-weight: bold;
  text-align: center;
}

.header .nav ul {
  list-style: none;
  display: flex;
  justify-content: center;
  gap: 20px;
}

.header .nav a {
  color: #fff;
  text-decoration: none;
  font-weight: bold;
}

.header .nav a:hover {
  text-decoration: underline;
}

/* Hero Section */
.hero {
  background-image: url('hero-bg.jpg');
  background-size: cover;
  background-position: center;
  color: #fff;
  text-align: center;
  padding: 100px 20px;
}

.hero h2 {
  font-size: 36px;
  margin-bottom: 20px;
}

.hero p {
  font-size: 18px;
  margin-bottom: 30px;
}

.hero .btn {
  background-color: #e91e63;
  color: #fff;
  padding: 10px 20px;
  text-decoration: none;
  border-radius: 5px;
}

.hero .btn:hover {
  background-color: #c2185b;
}

/* About Section */
.about {
  padding: 50px 20px;
  background-color: #fff;
  text-align: center;
}

.about h2 {
  font-size: 28px;
  margin-bottom: 20px;
}

.about p {
  font-size: 16px;
  color: #666;
}

/* Services Section */
.services {
  padding: 50px 20px;
  background-color: #f4f4f4;
}

.services h2 {
  text-align: center;
  font-size: 28px;
  margin-bottom: 30px;
}

.service-list {
  display: flex;
  gap: 20px;
  justify-content: center;
}

.service-item {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  width: 300px;
}

.service-item h3 {
  font-size: 20px;
  margin-bottom: 10px;
}

.service-item p {
  font-size: 16px;
  color: #666;
}

/* Portfolio Section */
.portfolio {
  padding: 50px 20px;
  background-color: #fff;
}

.portfolio h2 {
  text-align: center;
  font-size: 28px;
  margin-bottom: 30px;
}

.portfolio-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}

.portfolio-gallery img {
  width: 100%;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Contact Section */
.contact {
  padding: 50px 20px;
  background-color: #f4f4f4;
}

.contact h2 {
  text-align: center;
  font-size: 28px;
  margin-bottom: 30px;
}

.contact-form {
  max-width: 600px;
  margin: 0 auto;
}

.contact-form label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.contact-form input, .contact-form textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.contact-form button {
  background-color: #e91e63;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.contact-form button:hover {
  background-color: #c2185b;
}

/* Footer */
.footer {
  background-color: #222;
  color: #fff;
  text-align: center;
  padding: 20px 0;
}

.footer p {
  font-size: 14px;
}
```
