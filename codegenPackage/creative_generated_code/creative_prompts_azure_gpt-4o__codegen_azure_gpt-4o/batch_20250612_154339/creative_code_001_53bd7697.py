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

// PHP Cryptography Example using Sodium extension
// Sodium is a widely-used, modern cryptography library.
// Ensure the Sodium extension is installed and enabled on your PHP environment.

// Function to encrypt data using Sodium
function encryptData(string $plaintext, string $key): string {
    // Generate a random nonce (Number used once)
    $nonce = random_bytes(SODIUM_CRYPTO_SECRETBOX_NONCEBYTES);

    // Perform encryption using the secret key and nonce
    $ciphertext = sodium_crypto_secretbox($plaintext, $nonce, $key);

    // Combine the nonce and ciphertext for safe storage or transmission
    return base64_encode($nonce . $ciphertext);
}

// Function to decrypt data using Sodium
function decryptData(string $encrypted, string $key): string {
    // Decode the base64-encoded string
    $decoded = base64_decode($encrypted);

    // Extract the nonce and ciphertext from the decoded data
    $nonce = substr($decoded, 0, SODIUM_CRYPTO_SECRETBOX_NONCEBYTES);
    $ciphertext = substr($decoded, SODIUM_CRYPTO_SECRETBOX_NONCEBYTES);

    // Perform decryption using the secret key and nonce
    $plaintext = sodium_crypto_secretbox_open($ciphertext, $nonce, $key);

    if ($plaintext === false) {
        throw new Exception('Decryption failed. Invalid key or data.');
    }

    return $plaintext;
}

// Example Usage
try {
    // Generate a random 256-bit (32-byte) key for encryption
    $key = random_bytes(SODIUM_CRYPTO_SECRETBOX_KEYBYTES);

    // Plaintext to encrypt
    $plaintext = "Hello, secure world!";

    // Encrypt the plaintext
    $encrypted = encryptData($plaintext, $key);
    echo "Encrypted: $encrypted\n";

    // Decrypt the encrypted data
    $decrypted = decryptData($encrypted, $key);
    echo "Decrypted: $decrypted\n";
} catch (Exception $e) {
    // Handle exceptions gracefully
    echo "Error: " . $e->getMessage();
}

// Ensure memory safety
sodium_memzero($key);

?>
```
