"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retinabd.org
Prompt: Write a code snippet in PHP to implement a contact form for a coaching center website like Retina, allowing students to submit inquiries about courses and batch schedules.
Generated: DETERMINISTIC_9addce32767f8af2
Batch ID: 20250612_154452
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

// Ensure error reporting for debugging during development
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Process the form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate input fields
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);
    
    // Initialize an array to store errors
    $errors = [];

    // Validate required fields
    if (!$name) {
        $errors[] = "Name is required.";
    }

    if (!$email) {
        $errors[] = "A valid email address is required.";
    }

    if (!$message) {
        $errors[] = "Message cannot be empty.";
    }

    // If no errors, proceed to handle the submission
    if (empty($errors)) {
        // Simulate sending the email (replace with actual email sending logic)
        $recipient = "info@retinacoachingcenter.com"; // Replace with your actual email address
        $subject = "Inquiry from $name about Courses & Batch Schedules";
        $body = "Name: $name\nEmail: $email\nMessage: $message";

        // Use mail() function or a better library like PHPMailer for production
        if (mail($recipient, $subject, $body)) {
            $successMessage = "Your inquiry has been submitted successfully. We will get back to you soon!";
        } else {
            $errors[] = "Failed to send the email. Please try again later.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form action="contact_form.php" method="POST">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" required></textarea><br><br>

        <button type="submit">Submit Inquiry</button>
    </form>

    <!-- Display error messages -->
    <?php if (!empty($errors)): ?>
        <div style="color: red;">
            <ul>
                <?php foreach ($errors as $error): ?>
                    <li><?php echo htmlspecialchars($error); ?></li>
                <?php endforeach; ?>
            </ul>
        </div>
    <?php endif; ?>

    <!-- Display success message -->
    <?php if (!empty($successMessage)): ?>
        <div style="color: green;">
            <?php echo htmlspecialchars($successMessage); ?>
        </div>
    <?php endif; ?>
</body>
</html>
```
