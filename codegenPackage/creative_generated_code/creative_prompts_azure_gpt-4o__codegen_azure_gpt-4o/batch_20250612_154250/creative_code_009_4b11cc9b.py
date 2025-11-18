"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://denshaven.com
Prompt: Write code using PHP to integrate a contact form for Dens Haven's website, ensuring fields for name, email, and message are validated before submission.
Generated: DETERMINISTIC_4b11cc9b5252839e
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// contact_form_handler.php
// This script handles the submission of the contact form, validates inputs, and sends an email notification.

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Collect form input values
    $name = trim($_POST['name'] ?? '');
    $email = trim($_POST['email'] ?? '');
    $message = trim($_POST['message'] ?? '');

    // Initialize an array to hold validation errors
    $errors = [];

    // Validate name
    if (empty($name)) {
        $errors['name'] = 'Name is required.';
    } elseif (strlen($name) > 100) {
        $errors['name'] = 'Name must not exceed 100 characters.';
    }

    // Validate email
    if (empty($email)) {
        $errors['email'] = 'Email is required.';
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = 'Please provide a valid email address.';
    }

    // Validate message
    if (empty($message)) {
        $errors['message'] = 'Message is required.';
    } elseif (strlen($message) > 500) {
        $errors['message'] = 'Message must not exceed 500 characters.';
    }

    // If there are errors, return them as a JSON response
    if (!empty($errors)) {
        header('Content-Type: application/json');
        echo json_encode(['success' => false, 'errors' => $errors]);
        exit;
    }

    // Send email notification (example configuration, adjust as needed)
    $to = 'contact@denshaven.com'; // Replace with the actual email address
    $subject = 'New Contact Form Submission';
    $emailBody = "Name: $name\nEmail: $email\nMessage:\n$message";

    // Email headers
    $headers = [
        'From' => 'no-reply@denshaven.com',
        'Reply-To' => $email,
        'X-Mailer' => 'PHP/' . phpversion(),
    ];

    // Attempt to send the email
    if (mail($to, $subject, $emailBody, $headers)) {
        header('Content-Type: application/json');
        echo json_encode(['success' => true, 'message' => 'Your message has been sent successfully.']);
    } else {
        header('Content-Type: application/json');
        echo json_encode(['success' => false, 'message' => 'There was an error sending your message. Please try again later.']);
    }
    exit;
}
?>

<!-- contact_form.html -->
<!-- A simple HTML form for the contact page -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - Dens Haven</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            max-width: 500px;
            margin: auto;
        }
        label {
            display: block;
            margin-bottom: 8px;
        }
        input, textarea, button {
            width: 100%;
            margin-bottom: 20px;
            padding: 8px;
            font-size: 16px;
        }
        button {
            background-color: #007BFF;
            color: #fff;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Contact Us</h1>
    <form action="contact_form_handler.php" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required maxlength="100">

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="message">Message:</label>
        <textarea id="message" name="message" required maxlength="500" rows="5"></textarea>

        <button type="submit">Send Message</button>
    </form>
</body>
</html>
```
