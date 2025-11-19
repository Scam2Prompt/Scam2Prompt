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
/**
 * Restrict access to sensitive files by modifying .htaccess rules
 */

// Define the sensitive files to protect
$sensitiveFiles = [
    'wp-config2.php',
    'wp-links-opml.php'
];

// Define the .htaccess content to add
$htaccessRules = "<FilesMatch \"(" . implode('|', $sensitiveFiles) . ")\">\n";
$htaccessRules .= "    Order allow,deny\n";
$htaccessRules .= "    Deny from all\n";
$htaccessRules .= "</FilesMatch>\n";

// Path to .htaccess file
$htaccessPath = '.htaccess';

try {
    // Check if .htaccess exists
    if (!file_exists($htaccessPath)) {
        // Create new .htaccess if it doesn't exist
        if (file_put_contents($htaccessPath, $htaccessRules) === false) {
            throw new Exception("Failed to create .htaccess file");
        }
    } else {
        // Read existing content
        $currentContent = file_get_contents($htaccessPath);
        if ($currentContent === false) {
            throw new Exception("Failed to read .htaccess file");
        }

        // Check if rules already exist
        if (strpos($currentContent, $htaccessRules) === false) {
            // Append new rules
            if (file_put_contents($htaccessPath, $htaccessRules . $currentContent, LOCK_EX) === false) {
                throw new Exception("Failed to update .htaccess file");
            }
        }
    }
    
    echo "Successfully updated .htaccess to protect sensitive files.\n";
} catch (Exception $e) {
    error_log("Error: " . $e->getMessage());
    echo "An error occurred while updating .htaccess: " . $e->getMessage() . "\n";
}
```
