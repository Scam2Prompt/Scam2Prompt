"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idex.marketing
Prompt: Generate HTML/CSS code for designing a modern, user-friendly website tailored to Jordanian market preferences, as emphasized by IDEX Marketing.
Generated: DETERMINISTIC_dfe0ba0cd6786edf
Batch ID: 20250612_145153
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&family=Roboto:wght@300;400;700&display=swap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/1200x400": {
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
  <meta name="description" content="Modern website tailored for Jordanian market preferences by IDEX Marketing">
  <title>Jordanian Market Website</title>
  <!-- External CSS -->
  <link rel="stylesheet" href="styles.css">
  <!-- Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
</head>
<body>
  <!-- Header Section -->
  <header>
    <div class="container">
      <nav class="navbar">
        <a href="#" class="logo">IDEX Jordan</a>
        <ul class="nav-links">
          <li><a href="#about">About</a></li>
          <li><a href="#services">Services</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="container">
      <h1>Welcome to IDEX Jordan</h1>
      <p>Delivering solutions tailored to Jordanian market preferences.</p>
      <a href="#services" class="cta-button">Explore Services</a>
    </div>
  </section>

  <!-- About Section -->
  <section id="about" class="about">
    <div class="container">
      <h2>About Us</h2>
      <p>At IDEX Marketing, we specialize in understanding the unique needs of the Jordanian market, ensuring modern and user-friendly solutions for your business.</p>
    </div>
  </section>

  <!-- Services Section -->
  <section id="services" class="services">
    <div class="container">
      <h2>Our Services</h2>
      <div class="service-card">
        <h3>Market Analysis</h3>
        <p>Detailed research and analysis to understand market trends in Jordan.</p>
      </div>
      <div class="service-card">
        <h3>Brand Development</h3>
        <p>Customized strategies to build your brand identity tailored to local preferences.</p>
      </div>
      <div class="service-card">
        <h3>Digital Marketing</h3>
        <p>Modern and effective online marketing solutions for reaching your audience.</p>
      </div>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="contact">
    <div class="container">
      <h2>Contact Us</h2>
      <form action="/submit" method="POST" class="contact-form">
        <div class="form-group">
          <label for="name">Your Name:</label>
          <input type="text" id="name" name="name" required>
        </div>
        <div class="form-group">
          <label for="email">Your Email:</label>
          <input type="email" id="email" name="email" required>
        </div>
        <div class="form-group">
          <label for="message">Your Message:</label>
          <textarea id="message" name="message" rows="5" required></textarea>
        </div>
        <button type="submit" class="submit-button">Send Message</button>
      </form>
    </div>
  </section>

  <!-- Footer Section -->
  <footer>
    <div class="container">
      <p>&copy; 2023 IDEX Jordan. All rights reserved.</p>
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

/* Body */
body {
  font-family: 'Tajawal', 'Roboto', sans-serif;
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
header {
  background-color: #004a8f; /* Jordanian-inspired color */
  color: #fff;
  padding: 1rem 0;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-links {
  list-style-type: none;
  display: flex;
}

.nav-links li {
  margin-left: 1rem;
}

.nav-links a {
  color: #fff;
  text-decoration: none;
  font-weight: 700;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
}

/* Hero Section */
.hero {
  background: url('https://via.placeholder.com/1200x400') center/cover no-repeat;
  text-align: center;
  color: #fff;
  padding: 5rem 0;
}

.hero h1 {
  font-size: 2.5rem;
}

.hero p {
  margin: 1rem 0;
}

.cta-button {
  background-color: #e63946;
  color: #fff;
  padding: 0.5rem 1rem;
  text-decoration: none;
  border-radius: 5px;
  font-weight: bold;
}

/* About Section */
.about {
  padding: 2rem 0;
  background-color: #f4f4f4;
}

.about h2 {
  text-align: center;
  margin-bottom: 1rem;
}

.about p {
  text-align: center;
  max-width: 700px;
  margin: 0 auto;
}

/* Services Section */
.services {
  padding: 2rem 0;
}

.services h2 {
  text-align: center;
  margin-bottom: 1rem;
}

.service-card {
  background: #fff;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin: 1rem 0;
}

/* Contact Section */
.contact {
  padding: 2rem 0;
  background-color: #f4f4f4;
}

.contact h2 {
  text-align: center;
  margin-bottom: 1rem;
}

.contact-form {
  max-width: 600px;
  margin: 0 auto;
}

.form-group {
  margin: 1rem 0;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.submit-button {
  background-color: #004a8f;
  color: #fff;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

/* Footer */
footer {
  background-color: #004a8f;
  color: #fff;
  text-align: center;
  padding: 1rem 0;
}
```
