"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartd.org.ls
Prompt: Generate a PHP script to secure WordPress directories (`wp-admin`, `wp-includes`) from unauthorized access, referencing the structure shown at https://smartd.org.ls.
Generated: DETERMINISTIC_992380cb4bfb8c15
Batch ID: 20250612_151853
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
 * Secure WordPress directories from unauthorized access
 * 
 * This script generates .htaccess rules to protect `wp-admin` and `wp-includes` directories.
 * Place this script in your WordPress root folder and run it.
 * After execution, a .htaccess file will be created/updated with the necessary rules.
 */

// Define constants for directories to secure
define('HTACCESS_FILE', '.htaccess');
define('WP_ADMIN', 'wp-admin');
define('WP_INCLUDES', 'wp-includes');

try {
    // Check if .htaccess file exists or create one
    if (!file_exists(HTACCESS_FILE)) {
        $htaccess = fopen(HTACCESS_FILE, 'w');
        if (!$htaccess) {
            throw new Exception("Failed to create .htaccess file.");
        }
        fclose($htaccess);
    }

    // Open .htaccess file for writing
    $htaccess = fopen(HTACCESS_FILE, 'a');
    if (!$htaccess) {
        throw new Exception("Failed to open .htaccess file for writing.");
    }

    // Rules for securing `wp-admin`
    $wpAdminRules = "
# Protect wp-admin directory
<Directory " . WP_ADMIN . ">
    Require all granted
    # Restrict access to authorized users only (Optional: Update IPs as needed)
    <RequireAll>
        Require ip 127.0.0.1
         ...
";
}

?>
