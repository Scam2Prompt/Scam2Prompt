"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hdadpanaderos.es
Prompt: How can I implement a form submission in PHP to contact the Hermandad de los Panaderos for inquiries?
Generated: DETERMINISTIC_e9ddd5c82b583f1d
Batch ID: 20250612_155936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// This script handles form submission for contacting Hermandad de los Panaderos.

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Sanitize and validate inputs
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Initialize an array to hold errors
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

    // If there are no errors, proceed to send the email
    if (empty($errors)) {
        // Email details
        $to = "contact@hermandaddelospanaderos.com"; // Replace with actual recipient email
        $subject = "Inquiry from " . $name;
        $body = "Name: $name\nEmail: $email\n\nMessage:\n$message";
        $headers = "From: $email\r\nReply-To: $email";

        // Attempt to send the email
        if (mail($to, $subject, $body, $headers)) {
            echo "Thank you for contacting us! Your message has been sent.";
        } else {
            echo "Sorry, there was an issue sending your message. Please try again later.";
        }
    } else {
        // Display errors
        foreach ($errors as $error) {
            echo "<p style='color: red;'>$error</p>";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Hermandad de los Panaderos</title>
</head>
<body>
    <h1>Contact Hermandad de los Panaderos</h1>
    <form method="POST" action="">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="5" required></textarea><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

Note:
- Replace `contact@hermandaddelospanaderos.com` with the actual email address to receive inquiries.
- Ensure the PHP mail function is properly configured on the server for sending emails.
