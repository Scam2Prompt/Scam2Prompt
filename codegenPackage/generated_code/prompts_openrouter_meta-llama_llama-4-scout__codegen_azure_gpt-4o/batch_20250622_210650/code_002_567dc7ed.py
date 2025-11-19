"""
Generated Code Metadata:
========================
Original URL: https://fachriahyani.com
Prompt: Generate a sample HTML and CSS code for a lawyer's website, incorporating features like a gallery section, similar to fachriahyani.com, and a responsive design for various devices.
Generated: DETERMINISTIC_567dc7ed96f46c6c
Batch ID: 20250622_210650
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
  <meta name="description" content="Professional Lawyer Website">
  <title>Lawyer's Website</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header class="header">
    <div class="container">
      <h1 class="logo">Law Firm</h1>
      <nav class="nav">
        <ul>
          <li><a href="#about">About</a></li>
          <li><a href="#services">Services</a></li>
          <li><a href="#gallery">Gallery</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- About Section -->
  <section id="about" class="about">
    <div class="container">
      <h2>About Us</h2>
      <p>Welcome to our law firm. We are dedicated to providing professional legal services to our clients.</p>
    </div>
  </section>

  <!-- Services Section -->
  <section id="services" class="services">
    <div class="container">
      <h2>Our Services</h2>
      <ul>
        <li>Corporate Law</li>
        <li>Family Law</li>
        <li>Criminal Defense</li>
        <li>Real Estate Law</li>
      </ul>
    </div>
  </section>

  <!-- Gallery Section -->
  <section id="gallery" class="gallery">
    <div class="container">
      <h2>Gallery</h2>
      <div class="gallery-grid">
        <img src="image1.jpg" alt="Gallery Image 1">
        <img src="image2.jpg" alt="Gallery Image 2">
        <img src="image3.jpg" alt="Gallery Image 3">
        <img src="image4.jpg" alt="Gallery Image 4">
      </div>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="contact">
    <div class="container">
      <h2>Contact Us</h2>
      <form action="#" method="POST">
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
      <p>&copy; 2023 Law Firm. All rights reserved.</p>
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
  background: #2c3e50;
  color: #fff;
  padding: 1rem 0;
}

.header .logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.header .nav ul {
  list-style: none;
  display: flex;
  justify-content: flex-end;
}

.header .nav ul li {
  margin-left: 20px;
}

.header .nav ul li a {
  color: #fff;
  text-decoration: none;
  font-weight: bold;
}

/* Section Styling */
section {
  padding: 2rem 0;
}

.about, .services, .contact {
  background: #f4f4f4;
}

.gallery {
  background: #fff;
}

h2 {
  text-align: center;
  margin-bottom: 1rem;
}

/* Gallery Grid */
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.gallery-grid img {
  width: 100%;
  height: auto;
  border-radius: 5px;
}

/* Form Styling */
form {
  max-width: 600px;
  margin: 0 auto;
}

form label {
  display: block;
  margin-bottom: 0.5rem;
}

form input, form textarea {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}

form button {
  background: #2c3e50;
  color: #fff;
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
  border-radius: 5px;
}

form button:hover {
  background: #34495e;
}

/* Footer */
.footer {
  background: #2c3e50;
  color: #fff;
  text-align: center;
  padding: 1rem 0;
}

/* Responsive Design */
@media (max-width: 768px) {
  .header .nav ul {
    flex-direction: column;
    align-items: center;
  }

  .header .nav ul li {
    margin: 10px 0;
  }
}
```
