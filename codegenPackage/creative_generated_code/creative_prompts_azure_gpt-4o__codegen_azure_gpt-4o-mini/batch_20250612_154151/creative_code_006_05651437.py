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
// api_key_validator.php

// Load API keys from an external file
require 'key.php';

// Set the content type to JSON
header('Content-Type: application/json');

// Function to validate the API key
function validateApiKey($apiKey) {
    // Check if the API key matches any of the stored keys
    global $apiKeys; // Access the global variable for API keys
    return in_array($apiKey, $apiKeys);
}

// Check if the API key is provided in the request
if (isset($_GET['api_key'])) {
    $apiKey = $_GET['api_key'];

    // Validate the API key
    if (validateApiKey($apiKey)) {
        // Return success response
        echo json_encode([
            'status' => 'success',
            'message' => 'API key is valid.'
        ]);
    } else {
        // Return failure response
        echo json_encode([
            'status' => 'failure',
            'message' => 'Invalid API key.'
        ]);
    }
} else {
    // Return error response for missing API key
    echo json_encode([
        'status' => 'error',
        'message' => 'API key is required.'
    ]);
}
?>
```

```php
<?php
// key.php

// Array to store valid API keys
$apiKeys = [
    '123456',
    'abcdef',
    'ghijkl',
    // Add more keys as needed
];
?>
```
