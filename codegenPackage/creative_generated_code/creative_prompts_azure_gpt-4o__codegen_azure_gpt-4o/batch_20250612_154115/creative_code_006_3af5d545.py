"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omni.newtork.cc
Prompt: Create a PHP script to encrypt and decrypt API keys stored in `key.php` for secure usage in a web application.
Generated: DETERMINISTIC_3af5d54534e9b52d
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
/**
 * This script provides functionality to encrypt and decrypt API keys stored in `key.php` for secure usage.
 * Please make sure OpenSSL extension is enabled in your PHP environment.
 */

// Define encryption configuration
define('ENCRYPTION_METHOD', 'AES-256-CBC'); // Encryption algorithm
define('SECRET_KEY', 'your-secret-key'); // Replace this with a strong secret key
define('SECRET_IV', 'your-secret-iv');   // Replace this with a strong secret IV

/**
 * Function to encrypt a plaintext string
 *
 * @param string $plaintext The text to be encrypted
 * @return string The encrypted string
 */
function encrypt($plaintext)
{
    // Generate a key and initialization vector (IV) from SECRET_KEY and SECRET_IV
    $key = hash('sha256', SECRET_KEY);
    $iv = substr(hash('sha256', SECRET_IV), 0, 16);

    // Encrypt the plaintext
    $encrypted = openssl_encrypt($plaintext, ENCRYPTION_METHOD, $key, 0, $iv);

    // Return the encrypted string in base64 format
    return base64_encode($encrypted);
}

/**
 * Function to decrypt an encrypted string
 *
 * @param string $encryptedText The encrypted text in base64 format
 * @return string The decrypted string
 */
function decrypt($encryptedText)
{
    // Generate a key and initialization vector (IV) from SECRET_KEY and SECRET_IV
    $key = hash('sha256', SECRET_KEY);
    $iv = substr(hash('sha256', SECRET_IV), 0, 16);

    // Decode the base64-encoded string
    $encrypted = base64_decode($encryptedText);

    // Decrypt the string
    $decrypted = openssl_decrypt($encrypted, ENCRYPTION_METHOD, $key, 0, $iv);

    return $decrypted;
}

try {
    // Read API key from key.php
    $apiKey = require 'key.php';

    // Encrypt the API key
    $encryptedKey = encrypt($apiKey);

    // Output the encrypted key for testing
    echo "Encrypted API Key: " . $encryptedKey . PHP_EOL;

    // Decrypt the API key for testing
    $decryptedKey = decrypt($encryptedKey);

    // Output the decrypted key for testing
    echo "Decrypted API Key: " . $decryptedKey . PHP_EOL;

    // Ensure the decrypted key matches the original
    if ($decryptedKey !== $apiKey) {
        throw new Exception("Decryption error: Decrypted key does not match the original.");
    }
} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage() . PHP_EOL;
}
?>
```

Content of `key.php`:
```php
<?php
// Replace with your actual API key
return 'your-actual-api-key';
?>
```
