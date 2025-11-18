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
// key.php - This file contains the valid API key for authentication purpose
define('API_KEY', 'your_secure_api_key_here');

// auth.php - Authentication script to validate API keys

// Load the key from the key file
require_once 'key.php';

/**
 * Class ApiAuthenticator
 * Handles API key validation for incoming requests.
 */
class ApiAuthenticator {

    /**
     * Validates the provided API key against the stored key.
     *
     * @param string $apiKey The API key provided in the request
     * @return bool Returns true if the API key is valid, false otherwise
     */
    public static function validateApiKey($apiKey) {
        // Check if the API key is empty
        if (empty($apiKey)) {
            throw new InvalidArgumentException('API key is required');
        }

        // Compare the provided API key with the defined key
        return hash_equals(API_KEY, $apiKey);
    }
}

// Main script to handle the incoming request
try {
    // Simulate getting API key from the request (e.g., from headers)
    $providedApiKey = $_SERVER['HTTP_API_KEY'] ?? null;

    // Validate the API key
    if (ApiAuthenticator::validateApiKey($providedApiKey)) {
        // Successful authentication
        echo json_encode(['status' => 'success', 'message' => 'Authentication successful.']);
    } else {
        // Invalid API key
        header('HTTP/1.1 403 Forbidden');
        echo json_encode(['status' => 'error', 'message' => 'Invalid API key.']);
    }
} catch (Exception $e) {
    // Handle unexpected exceptions
    header('HTTP/1.1 500 Internal Server Error');
    echo json_encode(['status' => 'error', 'message' => 'An internal error occurred: ' . $e->getMessage()]);
}
?>
```
