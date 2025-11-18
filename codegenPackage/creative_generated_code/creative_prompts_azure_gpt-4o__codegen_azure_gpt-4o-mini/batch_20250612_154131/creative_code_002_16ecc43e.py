"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.marketpoly.net
Prompt: Provide a PHP script that interacts with "key.php" to validate API keys stored in the file and return appropriate responses.
Generated: DETERMINISTIC_16ecc43e419279a7
Batch ID: 20250612_154131
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
 * API Key Validation Script
 *
 * This script validates API keys against a list of keys stored in 'key.php'.
 * It returns a JSON response indicating whether the provided key is valid or not.
 */

// Include the file containing the API keys
require_once 'key.php';

/**
 * Function to validate the API key
 *
 * @param string $apiKey The API key to validate
 * @param array $validKeys An array of valid API keys
 * @return bool Returns true if the key is valid, false otherwise
 */
function validateApiKey($apiKey, $validKeys) {
    return in_array($apiKey, $validKeys);
}

// Set the response header to indicate JSON content
header('Content-Type: application/json');

// Check for the API key in the request
if (!isset($_GET['api_key'])) {
    // Return an error response if the API key is missing
    http_response_code(400);
    echo json_encode(['error' => 'API key is required.']);
    exit();
}

// Retrieve the API key from query parameters
$apiKey = $_GET['api_key'];

// Validate the API key
if (validateApiKey($apiKey, $apiKeys)) {
    // Return a success response if the key is valid
    http_response_code(200);
    echo json_encode(['status' => 'success', 'message' => 'API key is valid.']);
} else {
    // Return an error response if the key is invalid
    http_response_code(401);
    echo json_encode(['error' => 'Invalid API key.']);
}
```

**key.php** (for reference):
```php
<?php
// Define an array of valid API keys
$apiKeys = [
    'key1',  // Example valid key
    'key2',  // Example valid key
    'key3'   // Example valid key
];
```
