"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.cornucopiastrategy.com
Prompt: Create a form submission handler in PHP that integrates with MailerLite, similar to the functionality in `test_mailerlite_form.html`.
Generated: DETERMINISTIC_d261f5f9519d877e
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// form_handler.php

// Ensure error reporting is enabled for debugging during development
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Include MailerLite's PHP SDK
require 'vendor/autoload.php';

use MailerLite\MailerLite;

// Configuration for MailerLite API
define('MAILERLITE_API_KEY', 'your-mailerlite-api-key'); // Replace with your actual API key

// Function to handle form submission and integrate with MailerLite
function handleFormSubmission()
{
    // Ensure the request is a POST request
    if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
        http_response_code(405); // Method Not Allowed
        echo json_encode(['error' => 'Invalid request method.']);
        exit;
    }

    // Validate input data
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);

    if (!$email || !$name) {
        http_response_code(400); // Bad Request
        echo json_encode(['error' => 'Invalid input data.']);
        exit;
    }

    try {
        // Initialize MailerLite client
        $mailerLite = new MailerLite(['api_key' => MAILERLITE_API_KEY]);

        // Prepare subscriber data
        $subscriberData = [
            'email' => $email,
            'fields' => [
                'name' => $name,
            ],
        ];

        // Add subscriber to MailerLite group (optional: specify group_id)
        $response = $mailerLite->subscribers()->create($subscriberData);

        // Check response for success
        if (isset($response['error'])) {
            throw new Exception('Failed to add subscriber: ' . $response['error']['message']);
        }

        // Respond with success message
        echo json_encode(['message' => 'Subscriber added successfully!']);
    } catch (Exception $e) {
        // Handle exceptions and errors gracefully
        http_response_code(500); // Internal Server Error
        echo json_encode(['error' => $e->getMessage()]);
    }
}

// Execute the form handler function
handleFormSubmission();
```

```html
<!-- test_mailerlite_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MailerLite Form</title>
</head>
<body>
    <form action="form_handler.php" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <button type="submit">Subscribe</button>
    </form>
</body>
</html>
```

**Note:** 
- Replace `your-mailerlite-api-key` with your actual MailerLite API key.
- Ensure that the `MailerLite` PHP SDK is installed via Composer (`composer require mailerlite/mailerlite-api-v2-php-sdk`).
