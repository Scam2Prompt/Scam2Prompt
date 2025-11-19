"""
Generated Code Metadata:
========================
Original URL: https://stoneage.com
Prompt: "Design a basic webpage structure for a tech company named Stoneage using HTML, CSS, and JavaScript."
Generated: DETERMINISTIC_eb0f68ebca356f21
Batch ID: 20250622_210856
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
  <meta name="description" content="Stoneage - Innovating the future of technology">
  <title>Stoneage | Tech Company</title>
  <!-- Link to external CSS -->
  <link rel="stylesheet" href="styles.css">
  <!-- Favicon -->
  <link rel="icon" href="favicon.ico" type="image/x-icon">
</head>
<body>
  <!-- Header Section -->
  <header>
    <div class="container">
      <h1>Stoneage</h1>
      <nav>
        <ul class="nav-links">
          <li><a href="#about">About</a></li>
          <li><a href="#services">Services</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Main Content -->
  <main>
    <!-- About Section -->
    <section id="about" class="section">
      <div class="container">
        <h2>About Us</h2>
        <p>Stoneage is a leading tech company dedicated to innovation and excellence in technology solutions.</p>
      </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="section">
      <div class="container">
        <h2>Our Services</h2>
        <ul>
          <li>Software Development</li>
          <li>Cloud Solutions</li>
          <li>AI & Machine Learning</li>
        </ul>
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
          <textarea id="message" name="message" rows="4" required></textarea>
          
          <button type="submit">Send</button>
        </form>
      </div>
    </section>
  </main>

  <!-- Footer Section -->
  <footer>
    <div class="container">
      <p>&copy; 2023 Stoneage. All rights reserved.</p>
    </div>
  </footer>

  <!-- Link to external JavaScript -->
  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, p, ul, li, form, input, textarea, button {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body Styling */
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f4f4f4;
}

/* Container */
.container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
}

/* Header */
header {
  background: #333;
  color: #fff;
  padding: 1rem 0;
}

header h1 {
  text-align: center;
}

.nav-links {
  list-style: none;
  text-align: center;
  margin-top: 0.5rem;
}

.nav-links li {
  display: inline;
  margin: 0 1rem;
}

.nav-links a {
  color: #fff;
  text-decoration: none;
}

.nav-links a:hover {
  text-decoration: underline;
}

/* Section Styling */
.section {
  padding: 2rem 0;
  background: #fff;
  margin: 1rem 0;
}

.section h2 {
  text-align: center;
  margin-bottom: 1rem;
}

.section p, .section ul {
  text-align: center;
}

/* Contact Form */
form {
  max-width: 600px;
  margin: 0 auto;
}

form label {
  display: block;
  margin: 0.5rem 0 0.2rem;
}

form input, form textarea, form button {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
}

form button {
  background: #333;
  color: #fff;
  border: none;
  cursor: pointer;
}

form button:hover {
  background: #555;
}

/* Footer */
footer {
  background: #333;
  color: #fff;
  text-align: center;
  padding: 1rem 0;
}
```

```javascript
// script.js

// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', () => {
  const contactForm = document.getElementById('contact-form');

  // Handle form submission
  contactForm.addEventListener('submit', (event) => {
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
    alert(`Thank you, ${name}! Your message has been received.`);
    contactForm.reset(); // Clear the form
  });
});
```
