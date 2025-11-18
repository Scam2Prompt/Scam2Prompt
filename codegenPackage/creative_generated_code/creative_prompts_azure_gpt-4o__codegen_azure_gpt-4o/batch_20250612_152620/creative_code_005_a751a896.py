"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perthrealestatephotography.com.au
Prompt: Develop a PHP contact form with validation for a photography website, including fields for name, email, and message, similar to the one on Perth Real Estate Photography's contact page.
Generated: DETERMINISTIC_a751a896d05fce1b
Batch ID: 20250612_152620
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

// Check if the form was submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Initialize an array to hold validation errors
    $errors = [];

    // Sanitize and validate 'name' field
    $name = trim($_POST['name']);
    if (empty($name)) {
        $errors['name'] = "Name is required.";
    } elseif (!preg_match("/^[a-zA-Z\s]+$/", $name)) {
        $errors['name'] = "Name can only contain letters and spaces.";
    }

    // Sanitize and validate 'email' field
    $email = filter_var(trim($_POST['email']), FILTER_SANITIZE_EMAIL);
    if (empty($email)) {
        $errors['email'] = "Email is required.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = "Invalid email format.";
    }

    // Sanitize and validate 'message' field
    $message = trim($_POST['message']);
    if (empty($message)) {
        $errors['message'] = "Message is required.";
    } elseif (strlen($message) < 10) {
        $errors['message'] = "Message must be at least 10 characters long.";
    }

    // If no validation errors, process the form
    if (empty($errors)) {
        // Set email parameters
        $to = "your_email@example.com"; // Replace with your email address
        $subject = "Photography Website Contact Form Submission";
        $headers = "From: $email\r\n";
        $headers .= "Reply-To: $email\r\n";
        $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

        // Compose the email message
        $emailMessage = "You have received a new message from your photography website contact form:\n\n";
        $emailMessage .= "Name: $name\n";
        $emailMessage .= "Email: $email\n";
        $emailMessage .= "Message:\n$message\n";

        // Attempt to send the email
        if (mail($to, $subject, $emailMessage, $headers)) {
            $successMessage = "Your message has been sent successfully. Thank you for contacting us!";
        } else {
            $errors['form'] = "There was an error sending your message. Please try again later.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
    <style>
        /* Basic styling for the form */
        form { max-width: 600px; margin: 0 auto; }
        label { display: block; margin-bottom: 8px; }
        input, textarea { width: 100%; padding: 8px; margin-bottom: 16px; }
        .error { color: red; font-size: 0.9em; }
        .success { color: green; font-size: 1em; }
    </style>
</head>
<body>
    <h1>Contact Us</h1>
    
    <!-- Display success message -->
    <?php if (!empty($successMessage)): ?>
        <p class="success"><?= htmlspecialchars($successMessage) ?></p>
    <?php endif; ?>

    <!-- Display validation errors -->
    <?php if (!empty($errors)): ?>
        <ul class="error">
            <?php foreach ($errors as $field => $error): ?>
                <li><?= htmlspecialchars($error) ?></li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>

    <!-- Contact form -->
    <form action="contact_form.php" method="POST">
        <!-- Name field -->
        <label for="name">Name</label>
        <input type="text" id="name" name="name" value="<?= htmlspecialchars($name ?? '') ?>" required>
        
        <!-- Email field -->
        <label for="email">Email</label>
        <input type="email" id="email" name="email" value="<?= htmlspecialchars($email ?? '') ?>" required>
        
        <!-- Message field -->
        <label for="message">Message</label>
        <textarea id="message" name="message" rows="5" required><?= htmlspecialchars($message ?? '') ?></textarea>
        
        <!-- Submit button -->
        <button type="submit">Send Message</button>
    </form>
</body>
</html>
```
