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
 * WordPress Debugging Script
 * This script identifies and fixes issues related to the wp_is_block_theme function
 * being called before the theme directory is registered, as described in WordPress version 6.8.0.
 * 
 * To use this script, place it in the root of your WordPress installation and run it.
 * Always back up your site before making changes.
 */

// Ensure this script runs only within a WordPress environment
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Check if the theme directory is registered.
 *
 * @return bool True if the theme directory is registered, false otherwise.
 */
function is_theme_directory_registered() {
    // Check if the theme is registered by verifying if the theme's data is available
    return isset( $GLOBALS['wp_themes'] ) && ! empty( $GLOBALS['wp_themes'] );
}

/**
 * Custom handler for wp_is_block_theme() to ensure it is called after theme registration.
 *
 * @return bool True if the current theme is a block theme, false otherwise.
 */
function safe_wp_is_block_theme() {
    if ( ! is_theme_directory_registered() ) {
        // Log a warning if the theme directory is not registered
        error_log( 'Warning: wp_is_block_theme() called before theme directory registration.' );
        return false; // Default to false if theme directory is not registered
    }

    // Proceed to call the original wp_is_block_theme function
    return wp_is_block_theme();
}

// Hook the safe_wp_is_block_theme to the appropriate action
add_action( 'after_setup_theme', function() {
    // Override the original function to use safe_wp_is_block_theme
    if ( ! function_exists( 'wp_is_block_theme' ) ) {
        function wp_is_block_theme() {
            return safe_wp_is_block_theme();
        }
    }
}, 1 ); // Ensure this runs early in the theme setup

/**
 * Debugging output for administrators to monitor theme status.
 */
function debug_theme_status() {
    if ( is_admin() ) {
        if ( ! is_theme_directory_registered() ) {
            echo '<div class="notice notice-warning">
                <p>Warning: The theme directory is not registered yet. wp_is_block_theme() may not function correctly.</p>
            </div>';
        } else {
            echo '<div class="notice notice-success">
                <p>The theme directory is properly registered. wp_is_block_theme() should work as expected.</p>
            </div>';
        }
    }
}

// Hook to display theme status on admin dashboard
add_action( 'admin_notices', 'debug_theme_status' );

?>
```
