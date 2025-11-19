"""
Generated Code Metadata:
========================
Original URL: https://cefor.org.br
Prompt: Generate a code snippet to create a simple website for a social organization, including sections for services, projects, and contact information, inspired by the CEFOR website.
Generated: DETERMINISTIC_f44dfefef11b1ee8
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
  <meta name="description" content="Social Organization Website">
  <meta name="author" content="Your Name">
  <title>Social Organization</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header>
    <div class="container">
      <h1>Welcome to Our Social Organization</h1>
      <nav>
        <ul>
          <li><a href="#services">Services</a></li>
          <li><a href="#projects">Projects</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Services Section -->
  <section id="services">
    <div class="container">
      <h2>Our Services</h2>
      <p>We offer a variety of services to support our community, including education, healthcare, and skill development programs.</p>
      <ul>
        <li>Education Programs</li>
        <li>Healthcare Initiatives</li>
        <li>Skill Development Workshops</li>
      </ul>
    </div>
  </section>

  <!-- Projects Section -->
  <section id="projects">
    <div class="container">
      <h2>Our Projects</h2>
      <p>Explore our ongoing and completed projects aimed at making a positive impact in society.</p>
      <ul>
        <li>Community Library Project</li>
        <li>Clean Water Initiative</li>
        <li>Youth Empowerment Campaign</li>
      </ul>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact">
    <div class="container">
      <h2>Contact Us</h2>
      <p>We would love to hear from you! Reach out to us using the form below or via our contact details.</p>
      <form action="/submit-contact" method="POST">
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
  <footer>
    <div class="container">
      <p>&copy; 2023 Social Organization. All rights reserved.</p>
    </div>
  </footer>
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

.container {
  width: 80%;
  margin: auto;
  overflow: hidden;
}

/* Header Styles */
header {
  background: #0073e6;
  color: #fff;
  padding: 20px 0;
}

header h1 {
  text-align: center;
}

header nav ul {
  list-style: none;
  padding: 0;
  text-align: center;
}

header nav ul li {
  display: inline;
  margin: 0 10px;
}

header nav ul li a {
  color: #fff;
  text-decoration: none;
}

/* Section Styles */
section {
  padding: 20px 0;
}

section h2 {
  text-align: center;
  margin-bottom: 20px;
}

section p {
  text-align: center;
}

section ul {
  list-style: none;
  padding: 0;
  text-align: center;
}

section ul li {
  margin: 10px 0;
}

/* Contact Form Styles */
form {
  max-width: 600px;
  margin: auto;
}

form label {
  display: block;
  margin: 10px 0 5px;
}

form input, form textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

form button {
  display: block;
  width: 100%;
  padding: 10px;
  background: #0073e6;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

form button:hover {
  background: #005bb5;
}

/* Footer Styles */
footer {
  background: #333;
  color: #fff;
  text-align: center;
  padding: 10px 0;
}
```
