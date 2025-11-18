"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.v3-bridge.com
Prompt: Create a PHP function to securely handle keys and authentication for the Arbitrum v3 bridge, using the structure implied by "key.php."
Generated: DETERMINISTIC_8b736fe686a6d71d
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
 * KeyManager class handles secure storage and retrieval of keys
 * for authentication in the Arbitrum v3 bridge.
 */
class KeyManager {
    private $keyFile; // Path to the key file

    /**
     * Constructor for KeyManager.
     *
     * @param string $keyFile Path to the file where keys are stored.
     * @throws Exception if the key file is not readable.
     */
    public function __construct($keyFile) {
        $this->keyFile = $keyFile;

        // Check if the key file is readable
        if (!is_readable($this->keyFile)) {
            throw new Exception("Key file is not readable: " . $this->keyFile);
        }
    }

    /**
     * Retrieve the API key from the key file.
     *
     * @return string The API key.
     * @throws Exception if the key cannot be retrieved.
     */
    public function getApiKey() {
        $key = $this->readKeyFromFile();

        if (empty($key)) {
            throw new Exception("API key is empty or not found.");
        }

        return $key;
    }

    /**
     * Function to safely read the key from the key file.
     *
     * @return string The content of the key file.
     */
    private function readKeyFromFile() {
        // Use file_get_contents to read the key
        $key = file_get_contents($this->keyFile);
        
        if ($key === false) {
            throw new Exception("Failed to read key from file: " . $this->keyFile);
        }

        return trim($key); // Trim any whitespace or new lines
    }
}

/**
 * Example usage of KeyManager
 */
try {
    $keyManager = new KeyManager('path/to/key.php');
    $apiKey = $keyManager->getApiKey();
    echo "API Key retrieved successfully: " . $apiKey;
} catch (Exception $e) {
    // Handle exceptions gracefully
    error_log($e->getMessage()); // Log the error message
    echo "An error occurred while retrieving the API key. Please check the logs.";
}
?>
```
