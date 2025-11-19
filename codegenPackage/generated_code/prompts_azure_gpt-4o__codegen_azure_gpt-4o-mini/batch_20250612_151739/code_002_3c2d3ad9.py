"""
Generated Code Metadata:
========================
Original URL: https://medium.byethost10.com
Prompt: Create a PHP script that utilizes multiple versions of PHP on a hosting service with unlimited bandwidth and free domain name registration, like iFastNet.
Generated: DETERMINISTIC_3c2d3ad971fe3f7f
Batch ID: 20250612_151739
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
 * PHP Version Switcher
 * This script demonstrates how to utilize multiple PHP versions on a hosting service.
 * It checks the current PHP version and allows the user to switch to a different version.
 * 
 * Note: This script assumes that the hosting service supports version switching via .htaccess
 * or similar configuration.
 */

// Define the available PHP versions
$available_php_versions = ['7.4', '8.0', '8.1', '8.2'];

// Get the current PHP version
$current_php_version = phpversion();

// Check if a version switch is requested
if (isset($_GET['php_version']) && in_array($_GET['php_version'], $available_php_versions)) {
    $requested_version = $_GET['php_version'];
    
    // Attempt to switch PHP version
    switch_php_version($requested_version);
} else {
    echo "Current PHP version: " . $current_php_version . "<br>";
    echo "Available PHP versions: " . implode(", ", $available_php_versions) . "<br>";
    echo "To switch PHP version, use the following URL format: ?php_version=X.X";
}

/**
 * Switch PHP version by modifying the .htaccess file
 *
 * @param string $version The PHP version to switch to
 * @return void
 */
function switch_php_version($version) {
    // Path to the .htaccess file
    $htaccess_file = __DIR__ . '/.htaccess';

    // Check if the .htaccess file is writable
    if (!is_writable($htaccess_file)) {
        echo "Error: .htaccess file is not writable.";
        return;
    }

    // Create the content to switch PHP version
    $php_switch_content = "AddHandler application/x-httpd-php" . str_replace('.', '', $version) . " .php\n";

    // Write the new PHP version switch to the .htaccess file
    try {
        file_put_contents($htaccess_file, $php_switch_content);
        echo "Successfully switched to PHP version: " . $version;
    } catch (Exception $e) {
        echo "Error switching PHP version: " . $e->getMessage();
    }
}
?>
```

**Note:** This script assumes that the hosting environment allows PHP version switching via the `.htaccess` file. Ensure that you have the necessary permissions to modify this file.
