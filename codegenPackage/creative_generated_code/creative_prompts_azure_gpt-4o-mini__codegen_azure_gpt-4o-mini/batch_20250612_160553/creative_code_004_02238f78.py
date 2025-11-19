"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cymrepuestos.com.ar
Prompt: Illustrate how to implement a contact form in HTML that sends inquiries to CYM Repuestos, ensuring it includes fields for name, email, and message.
Generated: DETERMINISTIC_02238f78fdcb159b
Batch ID: 20250612_160553
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
    <title>Contact Us - CYM Repuestos</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to an external stylesheet -->
</head>
<body>

    <header>
        <h1>Contact CYM Repuestos</h1>
        <p>We would love to hear from you! Please fill in the form below.</p>
    </header>

    <main>
        <!-- Contact Form -->
        <form id="contactForm" action="send_email.php" method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required placeholder="Your Name">

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="Your Email">

            <label for="message">Message:</label>
            <textarea id="message" name="message" required placeholder="Your Message"></textarea>

            <button type="submit">Send Inquiry</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 CYM Repuestos. All rights reserved.</p>
    </footer>

    <script>
        // Simple form validation before submission
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();

            // Check if fields are filled out
            if (!name || !email || !message) {
                event.preventDefault(); // Prevent form from submitting
                alert('Please fill out all fields.');
            }
        });
    </script>
</body>
</html>
```

```php
<?php
// send_email.php

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check if email is valid
    if ($email === false) {
        die("Invalid email format.");
    }

    // Prepare the email
    $to = "info@cymrepuestos.com"; // Replace with your actual email
    $subject = "New Inquiry from Contact Form";
    $body = "Name: $name\nEmail: $email\nMessage:\n$message";
    $headers = "From: $email";

    // Attempt to send the email
    if (mail($to, $subject, $body, $headers)) {
        echo "Your message has been sent successfully!";
    } else {
        echo "There was a problem sending your message. Please try again later.";
    }
} else {
    // If the request method is not POST, show an error message
    die("Invalid request method.");
}
?>
```
