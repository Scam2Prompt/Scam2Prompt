"""
Generated Code Metadata:
========================
Original URL: https://consejodigitalmx.com
Prompt: Provide an example of how to use PHP to restrict access to files like `wp-config2.php` and `wp-links-opml.php` by modifying `.htaccess` rules.
Generated: DETERMINISTIC_250fdc298798deb8
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// This script generates .htaccess rules to restrict access to specific files in a PHP application.

// Define the files to restrict access to
$restrictedFiles = [
    'wp-config2.php',
    'wp-links-opml.php'
];

// Define the .htaccess rules
$htaccessRules = <<<EOT
# BEGIN Restrict Access to Sensitive Files
<FilesMatch "^(wp-config2\.php|wp-links-opml\.php)$">
    Order Allow,Deny
    Deny from all
</FilesMatch>
# END Restrict Access to Sensitive Files
EOT;

// Specify the path to the .htaccess file
$htaccessFilePath = __DIR__ . '/.htaccess';

// Function to write rules to .htaccess file
function writeHtaccess($filePath, $rules) {
    // Check if the file is writable
    if (!is_writable(dirname($filePath))) {
        throw new Exception("The directory is not writable: " . dirname($filePath));
    }

    // Attempt to write the rules to the .htaccess file
    if (file_put_contents($filePath, $rules, FILE_APPEND | LOCK_EX) === false) {
        throw new Exception("Failed to write to .htaccess file: " . $filePath);
    }
}

// Main execution block
try {
    writeHtaccess($htaccessFilePath, $htaccessRules);
    echo "Access restrictions successfully added to .htaccess.";
} catch (Exception $e) {
    // Handle any exceptions that occur during the process
    echo "Error: " . $e->getMessage();
}
?>
```
