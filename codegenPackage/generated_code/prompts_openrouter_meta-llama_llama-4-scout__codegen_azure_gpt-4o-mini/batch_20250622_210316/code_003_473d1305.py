"""
Generated Code Metadata:
========================
Original URL: https://dionlineaja.id
Prompt: Create a design portfolio website using Photoshop, Illustrator, and CSS3 for a company that has completed 59 projects and has 18 clients.
Generated: DETERMINISTIC_473d1305079ca2af
Batch ID: 20250622_210316
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
    <title>Design Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Design Portfolio</h1>
        <nav>
            <ul>
                <li><a href="#about">About</a></li>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#clients">Clients</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <section id="about">
        <h2>About Us</h2>
        <p>We are a creative agency with a passion for design. Our team has completed 59 projects for 18 clients.</p>
    </section>

    <section id="projects">
        <h2>Our Projects</h2>
        <div class="project-list">
            <!-- Example project item -->
            <div class="project-item">
                <img src="project1.jpg" alt="Project 1">
                <h3>Project Title 1</h3>
                <p>Brief description of Project 1.</p>
            </div>
            <!-- Repeat for other projects -->
        </div>
    </section>

    <section id="clients">
        <h2>Our Clients</h2>
        <ul>
            <li>Client 1</li>
            <li>Client 2</li>
            <li>Client 3</li>
            <li>Client 4</li>
            <li>Client 5</li>
            <!-- Add more clients as needed -->
        </ul>
    </section>

    <section id="contact">
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
    </section>

    <footer>
        <p>&copy; 2023 Design Portfolio. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, h3, p, ul, li {
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

.project-list {
    display: flex;
    flex-wrap: wrap;
}

.project-item {
    border: 1px solid #ccc;
    margin: 10px;
    padding: 10px;
    width: calc(33% - 20px); /* Responsive layout */
}

.project-item img {
    max-width: 100%;
    height: auto;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #333;
    color: #fff;
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

```php
<?php
// submit_form.php

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check for valid email
    if ($email === false) {
        die("Invalid email format.");
    }

    // Prepare email
    $to = "info@designportfolio.com"; // Change to your email
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
    echo "Invalid request method.";
}
?>
```

```javascript
// script.js

// Add any necessary JavaScript functionality here
document.getElementById('contact-form').addEventListener('submit', function(event) {
    // Optional: Add form validation or other functionality
    alert('Form submitted successfully!');
});
```

This code provides a complete design portfolio website with HTML, CSS, PHP for form handling, and JavaScript for basic interactivity. Ensure to replace placeholder content and paths with actual data and files as needed.
