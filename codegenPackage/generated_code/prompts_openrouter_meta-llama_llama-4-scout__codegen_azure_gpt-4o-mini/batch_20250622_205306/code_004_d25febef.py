"""
Generated Code Metadata:
========================
Original URL: https://caraproductions.co.ke
Prompt: Develop a photography portfolio website for a Kenyan photographer, inspired by Cara Productions' photography services.
Generated: DETERMINISTIC_d25febef3552c1b1
Batch ID: 20250622_205306
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
    <title>Kenyan Photographer Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Kenyan Photographer Portfolio</h1>
        <nav>
            <ul>
                <li><a href="#about">About</a></li>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <section id="about">
        <h2>About Me</h2>
        <p>Welcome to my photography portfolio! I am a passionate photographer based in Kenya, specializing in capturing the beauty of nature, wildlife, and special moments.</p>
    </section>

    <section id="portfolio">
        <h2>Portfolio</h2>
        <div class="gallery">
            <img src="images/photo1.jpg" alt="Wildlife Photography" />
            <img src="images/photo2.jpg" alt="Nature Photography" />
            <img src="images/photo3.jpg" alt="Event Photography" />
            <img src="images/photo4.jpg" alt="Portrait Photography" />
        </div>
    </section>

    <section id="services">
        <h2>Services</h2>
        <ul>
            <li>Wildlife Photography</li>
            <li>Event Photography</li>
            <li>Portrait Photography</li>
            <li>Nature Photography</li>
        </ul>
    </section>

    <section id="contact">
        <h2>Contact Me</h2>
        <form id="contact-form" action="submit_form.php" method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>

            <button type="submit">Send Message</button>
        </form>
    </section>

    <footer>
        <p>&copy; 2023 Kenyan Photographer. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, p, ul, li {
    margin: 0;
    padding: 0;
}

/* Basic styling for body */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

/* Header styles */
header {
    background: #333;
    color: #fff;
    padding: 10px 0;
    text-align: center;
}

nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Section styles */
section {
    padding: 20px;
    margin: 20px 0;
}

/* Gallery styles */
.gallery {
    display: flex;
    flex-wrap: wrap;
}

.gallery img {
    width: 100%;
    max-width: 300px;
    margin: 10px;
}

/* Form styles */
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
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #333;
    color: #fff;
}
```

```php
<?php
// submit_form.php

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check for valid email
    if ($email === false) {
        die("Invalid email format.");
    }

    // Prepare email
    $to = "photographer@example.com"; // Replace with your email
    $subject = "New Contact Form Submission";
    $body = "Name: $name\nEmail: $email\nMessage: $message";
    $headers = "From: $email";

    // Send email
    if (mail($to, $subject, $body, $headers)) {
        echo "Message sent successfully!";
    } else {
        echo "Failed to send message. Please try again later.";
    }
} else {
    // Handle invalid access
    http_response_code(405);
    echo "Method Not Allowed";
}
?>
```

```javascript
// script.js

// Add any necessary JavaScript functionality here
document.getElementById('contact-form').addEventListener('submit', function(event) {
    // Optional: Add form validation or other functionality before submission
    alert('Thank you for your message! We will get back to you soon.');
});
```

This code provides a complete photography portfolio website with HTML, CSS, PHP, and JavaScript, following best practices and including error handling.
