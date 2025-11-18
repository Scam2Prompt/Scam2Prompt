"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casiefe636.webcindario.com
Prompt: Write PHP code to create a contact form for a free website hosted on miarroba.com.
Generated: DETERMINISTIC_7fcbf4cbaf7cff99
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Contact Form Script (PHP)
// Ensure to configure your miarroba.com hosting for proper handling of mail() function

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate input data
    $name = htmlspecialchars(strip_tags(trim($_POST['name'] ?? '')));
    $email = filter_var(trim($_POST['email'] ?? ''), FILTER_VALIDATE_EMAIL);
    $message = htmlspecialchars(strip_tags(trim($_POST['message'] ?? '')));

    // Initialize variables for error messages
    $errors = [];

    // Validate form fields
    if (empty($name)) {
        $errors[] = "Name is required.";
    }
    if (!$email) {
        $errors[] = "A valid email address is required.";
    }
    if (empty($message)) {
        $errors[] = "Message cannot be empty.";
    }

    // If there are no errors, send the email
    if (empty($errors)) {
        // Recipient email address (replace with your own)
        $to = "your_email@example.com";

        // Email subject
        $subject = "Contact Form Submission from $name";

        // Email body
        $body = "Name: $name\nEmail: $email\nMessage:\n$message";

        // Email headers
        $headers = "From: $email\r\n";
        $headers .= "Reply-To: $email\r\n";

        // Attempt to send the email
        if (mail($to, $subject, $body, $headers)) {
            $success = "Thank you! Your message has been sent.";
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
    <style>
        /* Simple styling for the contact form */
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background: #f4f4f4;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            padding: 10px 15px;
            background: #5cb85c;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background: #4cae4c;
        }
        .error {
            color: #d9534f;
        }
        .success {
            color: #5cb85c;
        }
    </style>
</head>
<body>
<div class="container">
    <h2>Contact Us</h2>
    <?php 
    // Display success message or errors
    if (!empty($success)) {
        echo "<p class='success'>$success</p>";
    }
    if (!empty($errors)) {
        foreach ($errors as $error) {
            echo "<p class='error'>$error</p>";
        }
    }
    ?>
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name" required>

        <label for="email">Email:</label>
        <input type="email" name="email" id="email" required>

        <label for="message">Message:</label>
        <textarea name="message" id="message" rows="6" required></textarea>

        <button type="submit">Send</button>
    </form>
</div>
</body>
</html>
```
