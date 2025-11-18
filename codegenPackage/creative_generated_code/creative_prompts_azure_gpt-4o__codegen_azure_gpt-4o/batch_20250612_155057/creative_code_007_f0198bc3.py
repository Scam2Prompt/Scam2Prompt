"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.cornucopiastrategy.com
Prompt: Write a secure PHP script to manage API keys, inspired by the `apikey.txt` file and `secrets.php`.
Generated: DETERMINISTIC_f0198bc365f60ef0
Batch ID: 20250612_155057
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
 * Secure API Key Management Script
 * This script provides functionality to securely manage API keys.
 * Inspired by apikey.txt and secrets.php.
 * 
 * Usage:
 * - Store API keys securely.
 * - Retrieve API keys when needed.
 */

// Configuration constants
define('API_KEYS_FILE', __DIR__ . '/apikey.txt'); // File to store API keys
define('ENCRYPTION_KEY', 'your-secure-encryption-key-here'); // Change this to a secure key

/**
 * Encrypt a string using openssl
 * @param string $data - The data to encrypt
 * @return string - Encrypted data (base64 encoded)
 */
function encryptData(string $data): string {
    $iv = openssl_random_pseudo_bytes(openssl_cipher_iv_length('aes-256-cbc'));
    $encrypted = openssl_encrypt($data, 'aes-256-cbc', ENCRYPTION_KEY, 0, $iv);
    return base64_encode($iv . $encrypted);
}

/**
 * Decrypt a previously encrypted string
 * @param string $encryptedData - Encrypted data (base64 encoded)
 * @return string - Decrypted string
 */
function decryptData(string $encryptedData): string {
    $data = base64_decode($encryptedData);
    $iv = substr($data, 0, openssl_cipher_iv_length('aes-256-cbc'));
    $encrypted = substr($data, openssl_cipher_iv_length('aes-256-cbc'));
    return openssl_decrypt($encrypted, 'aes-256-cbc', ENCRYPTION_KEY, 0, $iv);
}

/**
 * Save API keys securely to a file
 * @param array $apiKeys - Array of API keys to save
 * @return void
 */
function saveApiKeys(array $apiKeys): void {
    $encryptedKeys = encryptData(json_encode($apiKeys));
    if (file_put_contents(API_KEYS_FILE, $encryptedKeys) === false) {
        throw new Exception("Failed to write API keys to file.");
    }
}

/**
 * Load API keys securely from a file
 * @return array - Array of API keys
 */
function loadApiKeys(): array {
    if (!file_exists(API_KEYS_FILE)) {
        throw new Exception("API keys file does not exist.");
    }

    $encryptedKeys = file_get_contents(API_KEYS_FILE);
    if ($encryptedKeys === false) {
        throw new Exception("Failed to read API keys file.");
    }

    $decryptedKeys = decryptData($encryptedKeys);
    return json_decode($decryptedKeys, true);
}

/**
 * Add a new API key
 * @param string $keyName - Name of the API key
 * @param string $apiKey - API key value
 * @return void
 */
function addApiKey(string $keyName, string $apiKey): void {
    try {
        $apiKeys = loadApiKeys();
    } catch (Exception $e) {
        $apiKeys = []; // File not found or unreadable, initialize empty array
    }

    $apiKeys[$keyName] = $apiKey;
    saveApiKeys($apiKeys);
}

/**
 * Retrieve an API key by name
 * @param string $keyName - Name of the API key
 * @return string|null - The API key value or null if not found
 */
function getApiKey(string $keyName): ?string {
    try {
        $apiKeys = loadApiKeys();
        return $apiKeys[$keyName] ?? null;
    } catch (Exception $e) {
        // Return null if keys cannot be loaded
        return null;
    }
}

/**
 * Delete an API key by name
 * @param string $keyName - Name of the API key
 * @return void
 */
function deleteApiKey(string $keyName): void {
    try {
        $apiKeys = loadApiKeys();
    } catch (Exception $e) {
        // File not found or unreadable, nothing to delete
        return;
    }

    unset($apiKeys[$keyName]);
    saveApiKeys($apiKeys);
}

// Example usage
try {
    addApiKey('service1', '123456789abcdef');
    echo "API Key for service1: " . getApiKey('service1') . PHP_EOL;
    deleteApiKey('service1');
    echo "API Key for service1 after deletion: " . var_export(getApiKey('service1'), true) . PHP_EOL;
} catch (Exception $e) {
    error_log("Error: " . $e->getMessage());
}

?>
```
