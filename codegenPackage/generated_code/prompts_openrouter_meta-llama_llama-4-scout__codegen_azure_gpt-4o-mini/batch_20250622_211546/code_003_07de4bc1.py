"""
Generated Code Metadata:
========================
Original URL: https://btc5000.epizy.com
Prompt: Generate a PHP code snippet that demonstrates how to configure and use multiple versions of PHP on iFastNet Web Hosting.
Generated: DETERMINISTIC_07de4bc149f556f8
Batch ID: 20250622_211546
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
 * PHP Version Switcher for iFastNet Web Hosting
 * 
 * This script demonstrates how to configure and use multiple versions of PHP
 * on iFastNet Web Hosting. It checks the current PHP version and allows
 * switching to a specified version if available.
 */

// Define the available PHP versions
$available_php_versions = [
    '7.2',
    '7.3',
    '7.4',
    '8.0',
    '8.1',
    '8.2'
];

// Function to get the current PHP version
function getCurrentPhpVersion() {
    return phpversion();
}

// Function to switch PHP version
function switchPhpVersion($version) {
    global $available_php_versions;

    // Check if the requested version is available
    if (in_array($version, $available_php_versions)) {
        // Set the PHP version (this is a placeholder for actual implementation)
        // In a real scenario, you would typically modify a .htaccess file or use
        // a hosting control panel API to change the PHP version.
        // Example: file_put_contents('.htaccess', "AddHandler application/x-httpd-php{$version} .php");

        // For demonstration, we will just return a success message
        return "Successfully switched to PHP version {$version}.";
    } else {
        // Handle the error if the version is not available
        throw new Exception("Error: PHP version {$version} is not available.");
    }
}

// Main execution
try {
    // Display the current PHP version
    $current_version = getCurrentPhpVersion();
    echo "Current PHP Version: {$current_version}\n";

    // Specify the desired PHP version (this could come from user input)
    $desired_version = '8.0'; // Change this to the desired version

    // Attempt to switch to the desired PHP version
    $result = switchPhpVersion($desired_version);
    echo $result . "\n";

} catch (Exception $e) {
    // Handle any exceptions that occur during the version switch
    echo $e->getMessage() . "\n";
}
?>
```
