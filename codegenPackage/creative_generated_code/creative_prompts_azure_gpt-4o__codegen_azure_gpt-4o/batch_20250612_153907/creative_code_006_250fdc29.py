"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consejodigitalmx.com
Prompt: Provide an example of how to use PHP to restrict access to files like `wp-config2.php` and `wp-links-opml.php` by modifying `.htaccess` rules.
Generated: DETERMINISTIC_250fdc298798deb8
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Generate .htaccess rules to restrict access to sensitive files

// Define the list of sensitive files to restrict access to
$sensitive_files = [
    'wp-config2.php',
    'wp-links-opml.php'
];

// Start building the .htaccess rules
$htaccess_content = <<<HTACCESS
# BEGIN Restrict Sensitive Files
<FilesMatch "^(wp-config2\.php|wp-links-opml\.php)$">
    Require all denied
</FilesMatch>
# END Restrict Sensitive Files

HTACCESS;

try {
    // Path to the .htaccess file (assuming it is in the root directory)
    $htaccess_path = __DIR__ . '/.htaccess';

    // Check if the .htaccess file is writable
    if (!is_writable($htaccess_path) && file_exists($htaccess_path)) {
        throw new RuntimeException("The .htaccess file is not writable.");
    }

    // Append the rules to the .htaccess file or create it if it doesn't exist
    file_put_contents($htaccess_path, $htaccess_content, FILE_APPEND | LOCK_EX);

    // Success message
    echo "Access restriction rules successfully added to .htaccess.";
} catch (Exception $e) {
    // Handle errors gracefully
    error_log("Error occurred while modifying .htaccess: " . $e->getMessage());
    echo "Failed to update .htaccess. Please check the error log for more details.";
}
```
