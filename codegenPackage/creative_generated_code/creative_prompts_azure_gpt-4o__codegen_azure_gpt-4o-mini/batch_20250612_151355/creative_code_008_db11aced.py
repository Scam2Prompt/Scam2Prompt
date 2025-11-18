"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaks.xyz
Prompt: Create a PHP script to handle form submissions for a contact page, including validation for email and phone number fields, inspired by Ayoft's contact form.
Generated: DETERMINISTIC_db11acedf241671c
Batch ID: 20250612_151355
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

// Start session for flash messaging
session_start();

/**
 * Validate email format
 *
 * @param string $email
 * @return bool
 */
function validateEmail($email) {
    return filter_var($email, FILTER_VALIDATE_EMAIL) !== false;
}

/**
 * Validate phone number format
 *
 * @param string $phone
 * @return bool
 */
function validatePhone($phone) {
    // Assuming phone number should be in the format: (123) 456-7890 or 123-456-7890
    return preg_match('/^\(?\d{3}\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$/', $phone);
}

// Initialize error messages array
$errors = [];

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Retrieve and sanitize form data
    $name = trim($_POST['name']);
    $email = trim($_POST['email']);
    $phone = trim($_POST['phone']);
    $message = trim($_POST['message']);

    // Validate name
    if (empty($name)) {
        $errors['name'] = 'Name is required.';
    }

    // Validate email
    if (empty($email) || !validateEmail($email)) {
        $errors['email'] = 'A valid email is required.';
    }

    // Validate phone number
    if (empty($phone) || !validatePhone($phone)) {
        $errors['phone'] = 'A valid phone number is required.';
    }

    // Validate message
    if (empty($message)) {
        $errors['message'] = 'Message cannot be empty.';
    }

    // If no errors, process the form
    if (empty($errors)) {
        // Prepare email headers
        $to = 'your-email@example.com'; // Change to your email address
        $subject = 'New Contact Form Submission';
        $headers = "From: $name <$email>\r\n";
        $headers .= "Reply-To: $email\r\n";

        // Create email body
        $emailBody = "Name: $name\n";
        $emailBody .= "Email: $email\n";
        $emailBody .= "Phone: $phone\n";
        $emailBody .= "Message:\n$message\n";

        // Send email
        if (mail($to, $subject, $emailBody, $headers)) {
            // Set success message
            $_SESSION['success'] = 'Your message has been sent successfully!';
            header('Location: contact.php'); // Redirect to contact page
            exit();
        } else {
            // Set error message for email failure
            $_SESSION['error'] = 'Unable to send email. Please try again later.';
            header('Location: contact.php'); // Redirect to contact page
            exit();
        }
    } else {
        // Save errors in session for display
        $_SESSION['errors'] = $errors;
        header('Location: contact.php'); // Redirect to contact page with errors
        exit();
    }
}
?>
```
