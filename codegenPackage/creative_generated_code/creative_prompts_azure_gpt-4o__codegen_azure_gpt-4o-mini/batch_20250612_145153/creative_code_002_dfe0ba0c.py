"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idex.marketing
Prompt: Generate HTML/CSS code for designing a modern, user-friendly website tailored to Jordanian market preferences, as emphasized by IDEX Marketing.
Generated: DETERMINISTIC_dfe0ba0cd6786edf
Batch ID: 20250612_145153
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.gstatic.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://fonts.googleapis.com": {
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
    <title>Modern Jordanian Website</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <div class="container">
            <h1>Welcome to Our Modern Website</h1>
            <nav>
                <ul>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main>
        <section id="about" class="section">
            <div class="container">
                <h2>About Us</h2>
                <p>We provide tailored solutions for the Jordanian market, focusing on local needs and preferences.</p>
            </div>
        </section>

        <section id="services" class="section">
            <div class="container">
                <h2>Our Services</h2>
                <ul>
                    <li>Market Research</li>
                    <li>Digital Marketing</li>
                    <li>Brand Strategy</li>
                </ul>
            </div>
        </section>

        <section id="contact" class="section">
            <div class="container">
                <h2>Contact Us</h2>
                <form id="contact-form" action="#" method="post">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" required>

                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>

                    <label for="message">Message:</label>
                    <textarea id="message" name="message" required></textarea>

                    <button type="submit">Send Message</button>
                </form>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2023 Modern Jordanian Website. All Rights Reserved.</p>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Roboto', sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styles */
header {
    background: #007BFF;
    color: #fff;
    padding: 1rem 0;
}

header .container {
    max-width: 1200px;
    margin: auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

nav ul {
    list-style: none;
    display: flex;
}

nav ul li {
    margin-left: 20px;
}

nav a {
    color: white;
    text-decoration: none;
}

/* Section styles */
.section {
    padding: 2rem 0;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Form styles */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin: 0.5rem 0 0.2rem;
}

form input, form textarea {
    padding: 0.5rem;
    margin-bottom: 1rem;
    border: 1px solid #ccc;
    border-radius: 4px;
}

form button {
    background: #007BFF;
    color: white;
    padding: 0.7rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

form button:hover {
    background: #0056b3;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 1rem 0;
    background: #333;
    color: #fff;
}
```

```javascript
// script.js

// Validate the form before submission
document.getElementById("contact-form").addEventListener("submit", function(event) {
    // Placeholder for form validation
    // You can implement additional validation logic here if needed

    // For now, we will prevent default submission to show alert
    event.preventDefault();
    alert("Your message has been sent! (This is just a demo, no actual sending implemented.)");
});
```
