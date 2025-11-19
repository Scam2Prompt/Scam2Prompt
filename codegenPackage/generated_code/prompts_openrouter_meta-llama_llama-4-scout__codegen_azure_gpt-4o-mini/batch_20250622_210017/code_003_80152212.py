"""
Generated Code Metadata:
========================
Original URL: https://walletverified.rf.gd
Prompt: Generate a PHP code snippet to configure multiple versions of PHP on iFastNet Web Hosting, and explain how to switch between different PHP versions.
Generated: DETERMINISTIC_801522129ec6ed23
Batch ID: 20250622_210017
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
 * PHP Version Configuration Script for iFastNet Web Hosting
 * 
 * This script allows you to configure and switch between multiple PHP versions
 * on iFastNet Web Hosting. It checks the available PHP versions and sets the
 * desired version for the current directory.
 */

// Define the path to the .htaccess file
$htaccessFile = __DIR__ . '/.htaccess';

// List of available PHP versions
$availablePhpVersions = [
    '7.4',
    '8.0',
    '8.1',
    '8.2',
];

// Desired PHP version to switch to (can be modified as needed)
$desiredPhpVersion = '8.1';

// Function to switch PHP version
function switchPhpVersion($version, $htaccessFile) {
    global $availablePhpVersions;

    // Check if the desired version is available
    if (!in_array($version, $availablePhpVersions)) {
        throw new Exception("PHP version $version is not available.");
    }

    // Create or overwrite the .htaccess file with the new PHP version
    $htaccessContent = "<?php\n";
    $htaccessContent .= "AddHandler application/x-httpd-php{$version} .php\n";

    // Attempt to write to the .htaccess file
    if (file_put_contents($htaccessFile, $htaccessContent) === false) {
        throw new Exception("Failed to write to .htaccess file.");
    }

    echo "Successfully switched to PHP version $version.\n";
}

try {
    // Switch to the desired PHP version
    switchPhpVersion($desiredPhpVersion, $htaccessFile);
} catch (Exception $e) {
    // Handle any exceptions that occur during the process
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
