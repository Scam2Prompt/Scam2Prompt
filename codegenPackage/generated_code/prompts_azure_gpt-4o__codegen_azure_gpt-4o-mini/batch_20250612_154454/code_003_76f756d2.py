"""
Generated Code Metadata:
========================
Original URL: https://mundialconsorcios.com.br
Prompt: Recommend a WordPress debugging library or tool to address issues with the `wp_is_block_theme` function being called prematurely, as noted in the error log.
Generated: DETERMINISTIC_76f756d29eb00adb
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
 * Plugin Name: WP Debugging Helper
 * Description: A simple debugging tool for WordPress to help identify issues with the wp_is_block_theme function.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Class WP_Debugging_Helper
 * A class to encapsulate debugging functionalities for WordPress.
 */
class WP_Debugging_Helper {

    /**
     * Constructor to initialize the debugging tool.
     */
    public function __construct() {
        // Hook into the 'init' action to check for block theme issues
        add_action( 'init', array( $this, 'check_block_theme' ) );
    }

    /**
     * Check if the wp_is_block_theme function is called prematurely.
     */
    public function check_block_theme() {
        // Check if the function exists before calling it
        if ( function_exists( 'wp_is_block_theme' ) ) {
            // Check if the function is being called prematurely
            if ( ! wp_is_block_theme() ) {
                // Log a warning message
                error_log( 'Warning: wp_is_block_theme() called prematurely. Please ensure it is called after the theme setup.' );
            }
        } else {
            // Log an error if the function does not exist
            error_log( 'Error: wp_is_block_theme() function does not exist. Please check your WordPress version.' );
        }
    }
}

// Initialize the debugging helper
new WP_Debugging_Helper();
```
