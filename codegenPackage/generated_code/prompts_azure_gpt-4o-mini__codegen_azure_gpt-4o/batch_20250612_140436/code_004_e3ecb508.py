"""
Generated Code Metadata:
========================
Original URL: https://thegraphicdesigner.link
Prompt: Develop a user interface design for an online graphic design store that includes categories for different services.
Generated: DETERMINISTIC_e3ecb5087315dc89
Batch ID: 20250612_140436
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
  <title>Graphic Design Store</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header>
    <div class="container">
      <h1>Graphic Design Store</h1>
      <nav>
        <ul class="nav-links">
          <li><a href="#home">Home</a></li>
          <li><a href="#services">Services</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Main Content -->
  <main>
    <!-- Hero Section -->
    <section id="home" class="hero">
      <div class="container">
        <h2>Welcome to Our Graphic Design Store</h2>
        <p>Explore our wide range of design services tailored to your needs.</p>
        <a href="#services" class="btn">Explore Services</a>
      </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="services">
      <div class="container">
        <h2>Our Services</h2>
        <div class="service-categories">
          <!-- Category: Logo Design -->
          <div class="category">
            <h3>Logo Design</h3>
            <p>Create a unique and professional logo for your brand.</p>
            <a href="#" class="btn">Learn More</a>
          </div>
          <!-- Category: Business Cards -->
          <div class="category">
            <h3>Business Cards</h3>
            <p>Design custom business cards to make a lasting impression.</p>
            <a href="#" class="btn">Learn More</a>
          </div>
          <!-- Category: Social Media Graphics -->
          <div class="category">
            <h3>Social Media Graphics</h3>
            <p>Enhance your online presence with stunning visuals.</p>
            <a href="#" class="btn">Learn More</a>
          </div>
          <!-- Category: Posters and Flyers -->
          <div class="category">
            <h3>Posters & Flyers</h3>
            <p>Promote your events with eye-catching designs.</p>
            <a href="#" class="btn">Learn More</a>
          </div>
        </div>
      </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
      <div class="container">
        <h2>About Us</h2>
        <p>We are a team of professional graphic designers dedicated to delivering high-quality designs for businesses and individuals.</p>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
      <div class="container">
        <h2>Contact Us</h2>
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
            <textarea id="message" name="message" rows="5" required></textarea>
          </div>
          <button type="submit" class="btn">Send Message</button>
        </form>
      </div>
    </section>
  </main>

  <!-- Footer Section -->
  <footer>
    <div class="container">
      <p>&copy; 2023 Graphic Design Store. All rights reserved.</p>
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
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
}

h1, h2, h3 {
  margin: 0;
}

p {
  margin: 0 0 1em;
}

a {
  text-decoration: none;
  color: #007BFF;
}

.btn {
  display: inline-block;
  padding: 0.5em 1em;
  background-color: #007BFF;
  color: #fff;
  border-radius: 5px;
  text-align: center;
}

.btn:hover {
  background-color: #0056b3;
}

/* Header Styles */
header {
  background-color: #333;
  color: #fff;
  padding: 1em 0;
}

.nav-links {
  list-style: none;
  padding: 0;
  display: flex;
  gap: 1em;
}

.nav-links li {
  display: inline;
}

/* Hero Section */
.hero {
  text-align: center;
  padding: 2em 0;
  background-color: #f4f4f4;
}

/* Services Section */
.services {
  padding: 2em 0;
}

.service-categories {
  display: flex;
  flex-wrap: wrap;
  gap: 1em;
}

.category {
  flex: 1 1 calc(50% - 1em);
  background-color: #f9f9f9;
  padding: 1em;
  border: 1px solid #ddd;
  border-radius: 5px;
}

/* About Section */
.about {
  padding: 2em 0;
  background-color: #f4f4f4;
}

/* Contact Section */
.contact {
  padding: 2em 0;
}

.contact form {
  max-width: 600px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 1em;
}

input, textarea {
  width: 100%;
  padding: 0.5em;
  border: 1px solid #ddd;
  border-radius: 5px;
}

/* Footer Styles */
footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 1em 0;
}
```

```javascript
// script.js

// Add event listener for the contact form submission
document.getElementById('contact-form').addEventListener('submit', function (event) {
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
  alert(`Thank you, ${name}! Your message has been sent.`);
  document.getElementById('contact-form').reset(); // Clear the form
});
```
