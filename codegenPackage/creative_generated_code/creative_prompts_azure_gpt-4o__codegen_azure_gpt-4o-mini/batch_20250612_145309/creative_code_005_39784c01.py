"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://post-customsgovua.infinityfreeapp.com
Prompt: Provide a step-by-step guide to configure multiple PHP versions on iFastNet hosting using cPanel.
Generated: DETERMINISTIC_39784c0104ff1847
Batch ID: 20250612_145309
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
 * Step-by-step guide to configure multiple PHP versions on iFastNet hosting using cPanel
 */

/**
 * Function to check and display current PHP version.
 */
function checkCurrentPhpVersion() {
    // Display the current PHP version
    echo 'Current PHP Version: ' . phpversion() . PHP_EOL;
}

/**
 * Function to change PHP version for a specific directory.
 *
 * @param string $directory The target directory where the PHP version needs to be changed.
 * @param string $phpVersion The desired PHP version (e.g., '7.4', '8.0').
 * @return void
 */
function changePhpVersion($directory, $phpVersion) {
    // Validate the PHP version
    $validVersions = ['5.6', '7.0', '7.1', '7.2', '7.3', '7.4', '8.0', '8.1', '8.2'];
    
    if (!in_array($phpVersion, $validVersions)) {
        throw new InvalidArgumentException('Invalid PHP version specified: ' . $phpVersion);
    }
    
    // Path to the .htaccess file
    $htaccessPath = $directory . '/.htaccess';

    // Change PHP version using .htaccess
    $htaccessContent = "AddHandler application/x-httpd-" . $phpVersion . " .php\n";
    
    // Check if .htaccess file exists
    if (file_exists($htaccessPath)) {
        // Append the PHP version handler
        file_put_contents($htaccessPath, $htaccessContent, FILE_APPEND);
    } else {
        // Create a new .htaccess file with the PHP version handler
        file_put_contents($htaccessPath, $htaccessContent);
    }

    echo 'PHP version changed to ' . $phpVersion . ' for directory: ' . $directory . PHP_EOL;
}

// Usage example
try {
    // Check the current PHP version
    checkCurrentPhpVersion();

    // Set the desired PHP version and target directory
    $desiredVersion = '7.4'; // Change this to the required version
    $targetDirectory = '/home/user/public_html'; // Change to your target directory

    // Change the PHP version
    changePhpVersion($targetDirectory, $desiredVersion);
} catch (Exception $e) {
    // Handle any exceptions that arise during the process
    echo 'Error: ' . $e->getMessage() . PHP_EOL;
}
```
