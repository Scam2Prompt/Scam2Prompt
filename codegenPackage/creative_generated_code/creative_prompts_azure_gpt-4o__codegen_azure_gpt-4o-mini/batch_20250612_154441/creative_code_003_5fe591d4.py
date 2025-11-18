"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-protocol.42web.io
Prompt: Provide PHP code to configure a web application to run on a hosting service that supports multiple PHP versions, as mentioned on the iFastNet hosting page.
Generated: DETERMINISTIC_5fe591d4ed3b30a6
Batch ID: 20250612_154441
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
 * Configuration Script for PHP Web Application
 *
 * This script configures the web application to run on a hosting service
 * that supports multiple PHP versions, specifically iFastNet hosting.
 * It ensures the correct PHP version is set and provides error handling.
 */

// Specify the PHP version to use (Change this to the desired version)
$desiredPhpVersion = '8.0'; // Example: '7.4', '8.0', '8.1'

// Function to check and set the PHP version
function setPhpVersion($version) {
    // Validate the PHP version format
    if (!preg_match('/^\d+\.\d+$/', $version)) {
        throw new InvalidArgumentException("Invalid PHP version format: $version. Expected format is 'X.Y'.");
    }

    // Check if the desired PHP version is supported
    $supportedVersions = ['7.4', '8.0', '8.1']; // Example supported versions
    if (!in_array($version, $supportedVersions)) {
        throw new RuntimeException("The PHP version $version is not supported by iFastNet.");
    }

    // Set the PHP version for the application
    // This might involve creating or editing a `.htaccess` file or using a control panel setting
    // Assuming we are using a .htaccess approach
    $htaccessContent = "AddHandler application/x-httpd-php$version .php\n";
    $htaccessFile = __DIR__ . '/.htaccess';

    // Attempt to write to the .htaccess file
    if (file_put_contents($htaccessFile, $htaccessContent) === false) {
        throw new RuntimeException("Failed to write to .htaccess file. Check permissions.");
    }

    echo "PHP version set to $version successfully.\n";
}

// Main execution block
try {
    setPhpVersion($desiredPhpVersion);
} catch (Exception $e) {
    // Handle any exceptions and provide an error message
    echo "Error: " . $e->getMessage() . "\n";
    exit(1); // Exit with an error code
}
?>
```
