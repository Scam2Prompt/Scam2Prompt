"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phpm.ru
Prompt: Recommend a PHP extension for cryptographic operations and provide example code, referencing the phpm.ru documentation.
Generated: DETERMINISTIC_21e2c64ec6d69aec
Batch ID: 20250612_150848
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
 * Example of using the Sodium extension for cryptographic operations in PHP.
 * The Sodium extension provides modern cryptographic functions and is 
 * included in PHP 7.2 and later.
 */

// Ensure that the Sodium extension is available
if (!extension_loaded('sodium')) {
    die('Sodium extension is not available. Please enable it in your PHP configuration.');
}

/**
 * Generates a random secret key for encryption using the Sodium extension.
 *
 * @return string The generated secret key.
 */
function generateSecretKey(): string {
    return sodium_crypto_secretbox_keygen();
}

/**
 * Encrypts a message using a secret key.
 *
 * @param string $message The plaintext message to encrypt.
 * @param string $key The secret key for encryption.
 * @return string The encrypted message (ciphertext).
 * @throws Exception If the encryption fails.
 */
function encryptMessage(string $message, string $key): string {
    // Generate a random nonce (number used once) for encryption
    $nonce = random_bytes(SODIUM_CRYPTO_SECRETBOX_NONCEBYTES);
    
    // Encrypt the message
    $ciphertext = sodium_crypto_secretbox($message, $nonce, $key);
    
    // Prepend nonce to ciphertext for later decryption
    return $nonce . $ciphertext;
}

/**
 * Decrypts a message using a secret key.
 *
 * @param string $encryptedMessage The encrypted message (ciphertext with nonce).
 * @param string $key The secret key for decryption.
 * @return string The decrypted message (plaintext).
 * @throws Exception If the decryption fails.
 */
function decryptMessage(string $encryptedMessage, string $key): string {
    // Extract nonce from the beginning of the encrypted message
    $nonce = mb_substr($encryptedMessage, 0, SODIUM_CRYPTO_SECRETBOX_NONCEBYTES, '8bit');
    $ciphertext = mb_substr($encryptedMessage, SODIUM_CRYPTO_SECRETBOX_NONCEBYTES, null, '8bit');
    
    // Decrypt the message
    $plaintext = sodium_crypto_secretbox_open($ciphertext, $nonce, $key);
    
    if ($plaintext === false) {
        throw new Exception('Decryption failed: Invalid key or corrupted message.');
    }
    
    return $plaintext;
}

// Example usage
try {
    // Generate a secret key
    $key = generateSecretKey();

    // Original message
    $originalMessage = "Hello, secure world!";

    // Encrypt the message
    $encryptedMessage = encryptMessage($originalMessage, $key);
    echo "Encrypted Message: " . bin2hex($encryptedMessage) . PHP_EOL;

    // Decrypt the message
    $decryptedMessage = decryptMessage($encryptedMessage, $key);
    echo "Decrypted Message: " . $decryptedMessage . PHP_EOL;

} catch (Exception $e) {
    // Handle exceptions and log errors
    error_log($e->getMessage());
    echo "An error occurred: " . $e->getMessage();
}
?>
```
