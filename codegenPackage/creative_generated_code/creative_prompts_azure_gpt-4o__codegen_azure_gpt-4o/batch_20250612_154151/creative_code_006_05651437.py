"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon-farming.pro
Prompt: Generate a PHP script that validates API keys stored in a file like `key.php` and returns a JSON response indicating success or failure.
Generated: DETERMINISTIC_05651437648440c1
Batch ID: 20250612_154151
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
 * Validate API Key
 *
 * This script validates API keys stored in an external `key.php` file.
 * It returns a JSON response indicating success or failure.
 */

// Enable strict types for better type safety
declare(strict_types=1);

// Set headers to handle JSON responses
header('Content-Type: application/json');

// Path to the file containing the API keys
$keyFilePath = __DIR__ . '/key.php';

try {
    // Check if the key file exists
    if (!file_exists($keyFilePath)) {
        throw new Exception('Key file not found.');
    }

    // Include the key file (ensure the file returns an array of keys)
    $keys = include $keyFilePath;

    // Validate that the included file returns an array
    if (!is_array($keys)) {
        throw new Exception('Invalid key file format.');
    }

    // Get the API key from the request (via GET parameter 'api_key')
    $inputKey = filter_input(INPUT_GET, 'api_key', FILTER_SANITIZE_STRING);

    // Validate input key presence
    if (empty($inputKey)) {
        echo json_encode(['success' => false, 'message' => 'API key is missing.']);
        exit;
    }

    // Check if the input key is in the list of valid keys
    if (in_array($inputKey, $keys, true)) {
        echo json_encode(['success' => true, 'message' => 'API key validated successfully.']);
    } else {
        echo json_encode(['success' => false, 'message' => 'Invalid API key.']);
    }
} catch (Exception $e) {
    // Handle errors gracefully and return meaningful response
    echo json_encode(['success' => false, 'message' => 'An error occurred: ' . $e->getMessage()]);
}
```

`key.php` (example file):
```php
<?php
// This file should return an array of valid API keys.
return [
    'key1',
    'key2',
    'key3',
];
```
