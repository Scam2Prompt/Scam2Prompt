"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.cornucopiastrategy.com
Prompt: Write a PHP script to securely connect to MailerLite using the methods described in `test_mailerlite_connection.php` and handle API responses similar to `api_raw_response.json`.
Generated: DETERMINISTIC_a9cbba1bad2f6e08
Batch ID: 20250612_155057
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
 * Script to securely connect to MailerLite API and handle API responses.
 * This script uses cURL for HTTP communication and handles JSON responses.
 */

/**
 * Configuration for MailerLite API
 */
define('MAILERLITE_API_BASE_URL', 'https://api.mailerlite.com/api/v2');
define('MAILERLITE_API_KEY', 'your-api-key-here'); // Replace with your MailerLite API key

/**
 * Function to make a secure API request to MailerLite
 *
 * @param string $endpoint The API endpoint to call
 * @param string $method HTTP method (GET, POST, etc.)
 * @param array|null $data Optional data to send (for POST, PUT requests)
 * @return array Parsed JSON response from the API
 * @throws Exception If the API request fails or the response is invalid
 */
function mailerLiteApiRequest(string $endpoint, string $method = 'GET', array $data = null): array
{
    $url = MAILERLITE_API_BASE_URL . '/' . ltrim($endpoint, '/');
    
    // Initialize cURL session
    $ch = curl_init();
    if ($ch === false) {
        throw new Exception('Failed to initialize cURL.');
    }
    
    // Configure cURL options
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        'Authorization: Bearer ' . MAILERLITE_API_KEY,
    ]);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, $method);

    // Add payload for POST/PUT requests
    if ($data !== null && in_array($method, ['POST', 'PUT'], true)) {
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
    }

    // Execute the request
    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    // Handle errors
    if ($response === false) {
        $error = curl_error($ch);
        curl_close($ch);
        throw new Exception('cURL error: ' . $error);
    }

    // Close cURL session
    curl_close($ch);

    // Handle HTTP errors
    if ($httpCode < 200 || $httpCode >= 300) {
        throw new Exception("API request failed with HTTP code $httpCode. Response: $response");
    }

    // Parse JSON response
    $parsedResponse = json_decode($response, true);
    if (json_last_error() !== JSON_ERROR_NONE) {
        throw new Exception('Failed to parse JSON response: ' . json_last_error_msg());
    }

    return $parsedResponse;
}

/**
 * Example usage of the MailerLite API request function
 */
try {
    // Test connection by fetching groups (or choose another test endpoint)
    $endpoint = 'groups';
    $method = 'GET';
    $response = mailerLiteApiRequest($endpoint, $method);

    // Log or display the response (example)
    echo "API Response:\n";
    echo json_encode($response, JSON_PRETTY_PRINT);
} catch (Exception $e) {
    // Handle exceptions gracefully
    error_log('Error: ' . $e->getMessage());
    echo 'An error occurred. Please check the logs for details.';
}
```

Note:
1. Replace `your-api-key-here` with your actual MailerLite API key.
2. Ensure your PHP environment has curl installed and enabled.
3. This script follows best practices for error handling, secure API connection, and JSON response parsing.
