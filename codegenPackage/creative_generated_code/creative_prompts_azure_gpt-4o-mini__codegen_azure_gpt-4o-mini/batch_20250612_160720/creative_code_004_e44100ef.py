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
 * Script to switch PHP versions in iFastNet hosting environment via .htaccess
 * This script assumes you have access to modify the .htaccess file
 */

// Define the path to the .htaccess file
$htaccessFile = __DIR__ . '/.htaccess';

// Function to switch PHP version
function switchPhpVersion($version) {
    global $htaccessFile;

    // Validate the PHP version input
    $validVersions = ['5.6', '7.0', '7.1', '7.2', '7.3', '7.4', '8.0', '8.1', '8.2'];
    
    if (!in_array($version, $validVersions)) {
        throw new InvalidArgumentException("Invalid PHP version specified. Valid options are: " . implode(', ', $validVersions));
    }

    // Generate the PHP handler directive
    $phpHandler = "AddHandler application/x-httpd-php{$version} .php";

    // Attempt to write to the .htaccess file
    try {
        // Check if the .htaccess file exists and is writable
        if (!is_writable($htaccessFile)) {
            throw new RuntimeException('.htaccess file is not writable. Please check permissions.');
        }

        // Read the current contents of the .htaccess file
        $currentContents = file_get_contents($htaccessFile);
        
        // Check if PHP version handler already exists
        if (strpos($currentContents, 'AddHandler application/x-httpd-php') !== false) {
            // Replace existing PHP handler with the new version
            $updatedContents = preg_replace('/AddHandler application\/x-httpd-php[0-9.]+\.php/', $phpHandler, $currentContents);
        } else {
            // Append the new PHP handler to the .htaccess file
            $updatedContents = $currentContents . "\n" . $phpHandler;
        }

        // Write updated contents back to the .htaccess file
        file_put_contents($htaccessFile, $updatedContents);
        echo "PHP version switched to {$version} successfully in the .htaccess file.";
        
    } catch (Exception $e) {
        // Handle exceptions and display error message
        echo 'Error: ' . $e->getMessage();
    }
}

// Example usage: switch to PHP version 7.4
switchPhpVersion('7.4');
?>
```
