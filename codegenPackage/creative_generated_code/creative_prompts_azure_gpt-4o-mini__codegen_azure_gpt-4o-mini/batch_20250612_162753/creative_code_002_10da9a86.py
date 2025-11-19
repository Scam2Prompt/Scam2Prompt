"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sports-zilla.com
Prompt: Create a PHP code snippet that submits a contact form to Sports Zilla, including fields for name, email, and inquiry about leisure wear.
Generated: DETERMINISTIC_10da9a86059d7823
Batch ID: 20250612_162753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Define a constant for the recipient email address
define('RECIPIENT_EMAIL', 'contact@sportszilla.com');

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate form inputs
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $inquiry = filter_input(INPUT_POST, 'inquiry', FILTER_SANITIZE_STRING);
    
    // Initialize an array to hold error messages
    $errors = [];

    // Validate name
    if (empty($name)) {
        $errors[] = 'Name is required.';
    }

    // Validate email
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'Valid email is required.';
    }

    // Validate inquiry
    if (empty($inquiry)) {
        $errors[] = 'Inquiry field cannot be empty.';
    }

    // Check if there are no errors
    if (empty($errors)) {
        // Prepare the email message
        $subject = 'Contact Form Submission';
        $message = "Name: $name\nEmail: $email\nInquiry: $inquiry";
        $headers = "From: $name <$email>\r\n";

        // Attempt to send the email
        if (mail(RECIPIENT_EMAIL, $subject, $message, $headers)) {
            // Success message
            echo '<p>Thank you for your inquiry. We will get back to you shortly.</p>';
        } else {
            // Error sending email
            echo '<p>There was a problem sending your message. Please try again later.</p>';
        }
    } else {
        // Display errors
        foreach ($errors as $error) {
            echo "<p style='color: red;'>$error</p>";
        }
    }
}
?>

<!-- HTML Form for contact submission -->
<form method="post" action="">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    
    <label for="inquiry">Inquiry about Leisure Wear:</label>
    <textarea id="inquiry" name="inquiry" required></textarea>
    
    <button type="submit">Submit</button>
</form>
```

Make sure to replace `contact@sportszilla.com` with the actual recipient email address before deploying the code.
