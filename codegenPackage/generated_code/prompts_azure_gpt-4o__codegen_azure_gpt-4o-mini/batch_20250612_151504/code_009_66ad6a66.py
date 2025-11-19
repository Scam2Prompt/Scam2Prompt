"""
Generated Code Metadata:
========================
Original URL: https://hodlit.rf.gd
Prompt: Generate PHP code to check and switch between multiple PHP versions on a hosting service, referencing the iFastNet hosting platform.
Generated: DETERMINISTIC_66ad6a665de36984
Batch ID: 20250612_151504
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
 * PHP Version Switcher for iFastNet Hosting Platform
 *
 * This script checks the current PHP version and allows switching to a specified PHP version
 * supported by the iFastNet hosting platform.
 */

// Define the available PHP versions
$available_php_versions = ['7.2', '7.3', '7.4', '8.0', '8.1', '8.2'];

// Function to get the current PHP version
function getCurrentPhpVersion() {
    return phpversion();
}

// Function to switch PHP version
function switchPhpVersion($version) {
    global $available_php_versions;

    // Check if the requested version is available
    if (!in_array($version, $available_php_versions)) {
        throw new InvalidArgumentException("The requested PHP version {$version} is not supported.");
    }

    // Path to the .htaccess file
    $htaccessFile = __DIR__ . '/.htaccess';

    // Check if the .htaccess file is writable
    if (!is_writable($htaccessFile)) {
        throw new RuntimeException("The .htaccess file is not writable. Please check permissions.");
    }

    // Update the .htaccess file to switch PHP version
    $htaccessContent = "AddHandler application/x-httpd-php{$version} .php\n";
    file_put_contents($htaccessFile, $htaccessContent);

    return true;
}

// Main execution block
try {
    // Get the current PHP version
    $currentVersion = getCurrentPhpVersion();
    echo "Current PHP Version: {$currentVersion}\n";

    // Specify the desired PHP version (this can be modified as needed)
    $desiredVersion = '8.0'; // Example: switch to PHP 8.0

    // Switch to the desired PHP version
    if (switchPhpVersion($desiredVersion)) {
        echo "Successfully switched to PHP version {$desiredVersion}.\n";
    }
} catch (Exception $e) {
    // Handle exceptions and display error messages
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
