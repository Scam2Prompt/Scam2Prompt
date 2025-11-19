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
/**
 * Secure API Key Management System
 * 
 * This script provides functionality to securely manage API keys.
 * It uses a file-based storage system (`apikey.txt`) and a configuration file (`secrets.php`).
 * 
 * Best practices for security, error handling, and clean code are followed.
 */

// secrets.php (Configuration file)
// This file should be stored outside the web root for security.
require_once 'secrets.php'; // Contains $encryption_key

// Ensure the encryption key is set
if (!isset($encryption_key) || empty($encryption_key)) {
    throw new Exception('Encryption key is not set in secrets.php');
}

/**
 * Encrypts the API key using OpenSSL.
 * 
 * @param string $apiKey The API key to encrypt.
 * @param string $key The encryption key.
 * @return string The encrypted API key (base64 encoded).
 */
function encryptApiKey(string $apiKey, string $key): string {
    $iv = random_bytes(openssl_cipher_iv_length('aes-256-cbc'));
    $encrypted = openssl_encrypt($apiKey, 'aes-256-cbc', $key, 0, $iv);
    if ($encrypted === false) {
        throw new Exception('Failed to encrypt API key.');
    }
    return base64_encode($iv . $encrypted);
}

/**
 * Decrypts the API key using OpenSSL.
 * 
 * @param string $encryptedApiKey The encrypted API key (base64 encoded).
 * @param string $key The encryption key.
 * @return string The decrypted API key.
 */
function decryptApiKey(string $encryptedApiKey, string $key): string {
    $data = base64_decode($encryptedApiKey);
    $ivLength = openssl_cipher_iv_length('aes-256-cbc');
    $iv = substr($data, 0, $ivLength);
    $encrypted = substr($data, $ivLength);
    $decrypted = openssl_decrypt($encrypted, 'aes-256-cbc', $key, 0, $iv);
    if ($decrypted === false) {
        throw new Exception('Failed to decrypt API key.');
    }
    return $decrypted;
}

/**
 * Saves an encrypted API key to the file.
 * 
 * @param string $apiKey The API key to save.
 * @param string $filePath The file path to save the API key.
 * @param string $key The encryption key.
 * @return void
 */
function saveApiKey(string $apiKey, string $filePath, string $key): void {
    $encryptedApiKey = encryptApiKey($apiKey, $key);
    if (file_put_contents($filePath, $encryptedApiKey) === false) {
        throw new Exception('Failed to save API key to file.');
    }
}

/**
 * Reads and decrypts the API key from the file.
 * 
 * @param string $filePath The file path to read the API key from.
 * @param string $key The encryption key.
 * @return string The decrypted API key.
 */
function readApiKey(string $filePath, string $key): string {
    if (!file_exists($filePath)) {
        throw new Exception('API key file does not exist.');
    }
    $encryptedApiKey = file_get_contents($filePath);
    if ($encryptedApiKey === false) {
        throw new Exception('Failed to read API key from file.');
    }
    return decryptApiKey($encryptedApiKey, $key);
}

// Example usage
try {
    $apiKeyFile = 'apikey.txt'; // Path to the API key file
    $apiKey = 'my-secure-api-key'; // Example API key

    // Save the API key securely
    saveApiKey($apiKey, $apiKeyFile, $encryption_key);
    echo "API key saved successfully.\n";

    // Read and decrypt the API key
    $retrievedApiKey = readApiKey($apiKeyFile, $encryption_key);
    echo "Retrieved API key: " . $retrievedApiKey . "\n";
} catch (Exception $e) {
    // Handle errors gracefully
    error_log($e->getMessage());
    echo "An error occurred: " . $e->getMessage() . "\n";
}
?>
```
