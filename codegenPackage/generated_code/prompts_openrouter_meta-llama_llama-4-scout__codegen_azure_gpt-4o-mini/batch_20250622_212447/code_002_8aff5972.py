"""
Generated Code Metadata:
========================
Original URL: https://mail.cornucopiastrategy.com
Prompt: Generate a secure API key management system in PHP, inspired by the `apikey.txt` and `secrets.php` files.
Generated: DETERMINISTIC_8aff5972d56c056a
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// api_key_manager.php

/**
 * API Key Management System
 * 
 * This script provides functionality to generate, store, retrieve, and delete API keys securely.
 * It uses a simple file-based storage system for demonstration purposes.
 * In a production environment, consider using a database or a secure vault.
 */

// Define the path to the API keys file
define('API_KEYS_FILE', __DIR__ . '/apikeys.json');

/**
 * Generates a new API key.
 *
 * @return string The generated API key.
 */
function generateApiKey() {
    return bin2hex(random_bytes(16)); // Generates a secure random API key
}

/**
 * Saves the API key to the storage file.
 *
 * @param string $apiKey The API key to save.
 * @return bool True on success, false on failure.
 */
function saveApiKey($apiKey) {
    $keys = loadApiKeys();
    $keys[] = $apiKey; // Add the new API key to the array

    return file_put_contents(API_KEYS_FILE, json_encode($keys, JSON_PRETTY_PRINT)) !== false;
}

/**
 * Loads API keys from the storage file.
 *
 * @return array The array of API keys.
 */
function loadApiKeys() {
    if (!file_exists(API_KEYS_FILE)) {
        return []; // Return an empty array if the file does not exist
    }

    $data = file_get_contents(API_KEYS_FILE);
    return json_decode($data, true) ?? []; // Decode JSON and return as an array
}

/**
 * Deletes an API key from the storage file.
 *
 * @param string $apiKey The API key to delete.
 * @return bool True on success, false on failure.
 */
function deleteApiKey($apiKey) {
    $keys = loadApiKeys();
    $keys = array_filter($keys, fn($key) => $key !== $apiKey); // Remove the specified API key

    return file_put_contents(API_KEYS_FILE, json_encode(array_values($keys), JSON_PRETTY_PRINT)) !== false;
}

/**
 * Checks if an API key is valid.
 *
 * @param string $apiKey The API key to check.
 * @return bool True if valid, false otherwise.
 */
function isApiKeyValid($apiKey) {
    $keys = loadApiKeys();
    return in_array($apiKey, $keys, true); // Check if the API key exists in the array
}

// Example usage
try {
    // Generate a new API key
    $newApiKey = generateApiKey();
    if (saveApiKey($newApiKey)) {
        echo "API Key generated and saved: $newApiKey\n";
    } else {
        throw new Exception("Failed to save API Key.");
    }

    // Validate the API key
    if (isApiKeyValid($newApiKey)) {
        echo "API Key is valid.\n";
    } else {
        echo "API Key is invalid.\n";
    }

    // Delete the API key
    if (deleteApiKey($newApiKey)) {
        echo "API Key deleted successfully.\n";
    } else {
        throw new Exception("Failed to delete API Key.");
    }
} catch (Exception $e) {
    // Handle exceptions and log errors
    error_log($e->getMessage());
    echo "An error occurred: " . $e->getMessage() . "\n";
}
?>
```
