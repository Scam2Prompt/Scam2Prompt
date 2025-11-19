"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-protocol.42web.io
Prompt: How can I configure multiple PHP versions on iFastNet's web hosting platform?
Generated: DETERMINISTIC_38ac6401554c1b18
Batch ID: 20250612_164110
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
 * iFastNet PHP Version Configuration Script
 * 
 * This script allows you to switch between multiple PHP versions on an iFastNet hosting platform.
 * 
 * Usage:
 * 1. Set the desired PHP version in the $desiredPhpVersion variable.
 * 2. Run the script to apply the changes.
 */

// Define the path to the `php.ini` file
$phpIniPath = '/path/to/your/php.ini';

// Desired PHP version (e.g., '7.4', '8.0', '8.1')
$desiredPhpVersion = '8.0'; // Change this to the PHP version you want to use

// List of supported PHP versions
$supportedPhpVersions = ['7.4', '8.0', '8.1'];

// Function to check if the desired PHP version is supported
function isValidPhpVersion($version, $supportedVersions) {
    return in_array($version, $supportedVersions);
}

// Function to configure PHP version
function configurePhpVersion($phpVersion, $phpIniPath) {
    // Check if the php.ini file is writable
    if (!is_writable($phpIniPath)) {
        throw new Exception("The php.ini file is not writable: $phpIniPath");
    }

    // Write the PHP version configuration
    $phpConfig = "extension=php_$phpVersion.dll\n";
    
    // Attempt to write the configuration to the php.ini file
    if (file_put_contents($phpIniPath, $phpConfig) === false) {
        throw new Exception("Failed to write to php.ini file: $phpIniPath");
    }

    return true;
}

// Main execution block
try {
    // Validate the desired PHP version
    if (!isValidPhpVersion($desiredPhpVersion, $supportedPhpVersions)) {
        throw new InvalidArgumentException("Invalid PHP version specified: $desiredPhpVersion. Supported versions: " . implode(', ', $supportedPhpVersions));
    }

    // Configure the desired PHP version
    configurePhpVersion($desiredPhpVersion, $phpIniPath);

    echo "Successfully configured PHP version to $desiredPhpVersion.\n";
} catch (Exception $e) {
    // Handle any exceptions and output the error message
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
