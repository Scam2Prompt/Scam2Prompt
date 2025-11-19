"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suilbwei.rf.gd
Prompt: Write a code snippet to configure multiple PHP versions on an iFastNet hosting account.
Generated: DETERMINISTIC_bf7d089274e09ada
Batch ID: 20250612_161453
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
 * Script to configure multiple PHP versions on an iFastNet hosting account.
 * This script assumes that the hosting account supports multi-PHP configurations.
 * Ensure that your hosting account allows custom .htaccess configurations.
 */

// Define the directory paths and PHP versions you want to set up
$phpConfigurations = [
    '/path/to/app1' => 'php56', // Use PHP 5.6 for app1
    '/path/to/app2' => 'php74', // Use PHP 7.4 for app2
    '/path/to/app3' => 'php80', // Use PHP 8.0 for app3
];

// Loop through each configuration and create/update .htaccess files
foreach ($phpConfigurations as $directory => $phpVersion) {
    $htaccessPath = $directory . '/.htaccess';

    // Prepare .htaccess content for the specified PHP version
    $htaccessContent = <<<HTACCESS
# Set PHP version for the directory
AddHandler application/x-httpd-{$phpVersion} .php
HTACCESS;

    try {
        // Check if the directory exists before writing
        if (!is_dir($directory)) {
            throw new Exception("Directory does not exist: $directory");
        }

        // Write the .htaccess content to the specified path
        if (file_put_contents($htaccessPath, $htaccessContent) === false) {
            throw new Exception("Failed to write .htaccess file at: $htaccessPath");
        }

        echo "Successfully configured PHP version '{$phpVersion}' for directory '{$directory}'.\n";
    } catch (Exception $e) {
        // Error handling
        echo "Error: {$e->getMessage()}\n";
    }
}
?>
```
