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
 * Validates API keys stored in a file.
 *
 * @author [Your Name]
 */

// Configuration
const API_KEYS_FILE = 'key.php';
const API_KEY_VAR_NAME = 'api_key';

/**
 * Loads API keys from a PHP file.
 *
 * @return array|false API keys or false on failure.
 */
function loadApiKeys(): array|false
{
    if (!file_exists(API_KEYS_FILE)) {
        error_log("API keys file '" . API_KEYS_FILE . "' not found.");
        return false;
    }

    try {
        require API_KEYS_FILE;
        if (!isset($api_keys) || !is_array($api_keys)) {
            error_log("Invalid API keys format in '" . API_KEYS_FILE . "'.");
            return false;
        }
        return $api_keys;
    } catch (Throwable $e) {
        error_log("Failed to load API keys from '" . API_KEYS_FILE . "': " . $e->getMessage());
        return false;
    }
}

/**
 * Validates an API key.
 *
 * @param string $apiKey API key to validate.
 * @return bool True if valid, false otherwise.
 */
function validateApiKey(string $apiKey): bool
{
    $apiKeys = loadApiKeys();
    if ($apiKeys === false) {
        return false;
    }

    return in_array($apiKey, $apiKeys, true);
}

/**
 * Returns a JSON response.
 *
 * @param bool $success Success status.
 * @param string|null $message Optional message.
 */
function sendJsonResponse(bool $success, string $message = null): void
{
    http_response_code($success ? 200 : 401);
    header('Content-Type: application/json');

    $response = [
        'success' => $success,
    ];

    if ($message !== null) {
        $response['message'] = $message;
    }

    echo json_encode($response, JSON_THROW_ON_ERROR);
}

// Main logic
if ($_SERVER['REQUEST_METHOD'] !== 'GET') {
    sendJsonResponse(false, 'Invalid request method.');
    exit;
}

$apiKey = $_GET[API_KEY_VAR_NAME] ?? null;

if (!is_string($apiKey) || trim($apiKey) === '') {
    sendJsonResponse(false, 'API key is missing or empty.');
    exit;
}

if (validateApiKey($apiKey)) {
    sendJsonResponse(true);
} else {
    sendJsonResponse(false, 'Invalid API key.');
}
```
