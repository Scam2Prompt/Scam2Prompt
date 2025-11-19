"""
Generated Code Metadata:
========================
Original URL: https://mundialconsorcios.com.br
Prompt: Provide a solution to suppress repetitive error messages in WordPress logs, such as those related to the `wp_is_block_theme` function in the `functions.php` file.
Generated: DETERMINISTIC_2fcc71755fd11fd7
Batch ID: 20250612_154454
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
 * Plugin Name: Error Log Suppressor
 * Description: Suppresses repetitive error messages in WordPress logs.
 * Version: 1.0
 * Author: Your Name
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Suppresses specific error messages from being logged.
 *
 * @param bool   $log Whether to log the error.
 * @param string $error_message The error message.
 * @param string $error_type The error type.
 * @return bool Modified log status.
 */
function suppress_repetitive_errors($log, $error_message, $error_type) {
    // List of error messages to suppress
    $suppressed_messages = array(
        'wp_is_block_theme',
        // Add other error messages to suppress here
    );

    foreach ($suppressed_messages as $message) {
        if (strpos($error_message, $message) !== false) {
            return false;
        }
    }

    return $log;
}

// Hook into the error logging system
add_filter('log_error_custom', 'suppress_repetitive_errors', 10, 3);

/**
 * Handles deprecated function errors for wp_is_block_theme.
 */
function handle_deprecated_block_theme_errors() {
    if (!function_exists('wp_is_block_theme')) {
        // Define the function if it doesn't exist to prevent errors
        function wp_is_block_theme() {
            return false;
        }
    }
}

add_action('after_setup_theme', 'handle_deprecated_block_theme_errors');
```
