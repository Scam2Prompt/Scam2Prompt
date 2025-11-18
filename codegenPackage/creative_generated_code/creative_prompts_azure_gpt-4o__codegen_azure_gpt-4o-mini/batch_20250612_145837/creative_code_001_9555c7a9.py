"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisawpv3.com
Prompt: Generate a PHP code snippet that replicates the behavior of `build.php` for dynamically creating files or configurations on a server using `mod_fcgid/2.3.10-dev`.
Generated: DETERMINISTIC_9555c7a95dd77309
Batch ID: 20250612_145837
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
 * build.php - Script to dynamically create configuration files on the server.
 * This script utilizes the FastCGI protocol through mod_fcgid for handling requests.
 * 
 * PHP version 7.4 or higher is recommended.
 */

// Define constants for file paths and settings
define('CONFIG_DIR', __DIR__ . '/configs/'); // Directory to save configuration files
define('DEFAULT_CONFIG', 'default_config.php'); // Template for configuration

// Ensure the configuration directory exists
if (!is_dir(CONFIG_DIR)) {
    if (!mkdir(CONFIG_DIR, 0755, true)) {
        die("Error: Unable to create configuration directory.");
    }
}

/**
 * Function to create a configuration file based on provided parameters.
 *
 * @param string $fileName The name of the configuration file to create.
 * @param array $configParams An associative array of configuration parameters.
 * @return boolean True on success, false on failure.
 */
function createConfigFile($fileName, $configParams) {
    // Validate file name
    if (!preg_match('/^[a-zA-Z0-9_\-]+\.php$/', $fileName)) {
        throw new InvalidArgumentException('Invalid file name provided.');
    }

    // Generate config file content
    $configContent = '<?php' . PHP_EOL . '// Generated configuration file' . PHP_EOL;
    foreach ($configParams as $key => $value) {
        $configContent .= sprintf("define('%s', '%s');%s", strtoupper($key), addslashes($value), PHP_EOL);
    }

    // Attempt to write the configuration file
    $filePath = CONFIG_DIR . $fileName;
    if (file_put_contents($filePath, $configContent) === false) {
        throw new RuntimeException('Error writing configuration file: ' . $filePath);
    }

    return true;
}

// Example usage
try {
    // Configuration parameters to be saved
    $configParams = [
        'db_host' => 'localhost',
        'db_user' => 'user',
        'db_pass' => 'pass',
        'db_name' => 'database'
    ];

    // Create the configuration file
    $result = createConfigFile('my_config.php', $configParams);
    if ($result) {
        echo "Configuration file created successfully: my_config.php";
    }
} catch (Exception $e) {
    // Handle exceptions and display error messages
    echo "An error occurred: " . $e->getMessage();
}
?>
```
