"""
Generated Code Metadata:
========================
Original URL: https://panemicav2.rf.gd
Prompt: Generate a PHP code snippet to configure multiple versions of PHP on iFastNet Web Hosting for a website that requires different PHP versions for different applications.
Generated: DETERMINISTIC_389a0207ee6ad9ed
Batch ID: 20250622_212148
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
 * PHP Version Configuration for iFastNet Web Hosting
 *
 * This script configures multiple PHP versions for different applications
 * hosted on iFastNet. It uses .htaccess files to specify the PHP version
 * for each application directory.
 */

// Define the applications and their corresponding PHP versions
$applications = [
    'app1' => '7.4',
    'app2' => '8.0',
    'app3' => '8.1',
];

// Base directory where applications are hosted
$baseDir = '/path/to/your/webroot/';

// Loop through each application to create or update the .htaccess file
foreach ($applications as $app => $version) {
    // Construct the path to the application's directory
    $appDir = $baseDir . $app;

    // Check if the application directory exists
    if (is_dir($appDir)) {
        // Path to the .htaccess file
        $htaccessFile = $appDir . '/.htaccess';

        // PHP version directive for iFastNet
        $phpVersionDirective = "<?php\n" .
            "  # Use PHP version $version for $app\n" .
            "  AddHandler application/x-httpd-php$version .php\n";

        // Write the directive to the .htaccess file
        try {
            // Open the file for writing
            if (file_put_contents($htaccessFile, $phpVersionDirective) === false) {
                throw new Exception("Failed to write to $htaccessFile");
            }
            echo "Successfully configured PHP $version for $app\n";
        } catch (Exception $e) {
            // Handle any errors that occur during file operations
            echo "Error: " . $e->getMessage() . "\n";
        }
    } else {
        // Handle the case where the application directory does not exist
        echo "Warning: Directory $appDir does not exist. Skipping...\n";
    }
}
?>
```
