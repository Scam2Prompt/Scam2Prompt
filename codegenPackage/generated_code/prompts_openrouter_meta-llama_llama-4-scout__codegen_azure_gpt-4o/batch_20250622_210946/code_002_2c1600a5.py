"""
Generated Code Metadata:
========================
Original URL: https://dtcgroup.in
Prompt: "Generate a JavaScript code to create a simple website layout for a real estate project, like DTC Group's Southern Heights, including features like property listings, amenities, and contact information."
Generated: DETERMINISTIC_2c1600a538fbb4a5
Batch ID: 20250622_210946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// HTML Structure
const htmlContent = `
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Southern Heights - Real Estate</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <h1>Southern Heights</h1>
    <nav>
      <ul>
        <li><a href="#properties">Properties</a></li>
        <li><a href="#amenities">Amenities</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <section id="properties">
      <h2>Property Listings</h2>
      <div id="property-list"></div>
    </section>
    <section id="amenities">
      <h2>Amenities</h2>
      <ul>
        <li>Swimming Pool</li>
        <li>Gym</li>
        <li>24/7 Security</li>
        <li>Children's Play Area</li>
      </ul>
    </section>
    <section id="contact">
      <h2>Contact Us</h2>
      <form id="contact-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
        <button type="submit">Submit</button>
      </form>
    </section>
  </main>
  <footer>
    <p>&copy; 2023 Southern Heights. All rights reserved.</p>
  </footer>
  <script src="script.js"></script>
</body>
</html>
`;

// CSS Styles
const cssContent = `
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

header {
  background-color: #333;
  color: #fff;
  padding: 1rem;
  text-align: center;
}

nav ul {
  list-style: none;
  padding: 0;
}

nav ul li {
  display: inline;
  margin: 0 1rem;
}

nav ul li a {
  color: #fff;
  text-decoration: none;
}

main {
  padding: 2rem;
}

section {
  margin-bottom: 2rem;
}

footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 1rem;
}
`;

// JavaScript Functionality
const jsContent = `
document.addEventListener('DOMContentLoaded', () => {
  // Property Listings Data
  const properties = [
    { name: '2 BHK Apartment', price: '$120,000', description: 'Spacious 2-bedroom apartment with modern amenities.' },
    { name: '3 BHK Apartment', price: '$180,000', description: 'Luxurious 3-bedroom apartment with a great view.' },
    { name: 'Villa', price: '$300,000', description: 'Beautiful villa with private garden and pool.' }
  ];

  // Render Property Listings
  const propertyList = document.getElementById('property-list');
  properties.forEach(property => {
    const propertyDiv = document.createElement('div');
    propertyDiv.className = 'property';
    propertyDiv.innerHTML = `
      <h3>${property.name}</h3>
      <p>Price: ${property.price}</p>
      <p>${property.description}</p>
    `;
    propertyList.appendChild(propertyDiv);
  });

  // Handle Contact Form Submission
  const contactForm = document.getElementById('contact-form');
  contactForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    if (!name || !email || !message) {
      alert('Please fill out all fields.');
      return;
    }

    // Simulate form submission
    alert('Thank you for your message! We will get back to you soon.');
    contactForm.reset();
  });
});
`;

// Create Files
const fs = require('fs');

// Write HTML file
fs.writeFileSync('index.html', htmlContent);

// Write CSS file
fs.writeFileSync('styles.css', cssContent);

// Write JavaScript file
fs.writeFileSync('script.js', jsContent);

console.log('Website files generated successfully!');
```
