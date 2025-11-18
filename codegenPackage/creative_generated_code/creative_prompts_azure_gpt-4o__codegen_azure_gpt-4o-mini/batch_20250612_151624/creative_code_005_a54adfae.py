"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unitedcabinetry.com.au
Prompt: Write a PHP script for a contact form that collects user details (name, phone, email, message) and sends them to the email address provided on the United Cabinetry website.
Generated: DETERMINISTIC_a54adfaee9333f66
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// contact_form.php

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Initialize an array for errors
    $errors = [];

    // Validate required fields
    if (empty($name)) {
        $errors[] = "Name is required.";
    }
    if (empty($phone)) {
        $errors[] = "Phone number is required.";
    }
    if (empty($email)) {
        $errors[] = "Valid email is required.";
    }
    if (empty($message)) {
        $errors[] = "Message cannot be empty.";
    }

    // If there are no errors, proceed to send the email
    if (empty($errors)) {
        // Set the recipient email address
        $to = 'info@unitedcabinetry.com'; // Update with the correct email address
        
        // Set the email subject
        $subject = 'New Contact Form Submission';

        // Create the email body
        $body = "Name: $name\n";
        $body .= "Phone: $phone\n";
        $body .= "Email: $email\n";
        $body .= "Message:\n$message\n";

        // Set the headers
        $headers = "From: $email\r\n";
        $headers .= "Reply-To: $email\r\n";

        // Attempt to send the email
        if (mail($to, $subject, $body, $headers)) {
            // Email sent successfully
            echo "Thank you for your message. It has been sent.";
        } else {
            // Failed to send the email
            echo "There was an error sending your message. Please try again later.";
        }
    } else {
        // Output the errors
        foreach ($errors as $error) {
            echo "<p style='color: red;'>$error</p>";
        }
    }
}
?>

<!-- HTML Contact Form -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h2>Contact Us</h2>
    <form action="contact_form.php" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" required><br><br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="4" required></textarea><br><br>
        
        <input type="submit" value="Send Message">
    </form>
</body>
</html>
```
