"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afebi.org
Prompt: Generate a code snippet in PHP to send a contact message to AFEBI's official email address, including fields for name, email, and message.
Generated: DETERMINISTIC_e2736ad831af259f
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Sends a contact message to AFEBI's official email address.
 *
 * This script collects user input from a form and sends it via email.
 * It includes basic validation and error handling to ensure that
 * the email is sent successfully.
 */

// Define the recipient email address
define('RECIPIENT_EMAIL', 'contact@afebi.org'); // Replace with the actual email address

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Collect and sanitize input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Validate inputs
    $errors = [];
    if (empty($name)) {
        $errors[] = 'Name is required.';
    }
    if (empty($email)) {
        $errors[] = 'A valid email address is required.';
    }
    if (empty($message)) {
        $errors[] = 'Message cannot be empty.';
    }

    // If there are validation errors, display them
    if (!empty($errors)) {
        foreach ($errors as $error) {
            echo "<p style='color: red;'>$error</p>";
        }
    } else {
        // Prepare email headers
        $subject = 'New Contact Message from ' . $name;
        $headers = "From: $name <$email>" . "\r\n" .
                   "Reply-To: $email" . "\r\n" .
                   "X-Mailer: PHP/" . phpversion();

        // Send the email
        if (mail(RECIPIENT_EMAIL, $subject, $message, $headers)) {
            echo "<p style='color: green;'>Message sent successfully!</p>";
        } else {
            echo "<p style='color: red;'>Failed to send the message. Please try again later.</p>";
        }
    }
}
?>

<!-- HTML Form for user input -->
<form action="" method="POST">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    <br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    <br>
    <label for="message">Message:</label>
    <textarea id="message" name="message" required></textarea>
    <br>
    <button type="submit">Send Message</button>
</form>
```
