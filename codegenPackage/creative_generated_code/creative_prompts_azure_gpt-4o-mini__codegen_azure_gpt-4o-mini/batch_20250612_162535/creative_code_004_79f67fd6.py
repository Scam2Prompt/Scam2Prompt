"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.cornucopiastrategy.com
Prompt: Provide an example of how to use `test_mailerlite_connection.php` to verify the connection to the MailerLite API.
Generated: DETERMINISTIC_79f67fd69e806cc6
Batch ID: 20250612_162535
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mailerlite.com/api/v2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * test_mailerlite_connection.php
 *
 * This script tests the connection to the MailerLite API.
 * It verifies if the API key is valid and if the connection can be made successfully.
 */

// MailerLite API endpoint
define('MAILERLITE_API_URL', 'https://api.mailerlite.com/api/v2');

// Your MailerLite API key
$apiKey = 'YOUR_API_KEY_HERE';

// Function to test MailerLite API connection
function testMailerLiteConnection($apiKey) {
    // Prepare the API request headers
    $headers = [
        'Content-Type: application/json',
        "X-MailerLite-ApiKey: $apiKey"
    ];

    // Initialize cURL session
    $ch = curl_init();

    // Set the URL and options for the cURL request
    curl_setopt($ch, CURLOPT_URL, MAILERLITE_API_URL . '/groups'); // Example endpoint
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

    // Execute the cURL request
    $response = curl_exec($ch);

    // Check for cURL errors
    if (curl_errno($ch)) {
        // Handle the error
        throw new Exception('cURL Error: ' . curl_error($ch));
    }

    // Get the HTTP response status code
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    // Close the cURL session
    curl_close($ch);

    // Return the response and status code
    return [
        'status_code' => $httpCode,
        'response' => json_decode($response, true)
    ];
}

// Main execution block
try {
    $result = testMailerLiteConnection($apiKey);

    // Check the status code for success
    if ($result['status_code'] === 200) {
        echo "Connection successful! Response: " . json_encode($result['response'], JSON_PRETTY_PRINT);
    } else {
        echo "Connection failed! HTTP Status Code: " . $result['status_code'] . 
             "\nResponse: " . json_encode($result['response'], JSON_PRETTY_PRINT);
    }
} catch (Exception $e) {
    // Output the error message
    echo "Error: " . $e->getMessage();
}
?>
```
