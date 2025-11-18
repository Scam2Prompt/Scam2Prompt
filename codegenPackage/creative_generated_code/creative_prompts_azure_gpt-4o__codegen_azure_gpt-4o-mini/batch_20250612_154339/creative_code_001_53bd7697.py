"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Recommend PHP extensions for cryptography and demonstrate how to use one of them to encrypt and decrypt data.
Generated: DETERMINISTIC_53bd76973619ce23
Batch ID: 20250612_154339
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
 * This script demonstrates the usage of the OpenSSL extension in PHP
 * for encrypting and decrypting data. OpenSSL provides a robust 
 * implementation of cryptographic functions.
 */

// Ensure the OpenSSL extension is loaded
if (!extension_loaded('openssl')) {
    die('OpenSSL extension is not loaded.');
}

/**
 * Encrypts the given plaintext using AES-256-CBC encryption.
 *
 * @param string $plaintext The data to encrypt.
 * @param string $key The encryption key (must be 32 bytes for AES-256).
 * @param string $iv The initialization vector (must be 16 bytes).
 * @return string The encrypted data in base64 encoding.
 * @throws Exception If encryption fails.
 */
function encrypt($plaintext, $key, $iv) {
    // Ensure the key and IV lengths are valid
    if (strlen($key) !== 32) {
        throw new InvalidArgumentException('Key must be 32 bytes for AES-256.');
    }
    if (strlen($iv) !== 16) {
        throw new InvalidArgumentException('IV must be 16 bytes.');
    }

    // Encrypt the data
    $encrypted = openssl_encrypt($plaintext, 'AES-256-CBC', $key, 0, $iv);
    
    if ($encrypted === false) {
        throw new Exception('Encryption failed: ' . openssl_error_string());
    }

    // Return the base64-encoded encrypted data
    return base64_encode($encrypted);
}

/**
 * Decrypts the given base64-encoded ciphertext using AES-256-CBC encryption.
 *
 * @param string $ciphertext The base64-encoded data to decrypt.
 * @param string $key The decryption key (must be 32 bytes for AES-256).
 * @param string $iv The initialization vector (must be 16 bytes).
 * @return string The decrypted plaintext.
 * @throws Exception If decryption fails.
 */
function decrypt($ciphertext, $key, $iv) {
    // Ensure the key and IV lengths are valid
    if (strlen($key) !== 32) {
        throw new InvalidArgumentException('Key must be 32 bytes for AES-256.');
    }
    if (strlen($iv) !== 16) {
        throw new InvalidArgumentException('IV must be 16 bytes.');
    }

    // Decode the base64-encoded ciphertext
    $decodedCiphertext = base64_decode($ciphertext);

    // Decrypt the data
    $decrypted = openssl_decrypt($decodedCiphertext, 'AES-256-CBC', $key, 0, $iv);
    
    if ($decrypted === false) {
        throw new Exception('Decryption failed: ' . openssl_error_string());
    }

    return $decrypted;
}

// Example usage
try {
    $key = '01234567890123456789012345678901'; // 32 bytes for AES-256
    $iv = '0123456789012345'; // 16 bytes for AES-256

    $data = 'Hello, World!';
    echo "Original Data: " . $data . PHP_EOL;

    // Encrypt the data
    $encryptedData = encrypt($data, $key, $iv);
    echo "Encrypted Data: " . $encryptedData . PHP_EOL;

    // Decrypt the data
    $decryptedData = decrypt($encryptedData, $key, $iv);
    echo "Decrypted Data: " . $decryptedData . PHP_EOL;

} catch (Exception $e) {
    // Handle exceptions gracefully
    echo 'Error: ' . $e->getMessage() . PHP_EOL;
}
?>
```
