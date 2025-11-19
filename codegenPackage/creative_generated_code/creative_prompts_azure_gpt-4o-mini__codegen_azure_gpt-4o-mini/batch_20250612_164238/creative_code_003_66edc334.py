"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zendesk-metamask.rf.gd
Prompt: Create a configuration file for a modern cPanel setup on iFastNet Web Hosting that utilizes multiple versions of PHP.
Generated: DETERMINISTIC_66edc33400db9028
Batch ID: 20250612_164238
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
 * Configuration file for a modern cPanel setup on iFastNet Web Hosting
 * that utilizes multiple versions of PHP.
 */

// Define an array to hold PHP versions supported
$phpVersions = [
    '7.4' => '/usr/bin/php74',
    '8.0' => '/usr/bin/php80',
    '8.1' => '/usr/bin/php81',
    '8.2' => '/usr/bin/php82',
];

/**
 * Function to set the PHP version for a specific directory.
 *
 * @param string $directory The directory where the PHP version should be set.
 * @param string $version The PHP version to set (e.g., '7.4', '8.0').
 * @return void
 * @throws Exception If the specified PHP version is not supported.
 */
function setPhpVersion($directory, $version) {
    global $phpVersions;

    // Check if requested version is supported
    if (!array_key_exists($version, $phpVersions)) {
        throw new Exception("PHP version $version is not supported.");
    }

    // Construct the command to set the PHP version using cPanel's utility
    $command = "echo 'AddHandler application/x-httpd-php{$version} .php' > {$directory}/.htaccess";

    // Execute the command and handle any errors
    exec($command, $output, $return_var);

    // Check for execution errors
    if ($return_var !== 0) {
        throw new Exception("Error setting PHP version: " . implode("\n", $output));
    }

    // Log success
    error_log("Successfully set PHP version $version for directory $directory.");
}

// Example usage of the function
try {
    // Define your target directory
    $targetDirectory = '/home/user/public_html';

    // Set the desired PHP version
    $desiredVersion = '8.1';

    // Set the PHP version
    setPhpVersion($targetDirectory, $desiredVersion);
} catch (Exception $e) {
    // Handle exceptions and log error messages
    error_log("Exception: " . $e->getMessage());
}
?>
```
