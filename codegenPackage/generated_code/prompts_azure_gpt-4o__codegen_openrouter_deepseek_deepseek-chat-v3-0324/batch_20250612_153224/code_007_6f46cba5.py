"""
Generated Code Metadata:
========================
Original URL: https://londonce.com
Prompt: Provide a step-by-step guide for configuring PHP error reporting to debug issues like missing `wp-blog-header.php` in a WordPress project.
Generated: DETERMINISTIC_6f46cba51734e59c
Batch ID: 20250612_153224
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
 * Configures PHP error reporting for debugging WordPress issues.
 * 
 * This script helps debug common WordPress errors like missing wp-blog-header.php
 * by enabling comprehensive error reporting and logging.
 */

// Step 1: Enable all error reporting during development
error_reporting(E_ALL);
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);

// Step 2: Set up error logging to a file
ini_set('log_errors', 1);
ini_set('error_log', dirname(__FILE__) . '/php-errors.log');

// Step 3: Define WordPress debug constants in wp-config.php
// Add these lines to your wp-config.php file (usually above the "That's all, stop editing!" line)
define('WP_DEBUG', true);
define('WP_DEBUG_LOG', true);
define('WP_DEBUG_DISPLAY', true);
define('SCRIPT_DEBUG', true);

// Step 4: Handle fatal errors with a custom handler
register_shutdown_function(function() {
    $error = error_get_last();
    if ($error !== null && in_array($error['type'], [E_ERROR, E_PARSE, E_CORE_ERROR, E_COMPILE_ERROR])) {
        error_log("Fatal error: {$error['message']} in {$error['file']} on line {$error['line']}");
        if (defined('WP_DEBUG_DISPLAY') && WP_DEBUG_DISPLAY) {
            echo "<pre>Fatal error: {$error['message']} in {$error['file']} on line {$error['line']}</pre>";
        }
    }
});

// Step 5: Check for missing wp-blog-header.php (example usage)
if (!file_exists(dirname(__FILE__) . '/wp-blog-header.php')) {
    trigger_error('wp-blog-header.php is missing from the root directory', E_USER_ERROR);
}
```
