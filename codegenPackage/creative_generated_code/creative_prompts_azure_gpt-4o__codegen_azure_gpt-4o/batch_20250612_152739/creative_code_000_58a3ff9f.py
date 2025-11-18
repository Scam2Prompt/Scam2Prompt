"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dionlineaja.id
Prompt: Write HTML5 and CSS3 code for a corporate design webpage that includes sections for "About Us," "Clients," and "Contact," similar to the structure described on dionlineaja.id.
Generated: DETERMINISTIC_58a3ff9fb18d919e
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Corporate webpage featuring About Us, Clients, and Contact sections">
    <meta name="author" content="Your Company Name">
    <title>Corporate Design Webpage</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <h1>Your Company Name</h1>
            <nav>
                <ul>
                    <li><a href="#about-us">About Us</a></li>
                    <li><a href="#clients">Clients</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- About Us Section -->
    <section id="about-us" class="about-us">
        <div class="container">
            <h2>About Us</h2>
            <p>Welcome to our company. We specialize in delivering top-notch solutions to our customers, ensuring their success in every venture. Our team of experts is dedicated to providing quality service and innovation.</p>
        </div>
    </section>

    <!-- Clients Section -->
    <section id="clients" class="clients">
        <div class="container">
            <h2>Clients</h2>
            <p>We are proud to have partnered with some of the biggest names in the industry. Our clients include:</p>
            <ul>
                <li>Client A</li>
                <li>Client B</li>
                <li>Client C</li>
            </ul>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <h2>Contact</h2>
            <p>Have questions or need assistance? Reach out to us:</p>
            <form action="/submit-form" method="POST">
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
            <p>&copy; 2023 Your Company Name. All rights reserved.</p>
        </div>
    </footer>
</body>

</html>
```

```css
/* styles.css */

/* General Reset */
* {
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

/* Container Utility */
.container {
    width: 80%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* Header Styling */
header {
    background-color: #004080;
    color: #fff;
    padding: 20px 0;
}

header h1 {
    font-size: 2rem;
    text-align: center;
}

header nav ul {
    list-style: none;
    text-align: center;
    margin-top: 10px;
}

header nav ul li {
    display: inline;
    margin: 0 10px;
}

header nav ul li a {
    color: #fff;
    text-decoration: none;
    font-weight: bold;
}

/* Section Styling */
section {
    margin: 40px 0;
}

section h2 {
    text-align: center;
    font-size: 1.8rem;
    margin-bottom: 20px;
}

section p {
    text-align: center;
    margin-bottom: 15px;
}

section ul {
    text-align: center;
    list-style: none;
    padding: 0;
}

section ul li {
    margin: 5px 0;
}

/* Contact Form Styling */
form {
    max-width: 600px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
}

form label {
    margin: 10px 0 5px;
}

form input, form textarea {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

form button {
    margin-top: 15px;
    padding: 10px;
    background-color: #004080;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

form button:hover {
    background-color: #003060;
}

/* Footer Styling */
footer {
    background-color: #004080;
    color: #fff;
    text-align: center;
    padding: 10px 0;
}

footer p {
    font-size: 0.9rem;
}
```
