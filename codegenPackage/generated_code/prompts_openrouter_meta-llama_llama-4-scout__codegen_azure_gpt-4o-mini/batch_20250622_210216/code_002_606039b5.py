"""
Generated Code Metadata:
========================
Original URL: https://lestersplace.com
Prompt: Generate a code snippet to create a simple website for an assisted living facility, including pages for About Us, Services, and Contact Us, with a focus on compassion and empowerment.
Generated: DETERMINISTIC_606039b583e27bef
Batch ID: 20250622_210216
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
    <title>Compassionate Living - Assisted Living Facility</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Compassionate Living</h1>
        <nav>
            <ul>
                <li><a href="#about">About Us</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact Us</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="about">
            <h2>About Us</h2>
            <p>At Compassionate Living, we believe in empowering our residents through compassionate care and support. Our facility is designed to provide a nurturing environment where individuals can thrive.</p>
        </section>

        <section id="services">
            <h2>Our Services</h2>
            <ul>
                <li>24/7 Nursing Care</li>
                <li>Personalized Meal Plans</li>
                <li>Recreational Activities</li>
                <li>Transportation Services</li>
                <li>Assistance with Daily Living</li>
            </ul>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contactForm" action="submit_form.php" method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>

                <button type="submit">Send Message</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Compassionate Living. All rights reserved.</p>
    </footer>

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

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styles */
header {
    background: #4CAF50;
    color: white;
    padding: 10px 0;
    text-align: center;
}

/* Navigation styles */
nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: white;
    text-decoration: none;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Section styles */
section {
    margin-bottom: 20px;
    padding: 15px;
    background: white;
    border-radius: 5px;
}

/* Form styles */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin-bottom: 5px;
}

form input, form textarea {
    margin-bottom: 15px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

form button {
    padding: 10px;
    background: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

form button:hover {
    background: #45a049;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #333;
    color: white;
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
    $to = "info@compassionateliving.com"; // Change to your email
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
document.getElementById('contactForm').addEventListener('submit', function(event) {
    // Optional: Add client-side validation or other functionality
    alert('Thank you for reaching out! We will get back to you soon.');
});
```
