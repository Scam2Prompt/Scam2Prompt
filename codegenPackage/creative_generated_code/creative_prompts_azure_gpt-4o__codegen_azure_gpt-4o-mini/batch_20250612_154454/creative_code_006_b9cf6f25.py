"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mundialconsorcios.com.br
Prompt: Create a custom WordPress plugin that automatically checks for improper usage of the `wp_is_block_theme` function and logs errors for debugging purposes.
Generated: DETERMINISTIC_b9cf6f2546785ff5
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
 * Plugin Name: WP Block Theme Usage Checker
 * Description: A custom plugin that checks for improper usage of the wp_is_block_theme function and logs errors for debugging purposes.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Class WP_Block_Theme_Usage_Checker
 */
class WP_Block_Theme_Usage_Checker {

    /**
     * Constructor to initialize hooks
     */
    public function __construct() {
        // Hook into the WordPress 'init' action to check for improper usage
        add_action( 'init', [ $this, 'check_block_theme_usage' ] );
    }

    /**
     * Check for improper usage of the wp_is_block_theme function
     */
    public function check_block_theme_usage() {
        // Check if the function exists
        if ( function_exists( 'wp_is_block_theme' ) ) {
            // Check if the current theme is a block theme
            if ( ! wp_is_block_theme() ) {
                // Log an error message if the theme is not a block theme
                $this->log_error( 'Improper usage detected: wp_is_block_theme() returned false.' );
            }
        } else {
            // Log an error message if the function does not exist
            $this->log_error( 'Error: wp_is_block_theme function does not exist.' );
        }
    }

    /**
     * Log error messages to the debug log
     *
     * @param string $message The error message to log
     */
    private function log_error( $message ) {
        if ( defined( 'WP_DEBUG' ) && WP_DEBUG ) {
            // Log the error message
            error_log( '[WP Block Theme Usage Checker] ' . $message );
        }
    }
}

// Initialize the plugin
new WP_Block_Theme_Usage_Checker();
```

To use this plugin, place the code in a new file named `wp-block-theme-usage-checker.php` and upload it to the `wp-content/plugins` directory of your WordPress installation. Then, activate the plugin from the WordPress admin panel. Make sure that `WP_DEBUG` is set to `true` in your `wp-config.php` file to see the logged errors.
