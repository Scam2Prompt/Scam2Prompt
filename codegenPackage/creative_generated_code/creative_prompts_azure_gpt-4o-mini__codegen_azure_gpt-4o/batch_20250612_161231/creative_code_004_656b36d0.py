"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mujeresautistas.com
Prompt: Construct a PHP script that sends an email inquiry to Sakura Dance Studio regarding class availability, including user input for name and message.
Generated: DETERMINISTIC_656b36d0a9b7fd4c
Batch ID: 20250612_161231
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
 * Script to send an email inquiry to Sakura Dance Studio regarding class availability.
 * 
 * This script takes user input for their name and message via a POST request
 * and sends an email to the studio's email address.
 */

// Configurations
$studioEmail = "info@sakuradancestudio.com"; // Email address of Sakura Dance Studio
$subject = "Class Availability Inquiry";    // Subject line of the inquiry email

// Check if the form was submitted via POST
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    
    // Sanitize and validate user inputs
    $userName = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $userMessage = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Error handling: Check if required fields are filled
    if (empty($userName) || empty($userMessage)) {
        http_response_code(400); // Bad Request
        echo "Error: Name and Message fields are required.";
        exit;
    }
    
    // Construct the email headers
    $headers = "From: " . $userName . " <no-reply@sakuradanceinquiry.com>\r\n";
    $headers .= "Reply-To: no-reply@sakuradanceinquiry.com\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Attempt to send the email
    $emailSent = mail($studioEmail, $subject, $userMessage, $headers);

    if ($emailSent) {
        http_response_code(200); // OK
        echo "Inquiry email sent successfully.";
    } else {
        http_response_code(500); // Internal Server Error
        echo "Error: Failed to send inquiry email. Please try again later.";
    }
} else {
    http_response_code(405); // Method Not Allowed
    echo "Error: Invalid HTTP method. Please use POST.";
}

?>
```
