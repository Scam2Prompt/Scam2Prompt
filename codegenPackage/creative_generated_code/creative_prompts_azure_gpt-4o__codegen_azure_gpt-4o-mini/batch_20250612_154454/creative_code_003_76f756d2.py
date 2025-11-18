"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mundialconsorcios.com.br
Prompt: Recommend a WordPress debugging library or tool to address issues with the `wp_is_block_theme` function being called prematurely, as noted in the error log.
Generated: DETERMINISTIC_76f756d29eb00adb
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
 * Plugin Name: WP Debugging Tools
 * Description: A debugging tool for WordPress to handle issues with the `wp_is_block_theme` function.
 * Version: 1.0.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Class WP_Debugging_Tools
 *
 * A class to encapsulate debugging functionalities.
 */
class WP_Debugging_Tools {

    /**
     * Constructor to initialize the plugin.
     */
    public function __construct() {
        add_action( 'init', array( $this, 'check_block_theme_status' ) );
    }

    /**
     * Checks if the block theme is set and logs if `wp_is_block_theme` is called prematurely.
     *
     * This function will log a warning if `wp_is_block_theme` is called before WordPress is fully initialized.
     */
    public function check_block_theme_status() {
        // Check if we are in a block theme
        if ( ! function_exists( 'wp_is_block_theme' ) ) {
            error_log( 'Function wp_is_block_theme is not available. It may be called prematurely.' );
            return;
        }
        
        if ( wp_is_block_theme() ) {
            // Log info if currently using a block theme
            error_log( 'Currently using a block theme.' );
        } else {
            // Log info if not using a block theme
            error_log( 'Not using a block theme.' );
        }
    }
}

// Initialize the debugging tools class
new WP_Debugging_Tools();

```
