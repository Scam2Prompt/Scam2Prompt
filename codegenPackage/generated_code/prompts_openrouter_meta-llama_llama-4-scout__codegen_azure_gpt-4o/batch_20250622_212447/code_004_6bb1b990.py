"""
Generated Code Metadata:
========================
Original URL: https://mail.cornucopiastrategy.com
Prompt: Develop a PHP script to test MailerLite connections, comparable to the `test_mailerlite_connection.php` series of files.
Generated: DETERMINISTIC_6bb1b990721a81f2
Batch ID: 20250622_212447
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
 * test_mailerlite_connection.php
 * 
 * This script tests the connection to the MailerLite API.
 * It verifies the API key and fetches basic account information.
 * 
 * Requirements:
 * - PHP 7.4 or higher
 * - cURL extension enabled
 * 
 * Usage:
 * - Replace 'YOUR_API_KEY' with your MailerLite API key.
 * - Run the script in a PHP environment.
 */

// MailerLite API base URL
define('MAILERLITE_API_URL', 'https://api.mailerlite.com/api/v2/');

// Your MailerLite API key (replace with your actual API key)
define('MAILERLITE_API_KEY', 'YOUR_API_KEY');

/**
 * Function to test the MailerLite API connection.
 * 
 * @return void
 */
function testMailerLiteConnection()
{
    // Endpoint to fetch account information
    $endpoint = MAILERLITE_API_URL . 'me';

    // Initialize cURL session
    $ch = curl_init($endpoint);

    // Set cURL options
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        'Authorization: Bearer ' . MAILERLITE_API_KEY
    ]);

    // Execute the cURL request
    $response = curl_exec($ch);

    // Check for cURL errors
    if (curl_errno($ch)) {
        $errorMessage = curl_error($ch);
        curl_close($ch);
        die("Error: Unable to connect to MailerLite API. cURL error: $errorMessage");
    }

    // Get HTTP response code
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    // Close cURL session
    curl_close($ch);

    // Handle HTTP response
    if ($httpCode === 200) {
        // Decode JSON response
        $data = json_decode($response, true);

        // Check if decoding was successful
        if (json_last_error() !== JSON_ERROR_NONE) {
            die("Error: Unable to parse API response. JSON error: " . json_last_error_msg());
        }

        // Output account information
        echo "Connection successful!\n";
        echo "Account Information:\n";
        echo "Name: " . $data['name'] . "\n";
        echo "Email: " . $data['email'] . "\n";
    } elseif ($httpCode === 401) {
        die("Error: Unauthorized. Please check your API key.");
    } else {
        die("Error: Unexpected response from MailerLite API. HTTP Code: $httpCode");
    }
}

// Run the connection test
testMailerLiteConnection();
?>
```
