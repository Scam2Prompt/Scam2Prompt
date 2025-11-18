"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://healthinsuranceshop.ie
Prompt: Write a PHP script to send a callback request form submission, including fields for "Name" and "Telephone," as seen on the Health Insurance Shop website.
Generated: DETERMINISTIC_895a53462d8e64d4
Batch ID: 20250612_154820
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
 * Callback Request Submission Script
 * 
 * This script receives form data for "Name" and "Telephone" and sends it via email
 * to a predefined recipient. It includes input validation and error handling.
 */

// Configuration
$recipientEmail = "callback@healthinsuranceshop.com"; // Replace with your actual email
$emailSubject = "Callback Request Submission";

try {
    // Check for request method
    if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
        throw new Exception("Invalid request method. Only POST requests are allowed.");
    }

    // Validate and sanitize input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $telephone = filter_input(INPUT_POST, 'telephone', FILTER_SANITIZE_STRING);

    if (empty($name) || empty($telephone)) {
        throw new Exception("Both 'Name' and 'Telephone' fields are required.");
    }

    if (!preg_match("/^\+?[0-9\s\-]+$/", $telephone)) {
        throw new Exception("Invalid telephone number format.");
    }

    // Prepare email content
    $emailBody = "Callback Request Submission:\n\n";
    $emailBody .= "Name: {$name}\n";
    $emailBody .= "Telephone: {$telephone}\n";

    // Send email
    $headers = "From: no-reply@healthinsuranceshop.com\r\n";
    $headers .= "Reply-To: no-reply@healthinsuranceshop.com\r\n";
    $headers .= "Content-Type: text/plain; charset=utf-8\r\n";

    if (!mail($recipientEmail, $emailSubject, $emailBody, $headers)) {
        throw new Exception("Failed to send the email. Please try again later.");
    }

    // Respond with success message
    echo json_encode([
        "status" => "success",
        "message" => "Callback request submitted successfully."
    ]);

} catch (Exception $e) {
    // Respond with error message
    http_response_code(400);
    echo json_encode([
        "status" => "error",
        "message" => $e->getMessage()
    ]);
}
?>
```
