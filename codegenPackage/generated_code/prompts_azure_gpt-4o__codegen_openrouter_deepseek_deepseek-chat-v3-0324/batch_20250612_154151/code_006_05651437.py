"""
Generated Code Metadata:
========================
Original URL: https://sophon-farming.pro
Prompt: Generate a PHP script that validates API keys stored in a file like `key.php` and returns a JSON response indicating success or failure.
Generated: DETERMINISTIC_05651437648440c1
Batch ID: 20250612_154151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * API Key Validator
 * 
 * This script validates an API key provided in the request against a list of valid keys stored in a file.
 * It returns a JSON response indicating whether the key is valid or not.
 */

// Set the content type to JSON
header('Content-Type: application/json');

// Define the path to the keys file
define('KEYS_FILE', 'key.php');

// Check if the API key is provided in the request
if (!isset($_GET['api_key']) || empty($_GET['api_key'])) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'API key is required']);
    exit;
}

$providedKey = $_GET['api_key'];

try {
    // Check if the keys file exists
    if (!file_exists(KEYS_FILE)) {
        throw new Exception('Keys file not found');
    }

    // Include the keys file (assuming it returns an array of valid keys)
    $validKeys = include KEYS_FILE;

    // Validate that the keys file returns an array
    if (!is_array($validKeys)) {
        throw new Exception('Invalid keys file format');
    }

    // Check if the provided key is in the list of valid keys
    if (in_array($providedKey, $validKeys)) {
        echo json_encode(['success' => true, 'message' => 'API key is valid']);
    } else {
        http_response_code(401);
        echo json_encode(['success' => false, 'error' => 'Invalid API key']);
    }
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => $e->getMessage()]);
}
?>
```
