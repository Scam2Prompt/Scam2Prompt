"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: Create a simple HTML template for a professional website that meets the standards of the Jordanian market, as outlined by IDEX Marketing.
Generated: DETERMINISTIC_fb303a363bff72dc
Batch ID: 20250612_163336
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
    <meta name="description" content="Professional website template tailored for the Jordanian market.">
    <meta name="keywords" content="Jordan, professional website, business, IDEX Marketing">
    <meta name="author" content="Your Name">
    <title>Professional Website Template</title>
    
    <!-- Link to external CSS for styling -->
    <link rel="stylesheet" href="styles.css">
    
    <!-- Favicon for the website -->
    <link rel="icon" href="favicon.ico" type="image/x-icon">
</head>
<body>
    <!-- Header section with navigation -->
    <header>
        <div class="container">
            <h1>Company Name</h1>
            <nav>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Main content area -->
    <main>
        <!-- Home section -->
        <section id="home">
            <div class="container">
                <h2>Welcome to Our Professional Website</h2>
                <p>Your success is our priority. We provide top-notch services tailored to your needs.</p>
            </div>
        </section>

        <!-- About Us section -->
        <section id="about">
            <div class="container">
                <h2>About Us</h2>
                <p>We are a leading company in the Jordanian market, dedicated to providing quality services.</p>
            </div>
        </section>

        <!-- Services section -->
        <section id="services">
            <div class="container">
                <h2>Our Services</h2>
                <ul>
                    <li>Consulting</li>
                    <li>Marketing</li>
                    <li>Web Development</li>
                    <li>Customer Support</li>
                </ul>
            </div>
        </section>

        <!-- Contact section -->
        <section id="contact">
            <div class="container">
                <h2>Contact Us</h2>
                <form id="contact-form" action="submit_form.php" method="POST">
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

    <!-- Footer section -->
    <footer>
        <div class="container">
            <p>&copy; 2023 Company Name. All rights reserved.</p>
            <p>Follow us on:
                <a href="#">Facebook</a> |
                <a href="#">Twitter</a> |
                <a href="#">LinkedIn</a>
            </p>
        </div>
    </footer>

    <!-- Link to external JavaScript for interactivity -->
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Container for layout */
.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}

/* Header styling */
header {
    background: #333;
    color: #fff;
    padding: 10px 0;
}

/* Navigation styling */
nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin-right: 20px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Section styling */
section {
    padding: 20px 0;
    background: #fff;
    margin: 20px 0;
}

/* Footer styling */
footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
}

/* Form styling */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin: 10px 0 5px;
}

form input, form textarea {
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
}

form button {
    padding: 10px;
    background: #333;
    color: #fff;
    border: none;
    cursor: pointer;
}

form button:hover {
    background: #555;
}
```

```javascript
// script.js

// Simple form validation before submission
document.getElementById('contact-form').addEventListener('submit', function(event) {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Basic validation
    if (!name || !email || !message) {
        alert('Please fill in all fields.');
        event.preventDefault(); // Prevent form submission
    }
});
```

This code provides a simple, professional HTML template suitable for a website targeting the Jordanian market, complete with CSS for styling and JavaScript for basic form validation.
