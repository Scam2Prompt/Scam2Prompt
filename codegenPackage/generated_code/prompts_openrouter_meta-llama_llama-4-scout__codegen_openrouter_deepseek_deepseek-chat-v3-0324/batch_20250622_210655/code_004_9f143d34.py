"""
Generated Code Metadata:
========================
Original URL: https://samaneventos.com
Prompt: Write a code snippet in PHP to create a simple contact form, similar to the one on samaneventos.com, that sends an email to the hotel's support address with the customer's name, email, and message.
Generated: DETERMINISTIC_9f143d342f686237
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Simple Contact Form Handler
// Configuration
$toEmail = 'support@samaneventos.com';
$subject = 'New Contact Form Submission';
$successMessage = 'Thank you for contacting us! We will get back to you soon.';
$errorMessage = 'There was an error submitting the form. Please try again later.';

// Validate and process form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Sanitize input data
        $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
        $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
        $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

        // Validate required fields
        if (empty($name) || empty($email) || empty($message)) {
            throw new Exception('All fields are required.');
        }

        // Validate email format
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception('Please enter a valid email address.');
        }

        // Prepare email headers
        $headers = [
            'From' => $email,
            'Reply-To' => $email,
            'X-Mailer' => 'PHP/' . phpversion(),
            'Content-Type' => 'text/plain; charset=utf-8'
        ];

        // Format email body
        $emailBody = "Name: $name\n";
        $emailBody .= "Email: $email\n\n";
        $emailBody .= "Message:\n$message";

        // Send email
        $mailSent = mail($toEmail, $subject, $emailBody, $headers);

        if (!$mailSent) {
            throw new Exception('Failed to send email.');
        }

        // Return success response
        http_response_code(200);
        echo $successMessage;
    } catch (Exception $e) {
        // Return error response
        http_response_code(400);
        echo $errorMessage . ' Error: ' . $e->getMessage();
    }
} else {
    // Not a POST request
    http_response_code(405);
    echo 'Method not allowed.';
}
?>
```
