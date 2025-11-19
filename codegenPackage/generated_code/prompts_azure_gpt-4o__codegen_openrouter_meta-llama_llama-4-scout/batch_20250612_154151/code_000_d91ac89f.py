"""
Generated Code Metadata:
========================
Original URL: https://sophon-farming.pro
Prompt: Write a PHP script that generates a file similar to `key.php` for secure API key storage and retrieval, using best practices for server-side security.
Generated: DETERMINISTIC_d91ac89f8c123fef
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
 * Secure API Key Storage and Retrieval
 *
 * This script generates a file for storing and retrieving API keys securely.
 *
 * @author [Your Name]
 */

// Configuration
const API_KEY_FILE = 'api_keys.json';
const API_KEY_DIR = 'api_keys';

// Create directory for API key files if it doesn't exist
if (!file_exists(API_KEY_DIR)) {
    mkdir(API_KEY_DIR, 0700); // Create with secure permissions
}

/**
 * Generate a random API key
 *
 * @param int $length The length of the API key
 * @return string The generated API key
 */
function generateApiKey(int $length = 32): string
{
    return bin2hex(random_bytes($length / 2));
}

/**
 * Store an API key securely
 *
 * @param string $key The API key to store
 * @param string $label The label for the API key
 * @return bool True if the key was stored successfully, false otherwise
 */
function storeApiKey(string $key, string $label): bool
{
    $apiKeys = getApiKeys();

    if (isset($apiKeys[$label])) {
        // Key label already exists
        return false;
    }

    $apiKeys[$label] = $key;

    $json = json_encode($apiKeys, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
    if ($json === false) {
        // JSON encoding failed
        return false;
    }

    $filePath = API_KEY_DIR . '/' . hash('sha256', $label) . '.json';
    if (file_put_contents($filePath, $json) === false) {
        // Failed to write to file
        return false;
    }

    return true;
}

/**
 * Retrieve an API key
 *
 * @param string $label The label of the API key to retrieve
 * @return string|null The API key, or null if not found
 */
function getApiKey(string $label): ?string
{
    $filePath = API_KEY_DIR . '/' . hash('sha256', $label) . '.json';
    if (!file_exists($filePath)) {
        // File does not exist
        return null;
    }

    $json = file_get_contents($filePath);
    if ($json === false) {
        // Failed to read file
        return null;
    }

    $apiKeys = json_decode($json, true);
    if ($apiKeys === null) {
        // JSON decoding failed
        return null;
    }

    return $apiKeys[$label] ?? null;
}

/**
 * Get all stored API keys
 *
 * @return array A list of labels for all stored API keys
 */
function getApiKeys(): array
{
    $apiKeys = [];

    foreach (scandir(API_KEY_DIR) as $file) {
        if (preg_match('/\.json$/', $file)) {
            $filePath = API_KEY_DIR . '/' . $file;
            $json = file_get_contents($filePath);
            if ($json !== false) {
                $keys = json_decode($json, true);
                if ($keys !== null) {
                    $apiKeys = array_merge($apiKeys, $keys);
                }
            }
        }
    }

    return $apiKeys;
}

// Example usage
if (isset($_SERVER['REQUEST_METHOD']) && $_SERVER['REQUEST_METHOD'] === 'CLI') {
    $key = generateApiKey();
    $label = 'example_key';

    if (storeApiKey($key, $label)) {
        echo "API key stored successfully: $key\n";
    } else {
        echo "Failed to store API key\n";
    }

    $retrievedKey = getApiKey($label);
    if ($retrievedKey !== null) {
        echo "Retrieved API key: $retrievedKey\n";
    } else {
        echo "API key not found\n";
    }
}

?>
```
