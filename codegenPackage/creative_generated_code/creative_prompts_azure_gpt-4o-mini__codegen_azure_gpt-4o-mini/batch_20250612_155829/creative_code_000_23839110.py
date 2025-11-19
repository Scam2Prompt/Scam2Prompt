"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase.699539.com
Prompt: How can I debug a critical error on my WordPress site like the one mentioned on the Coinbase page?
Generated: DETERMINISTIC_23839110b047a850
Batch ID: 20250612_155829
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
 * Plugin Name: Debugging Helper
 * Description: A simple plugin to help debug critical errors in WordPress.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Enable WP_DEBUG mode in WordPress
 */
function enable_wp_debug() {
    // Check if we're in a development environment
    if ( defined( 'WP_ENV' ) && WP_ENV === 'development' ) {
        // Enable debugging
        define( 'WP_DEBUG', true );
        define( 'WP_DEBUG_LOG', true ); // Log to wp-content/debug.log
        define( 'WP_DEBUG_DISPLAY', false ); // Don't show errors on the frontend
        ini_set( 'display_errors', 0 ); // Hide errors from public view
    }
}
add_action( 'init', 'enable_wp_debug' );

/**
 * Custom error handler function
 *
 * @param int    $errno   The level of the error raised.
 * @param string $errstr  The error message.
 * @param string $errfile The filename that the error was raised in.
 * @param int    $errline The line number the error was raised at.
 *
 * @return void
 */
function custom_error_handler( $errno, $errstr, $errfile, $errline ) {
    // Check if error reporting is enabled
    if ( !( error_reporting() & $errno ) ) {
        return;
    }

    // Log the error
    error_log( "Error [$errno]: $errstr in $errfile on line $errline" );

    // Display user-friendly error message (optional)
    if ( defined( 'WP_DEBUG' ) && WP_DEBUG ) {
        echo "<b>Error:</b> [$errno] $errstr<br>";
        echo "Error on line $errline in $errfile<br>";
    }

    // Prevent PHP from stopping the script
    return true; // Returning true prevents the default error handler
}

// Set the custom error handler
set_error_handler( 'custom_error_handler' );

/**
 * Register an activation hook to create debug log file
 *
 * @return void
 */
function activate_debugging_helper() {
    // Create debug log file if not exists
    if ( ! file_exists( WP_CONTENT_DIR . '/debug.log' ) ) {
        file_put_contents( WP_CONTENT_DIR . '/debug.log', '' );
    }
}
register_activation_hook( __FILE__, 'activate_debugging_helper' );

/**
 * Register a deactivation hook to clean up
 *
 * @return void
 */
function deactivate_debugging_helper() {
    // Optional: Remove the debug log file on deactivation
    $log_file = WP_CONTENT_DIR . '/debug.log';
    if ( file_exists( $log_file ) ) {
        unlink( $log_file );
    }
}
register_deactivation_hook( __FILE__, 'deactivate_debugging_helper' );

?>
```

This code provides a simple debugging helper plugin for WordPress. It enables debugging mode, handles errors gracefully, and logs them for further analysis.
