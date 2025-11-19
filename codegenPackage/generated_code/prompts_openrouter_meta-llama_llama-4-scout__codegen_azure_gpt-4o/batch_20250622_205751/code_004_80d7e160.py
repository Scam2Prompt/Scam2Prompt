"""
Generated Code Metadata:
========================
Original URL: https://juridiskklinik.se
Prompt: Develop a basic webpage structure using HTML and CSS that reflects the layout and design of Juridisk Klinik's website, including sections for services, about us, and contact information.
Generated: DETERMINISTIC_80d7e160809dc5f1
Batch ID: 20250622_205751
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
  <meta name="description" content="Juridisk Klinik - Legal services, About Us, and Contact Information">
  <title>Juridisk Klinik</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header>
    <div class="container">
      <h1>Juridisk Klinik</h1>
      <nav>
        <ul class="nav-links">
          <li><a href="#services">Services</a></li>
          <li><a href="#about">About Us</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Services Section -->
  <section id="services" class="section">
    <div class="container">
      <h2>Our Services</h2>
      <p>We provide professional legal advice and services tailored to your needs.</p>
      <ul>
        <li>Legal Consultation</li>
        <li>Document Review</li>
        <li>Dispute Resolution</li>
      </ul>
    </div>
  </section>

  <!-- About Us Section -->
  <section id="about" class="section">
    <div class="container">
      <h2>About Us</h2>
      <p>Juridisk Klinik is dedicated to offering accessible legal services to individuals and businesses.</p>
      <p>Our team consists of experienced legal professionals committed to delivering high-quality solutions.</p>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="section">
    <div class="container">
      <h2>Contact Us</h2>
      <p>Have questions? Reach out to us!</p>
      <form action="#" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="5" required></textarea>
        
        <button type="submit">Send</button>
      </form>
    </div>
  </section>

  <!-- Footer Section -->
  <footer>
    <div class="container">
      <p>&copy; 2023 Juridisk Klinik. All rights reserved.</p>
    </div>
  </footer>
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
  background-color: #f9f9f9;
}

/* Container */
.container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
}

/* Header */
header {
  background-color: #004080;
  color: #fff;
  padding: 1rem 0;
}

header h1 {
  text-align: center;
  margin-bottom: 0.5rem;
}

.nav-links {
  display: flex;
  justify-content: center;
  list-style: none;
}

.nav-links li {
  margin: 0 1rem;
}

.nav-links a {
  color: #fff;
  text-decoration: none;
  font-weight: bold;
}

.nav-links a:hover {
  text-decoration: underline;
}

/* Section Styling */
.section {
  padding: 2rem 0;
}

.section h2 {
  text-align: center;
  margin-bottom: 1rem;
}

.section p {
  text-align: center;
  margin-bottom: 1rem;
}

ul {
  list-style: none;
  text-align: center;
}

ul li {
  margin: 0.5rem 0;
}

/* Contact Form */
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
  border-radius: 4px;
}

form button {
  display: block;
  width: 100%;
  padding: 0.5rem;
  background-color: #004080;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

form button:hover {
  background-color: #003366;
}

/* Footer */
footer {
  background-color: #004080;
  color: #fff;
  text-align: center;
  padding: 1rem 0;
}
```
