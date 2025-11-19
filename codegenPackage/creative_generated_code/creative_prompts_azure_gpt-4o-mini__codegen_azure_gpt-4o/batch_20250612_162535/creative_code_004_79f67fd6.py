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
  "https://api.mailerlite.com/api/v2/": {
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
 * This script verifies the connection to the MailerLite API.
 * Ensure you have a valid API key and cURL enabled in your PHP setup.
 */

// Define constants for the MailerLite API
define('MAILERLITE_API_URL', 'https://api.mailerlite.com/api/v2/');
define('MAILERLITE_API_KEY', 'your_api_key_here'); // Replace with your MailerLite API key

/**
 * Test the connection to the MailerLite API
 *
 * @return void
 */
function testMailerLiteConnection()
{
    // Initialize cURL session
    $ch = curl_init();

    // Set cURL options
    curl_setopt($ch, CURLOPT_URL, MAILERLITE_API_URL . 'groups'); // Endpoint to fetch groups
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); // Return response as a string
    curl_setopt($ch, CURLOPT_HTTPHEADER, [ // Set required headers
        'Content-Type: application/json',
        'X-MailerLite-ApiKey: ' . MAILERLITE_API_KEY
    ]);

    // Execute the cURL request
    $response = curl_exec($ch);
    $httpStatusCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    // Check for cURL errors
    if (curl_errno($ch)) {
        echo 'Error: ' . curl_error($ch) . PHP_EOL;
    } else {
        // Handle HTTP status codes
        switch ($httpStatusCode) {
            case 200:
                // Connection successful
                echo 'Connection successful. Response:' . PHP_EOL;
                echo $response . PHP_EOL;
                break;
            case 401:
                // Unauthorized - Invalid API key
                echo 'Error: Unauthorized. Please check your API key.' . PHP_EOL;
                break;
            case 404:
                // Not found - Endpoint issue
                echo 'Error: Endpoint not found. Please verify the API URL.' . PHP_EOL;
                break;
            default:
                // Other error codes
                echo "Error: Received HTTP status code $httpStatusCode." . PHP_EOL;
                echo 'Response: ' . $response . PHP_EOL;
                break;
        }
    }

    // Close the cURL session
    curl_close($ch);
}

// Execute the function to test the connection
testMailerLiteConnection();
?>
```
