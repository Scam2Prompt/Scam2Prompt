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
 * Description: This plugin checks for improper usage of the wp_is_block_theme function and logs errors for debugging purposes.
 * Version: 1.0.0
 * Author: Your Name
 * License: GPL-2.0+
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Class WP_Block_Theme_Usage_Checker
 * Handles the functionality of the plugin.
 */
class WP_Block_Theme_Usage_Checker {

    /**
     * Constructor to initialize hooks.
     */
    public function __construct() {
        add_action('all', [$this, 'check_wp_is_block_theme_usage']); // Hook into all actions/filters
    }

    /**
     * Checks for improper usage of the wp_is_block_theme() function.
     *
     * @return void
     */
    public function check_wp_is_block_theme_usage() {
        // Get the name of the current hook being executed
        $current_hook = current_filter();

        // Check if the hook being executed improperly calls wp_is_block_theme()
        if (has_filter($current_hook, 'wp_is_block_theme') || has_action($current_hook, 'wp_is_block_theme')) {

            // Log the improper usage to the debug.log file
            if (WP_DEBUG && WP_DEBUG_LOG) {
                $error_message = sprintf(
                    'Improper usage detected: wp_is_block_theme() called within hook "%s". This may cause unexpected behavior.',
                    $current_hook
                );
                error_log($error_message);
            }
        }
    }
}

// Initialize the plugin functionality
new WP_Block_Theme_Usage_Checker();
```
