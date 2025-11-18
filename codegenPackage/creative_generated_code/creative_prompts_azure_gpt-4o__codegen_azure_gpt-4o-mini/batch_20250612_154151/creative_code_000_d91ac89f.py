"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon-farming.pro
Prompt: Write a PHP script that generates a file similar to `key.php` for secure API key storage and retrieval, using best practices for server-side security.
Generated: DETERMINISTIC_d91ac89f8c123fef
Batch ID: 20250612_154151
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
 * 
 * This script demonstrates how to securely store and retrieve an API key 
 * from a configuration file. It follows best practices for server-side 
 * security, including using environment variables and proper error handling.
 */

// Define the path to the configuration file
define('CONFIG_FILE', __DIR__ . '/config.php');

/**
 * Function to create a configuration file for API key storage
 *
 * @param string $apiKey The API key to store
 * @return void
 * @throws Exception If the file cannot be created or written to
 */
function createApiKeyFile($apiKey) {
    // Validate the API key (basic validation, enhance as needed)
    if (empty($apiKey) || !is_string($apiKey)) {
        throw new InvalidArgumentException('Invalid API key provided.');
    }

    // Prepare the content for the config file
    $content = "<?php\n\n";
    $content .= "// This file is auto-generated. Do not edit directly.\n";
    $content .= "define('API_KEY', '{$apiKey}');\n";
    
    // Attempt to write to the configuration file
    if (file_put_contents(CONFIG_FILE, $content) === false) {
        throw new Exception('Failed to write to the configuration file.');
    }

    // Set file permissions to restrict access
    if (!chmod(CONFIG_FILE, 0600)) {
        throw new Exception('Failed to set permissions on the configuration file.');
    }
}

/**
 * Function to retrieve the API key
 *
 * @return string|null The API key, or null if not set
 * @throws Exception If the config file is unreadable
 */
function getApiKey() {
    // Check if the configuration file exists
    if (!file_exists(CONFIG_FILE) || !is_readable(CONFIG_FILE)) {
        throw new Exception('Configuration file is not readable or does not exist.');
    }

    // Include the configuration file to access the API key
    include(CONFIG_FILE);
    
    // Validate that the API key is defined
    if (!defined('API_KEY')) {
        throw new Exception('API_KEY is not defined in the configuration file.');
    }

    return API_KEY;
}

// Usage example
try {
    // Uncomment the line below to create the config file for the first time
    // createApiKeyFile('your-secure-api-key-here');

    // Retrieve the API key
    $apiKey = getApiKey();
    echo 'API Key retrieved successfully: ' . htmlspecialchars($apiKey);
} catch (Exception $e) {
    // Handle errors gracefully
    echo 'Error: ' . $e->getMessage();
}
?>
```
