"""
Generated Code Metadata:
========================
Original URL: https://yourmaidinheaven.com
Prompt: Create a sample marketing website content for a cleaning services company, highlighting the benefits of their services and what sets them apart from competitors.
Generated: DETERMINISTIC_cd673b4cc34bf8c7
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GreenClean - Professional Cleaning Services</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="home">
        <h1>Welcome to GreenClean</h1>
        <p>Professional cleaning services for a healthier environment</p>
        <button>Learn More</button>
    </section>

    <!-- Services Section -->
    <section id="services">
        <h2>Our Services</h2>
        <div class="service-cards">
            <div class="card">
                <h3>Residential Cleaning</h3>
                <p>Our team provides thorough and efficient cleaning services for homes of all sizes.</p>
            </div>
            <div class="card">
                <h3>Commercial Cleaning</h3>
                <p>We offer customized cleaning solutions for offices, restaurants, and other businesses.</p>
            </div>
            <div class="card">
                <h3>Special Event Cleaning</h3>
                <p>Let us handle the cleaning after your event, so you can focus on what matters.</p>
            </div>
        </div>
    </section>

    <!-- Benefits Section -->
    <section>
        <h2>What Sets Us Apart</h2>
        <ul>
            <li><strong>Eco-Friendly Products</strong>: We use environmentally friendly cleaning products that are safe for people and pets.</li>
            <li><strong>Experienced Staff</strong>: Our team is thoroughly trained and background-checked for your peace of mind.</li>
            <li><strong>Customized Services</strong>: We tailor our services to meet your specific needs and schedule.</li>
        </ul>
    </section>

    <!-- About Section -->
    <section id="about">
        <h2>About Us</h2>
        <p>At GreenClean, we're dedicated to providing top-notch cleaning services while promoting sustainability and customer satisfaction.</p>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <h2>Get in Touch</h2>
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>

            <button type="submit">Send</button>
        </form>
    </section>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

header nav ul li {
    display: inline-block;
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

#home {
    background-image: linear-gradient(to bottom, #f7f7f7, #fff);
    padding: 5em;
    text-align: center;
}

#home button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

.service-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.card {
    background-color: #f7f7f7;
    margin: 20px;
    padding: 20px;
    width: 200px;
    text-align: center;
}

.card h3 {
    margin-top: 0;
}

ul {
    list-style: none;
    padding: 0;
}

li {
    margin-bottom: 10px;
}

label {
    display: block;
    margin-bottom: 10px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}
```

```javascript
// script.js

// Add event listener to form submission
document.querySelector('form').addEventListener('submit', (e) => {
    e.preventDefault();

    // Get form data
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Validate form data
    if (name && email && message) {
        // Send data to server or handle as needed
        console.log('Form submitted:', { name, email, message });

        // Reset form
        document.querySelector('form').reset();
    } else {
        alert('Please fill out all fields.');
    }
});
```
