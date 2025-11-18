"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://live-check.vercel.app
Prompt: Create a sample landing page in HTML, CSS, and JavaScript for a company like Flare Global Soft, showcasing their IT services and mobile app development expertise.
Generated: DETERMINISTIC_4f0c1aeed45c1d1c
Batch ID: 20250612_153702
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap": {
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
  <meta name="description" content="Flare Global Soft - IT Services & Mobile App Development Solutions">
  <meta name="author" content="Flare Global Soft">
  <title>Flare Global Soft - IT Services & Mobile App Development</title>
  
  <!-- Link to external CSS -->
  <link rel="stylesheet" href="styles.css">
  
  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>

<body>
  <!-- Header Section -->
  <header class="header">
    <div class="container">
      <h1 class="logo">Flare Global Soft</h1>
      <nav class="nav">
        <ul>
          <li><a href="#services">Services</a></li>
          <li><a href="#about">About Us</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="container">
      <h2>Welcome to Flare Global Soft</h2>
      <p>Your trusted partner for IT services and cutting-edge mobile app development.</p>
      <button onclick="scrollToContact()">Get in Touch</button>
    </div>
  </section>

  <!-- Services Section -->
  <section id="services" class="services">
    <div class="container">
      <h2>Our Services</h2>
      <div class="service-list">
        <article class="service">
          <h3>Custom Software Development</h3>
          <p>Tailored IT solutions to meet your business needs.</p>
        </article>
        <article class="service">
          <h3>Mobile App Development</h3>
          <p>Innovative and user-friendly apps for iOS and Android platforms.</p>
        </article>
        <article class="service">
          <h3>IT Consulting</h3>
          <p>Expert guidance to optimize your technology strategy.</p>
        </article>
      </div>
    </div>
  </section>

  <!-- About Us Section -->
  <section id="about" class="about">
    <div class="container">
      <h2>About Us</h2>
      <p>Flare Global Soft is a leading IT solutions provider with years of experience in delivering high-quality software and apps. We are committed to excellence and customer satisfaction.</p>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="contact">
    <div class="container">
      <h2>Contact Us</h2>
      <form id="contactForm">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="4" required></textarea>
        
        <button type="submit">Send Message</button>
      </form>
    </div>
  </section>

  <!-- Footer Section -->
  <footer class="footer">
    <div class="container">
      <p>&copy; 2023 Flare Global Soft. All rights reserved.</p>
    </div>
  </footer>

  <!-- External JavaScript -->
  <script src="script.js"></script>
</body>

</html>
```

```css
/* styles.css */

/* General Styles */
body {
  font-family: 'Roboto', sans-serif;
  margin: 0;
  line-height: 1.6;
}

/* Header Styles */
.header {
  background-color: #333;
  color: #fff;
  padding: 1rem 0;
}

.container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.nav ul {
  list-style: none;
  padding: 0;
}

.nav li {
  display: inline;
  margin: 0 15px;
}

.nav a {
  color: #fff;
  text-decoration: none;
}

/* Hero Section */
.hero {
  background-color: #007BFF;
  color: #fff;
  text-align: center;
  padding: 2rem 0;
}

.hero button {
  background-color: #fff;
  color: #007BFF;
  border: none;
  padding: 0.5rem 1rem;
  font-size: 1rem;
  cursor: pointer;
}

/* Services Section */
.services {
  padding: 2rem 0;
}

.service-list {
  display: flex;
  gap: 20px;
  justify-content: space-between;
}

.service {
  flex: 1;
  border: 1px solid #ddd;
  padding: 1rem;
  border-radius: 5px;
}

/* About Section */
.about {
  padding: 2rem 0;
}

/* Contact Section */
.contact {
  background-color: #f9f9f9;
  padding: 2rem 0;
}

form {
  max-width: 500px;
  margin: 0 auto;
}

form label {
  display: block;
  margin: 10px 0 5px;
}

form input,
form textarea {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border: 1px solid #ddd;
  border-radius: 5px;
}

form button {
  background-color: #007BFF;
  color: #fff;
  border: none;
  padding: 0.5rem 1rem;
  font-size: 1rem;
  cursor: pointer;
}

/* Footer Section */
.footer {
  text-align: center;
  background-color: #333;
  color: #fff;
  padding: 1rem 0;
}
```

```javascript
// script.js

// Function to smoothly scroll to the Contact section
function scrollToContact() {
  const contactSection = document.getElementById('contact');
  
  if (contactSection) {
    contactSection.scrollIntoView({ behavior: 'smooth' });
  } else {
    console.error('Contact section not found.');
  }
}

// Contact form submission event handling
const contactForm = document.getElementById('contactForm');
contactForm.addEventListener('submit', function (event) {
  event.preventDefault(); // Prevent default form submission
  
  // Gather form data
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const message = document.getElementById('message').value;

  // Basic form validation
  if (name && email && message) {
    alert('Thank you for contacting us! We will get back to you soon.');
    contactForm.reset(); // Reset form fields
  } else {
    alert('Please fill out all fields before submitting.');
  }
});
```
