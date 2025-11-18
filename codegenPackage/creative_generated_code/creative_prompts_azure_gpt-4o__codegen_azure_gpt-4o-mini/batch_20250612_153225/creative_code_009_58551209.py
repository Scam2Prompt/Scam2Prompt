"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morevacare.com
Prompt: Write PHP code to implement a "contact us" form for an e-commerce website, ensuring compliance with GDPR, as seen in MorevaCare's legal section.
Generated: DETERMINISTIC_5855120953227037
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// contact.php

// Start the session
session_start();

// Load configuration variables (e.g., email recipients)
require 'config.php';

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate and sanitize inputs
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);
    $privacyConsent = isset($_POST['privacy_consent']);

    // Initialize an array to hold error messages
    $errors = [];

    // Validate the inputs
    if (empty($name)) {
        $errors[] = "Name is required.";
    }
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "A valid email is required.";
    }
    if (empty($message)) {
        $errors[] = "Message cannot be empty.";
    }
    if (!$privacyConsent) {
        $errors[] = "You must consent to the privacy policy.";
    }

    // If there are errors, store them in the session and redirect back
    if (!empty($errors)) {
        $_SESSION['errors'] = $errors;
        header("Location: contact_form.php");
        exit();
    }

    // Prepare email headers
    $to = CONTACT_EMAIL; // Set this in your config.php
    $subject = "New Contact Us Form Submission";
    $headers = "From: $name <$email>\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Prepare the email body
    $body = "Name: $name\nEmail: $email\nMessage:\n$message";

    // Send the email and handle potential errors
    if (mail($to, $subject, $body, $headers)) {
        // Success message
        $_SESSION['success'] = "Your message has been sent successfully.";
    } else {
        // Error message
        $_SESSION['errors'][] = "There was an error sending your message. Please try again later.";
    }

    // Redirect back to the contact form
    header("Location: contact_form.php");
    exit();
}

?>

<!-- contact_form.php -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>

    <?php
    // Display success or error messages
    if (isset($_SESSION['success'])) {
        echo "<p style='color: green;'>".$_SESSION['success']."</p>";
        unset($_SESSION['success']);
    }
    if (isset($_SESSION['errors'])) {
        echo "<ul style='color: red;'>";
        foreach ($_SESSION['errors'] as $error) {
            echo "<li>$error</li>";
        }
        echo "</ul>";
        unset($_SESSION['errors']);
    }
    ?>

    <form action="contact.php" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="4" required></textarea><br>

        <label>
            <input type="checkbox" name="privacy_consent" required>
            I consent to the processing of my personal data in accordance with the privacy policy.
        </label><br>

        <input type="submit" value="Send Message">
    </form>
</body>
</html>
```

```php
<?php
// config.php

// Define constants for configuration
define('CONTACT_EMAIL', 'contact@example.com'); // Change to actual contact email
?>
```
