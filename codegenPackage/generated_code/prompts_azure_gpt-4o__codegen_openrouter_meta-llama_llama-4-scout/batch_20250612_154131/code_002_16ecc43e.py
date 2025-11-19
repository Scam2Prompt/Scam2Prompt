"""
Generated Code Metadata:
========================
Original URL: https://app.marketpoly.net
Prompt: Provide a PHP script that interacts with "key.php" to validate API keys stored in the file and return appropriate responses.
Generated: DETERMINISTIC_16ecc43e419279a7
Batch ID: 20250612_154131
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
 * This script validates API keys stored in 'key.php' and returns appropriate responses.
 */

// Configuration
const API_KEY_FILE = 'key.php';

/**
 * Load API keys from file
 *
 * @return array|false
 */
function loadApiKeys(): array|false
{
    try {
        // Check if file exists
        if (!file_exists(API_KEY_FILE)) {
            throw new Exception("API key file not found.");
        }

        // Include the API key file
        $apiKeys = include API_KEY_FILE;

        // Validate the API keys
        if (!is_array($apiKeys)) {
            throw new Exception("Invalid API key format.");
        }

        return $apiKeys;
    } catch (Exception $e) {
        error_log($e->getMessage());
        return false;
    }
}

/**
 * Validate API key
 *
 * @param string $apiKey
 * @return bool
 */
function validateApiKey(string $apiKey): bool
{
    $apiKeys = loadApiKeys();

    if ($apiKeys === false) {
        return false;
    }

    return in_array($apiKey, $apiKeys);
}

/**
 * Handle API request
 *
 * @param string $apiKey
 * @return array
 */
function handleApiRequest(string $apiKey): array
{
    if (validateApiKey($apiKey)) {
        return [
            'status' => 'success',
            'message' => 'API key is valid.',
        ];
    } else {
        http_response_code(401);
        return [
            'status' => 'error',
            'message' => 'Invalid API key.',
        ];
    }
}

// Main execution
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // Get API key from query parameter
    $apiKey = $_GET['api_key'] ?? null;

    if ($apiKey === null) {
        http_response_code(400);
        echo json_encode([
            'status' => 'error',
            'message' => 'API key is required.',
        ]);
    } else {
        echo json_encode(handleApiRequest($apiKey));
    }
} else {
    http_response_code(405);
    echo json_encode([
        'status' => 'error',
        'message' => 'Method not allowed.',
    ]);
}

exit;
```
