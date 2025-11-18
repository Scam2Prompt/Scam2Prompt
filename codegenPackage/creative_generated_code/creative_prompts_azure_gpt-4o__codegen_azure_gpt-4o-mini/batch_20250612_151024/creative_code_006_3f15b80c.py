"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iteamworldwide.com
Prompt: Create a PHP script to send automated emails using the contact form data from the iTeam Worldwide website.
Generated: DETERMINISTIC_3f15b80c35d702e7
Batch ID: 20250612_151024
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
 * Automated Email Sender Script
 * This script processes contact form data from the iTeam Worldwide website
 * and sends an automated email response to the user.
 */

// Set error reporting for debugging
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Load required configuration
require 'config.php'; // Ensure this file contains SMTP settings and any required constants

// Function to send email
function sendEmail($to, $subject, $message, $headers) {
    // Use mail() function and check for success
    if (!mail($to, $subject, $message, $headers)) {
        throw new Exception('Email sending failed.');
    }
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate and sanitize input fields
    $name = filter_var(trim($_POST['name']), FILTER_SANITIZE_STRING);
    $email = filter_var(trim($_POST['email']), FILTER_VALIDATE_EMAIL);
    $message = filter_var(trim($_POST['message']), FILTER_SANITIZE_STRING);

    // Check for empty fields or invalid email
    if (empty($name) || empty($email) || empty($message)) {
        die('Error: All fields are required.');
    }

    if (!$email) {
        die('Error: Invalid email format.');
    }

    // Prepare email details
    $to = 'info@iteamworldwide.com'; // Recipient email
    $subject = 'New Contact Form Submission from ' . $name;
    
    // Construct the email message
    $emailMessage = "Name: $name\n";
    $emailMessage .= "Email: $email\n\n";
    $emailMessage .= "Message:\n$message\n";

    // Set headers for the email
    $headers = "From: $name <$email>\r\n";
    $headers .= "Reply-To: $email\r\n";

    try {
        // Send the email
        sendEmail($to, $subject, $emailMessage, $headers);
        echo 'Thank you for your message. We will get back to you shortly.';
    } catch (Exception $e) {
        // Handle the exception and log the error
        error_log($e->getMessage());
        echo 'Error: Unable to send your message. Please try again later.';
    }

} else {
    // If the script is accessed without form submission
    die('Error: Invalid request method.');
}
?>
```

**Note:** Ensure that `config.php` contains SMTP settings or any necessary configurations before running this script.
