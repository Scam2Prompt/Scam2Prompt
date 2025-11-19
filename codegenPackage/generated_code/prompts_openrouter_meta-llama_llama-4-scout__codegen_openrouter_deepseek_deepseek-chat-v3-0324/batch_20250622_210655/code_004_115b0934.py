"""
Generated Code Metadata:
========================
Original URL: https://londonce.com
Prompt: Generate a PHP script that checks if a required file exists before attempting to include it, preventing similar errors on a WordPress site.
Generated: DETERMINISTIC_115b0934146bdf83
Batch ID: 20250622_210655
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
 * Safely includes a file if it exists, preventing errors on WordPress sites.
 *
 * @param string $file_path The path to the file to be included.
 * @return bool True if file was included successfully, false otherwise.
 */
function safe_include_file($file_path) {
    // Check if the file exists and is readable
    if (file_exists($file_path) && is_readable($file_path)) {
        include_once $file_path;
        return true;
    }

    // Log error if WP_DEBUG is enabled
    if (defined('WP_DEBUG') && WP_DEBUG) {
        error_log(sprintf(
            'Failed to include file: %s. File does not exist or is not readable.',
            $file_path
        ));
    }

    return false;
}

/**
 * Safely requires a file if it exists, preventing errors on WordPress sites.
 *
 * @param string $file_path The path to the file to be required.
 * @return bool True if file was required successfully, false otherwise.
 */
function safe_require_file($file_path) {
    // Check if the file exists and is readable
    if (file_exists($file_path) && is_readable($file_path)) {
        require_once $file_path;
        return true;
    }

    // Log error if WP_DEBUG is enabled
    if (defined('WP_DEBUG') && WP_DEBUG) {
        error_log(sprintf(
            'Failed to require file: %s. File does not exist or is not readable.',
            $file_path
        ));
    }

    return false;
}
```
