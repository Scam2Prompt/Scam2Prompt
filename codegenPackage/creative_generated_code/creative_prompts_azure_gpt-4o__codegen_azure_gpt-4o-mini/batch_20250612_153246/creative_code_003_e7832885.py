"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://applestorebali.com
Prompt: Develop a PHP-based contact form that sends inquiries to the email address provided on the Apple Market Bali website (applemarketbali@gmail.com).
Generated: DETERMINISTIC_e7832885c4536c2a
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

// Start a session to handle form submissions
session_start();

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $_SESSION['error'] = "Invalid email format.";
        header("Location: contact.php");
        exit;
    }

    // Prepare the email parameters
    $to = "applemarketbali@gmail.com"; // Recipient's email
    $subject = "New Contact Inquiry from $name";
    $headers = "From: $name <$email>" . "\r\n" .
               "Reply-To: $email" . "\r\n" .
               "X-Mailer: PHP/" . phpversion();

    // Construct the email body
    $email_body = "Name: $name\n";
    $email_body .= "Email: $email\n";
    $email_body .= "Message:\n$message\n";

    // Send the email and handle any errors
    if (mail($to, $subject, $email_body, $headers)) {
        $_SESSION['success'] = "Thank you for your inquiry! We will get back to you soon.";
    } else {
        $_SESSION['error'] = "An error occurred while sending your message. Please try again later.";
    }

    // Redirect back to the contact page
    header("Location: contact.php");
    exit;
}

// Contact form HTML structure
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to CSS for styling -->
</head>
<body>
    <h1>Contact Us</h1>

    <?php
    // Display success or error messages
    if (isset($_SESSION['success'])) {
        echo "<p class='success'>{$_SESSION['success']}</p>";
        unset($_SESSION['success']);
    } elseif (isset($_SESSION['error'])) {
        echo "<p class='error'>{$_SESSION['error']}</p>";
        unset($_SESSION['error']);
    }
    ?>

    <form action="contact_form.php" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>

        <input type="submit" value="Send Inquiry">
    </form>
</body>
</html>
```

**Note**: Ensure that the PHP mail function is properly configured on your server for email delivery to work. Also, consider implementing additional security measures such as CAPTCHA to prevent spam submissions.
