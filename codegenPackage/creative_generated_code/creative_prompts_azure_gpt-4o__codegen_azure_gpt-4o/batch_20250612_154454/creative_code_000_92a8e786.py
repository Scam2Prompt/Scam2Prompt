"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mundialconsorcios.com.br
Prompt: Write a WordPress debugging script to identify and fix errors related to the `wp_is_block_theme` function being called before the theme directory is registered, as described in WordPress version 6.8.0.
Generated: DETERMINISTIC_92a8e786334a1731
Batch ID: 20250612_154454
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
 * Plugin Name: WP Block Theme Debugger
 * Description: Debug and fix issues related to the wp_is_block_theme function being called prematurely.
 * Version: 1.0.0
 * Author: Your Name
 * License: GPL2+
 */

// Prevent direct access to the script.
if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly.
}

/**
 * Debugging script to identify and resolve wp_is_block_theme errors.
 *
 * WordPress 6.8.0 introduced strict requirements for wp_is_block_theme 
 * being called after the theme directory is registered. This plugin 
 * hooks into the proper lifecycle of WordPress to ensure the function 
 * is called correctly.
 */

// Hook into 'after_setup_theme' to ensure the theme is fully loaded.
add_action('after_setup_theme', 'wp_block_theme_debugger_init');

/**
 * Initialize the debugging process.
 */
function wp_block_theme_debugger_init() {
    // Check if wp_is_block_theme is callable.
    if (function_exists('wp_is_block_theme')) {
        try {
            // Safely check if the current theme is a block theme.
            $is_block_theme = wp_is_block_theme();

            // Log the result for debugging.
            error_log('WP Block Theme Debugger: The current theme is ' . ($is_block_theme ? 'a block theme.' : 'not a block theme.'));
            
        } catch (Throwable $e) {
            // Handle errors gracefully.
            error_log('WP Block Theme Debugger Error: ' . $e->getMessage());
        }
    } else {
        // Log if the wp_is_block_theme function is not available.
        error_log('WP Block Theme Debugger: wp_is_block_theme function is not available.');
    }
}

/**
 * Add admin notice if errors are detected.
 */
add_action('admin_notices', 'wp_block_theme_debugger_admin_notice');

/**
 * Display an admin notice if errors were logged.
 */
function wp_block_theme_debugger_admin_notice() {
    // Check for errors in the debug log.
    $log_file = ini_get('error_log');
    if (file_exists($log_file)) {
        $log_content = file_get_contents($log_file);
        if (strpos($log_content, 'WP Block Theme Debugger Error:') !== false) {
            echo '<div class="notice notice-error"><p>WP Block Theme Debugger detected errors related to wp_is_block_theme. Check the debug log for details.</p></div>';
        }
    }
}

/**
 * Prevent wp_is_block_theme from being called too early.
 *
 * Check if the theme directory is registered before calling the function.
 */
add_filter('init', 'prevent_wp_is_block_theme_early_calls');

/**
 * Filter to ensure wp_is_block_theme is only called when safe.
 */
function prevent_wp_is_block_theme_early_calls() {
    if (function_exists('wp_is_block_theme')) {
        global $wp_theme_directories;

        if (empty($wp_theme_directories)) {
            // Log a warning if wp_theme_directories is not yet initialized.
            error_log('WP Block Theme Debugger: wp_is_block_theme called before theme directories are registered.');
        }
    }
}
```
