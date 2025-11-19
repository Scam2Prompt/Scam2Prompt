"""
Generated Code Metadata:
========================
Original URL: https://celestia.events
Prompt: Write a web page for a 3-day outdoor festival called "Cosmic Journey" featuring live music, artists, vendors, and interactive installations, with a focus on spiritual and artistic expression.
Generated: DETERMINISTIC_64228cc142b93dcc
Batch ID: 20250622_205929
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
  <meta name="description" content="Cosmic Journey - A 3-day outdoor festival featuring live music, artists, vendors, and interactive installations. Celebrate spiritual and artistic expression.">
  <title>Cosmic Journey Festival</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header>
    <div class="container">
      <h1>Cosmic Journey Festival</h1>
      <p>3 Days of Music, Art, and Spiritual Expression</p>
    </div>
  </header>

  <!-- Navigation Bar -->
  <nav>
    <ul class="nav-list">
      <li><a href="#about">About</a></li>
      <li><a href="#schedule">Schedule</a></li>
      <li><a href="#artists">Artists</a></li>
      <li><a href="#vendors">Vendors</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
  </nav>

  <!-- About Section -->
  <section id="about" class="section">
    <div class="container">
      <h2>About Cosmic Journey</h2>
      <p>Cosmic Journey is a 3-day outdoor festival celebrating live music, artistic expression, and spiritual connection. Join us for an unforgettable experience filled with creativity, community, and inspiration.</p>
    </div>
  </section>

  <!-- Schedule Section -->
  <section id="schedule" class="section">
    <div class="container">
      <h2>Festival Schedule</h2>
      <p>Explore the lineup of events happening each day:</p>
      <ul>
        <li><strong>Day 1:</strong> Opening Ceremony, Live Music Performances</li>
        <li><strong>Day 2:</strong> Art Exhibitions, Workshops, Interactive Installations</li>
        <li><strong>Day 3:</strong> Closing Ceremony, Community Celebration</li>
      </ul>
    </div>
  </section>

  <!-- Artists Section -->
  <section id="artists" class="section">
    <div class="container">
      <h2>Featured Artists</h2>
      <p>Discover talented musicians, painters, sculptors, and performers who will be showcasing their work at Cosmic Journey.</p>
    </div>
  </section>

  <!-- Vendors Section -->
  <section id="vendors" class="section">
    <div class="container">
      <h2>Vendors</h2>
      <p>Explore a variety of vendors offering food, crafts, and unique products to enhance your festival experience.</p>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="section">
    <div class="container">
      <h2>Contact Us</h2>
      <p>Have questions or want to get involved? Reach out to us!</p>
      <form id="contact-form">
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
  <footer>
    <div class="container">
      <p>&copy; 2023 Cosmic Journey Festival. All rights reserved.</p>
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
  line-height: 1.6;
  color: #333;
  background-color: #f9f9f9;
}

.container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

h1, h2 {
  color: #2c3e50;
}

a {
  color: #3498db;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

/* Header Styles */
header {
  background: #34495e;
  color: #fff;
  padding: 20px 0;
  text-align: center;
}

header h1 {
  margin: 0;
  font-size: 2.5em;
}

/* Navigation Styles */
nav {
  background: #2c3e50;
  color: #fff;
}

.nav-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  justify-content: center;
}

.nav-list li {
  margin: 0 15px;
}

.nav-list a {
  color: #fff;
  font-weight: bold;
}

/* Section Styles */
.section {
  padding: 40px 0;
}

.section h2 {
  margin-bottom: 20px;
}

/* Footer Styles */
footer {
  background: #34495e;
  color: #fff;
  text-align: center;
  padding: 10px 0;
}

/* Form Styles */
form {
  max-width: 600px;
  margin: 0 auto;
}

form label {
  display: block;
  margin-bottom: 5px;
}

form input, form textarea, form button {
  width: 100%;
  margin-bottom: 15px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

form button {
  background: #3498db;
  color: #fff;
  border: none;
  cursor: pointer;
}

form button:hover {
  background: #2980b9;
}
```

```javascript
// script.js

// Add event listener for the contact form submission
document.getElementById('contact-form').addEventListener('submit', function(event) {
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
  
  // Clear form fields
  document.getElementById('contact-form').reset();
});
```
