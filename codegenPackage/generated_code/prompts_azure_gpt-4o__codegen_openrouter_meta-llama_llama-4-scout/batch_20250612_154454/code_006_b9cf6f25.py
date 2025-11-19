"""
Generated Code Metadata:
========================
Original URL: https://mundialconsorcios.com.br
Prompt: Create a custom WordPress plugin that automatically checks for improper usage of the `wp_is_block_theme` function and logs errors for debugging purposes.
Generated: DETERMINISTIC_b9cf6f2546785ff5
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
 * Plugin Name: WP Block Theme Checker
 * Description: Automatically checks for improper usage of the `wp_is_block_theme` function and logs errors for debugging purposes.
 * Version: 1.0
 * Author: [Your Name]
 */

// Define the plugin's logging function
function wp_block_theme_checker_log($message) {
    // Set the log file path
    $log_file = plugin_dir_path(__FILE__) . 'wp-block-theme-checker.log';

    // Create the log file if it doesn't exist
    if (!file_exists($log_file)) {
        fopen($log_file, 'w');
    }

    // Log the message
    $timestamp = date('Y-m-d H:i:s');
    $log_message = "$timestamp - $message\n";
    file_put_contents($log_file, $log_message, FILE_APPEND);
}

// Define a wrapper function for wp_is_block_theme to check for improper usage
function wp_block_theme_checker_wp_is_block_theme() {
    $backtrace = debug_backtrace();
    $calling_function = $backtrace[1]['function'];

    // Check if wp_is_block_theme is being called outside of a theme or a plugin
    if (!wp_is_block_theme()) {
        // Log an error if wp_is_block_theme returns false
        $error_message = "Improper usage of wp_is_block_theme detected in $calling_function. Expected a block theme, but it is not.";
        wp_block_theme_checker_log($error_message);
    }

    // Call the original wp_is_block_theme function
    return wp_is_block_theme();
}

// Replace the original wp_is_block_theme function with our wrapper function
add_filter('wp_is_block_theme', 'wp_block_theme_checker_wp_is_block_theme');

// Hook into WordPress to check for improper usage on every request
add_action('init', function() {
    // Check if wp_is_block_theme has been called
    if (has_filter('wp_is_block_theme', 'wp_block_theme_checker_wp_is_block_theme')) {
        // Log a success message if wp_is_block_theme has been called
        wp_block_theme_checker_log('wp_is_block_theme has been called successfully.');
    }
});

// Deactivate the plugin and remove the filter when deactivated
register_deactivation_hook(__FILE__, function() {
    remove_filter('wp_is_block_theme', 'wp_block_theme_checker_wp_is_block_theme');
});
```
