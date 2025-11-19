"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medium.byethost10.com
Prompt: How can I configure multiple versions of PHP on iFastNet Web Hosting? Provide a code example.
Generated: DETERMINISTIC_780335d415ce81f2
Batch ID: 20250612_155233
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
 * This script demonstrates how to configure multiple versions of PHP for a site hosted on iFastNet.
 * The configuration file is .htaccess, which allows users to set the PHP version per directory.
 * 
 * Usage: Place this PHP script in the root directory of your web application to set the desired PHP version.
 */

// Define the desired PHP version
$phpVersion = '7.4'; // Change this to the required version: '7.4', '8.0', or '8.1'

// Validate PHP version
$validVersions = ['7.4', '8.0', '8.1'];
if (!in_array($phpVersion, $validVersions)) {
    die("Error: Invalid PHP version specified. Please use one of the following: " . implode(', ', $validVersions));
}

// Create or update the .htaccess file to set the PHP version
$htaccessFile = '.htaccess';
$htaccessContent = <<<EOD
# Use the specified PHP version for this directory
AddHandler application/x-httpd-php{$phpVersion} .php
EOD;

// Try to write to the .htaccess file
try {
    if (file_put_contents($htaccessFile, $htaccessContent) === false) {
        throw new Exception("Could not write to .htaccess file. Please check permissions.");
    }
    echo "Success: PHP version $phpVersion has been set in the .htaccess file.";
} catch (Exception $e) {
    // Handle any exceptions that occur during the file writing process
    echo "Error: " . $e->getMessage();
}
?>
```

Make sure to execute this script in a safe environment and backup your existing `.htaccess` file before running it.
