"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1minutedog.com
Prompt: Write code in PHP to implement a contact form for dog owners to reach out for personalized advice, similar to the contact options available on the "1 Minute Dog Training" website.
Generated: DETERMINISTIC_4427c41c4e6a61dd
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// contact-form-handler.php

// Enable error reporting for debugging during development; disable in production.
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Check if the form was submitted via POST
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Sanitize user input to prevent XSS attacks
    $name = htmlspecialchars(trim($_POST["name"]));
    $email = htmlspecialchars(trim($_POST["email"]));
    $dogBreed = htmlspecialchars(trim($_POST["dog_breed"]));
    $message = htmlspecialchars(trim($_POST["message"]));

    // Array to hold errors
    $errors = [];

    // Validate the input fields
    if (empty($name)) {
        $errors[] = "Name is required.";
    }
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Valid email address is required.";
    }
    if (empty($dogBreed)) {
        $errors[] = "Dog breed is required.";
    }
    if (empty($message)) {
        $errors[] = "Message is required.";
    }

    // If there are no errors, proceed to handle the form submission
    if (empty($errors)) {
        // Example: send the form data via email
        // Replace with your own email configuration
        $to = "contact@example.com"; // Update with the recipient's email address
        $subject = "New Contact Form Submission";
        $body = "Name: $name\nEmail: $email\nDog Breed: $dogBreed\nMessage:\n$message";
        $headers = "From: $email";

        if (mail($to, $subject, $body, $headers)) {
            $successMessage = "Your message has been sent successfully!";
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
    <title>Dog Owner Contact Form</title>
</head>
<body>
    <h1>Contact Form for Dog Owners</h1>

    <!-- Display success message if form submission was successful -->
    <?php if (isset($successMessage)): ?>
        <p style="color: green;"><?php echo $successMessage; ?></p>
    <?php endif; ?>

    <!-- Display errors if there are any -->
    <?php if (!empty($errors)): ?>
        <ul style="color: red;">
            <?php foreach ($errors as $error): ?>
                <li><?php echo $error; ?></li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>

    <!-- Contact form -->
    <form action="contact-form-handler.php" method="POST">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="dog_breed">Dog Breed:</label><br>
        <input type="text" id="dog_breed" name="dog_breed" required><br><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="5" required></textarea><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
