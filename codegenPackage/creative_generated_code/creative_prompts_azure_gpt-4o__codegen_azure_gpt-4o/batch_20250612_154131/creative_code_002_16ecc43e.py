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
 * This script validates API keys against the keys stored in "key.php".
 * It returns appropriate JSON responses for valid and invalid keys.
 */

// Enable error reporting for development (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Set response headers to return JSON content
header('Content-Type: application/json');

// Include the file containing stored API keys
require_once 'key.php'; // Assumes "key.php" defines $apiKeys as an array of valid keys

// Check if the API key is provided in the request
if (!isset($_GET['api_key'])) {
    http_response_code(400);
    echo json_encode([
        'success' => false,
        'error' => 'API key is missing.'
    ]);
    exit;
}

// Retrieve the API key from the query parameter
$providedKey = $_GET['api_key'];

// Validate the API key
if (in_array($providedKey, $apiKeys, true)) {
    // Key is valid
    http_response_code(200);
    echo json_encode([
        'success' => true,
        'message' => 'API key is valid.'
    ]);
} else {
    // Key is invalid
    http_response_code(403);
    echo json_encode([
        'success' => false,
        'error' => 'Invalid API key.'
    ]);
}

?>
```

**Contents of `key.php` (Example):**
```php
<?php
// Define an array of valid API keys
$apiKeys = [
    '123456789abcdef',
    'abc123xyz456',
    'key_example_789'
];
?>
```
