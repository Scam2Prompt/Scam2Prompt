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
 * This script securely manages API keys by reading from a configuration file
 * and providing functions to retrieve and validate API keys.
 * 
 * @package ApiKeyManager
 */

class ApiKeyManager {
    private $apiKeys = [];
    private $configFile = 'apikeys.json';

    /**
     * Constructor to initialize the API key manager.
     * Loads API keys from the configuration file.
     */
    public function __construct() {
        $this->loadApiKeys();
    }

    /**
     * Load API keys from the JSON configuration file.
     * 
     * @throws Exception if the configuration file cannot be read or is invalid.
     */
    private function loadApiKeys() {
        if (!file_exists($this->configFile)) {
            throw new Exception("Configuration file not found: " . $this->configFile);
        }

        $jsonContent = file_get_contents($this->configFile);
        if ($jsonContent === false) {
            throw new Exception("Failed to read configuration file: " . $this->configFile);
        }

        $this->apiKeys = json_decode($jsonContent, true);
        if (json_last_error() !== JSON_ERROR_NONE) {
            throw new Exception("Invalid JSON in configuration file: " . json_last_error_msg());
        }
    }

    /**
     * Validate an API key against the stored keys.
     * 
     * @param string $key The API key to validate.
     * @return bool True if the key is valid, false otherwise.
     */
    public function validateApiKey($key) {
        return in_array($key, $this->apiKeys);
    }

    /**
     * Get all stored API keys.
     * 
     * @return array The list of API keys.
     */
    public function getApiKeys() {
        return $this->apiKeys;
    }
}

// Example usage
try {
    $apiKeyManager = new ApiKeyManager();
    
    // Validate an API key
    $keyToValidate = 'your_api_key_here';
    if ($apiKeyManager->validateApiKey($keyToValidate)) {
        echo "API key is valid.";
    } else {
        echo "Invalid API key.";
    }
} catch (Exception $e) {
    // Handle exceptions gracefully
    error_log($e->getMessage());
    echo "An error occurred while managing API keys.";
}
?>
```

**Note:** Ensure that the `apikeys.json` file exists in the same directory as this script and contains a valid JSON array of API keys, e.g., `["key1", "key2", "key3"]`.
