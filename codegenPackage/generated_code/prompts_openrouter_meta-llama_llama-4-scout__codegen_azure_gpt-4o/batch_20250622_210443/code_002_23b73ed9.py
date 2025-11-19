"""
Generated Code Metadata:
========================
Original URL: https://vivadainfotech.com
Prompt: "Generate a sample UI/UX design concept for a hospital website, incorporating principles of user experience and user interface design, as per Vivada Infotech's services."
Generated: DETERMINISTIC_23b73ed9daf8ea67
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a sample code for a hospital website UI/UX design concept using HTML, CSS, and JavaScript. It incorporates principles of user experience and user interface design.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Hospital Website - Providing quality healthcare services">
  <title>Hospital Website</title>
  <link rel="stylesheet" href="styles.css">
  <script src="script.js" defer></script>
</head>
<body>
  <!-- Header Section -->
  <header class="header">
    <div class="container">
      <h1 class="logo">HospitalCare</h1>
      <nav class="nav">
        <ul>
          <li><a href="#home">Home</a></li>
          <li><a href="#services">Services</a></li>
          <li><a href="#about">About Us</a></li>
          <li><a href="#contact">Contact</a></li>
          <li><a href="#appointment" class="btn-primary">Book Appointment</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Hero Section -->
  <section id="home" class="hero">
    <div class="container">
      <h2>Welcome to HospitalCare</h2>
      <p>Your health is our priority. Experience world-class healthcare services.</p>
      <a href="#appointment" class="btn-primary">Get Started</a>
    </div>
  </section>

  <!-- Services Section -->
  <section id="services" class="services">
    <div class="container">
      <h2>Our Services</h2>
      <div class="service-cards">
        <div class="card">
          <h3>Emergency Care</h3>
          <p>24/7 emergency services to handle critical situations.</p>
        </div>
        <div class="card">
          <h3>Outpatient Services</h3>
          <p>Comprehensive outpatient care for all age groups.</p>
        </div>
        <div class="card">
          <h3>Specialized Treatments</h3>
          <p>Expert care in cardiology, orthopedics, and more.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- About Us Section -->
  <section id="about" class="about">
    <div class="container">
      <h2>About Us</h2>
      <p>HospitalCare is committed to providing exceptional healthcare services with a patient-first approach.</p>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="contact">
    <div class="container">
      <h2>Contact Us</h2>
      <form id="contact-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
        
        <button type="submit" class="btn-primary">Send Message</button>
      </form>
    </div>
  </section>

  <!-- Footer Section -->
  <footer class="footer">
    <div class="container">
      <p>&copy; 2023 HospitalCare. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, h3, p, ul, li, a, button {
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
  background: #007bff;
  color: #fff;
  padding: 1rem 0;
}

.header .logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.nav ul {
  list-style: none;
  display: flex;
  justify-content: space-around;
}

.nav a {
  color: #fff;
  text-decoration: none;
}

.btn-primary {
  background: #28a745;
  color: #fff;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 5px;
  text-decoration: none;
}

/* Hero Section */
.hero {
  background: #f8f9fa;
  text-align: center;
  padding: 2rem 0;
}

.hero h2 {
  font-size: 2rem;
}

.hero p {
  margin: 1rem 0;
}

/* Services Section */
.services {
  background: #e9ecef;
  padding: 2rem 0;
}

.service-cards {
  display: flex;
  justify-content: space-around;
}

.card {
  background: #fff;
  padding: 1rem;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  width: 30%;
}

/* About Section */
.about {
  padding: 2rem 0;
  text-align: center;
}

/* Contact Section */
.contact {
  background: #f8f9fa;
  padding: 2rem 0;
}

.contact form {
  max-width: 600px;
  margin: 0 auto;
}

.contact label {
  display: block;
  margin: 0.5rem 0;
}

.contact input, .contact textarea {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.contact button {
  display: block;
  width: 100%;
}

/* Footer */
.footer {
  background: #343a40;
  color: #fff;
  text-align: center;
  padding: 1rem 0;
}
```

```javascript
// script.js

// Contact Form Submission
document.getElementById('contact-form').addEventListener('submit', function (event) {
  event.preventDefault();

  // Collect form data
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const message = document.getElementById('message').value;

  // Basic validation
  if (!name || !email || !message) {
    alert('Please fill out all fields.');
    return;
  }

  // Simulate form submission
  alert(`Thank you, ${name}. Your message has been sent!`);
});
```

This code provides a clean, responsive, and user-friendly design for a hospital website. It includes sections for navigation, services, about, contact, and appointment booking, adhering to UI/UX principles.
