"""
Generated Code Metadata:
========================
Original URL: https://haus-alpenrose.com
Prompt: Generate HTML and CSS code for a simple website homepage, similar to Haus Alpenrose, with sections for accommodations, location, and contact information.
Generated: DETERMINISTIC_c16930ba63053b8b
Batch ID: 20250622_205025
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3153.835434509123!2d-122.419415684681!3d37.77492927975995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80858064f0f0f0f0%3A0x0!2zTWFwIFBvaW50!5e0!3m2!1sen!2sus!4v1633024800000!5m2!1sen!2sus": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Welcome to Haus Alpenrose - Your perfect getaway. Explore our accommodations, location, and contact us for more information.">
    <title>Haus Alpenrose</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header class="header">
        <div class="container">
            <h1>Haus Alpenrose</h1>
            <p>Your perfect getaway in the mountains</p>
        </div>
    </header>

    <!-- Accommodations Section -->
    <section id="accommodations" class="section">
        <div class="container">
            <h2>Accommodations</h2>
            <p>We offer cozy rooms and suites with breathtaking views of the mountains. Perfect for families, couples, and solo travelers.</p>
            <ul>
                <li>Single Rooms</li>
                <li>Double Rooms</li>
                <li>Family Suites</li>
            </ul>
        </div>
    </section>

    <!-- Location Section -->
    <section id="location" class="section">
        <div class="container">
            <h2>Location</h2>
            <p>Located in the heart of the Alps, Haus Alpenrose is surrounded by stunning landscapes and offers easy access to hiking trails, ski resorts, and local attractions.</p>
            <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3153.835434509123!2d-122.419415684681!3d37.77492927975995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80858064f0f0f0f0%3A0x0!2zTWFwIFBvaW50!5e0!3m2!1sen!2sus!4v1633024800000!5m2!1sen!2sus" 
                width="600" 
                height="450" 
                style="border:0;" 
                allowfullscreen="" 
                loading="lazy">
            </iframe>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section">
        <div class="container">
            <h2>Contact Us</h2>
            <p>Have questions or want to book your stay? Reach out to us!</p>
            <form action="/submit" method="POST">
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
            <p>&copy; 2023 Haus Alpenrose. All rights reserved.</p>
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
    padding: 20px;
}

/* Header */
.header {
    background-color: #4CAF50;
    color: white;
    text-align: center;
    padding: 20px 0;
}

.header h1 {
    font-size: 2.5em;
}

.header p {
    font-size: 1.2em;
}

/* Section Styling */
.section {
    margin: 40px 0;
    padding: 20px;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.section h2 {
    font-size: 2em;
    margin-bottom: 20px;
}

.section p {
    margin-bottom: 20px;
}

.section ul {
    list-style-type: disc;
    margin-left: 20px;
}

/* Form Styling */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin-bottom: 5px;
    font-weight: bold;
}

form input, form textarea, form button {
    margin-bottom: 15px;
    padding: 10px;
    font-size: 1em;
    border: 1px solid #ccc;
    border-radius: 4px;
}

form button {
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
}

form button:hover {
    background-color: #45a049;
}

/* Footer */
.footer {
    text-align: center;
    padding: 20px 0;
    background-color: #333;
    color: white;
}

.footer p {
    font-size: 0.9em;
}
```
