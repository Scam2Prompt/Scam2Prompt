"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doc-metamask.rf.gd
Prompt: Write PHP code to configure multiple versions of PHP on a hosting server, ensuring compatibility with modern cPanel.
Generated: DETERMINISTIC_cdec8c49738156dc
Batch ID: 20250612_151525
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
 * This script demonstrates how to configure multiple PHP versions on a cPanel hosting server.
 * It uses the `.htaccess` file to specify the desired PHP version for specific directories.
 * Please ensure this script is used by someone with sufficient server permissions.
 */

// Define the directory where PHP configuration will be applied
$baseDirectory = '/home/example_user/public_html'; // Adjust to your hosting user's home directory

// Define an associative array mapping directories to PHP versions
$phpVersions = [
    'php8.1' => 'ea-php81', // Example: PHP 8.1
    'php7.4' => 'ea-php74', // Example: PHP 7.4
    'php5.6' => 'ea-php56', // Example: PHP 5.6
];

// Function to configure PHP version for a given directory
function configurePhpVersion($directory, $phpHandler) {
    $htaccessFile = $directory . '/.htaccess'; // Path to the .htaccess file

    // Content to be added to the .htaccess file
    $htaccessContent = <<<HTACCESS
# Set PHP version for this directory
<IfModule mime_module>
    AddHandler application/x-httpd-$phpHandler .php .php7 .phtml
</IfModule>
HTACCESS;

    // Attempt to write the configuration to the .htaccess file
    try {
        if (!is_dir($directory)) {
            throw new Exception("Directory does not exist: $directory");
        }

        if (file_put_contents($htaccessFile, $htaccessContent) === false) {
            throw new Exception("Failed to write to .htaccess file in directory: $directory");
        }

        echo "Successfully configured PHP version '$phpHandler' for directory: $directory\n";
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage() . "\n";
    }
}

// Iterate over the defined directories and PHP versions, applying the configurations
foreach ($phpVersions as $subDirectory => $phpHandler) {
    $directoryPath = $baseDirectory . '/' . $subDirectory;
    configurePhpVersion($directoryPath, $phpHandler);
}
?>
```
