"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onedivepb.com
Prompt: Develop a PHP script that allows users to contact One Dive for more information about their diving certifications.
Generated: DETERMINISTIC_6605a905952b6ff0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Contact form handler for "One Dive"
//
// This script allows users to submit inquiries about diving certifications.
// It handles user inputs, validates the data, and sends an email to the appropriate recipient.

// Enable strict error reporting for development
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Configuration
define('RECIPIENT_EMAIL', 'info@onedive.com'); // Replace with the actual email address
define('SUCCESS_MESSAGE', 'Your inquiry has been sent successfully. Thank you for reaching out!');
define('ERROR_MESSAGE', 'An error occurred while processing your request. Please try again later.');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate inputs
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check if all required fields are filled
    if (!$name || !$email || !$message) {
        $response = [
            'status' => 'error',
            'message' => 'All fields are required. Please provide valid inputs.',
        ];
        echo json_encode($response);
        exit;
    }

    // Prepare the email
    $subject = 'Inquiry about Diving Certifications';
    $emailBody = "Name: $name\nEmail: $email\nMessage:\n$message";
    $headers = [
        'From' => $email,
        'Reply-To' => $email,
    ];

    // Attempt to send the email
    try {
        $isEmailSent = mail(RECIPIENT_EMAIL, $subject, $emailBody, $headers);
        if ($isEmailSent) {
            $response = [
                'status' => 'success',
                'message' => SUCCESS_MESSAGE,
            ];
        } else {
            throw new Exception('Email sending failed.');
        }
    } catch (Exception $e) {
        $response = [
            'status' => 'error',
            'message' => ERROR_MESSAGE,
        ];
    }

    // Return JSON response to the client
    echo json_encode($response);
    exit;
}

?>

<!-- HTML Form for user input -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact One Dive</title>
</head>
<body>
    <h1>Contact One Dive</h1>
    <form id="contactForm" method="post">
        <label for="name">Your Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Your Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="message">Your Message:</label>
        <textarea id="message" name="message" required></textarea>

        <button type="submit">Send Inquiry</button>
    </form>

    <script>
        // Optional: Handle form submission without page reload (AJAX)
        document.getElementById('contactForm').addEventListener('submit', async function(event) {
            event.preventDefault();
            
            const formData = new FormData(this);
            const response = await fetch('', {
                method: 'POST',
                body: formData
            });

            const result = await response.json();
            alert(result.message);
        });
    </script>
</body>
</html>
```
