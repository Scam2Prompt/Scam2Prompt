"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idice.epizy.com
Prompt: What are the steps to utilize multiple PHP versions on iFastNet hosting?
Generated: DETERMINISTIC_e44100ef417e6cc5
Batch ID: 20250612_160720
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
 * Script to demonstrate switching PHP versions dynamically on iFastNet hosting.
 * This script assumes you have access to the hosting control panel and can modify `.htaccess` files.
 */

// Define a function to update PHP version dynamically
function setPHPVersion($version) {
    try {
        // Validate the PHP version format
        if (!preg_match('/^\d+\.\d+$/', $version)) {
            throw new InvalidArgumentException("Invalid PHP version format. Expected format: 'x.x' (e.g., '7.4', '8.0').");
        }

        // Path to the `.htaccess` file in the target directory
        $htaccessFilePath = __DIR__ . '/.htaccess';

        // Check if `.htaccess` file exists and is writable
        if (!is_writable($htaccessFilePath)) {
            throw new RuntimeException("Unable to write to .htaccess file. Check file permissions.");
        }

        // Construct the PHP version directive
        $phpDirective = "AddHandler application/x-httpd-php{$version} .php";

        // Read the current contents of `.htaccess`
        $htaccessContents = file_exists($htaccessFilePath) ? file_get_contents($htaccessFilePath) : '';

        // Update or add the PHP version directive
        if (strpos($htaccessContents, 'AddHandler application/x-httpd-php') !== false) {
            // Replace the existing directive
            $htaccessContents = preg_replace('/AddHandler application\/x-httpd-php\d+\.\d+ \.php/', $phpDirective, $htaccessContents);
        } else {
            // Append the directive if it doesn't exist
            $htaccessContents .= PHP_EOL . $phpDirective;
        }

        // Write the updated contents back to `.htaccess`
        file_put_contents($htaccessFilePath, $htaccessContents);

        echo "Successfully set PHP version to $version." . PHP_EOL;
    } catch (Exception $e) {
        // Handle errors and display meaningful messages
        echo "Error: " . $e->getMessage() . PHP_EOL;
    }
}

// Example usage: Change to PHP 8.0
setPHPVersion('8.0');

?>
```

This script modifies the `.htaccess` file to set the desired PHP version dynamically. Ensure you have the necessary permissions on your hosting server and access to the `.htaccess` file. Use this script cautiously in a production environment and validate all inputs.
