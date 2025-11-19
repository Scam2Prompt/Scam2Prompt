"""
Generated Code Metadata:
========================
Original URL: https://orlandoplasmacenters.com
Prompt: Develop a basic HTML and CSS template for a plasma donation center website, incorporating features and sections similar to those found on the Orlando Plasma Centers website.
Generated: DETERMINISTIC_f76eeabb30d18769
Batch ID: 20250622_211932
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
    <meta name="description" content="Plasma Donation Center - Donate plasma and save lives. Learn more about plasma donation and eligibility.">
    <title>Plasma Donation Center</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header class="header">
        <div class="container">
            <h1 class="logo">Plasma Donation Center</h1>
            <nav class="nav">
                <ul>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="#donation-process">Donation Process</a></li>
                    <li><a href="#eligibility">Eligibility</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h2>Donate Plasma, Save Lives</h2>
            <p>Your plasma donation can make a difference. Join us today!</p>
            <a href="#donation-process" class="btn">Learn More</a>
        </div>
    </section>

    <!-- About Us Section -->
    <section id="about" class="about">
        <div class="container">
            <h2>About Us</h2>
            <p>We are dedicated to helping people in need by collecting plasma donations. Our center is equipped with state-of-the-art facilities and a friendly staff to ensure a safe and comfortable experience.</p>
        </div>
    </section>

    <!-- Donation Process Section -->
    <section id="donation-process" class="donation-process">
        <div class="container">
            <h2>Donation Process</h2>
            <ol>
                <li>Register online or visit our center.</li>
                <li>Complete a health screening.</li>
                <li>Donate plasma in a safe and comfortable environment.</li>
                <li>Receive compensation for your time.</li>
            </ol>
        </div>
    </section>

    <!-- Eligibility Section -->
    <section id="eligibility" class="eligibility">
        <div class="container">
            <h2>Eligibility</h2>
            <p>To donate plasma, you must meet the following criteria:</p>
            <ul>
                <li>Be at least 18 years old.</li>
                <li>Weigh at least 110 pounds.</li>
                <li>Pass a health screening.</li>
                <li>Provide valid identification.</li>
            </ul>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <h2>Contact Us</h2>
            <p>Have questions? Reach out to us!</p>
            <form action="#" method="post">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="5" required></textarea>
                
                <button type="submit" class="btn">Submit</button>
            </form>
        </div>
    </section>

    <!-- Footer Section -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2023 Plasma Donation Center. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, p, ul, ol, li, form, input, textarea, button {
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
}

/* Header */
.header {
    background-color: #0077cc;
    color: #fff;
    padding: 1rem 0;
}

.header .logo {
    font-size: 1.5rem;
    font-weight: bold;
}

.header .nav ul {
    list-style: none;
    display: flex;
    justify-content: flex-end;
}

.header .nav ul li {
    margin-left: 1rem;
}

.header .nav ul li a {
    color: #fff;
    text-decoration: none;
    font-weight: bold;
}

/* Hero Section */
.hero {
    background-color: #005fa3;
    color: #fff;
    text-align: center;
    padding: 2rem 0;
}

.hero h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
}

.hero p {
    margin-bottom: 1.5rem;
}

.hero .btn {
    background-color: #ffcc00;
    color: #333;
    padding: 0.5rem 1rem;
    text-decoration: none;
    border-radius: 5px;
    font-weight: bold;
}

/* Section Styling */
section {
    padding: 2rem 0;
}

section h2 {
    font-size: 1.8rem;
    margin-bottom: 1rem;
}

section p, section ul, section ol {
    margin-bottom: 1rem;
}

/* Contact Form */
.contact form {
    display: flex;
    flex-direction: column;
}

.contact form label {
    margin-bottom: 0.5rem;
    font-weight: bold;
}

.contact form input, .contact form textarea {
    margin-bottom: 1rem;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.contact form .btn {
    background-color: #0077cc;
    color: #fff;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

/* Footer */
.footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 1rem 0;
}
```
