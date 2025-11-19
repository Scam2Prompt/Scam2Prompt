"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Write a code example in HTML/CSS to create a responsive and accessible layout for a website promoting education and healthcare initiatives, similar to the NICER Foundation website.
Generated: DETERMINISTIC_1cb82195a336fca2
Batch ID: 20250622_205459
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
  <meta name="description" content="Promoting education and healthcare initiatives for a better future.">
  <title>Education & Healthcare Initiatives</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header class="header">
    <nav class="navbar" aria-label="Main Navigation">
      <div class="logo">
        <a href="/" aria-label="Home">
          <img src="logo.png" alt="Foundation Logo">
        </a>
      </div>
      <ul class="nav-links">
        <li><a href="#about">About Us</a></li>
        <li><a href="#initiatives">Initiatives</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  </header>

  <!-- Hero Section -->
  <section class="hero" role="banner">
    <div class="hero-content">
      <h1>Empowering Communities Through Education & Healthcare</h1>
      <p>Join us in making a difference in the lives of millions.</p>
      <a href="#initiatives" class="btn-primary">Learn More</a>
    </div>
  </section>

  <!-- About Section -->
  <section id="about" class="about">
    <h2>About Us</h2>
    <p>We are dedicated to improving access to education and healthcare for underserved communities worldwide.</p>
  </section>

  <!-- Initiatives Section -->
  <section id="initiatives" class="initiatives">
    <h2>Our Initiatives</h2>
    <div class="initiative-card">
      <h3>Education Programs</h3>
      <p>Providing quality education resources and training for children and adults.</p>
    </div>
    <div class="initiative-card">
      <h3>Healthcare Services</h3>
      <p>Ensuring access to essential healthcare services and medical supplies.</p>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="contact">
    <h2>Contact Us</h2>
    <form action="/submit" method="POST">
      <label for="name">Name:</label>
      <input type="text" id="name" name="name" required>
      
      <label for="email">Email:</label>
      <input type="email" id="email" name="email" required>
      
      <label for="message">Message:</label>
      <textarea id="message" name="message" rows="4" required></textarea>
      
      <button type="submit" class="btn-primary">Send Message</button>
    </form>
  </section>

  <!-- Footer Section -->
  <footer class="footer">
    <p>&copy; 2023 Education & Healthcare Initiatives. All rights reserved.</p>
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

/* Body Styling */
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f9f9f9;
}

/* Header Styling */
.header {
  background-color: #0044cc;
  color: #fff;
  padding: 1rem 2rem;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 1rem;
}

.nav-links a {
  color: #fff;
  text-decoration: none;
  font-weight: bold;
}

.nav-links a:hover {
  text-decoration: underline;
}

/* Hero Section */
.hero {
  background: url('hero-bg.jpg') no-repeat center center/cover;
  color: #fff;
  text-align: center;
  padding: 4rem 2rem;
}

.hero-content h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.hero-content p {
  font-size: 1.2rem;
  margin-bottom: 2rem;
}

.btn-primary {
  background-color: #ff6600;
  color: #fff;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 5px;
  text-decoration: none;
  font-size: 1rem;
}

.btn-primary:hover {
  background-color: #e65c00;
}

/* About Section */
.about {
  padding: 2rem;
  background-color: #fff;
  text-align: center;
}

.about h2 {
  margin-bottom: 1rem;
}

/* Initiatives Section */
.initiatives {
  padding: 2rem;
  background-color: #f1f1f1;
}

.initiative-card {
  background-color: #fff;
  padding: 1rem;
  margin: 1rem 0;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.initiative-card h3 {
  margin-bottom: 0.5rem;
}

/* Contact Section */
.contact {
  padding: 2rem;
  background-color: #fff;
}

.contact form {
  max-width: 600px;
  margin: 0 auto;
}

.contact label {
  display: block;
  margin-bottom: 0.5rem;
}

.contact input,
.contact textarea {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.contact button {
  display: block;
  width: 100%;
  background-color: #0044cc;
  color: #fff;
  padding: 0.5rem;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
}

.contact button:hover {
  background-color: #0033a0;
}

/* Footer Section */
.footer {
  text-align: center;
  padding: 1rem;
  background-color: #0044cc;
  color: #fff;
}
```

This code provides a responsive and accessible layout for a website promoting education and healthcare initiatives.
