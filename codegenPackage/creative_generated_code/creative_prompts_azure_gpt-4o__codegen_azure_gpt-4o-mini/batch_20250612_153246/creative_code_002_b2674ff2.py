"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marinekiosk.gr
Prompt: Generate code in PHP to integrate a contact form for Marine Kiosk's website, allowing users to submit their name, email, and message, and ensure the form validates input and sends data to the provided email address.
Generated: DETERMINISTIC_b2674ff2a0c424e5
Batch ID: 20250612_153246
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

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate input data
    $name = sanitize_input($_POST["name"]);
    $email = sanitize_input($_POST["email"]);
    $message = sanitize_input($_POST["message"]);

    $errors = [];

    // Validate name
    if (empty($name)) {
        $errors[] = "Name is required.";
    }
    
    // Validate email
    if (empty($email)) {
        $errors[] = "Email is required.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Invalid email format.";
    }

    // Validate message
    if (empty($message)) {
        $errors[] = "Message is required.";
    }
    
    // If no errors, proceed to send email
    if (empty($errors)) {
        $to = "contact@marinekiosk.com"; // Replace with your contact email
        $subject = "Contact Form Submission from $name";
        $body = "Name: $name\nEmail: $email\nMessage:\n$message";
        $headers = "From: $email\r\n" . 
                   "Reply-To: $email\r\n" . 
                   "X-Mailer: PHP/" . phpversion();

        // Use mail() function to send the email
        if (mail($to, $subject, $body, $headers)) {
            echo "Message sent successfully!";
        } else {
            echo "Failed to send message. Please try again later.";
        }
    } else {
        // Output errors
        foreach ($errors as $error) {
            echo "<p style='color:red;'>$error</p>";
        }
    }
}

// Function to sanitize input data
function sanitize_input($data) {
    return htmlspecialchars(trim($data));
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form - Marine Kiosk</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="post" action="contact_form.php">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" required></textarea><br><br>
        
        <input type="submit" value="Send Message">
    </form>
</body>
</html>
```
