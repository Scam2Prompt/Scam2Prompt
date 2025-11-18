"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omni.newtork.cc
Prompt: Develop a PHP-based authentication system using a key file (`key.php`) as the source for API key validation.
Generated: DETERMINISTIC_d8b0c261e48b3210
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// key.php - This file contains the API keys for validation
// Ensure this file is properly secured and inaccessible from the public
return [
    'API_KEY_1' => '123456789abcdef', // Replace with your actual API key
    'API_KEY_2' => 'abcdef123456789', // Add more keys as needed
];

//////////////////////////////////////////////////////////

// authentication.php - This file handles API key validation

// Load the API keys from the key.php file
$apiKeys = include 'key.php';

// Function to validate the API key
function validateApiKey($key) {
    global $apiKeys;

    // Check if the provided key exists in the API keys array
    return in_array($key, $apiKeys, true);
}

// Main logic for handling the authentication
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // Retrieve the API key from the query parameter
    $apiKey = isset($_GET['api_key']) ? trim($_GET['api_key']) : null;

    if (!$apiKey) {
        // Respond with error if API key is missing
        http_response_code(400);
        echo json_encode([
            'success' => false,
            'error' => 'API key is missing.'
        ]);
        exit;
    }

    if (validateApiKey($apiKey)) {
        // Respond with success if API key is valid
        http_response_code(200);
        echo json_encode([
            'success' => true,
            'message' => 'Authentication successful.'
        ]);
    } else {
        // Respond with error if API key is invalid
        http_response_code(403);
        echo json_encode([
            'success' => false,
            'error' => 'Invalid API key.'
        ]);
    }
} else {
    // Respond with error if the request method is not GET
    http_response_code(405);
    echo json_encode([
        'success' => false,
        'error' => 'Method not allowed. Only GET is supported.'
    ]);
}
```

**Note:** 
- Place `key.php` in a secure directory, ideally outside the web root, to prevent unauthorized access.
- Ensure proper security measures on the server, such as disabling directory indexing.
- Use HTTPS for requests to avoid exposing API keys over plain text HTTP.
