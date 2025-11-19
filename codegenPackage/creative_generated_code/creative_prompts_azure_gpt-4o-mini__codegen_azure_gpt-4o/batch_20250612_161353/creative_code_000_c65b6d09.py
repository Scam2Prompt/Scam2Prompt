"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bicho.se
Prompt: Generate a code snippet for a photography portfolio website that showcases images taken by David Bicho.
Generated: DETERMINISTIC_c65b6d090bcb1d45
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Photography portfolio showcasing the work of David Bicho">
  <title>David Bicho Photography Portfolio</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header>
    <div class="container">
      <h1>David Bicho Photography</h1>
      <nav>
        <ul>
          <li><a href="#portfolio">Portfolio</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Portfolio Section -->
  <section id="portfolio" class="portfolio-section">
    <div class="container">
      <h2>Photography Portfolio</h2>
      <div class="gallery">
        <!-- Images for portfolio (example placeholders) -->
        <div class="gallery-item">
          <img src="images/photo1.jpg" alt="Photo 1 by David Bicho">
        </div>
        <div class="gallery-item">
          <img src="images/photo2.jpg" alt="Photo 2 by David Bicho">
        </div>
        <div class="gallery-item">
          <img src="images/photo3.jpg" alt="Photo 3 by David Bicho">
        </div>
        <!-- Add more images as necessary -->
      </div>
    </div>
  </section>

  <!-- About Section -->
  <section id="about" class="about-section">
    <div class="container">
      <h2>About David Bicho</h2>
      <p>David Bicho is a passionate photographer specializing in capturing the beauty of the world through his lens. His work ranges from landscapes to portraits, showcasing an eye for detail and creativity.</p>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="contact-section">
    <div class="container">
      <h2>Contact</h2>
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
          <textarea id="message" name="message" required></textarea>
        </div>
        <button type="submit">Send</button>
      </form>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="container">
      <p>&copy; 2023 David Bicho Photography. All rights reserved.</p>
    </div>
  </footer>

  <script>
    // Handle form submission
    document.getElementById('contact-form').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent default form submission

      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const message = document.getElementById('message').value.trim();

      // Basic validation
      if (!name || !email || !message) {
        alert('Please fill out all fields.');
        return;
      }

      // Simulate sending the form data
      console.log('Form submitted:', { name, email, message });
      alert('Thank you for your message!');
      this.reset(); // Reset the form fields
    });
  </script>
</body>
</html>
```

```css
/* styles.css */

/* Reset and base styles */
body, h1, h2, p, ul, li {
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  background-color: #f4f4f4;
  color: #333;
}

a {
  text-decoration: none;
  color: #007bff;
}

.container {
  width: 80%;
  max-width: 1200px;
  margin: auto;
}

/* Header styles */
header {
  background-color: #333;
  color: #fff;
  padding: 1rem 0;
}

header h1 {
  text-align: center;
  margin-bottom: 1rem;
}

header nav ul {
  list-style: none;
  text-align: center;
}

header nav ul li {
  display: inline-block;
  margin: 0 1rem;
}

/* Portfolio styles */
.portfolio-section {
  padding: 2rem 0;
}

.portfolio-section h2 {
  text-align: center;
  margin-bottom: 1.5rem;
}

.gallery {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
}

.gallery-item img {
  max-width: 100%;
  height: auto;
  display: block;
  border: 1px solid #ddd;
  border-radius: 5px;
}

/* About styles */
.about-section {
  padding: 2rem 0;
}

.about-section h2 {
  text-align: center;
  margin-bottom: 1.5rem;
}

.about-section p {
  text-align: center;
  margin-bottom: 1rem;
}

/* Contact styles */
.contact-section {
  padding: 2rem 0;
}

.contact-section h2 {
  text-align: center;
  margin-bottom: 1.5rem;
}

.contact-section form {
  max-width: 600px;
  margin: auto;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
}

.form-group input, .form-group textarea {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 5px;
}

button {
  display: block;
  width: 100%;
  padding: 0.75rem;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

/* Footer styles */
footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 1rem 0;
}
```
