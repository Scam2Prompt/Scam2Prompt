"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamasks-rewards.epizy.com
Prompt: How can I configure multiple PHP versions in my iFastNet Web Hosting account?
Generated: DETERMINISTIC_0ccacf3e11bf4a6b
Batch ID: 20250612_160823
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
 * Script to configure multiple PHP versions on an iFastNet Web Hosting account.
 *
 * This script assumes that the user has access to the control panel
 * and can execute PHP configuration changes via the `.htaccess` file.
 */

// Define the path to the .htaccess file
$htaccessFilePath = __DIR__ . '/.htaccess';

// Array of PHP versions to configure
$phpVersions = [
    '5.6' => 'AddHandler application/x-httpd-php56 .php',
    '7.0' => 'AddHandler application/x-httpd-php70 .php',
    '7.1' => 'AddHandler application/x-httpd-php71 .php',
    '7.2' => 'AddHandler application/x-httpd-php72 .php',
    '7.3' => 'AddHandler application/x-httpd-php73 .php',
    '7.4' => 'AddHandler application/x-httpd-php74 .php',
    '8.0' => 'AddHandler application/x-httpd-php80 .php',
    '8.1' => 'AddHandler application/x-httpd-php81 .php',
];

// Function to write PHP version handlers to .htaccess
function configurePhpVersions($filePath, $versions)
{
    try {
        // Check if the .htaccess file is writable
        if (!is_writable($filePath)) {
            throw new Exception("The file '$filePath' is not writable. Please check permissions.");
        }

        // Open the .htaccess file for writing
        $fileHandler = fopen($filePath, 'a'); // Open in append mode
        if (!$fileHandler) {
            throw new Exception("Failed to open '$filePath' for writing.");
        }

        // Write each PHP version handler to the file
        foreach ($versions as $version => $handler) {
            fwrite($fileHandler, "$handler\n");
        }

        // Close the file handler
        fclose($fileHandler);
        echo "PHP versions configured successfully in '$filePath'.\n";

    } catch (Exception $e) {
        // Handle exceptions and display error message
        echo "Error: " . $e->getMessage() . "\n";
    }
}

// Execute the configuration function
configurePhpVersions($htaccessFilePath, $phpVersions);
?>
```

Make sure to run this script in a safe environment and ensure that the necessary permissions are set for the `.htaccess` file.
