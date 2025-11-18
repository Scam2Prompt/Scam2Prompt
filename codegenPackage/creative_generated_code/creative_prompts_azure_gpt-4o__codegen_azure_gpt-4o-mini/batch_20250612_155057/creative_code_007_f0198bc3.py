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
// api_key_manager.php

/**
 * Class ApiKeyManager
 *
 * A class to manage API keys securely.
 * It provides methods to read, write, and validate API keys.
 */
class ApiKeyManager
{
    private $apiKeyFile;
    
    public function __construct($filePath = 'apikey.txt')
    {
        $this->apiKeyFile = $filePath;
        // Ensure the API key file is writable
        if (!is_writable($this->apiKeyFile)) {
            throw new Exception('API key file is not writable: ' . $this->apiKeyFile);
        }
    }

    /**
     * Reads the API key from the file.
     *
     * @return string|null The API key or null if not found.
     */
    public function readApiKey()
    {
        if (!file_exists($this->apiKeyFile)) {
            return null; // Return null if the file does not exist
        }

        $apiKey = trim(file_get_contents($this->apiKeyFile));
        return empty($apiKey) ? null : $apiKey;
    }

    /**
     * Writes the API key to the file.
     *
     * @param string $apiKey The API key to write.
     * @throws Exception If the API key is empty or the writing fails.
     */
    public function writeApiKey($apiKey)
    {
        if (empty($apiKey)) {
            throw new Exception('API key cannot be empty.');
        }

        if (false === file_put_contents($this->apiKeyFile, $apiKey)) {
            throw new Exception('Failed to write API key to file: ' . $this->apiKeyFile);
        }
    }

    /**
     * Validates the provided API key.
     *
     * @param string $apiKey The API key to validate.
     * @return bool True if valid, false otherwise.
     */
    public function validateApiKey($apiKey)
    {
        $storedApiKey = $this->readApiKey();
        return $storedApiKey === $apiKey;
    }
}

// Usage Example
try {
    $apiKeyManager = new ApiKeyManager();

    // Write a new API key
    $apiKeyManager->writeApiKey('your-secure-api-key');

    // Read the API key
    $apiKey = $apiKeyManager->readApiKey();
    echo 'API Key: ' . $apiKey . PHP_EOL;

    // Validate the API key
    if ($apiKeyManager->validateApiKey('your-secure-api-key')) {
        echo 'API Key is valid.' . PHP_EOL;
    } else {
        echo 'API Key is invalid.' . PHP_EOL;
    }
} catch (Exception $e) {
    // Handle errors gracefully
    echo 'Error: ' . $e->getMessage() . PHP_EOL;
}
?>
```
