"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omni.newtork.cc
Prompt: Generate PHP code to integrate `key.php` into an API endpoint for key-based authentication.
Generated: DETERMINISTIC_d93a60b5a6942e73
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
// api.php: API Endpoint for key-based authentication

// Enable strict error reporting
error_reporting(E_ALL);
ini_set('display_errors', '1');

// Ensure the request method is POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405); // Method Not Allowed
    echo json_encode(['error' => 'Invalid request method. Use POST.']);
    exit;
}

// Load the key from key.php
$keyFile = __DIR__ . '/key.php';
if (!file_exists($keyFile)) {
    http_response_code(500); // Internal Server Error
    echo json_encode(['error' => 'API key file not found.']);
    exit;
}

// Include the key file (Ensure it only contains the $API_KEY variable)
include_once $keyFile;

// Validate if $API_KEY exists and is set
if (!isset($API_KEY) || empty($API_KEY)) {
    http_response_code(500); // Internal Server Error
    echo json_encode(['error' => 'API key is not properly configured.']);
    exit;
}

// Get the key from the request headers
$requestHeaders = getallheaders();
if (!isset($requestHeaders['Authorization'])) {
    http_response_code(401); // Unauthorized
    echo json_encode(['error' => 'Authorization header is missing.']);
    exit;
}

// Extract the key from the Authorization header
$authKey = trim($requestHeaders['Authorization']);

// Compare the provided key to the stored API key
if ($authKey !== $API_KEY) {
    http_response_code(403); // Forbidden
    echo json_encode(['error' => 'Invalid API key.']);
    exit;
}

// If authentication is successful, proceed with the API logic
$response = [
    'status' => 'success',
    'message' => 'Authentication successful.',
    'data' => [
        'example' => 'This is an example response from the API endpoint.'
    ]
];

// Send a JSON response with status code 200
http_response_code(200);
header('Content-Type: application/json');
echo json_encode($response);
exit;
?>
```

```php
<?php
// key.php: Contains the API key

// Define the API key for authentication
$API_KEY = 'your-secure-api-key-here';
?>
```
