"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getgrass.im
Prompt: Develop a code snippet in PHP that integrates with the GetGrass contact form, sending user inquiries directly to their support email.
Generated: DETERMINISTIC_5ad41af8a0ba5ee6
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configuration
define('SUPPORT_EMAIL', 'support@getgrass.com'); // Replace with the actual support email.
define('EMAIL_SUBJECT', 'New Inquiry from GetGrass Contact Form'); // Subject of the email.
define('EMAIL_HEADERS', 'From: no-reply@getgrass.com' . "\r\n" . 'Content-Type: text/plain; charset=utf-8');

// Check if the form was submitted via POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Sanitize user input
        $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
        $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
        $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

        // Validate required fields
        if (empty($name) || empty($email) || empty($message)) {
            throw new Exception("All fields (name, email, message) are required.");
        }

        // Validate email format
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception("Invalid email address.");
        }

        // Construct the email content
        $emailBody = "You have received a new inquiry from the GetGrass contact form:\n\n";
        $emailBody .= "Name: $name\n";
        $emailBody .= "Email: $email\n\n";
        $emailBody .= "Message:\n$message\n";

        // Send email
        if (!mail(SUPPORT_EMAIL, EMAIL_SUBJECT, $emailBody, EMAIL_HEADERS)) {
            throw new Exception("Failed to send the email. Please try again later.");
        }

        // Response success
        http_response_code(200); // OK
        echo json_encode(["status" => "success", "message" => "Your inquiry has been sent successfully."]);
    } catch (Exception $e) {
        // Handle errors
        http_response_code(400); // Bad Request
        echo json_encode(["status" => "error", "message" => $e->getMessage()]);
    }
} else {
    // Handle invalid request method
    http_response_code(405); // Method Not Allowed
    echo json_encode(["status" => "error", "message" => "Invalid request method."]);
}
?>
```
