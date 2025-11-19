"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Generate a code snippet in PHP that sends a contact form submission to Perfect Melbourne Carpet for a free quote on carpet repairs.
Generated: DETERMINISTIC_9dfeb0cb8b75c14e
Batch ID: 20250612_161017
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

// Define a function to handle the contact form submission
function sendContactFormSubmission($postData) {
    // Check if the required fields are set in the submitted data
    if (!isset($postData['name']) || !isset($postData['email']) || !isset($postData['message'])) {
        throw new InvalidArgumentException('Required fields are missing.');
    }

    // Sanitize and validate the input data
    $name = filter_var(trim($postData['name']), FILTER_SANITIZE_STRING);
    $email = filter_var(trim($postData['email']), FILTER_SANITIZE_EMAIL);
    $message = filter_var(trim($postData['message']), FILTER_SANITIZE_STRING);

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException('Invalid email format.');
    }

    // Recipient email address
    $to = 'info@perfectmelbournecarpet.com.au'; // Change to actual email address

    // Email subject
    $subject = 'New Contact Form Submission from ' . $name;

    // Email body
    $body = "Name: $name\n";
    $body .= "Email: $email\n\n";
    $body .= "Message:\n$message\n";

    // Set headers for the email
    $headers = 'From: ' . $email . "\r\n" .
               'Reply-To: ' . $email . "\r\n" .
               'X-Mailer: PHP/' . phpversion();

    // Send the email and handle potential errors
    if (!mail($to, $subject, $body, $headers)) {
        throw new RuntimeException('Mail not sent due to a server error.');
    }

    return true;
}

// Check if the form has been submitted via POST method
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Send the contact form submission
        sendContactFormSubmission($_POST);
        echo 'Thank you for your submission! We will get back to you shortly.';
    } catch (Exception $e) {
        // Display error message to the user
        echo 'Error: ' . $e->getMessage();
    }
}
?>
```

**Usage:**
- This code should be placed in a file named `contact_form.php`.
- Ensure that the email address in the `$to` variable is set to the actual address where you want to receive the submissions.
- This script expects an HTML form submission via POST with fields named `name`, `email`, and `message`.
