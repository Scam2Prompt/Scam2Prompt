"""
Generated Code Metadata:
========================
Original URL: https://mail.cornucopiastrategy.com
Prompt: Write a secure PHP script to manage API keys, inspired by the `apikey.txt` file and `secrets.php`.
Generated: DETERMINISTIC_f0198bc365f60ef0
Batch ID: 20250612_155057
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
 * API Key Management Script
 * 
 * This script provides secure management of API keys, including generation, storage,
 * validation, and revocation. Keys are stored in an encrypted format.
 */

// Ensure strict types for type safety
declare(strict_types=1);

// Configuration settings
define('API_KEY_FILE', __DIR__ . '/apikeys.dat');
define('ENCRYPTION_KEY', 'your-32-byte-encryption-key-here'); // Replace with a secure key
define('KEY_LENGTH', 32); // Length of generated API keys in bytes
define('HASH_ALGO', 'sha256'); // Hashing algorithm for key verification

// Custom exceptions for better error handling
class ApiKeyException extends Exception {}
class StorageException extends ApiKeyException {}
class SecurityException extends ApiKeyException {}

/**
 * Generate a new cryptographically secure API key
 * 
 * @return string The generated API key
 * @throws SecurityException If key generation fails
 */
function generateApiKey(): string {
    try {
        $randomBytes = random_bytes(KEY_LENGTH);
        return bin2hex($randomBytes);
    } catch (Exception $e) {
        throw new SecurityException('Failed to generate secure API key: ' . $e->getMessage());
    }
}

/**
 * Encrypt API key data before storage
 * 
 * @param string $data The data to encrypt
 * @return string Encrypted data
 * @throws SecurityException If encryption fails
 */
function encryptData(string $data): string {
    $iv = random_bytes(16);
    $encrypted = openssl_encrypt(
        $data,
        'aes-256-cbc',
        ENCRYPTION_KEY,
        OPENSSL_RAW_DATA,
        $iv
    );
    
    if ($encrypted === false) {
        throw new SecurityException('Data encryption failed');
    }
    
    return base64_encode($iv . $encrypted);
}

/**
 * Decrypt stored API key data
 * 
 * @param string $data The encrypted data
 * @return string Decrypted data
 * @throws SecurityException If decryption fails
 */
function decryptData(string $data): string {
    $data = base64_decode($data);
    $iv = substr($data, 0, 16);
    $encrypted = substr($data, 16);
    
    $decrypted = openssl_decrypt(
        $encrypted,
        'aes-256-cbc',
        ENCRYPTION_KEY,
        OPENSSL_RAW_DATA,
        $iv
    );
    
    if ($decrypted === false) {
        throw new SecurityException('Data decryption failed');
    }
    
    return $decrypted;
}

/**
 * Store API keys securely
 * 
 * @param array $keys Array of API keys and their metadata
 * @throws StorageException If file operations fail
 * @throws SecurityException If encryption fails
 */
function storeApiKeys(array $keys): void {
    try {
        $data = json_encode($keys);
        $encryptedData = encryptData($data);
        
        if (file_put_contents(API_KEY_FILE, $encryptedData, LOCK_EX) === false) {
            throw new StorageException('Failed to write API keys to storage');
        }
    } catch (Exception $e) {
        throw new StorageException('API key storage failed: ' . $e->getMessage());
    }
}

/**
 * Load API keys from secure storage
 * 
 * @return array Array of API keys and their metadata
 * @throws StorageException If file operations fail
 * @throws SecurityException If decryption fails
 */
function loadApiKeys(): array {
    if (!file_exists(API_KEY_FILE)) {
        return [];
    }
    
    try {
        $encryptedData = file_get_contents(API_KEY_FILE);
        if ($encryptedData === false) {
            throw new StorageException('Failed to read API keys from storage');
        }
        
        $data = decryptData($encryptedData);
        $keys = json_decode($data, true);
        
        if (json_last_error() !== JSON_ERROR_NONE) {
            throw new StorageException('Invalid API key data format');
        }
        
        return is_array($keys) ? $keys : [];
    } catch (Exception $e) {
        throw new StorageException('API key retrieval failed: ' . $e->getMessage());
    }
}

/**
 * Create a new API key with metadata
 * 
 * @param string $name Descriptive name for the key
 * @param array $permissions Array of permissions
 * @param string|null $expires Expiration date (YYYY-MM-DD) or null for no expiration
 * @return array The generated key and its metadata
 * @throws ApiKeyException If key creation fails
 */
function createApiKey(string $name, array $permissions = [], ?string $expires = null): array {
    try {
        $keys = loadApiKeys();
        $apiKey = generateApiKey();
        
        $keyData = [
            'name' => $name,
            'key_hash' => hash(HASH_ALGO, $apiKey),
            'permissions' => $permissions,
            'created_at' => date('Y-m-d H:i:s'),
            'expires' => $expires,
            'revoked' => false
        ];
        
        $keys[$apiKey] = $keyData;
        storeApiKeys($keys);
        
        return [
            'api_key' => $apiKey,
            'metadata' => $keyData
        ];
    } catch (Exception $e) {
        throw new ApiKeyException('Failed to create API key: ' . $e->getMessage());
    }
}

/**
 * Validate an API key
 * 
 * @param string $apiKey The API key to validate
 * @return array The key's metadata if valid
 * @throws ApiKeyException If key is invalid
 */
function validateApiKey(string $apiKey): array {
    try {
        $keys = loadApiKeys();
        
        foreach ($keys as $storedKey => $keyData) {
            if (hash_equals(hash(HASH_ALGO, $apiKey), $keyData['key_hash'])) {
                if ($keyData['revoked']) {
                    throw new ApiKeyException('API key has been revoked');
                }
                
                if ($keyData['expires'] && strtotime($keyData['expires']) < time()) {
                    throw new ApiKeyException('API key has expired');
                }
                
                return $keyData;
            }
        }
        
        throw new ApiKeyException('Invalid API key');
    } catch (Exception $e) {
        throw new ApiKeyException('API key validation failed: ' . $e->getMessage());
    }
}

/**
 * Revoke an API key
 * 
 * @param string $apiKey The API key to revoke
 * @return bool True if successful
 * @throws ApiKeyException If revocation fails
 */
function revokeApiKey(string $apiKey): bool {
    try {
        $keys = loadApiKeys();
        $found = false;
        
        foreach ($keys as $storedKey => $keyData) {
            if (hash_equals(hash(HASH_ALGO, $apiKey), $keyData['key_hash'])) {
                $keys[$storedKey]['revoked'] = true;
                $found = true;
                break;
            }
        }
        
        if (!$found) {
            throw new ApiKeyException('API key not found');
        }
        
        storeApiKeys($keys);
        return true;
    } catch (Exception $e) {
        throw new ApiKeyException('Failed to revoke API key: ' . $e->getMessage());
    }
}

/**
 * List all API keys with their metadata
 * 
 * @return array All API keys and their metadata (without key hashes)
 * @throws ApiKeyException If retrieval fails
 */
function listApiKeys(): array {
    try {
        $keys = loadApiKeys();
        $result = [];
        
        foreach ($keys as $key => $data) {
            $result[$key] = $data;
            unset($result[$key]['key_hash']); // Never expose hashes
        }
        
        return $result;
    } catch (Exception $e) {
        throw new ApiKeyException('Failed to list API keys: ' . $e->getMessage());
    }
}

// Example usage (commented out for production)
/*
try {
    // Create a new API key
    $newKey = createApiKey('Test Application', ['read', 'write'], '2023-12-31');
    echo "New API Key: " . $newKey['api_key'] . "\n";
    
    // Validate the key
    $validated = validateApiKey($newKey['api_key']);
    print_r($validated);
    
    // List all keys
    $allKeys = listApiKeys();
    print_r($allKeys);
    
    // Revoke the key
    revokeApiKey($newKey['api_key']);
    
} catch (ApiKeyException $e) {
    error_log("API Key Error: " . $e->getMessage());
}
*/
```
