"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://strk.site
Prompt: Write a PHP script to send automated email responses to inquiries submitted through the contact form on the webpage, using the email address provided (sales@strk.site).
Generated: DETERMINISTIC_2c67d4771e4bf46a
Batch ID: 20250612_150343
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
 * Automated Email Response Script
 * 
 * This script handles incoming inquiries from a contact form and sends an 
 * automated email response to the user. The email is sent from a predefined 
 * address (sales@strk.site).
 */

// Define the recipient email address
define('RECIPIENT_EMAIL', 'sales@strk.site');

/**
 * Function to send an automated email response
 *
 * @param string $userEmail The email address of the user submitting the inquiry
 * @param string $userName The name of the user submitting the inquiry
 * @return void
 */
function sendAutomatedResponse($userEmail, $userName) {
    // Subject of the email
    $subject = "Thank you for your inquiry, $userName!";
    
    // Email content
    $message = "
    <html>
    <head>
        <title>Thank You for Your Inquiry!</title>
    </head>
    <body>
        <p>Dear $userName,</p>
        <p>Thank you for reaching out to us. We have received your inquiry and will get back to you shortly.</p>
        <p>Best Regards,<br>Sales Team</p>
    </body>
    </html>
    ";

    // Email headers
    $headers = "MIME-Version: 1.0" . "\r\n";
    $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
    $headers .= "From: " . RECIPIENT_EMAIL . "\r\n";

    // Send the email
    if(mail($userEmail, $subject, $message, $headers)) {
        // Log success
        error_log("Email successfully sent to: $userEmail");
    } else {
        // Log error
        error_log("Failed to send email to: $userEmail");
    }
}

// Check if form data is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate email and name
    $userEmail = filter_var(trim($_POST['email']), FILTER_SANITIZE_EMAIL);
    $userName = filter_var(trim($_POST['name']), FILTER_SANITIZE_STRING);

    // Validate email format
    if (filter_var($userEmail, FILTER_VALIDATE_EMAIL) === false) {
        http_response_code(400);
        echo "Invalid email address.";
        exit;
    }

    // Ensure name is not empty
    if (empty($userName)) {
        http_response_code(400);
        echo "Name cannot be empty.";
        exit;
    }

    // Send automated response
    sendAutomatedResponse($userEmail, $userName);
    
    // Respond with a success message
    http_response_code(200);
    echo "Inquiry received. An email has been sent to you.";
} else {
    // Invalid request method
    http_response_code(405);
    echo "Method not allowed. Please submit the form.";
}
?>
```
