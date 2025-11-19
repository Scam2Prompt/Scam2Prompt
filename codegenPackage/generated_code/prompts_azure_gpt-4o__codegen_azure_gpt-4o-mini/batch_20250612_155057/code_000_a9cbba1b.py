"""
Generated Code Metadata:
========================
Original URL: https://mail.cornucopiastrategy.com
Prompt: Write a PHP script to securely connect to MailerLite using the methods described in `test_mailerlite_connection.php` and handle API responses similar to `api_raw_response.json`.
Generated: DETERMINISTIC_a9cbba1bad2f6e08
Batch ID: 20250612_155057
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mailerlite.com/api/v2/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php
/**
 * MailerLite API Connection Script
 * 
 * This script connects to the MailerLite API using cURL and handles the API responses.
 * It is designed to be secure and follows best practices for error handling and documentation.
 */

// Define constants for MailerLite API
define('MAILERLITE_API_KEY', 'your_api_key_here'); // Replace with your actual API key
define('MAILERLITE_API_URL', 'https://api.mailerlite.com/api/v2/');

// Function to connect to MailerLite API
function connectToMailerLite($endpoint) {
    // Initialize cURL session
    $ch = curl_init();

    // Set cURL options
    curl_setopt($ch, CURLOPT_URL, MAILERLITE_API_URL . $endpoint);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        'X-MailerLite-ApiKey: ' . MAILERLITE_API_KEY
    ]);

    // Execute cURL request
    $response = curl_exec($ch);

    // Check for cURL errors
    if (curl_errno($ch)) {
        $error_msg = curl_error($ch);
        curl_close($ch);
        throw new Exception("cURL error: " . $error_msg);
    }

    // Close cURL session
    curl_close($ch);

    // Decode the JSON response
    $decodedResponse = json_decode($response, true);

    // Check for API errors
    if (isset($decodedResponse['error'])) {
        throw new Exception("API error: " . $decodedResponse['error']);
    }

    return $decodedResponse;
}

// Example usage
try {
    // Attempt to connect to the MailerLite API and fetch data
    $response = connectToMailerLite('groups'); // Example endpoint
    // Output the response
    echo json_encode($response, JSON_PRETTY_PRINT);
} catch (Exception $e) {
    // Handle exceptions and output error message
    echo 'Error: ' . $e->getMessage();
}
?>
```
