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
// Contact Form Submission Handler for Perfect Melbourne Carpet

// Define recipient email and subject
$recipientEmail = "info@perfectmelbournecarpet.com"; // Replace with actual recipient email
$emailSubject = "Request for Free Carpet Repairs Quote";

// Check if form is submitted via POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate user inputs
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Error handling: Ensure required fields are not empty
    if (!$name || !$email || !$phone || !$message) {
        http_response_code(400); // Bad Request
        echo json_encode(['error' => 'All fields are required. Please fill out the form completely.']);
        exit;
    }

    // Create email content
    $emailBody = "New contact form submission:\n\n";
    $emailBody .= "Name: $name\n";
    $emailBody .= "Email: $email\n";
    $emailBody .= "Phone: $phone\n";
    $emailBody .= "Message:\n$message\n";

    // Additional email headers
    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Send email using mail function
    $mailSent = mail($recipientEmail, $emailSubject, $emailBody, $headers);

    // Handle success or failure of mail sending
    if ($mailSent) {
        http_response_code(200); // OK
        echo json_encode(['success' => 'Thank you! Your request has been sent.']);
    } else {
        http_response_code(500); // Internal Server Error
        echo json_encode(['error' => 'Failed to send your request. Please try again later.']);
    }
} else {
    // Handle invalid request method
    http_response_code(405); // Method Not Allowed
    echo json_encode(['error' => 'Invalid request method. Please use POST.']);
}
?>
```
