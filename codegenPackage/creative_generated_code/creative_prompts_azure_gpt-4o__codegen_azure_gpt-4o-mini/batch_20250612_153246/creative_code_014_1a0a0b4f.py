"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rankraze.fr
Prompt: Generate a landing page design for a digital marketing agency, incorporating Rankraze's branding principles and 3R formula.
Generated: DETERMINISTIC_1a0a0b4f9e9bf70d
Batch ID: 20250612_153246
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
    <meta name="description" content="Digital Marketing Agency - Rankraze">
    <title>Rankraze - Digital Marketing Agency</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="icon" href="favicon.ico" type="image/x-icon">
</head>

<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <h1 class="logo">Rankraze</h1>
            <nav>
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
            <h2>Boost Your Online Presence</h2>
            <p>We leverage the 3R formula: Reach, Relevance, and Results to drive success for your brand.</p>
            <a href="#contact" class="cta-button">Get Started</a>
        </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="services">
        <div class="container">
            <h2>Our Services</h2>
            <div class="service-item">
                <h3>Search Engine Optimization</h3>
                <p>Optimize your website to rank higher in search engines and attract more organic traffic.</p>
            </div>
            <div class="service-item">
                <h3>Social Media Marketing</h3>
                <p>Engage with your audience on social media platforms and build your brand's presence.</p>
            </div>
            <div class="service-item">
                <h3>Content Marketing</h3>
                <p>Create valuable content to attract and engage your target audience effectively.</p>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <h2>About Us</h2>
            <p>At Rankraze, we are dedicated to helping businesses grow through innovative digital marketing strategies.</p>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
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

    <!-- Footer Section -->
    <footer>
        <div class="container">
            <p>&copy; 2023 Rankraze. All Rights Reserved.</p>
        </div>
    </footer>

    <script src="script.js"></script>
</body>

</html>
```

```css
/* styles.css */

/* Global Styles */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    line-height: 1.6;
}

/* Container for centering content */
.container {
    width: 80%;
    margin: 0 auto;
}

/* Header Styles */
header {
    background: #333;
    color: #fff;
    padding: 20px 0;
}

header .logo {
    float: left;
}

header nav ul {
    list-style: none;
    padding: 0;
}

header nav ul li {
    display: inline;
    margin-left: 20px;
}

header nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Hero Section Styles */
.hero {
    background: #5c67f2;
    color: #fff;
    padding: 60px 0;
    text-align: center;
}

.cta-button {
    background: #fff;
    color: #5c67f2;
    padding: 10px 20px;
    text-decoration: none;
}

/* Services Styles */
.services {
    padding: 40px 0;
    background: #f4f4f4;
}

.service-item {
    margin-bottom: 20px;
}

/* About Section Styles */
.about {
    padding: 40px 0;
}

/* Contact Section Styles */
.contact {
    padding: 40px 0;
}

.contact form {
    display: flex;
    flex-direction: column;
}

.contact form input,
.contact form textarea {
    margin-bottom: 10px;
    padding: 10px;
    font-size: 16px;
}

/* Footer Styles */
footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 20px 0;
}
```

```javascript
// script.js

// This script handles the form submission and provides basic client-side validation
document.getElementById("contact-form").addEventListener("submit", function (event) {
    // Prevent form submission if any input is invalid
    let isValid = true;
    const inputs = this.querySelectorAll("input, textarea");

    inputs.forEach(input => {
        if (!input.value) {
            isValid = false;
            input.classList.add("error");
        } else {
            input.classList.remove("error");
        }
    });

    if (!isValid) {
        event.preventDefault(); // Stop form submission
        alert("Please fill in all fields.");
    }
});
```

```php
<?php
// submit_form.php

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve form data and sanitize it
    $name = htmlspecialchars(trim($_POST['name']));
    $email = htmlspecialchars(trim($_POST['email']));
    $message = htmlspecialchars(trim($_POST['message']));

    // Validate email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Invalid email format");
    }

    // Here you would typically send the data to your database or email
    // For demonstration purposes, we will just echo the values
    echo "Name: $name<br>Email: $email<br>Message: $message";

    // Respond with success message
    http_response_code(200);
} else {
    // Respond with an error if accessed incorrectly
    http_response_code(405);
    die("Method Not Allowed");
}
?>
```

This code represents a complete landing page design for a digital marketing agency, following best practices and including error handling in the form processing script.
