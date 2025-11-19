"""
Generated Code Metadata:
========================
Original URL: https://mundialconsorcios.com.br
Prompt: Create a custom WordPress plugin that automatically checks for improper usage of the `wp_is_block_theme` function and logs errors for debugging purposes.
Generated: DETERMINISTIC_b9cf6f2546785ff5
Batch ID: 20250612_154454
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.gnu.org/licenses/gpl-2.0.txt": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Plugin Name: Block Theme Function Checker
 * Description: Checks for improper usage of wp_is_block_theme function and logs errors.
 * Version: 1.0.0
 * Author: Your Name
 * License: GPL-2.0+
 * License URI: http://www.gnu.org/licenses/gpl-2.0.txt
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class Block_Theme_Function_Checker {

    /**
     * Initialize the plugin
     */
    public function __construct() {
        add_action('init', array($this, 'init_hooks'));
    }

    /**
     * Initialize hooks
     */
    public function init_hooks() {
        // Check if wp_is_block_theme exists (introduced in WordPress 5.9)
        if (!function_exists('wp_is_block_theme')) {
            $this->log_error('wp_is_block_theme function does not exist. Requires WordPress 5.9+');
            return;
        }

        // Hook into shutdown to check for improper usage
        add_action('shutdown', array($this, 'check_block_theme_usage'));
    }

    /**
     * Check for improper usage of wp_is_block_theme
     */
    public function check_block_theme_usage() {
        // Get all called functions during execution
        $called_functions = $this->get_called_functions();

        // Check if wp_is_block_theme was called
        if (in_array('wp_is_block_theme', $called_functions)) {
            // Check if called before 'after_setup_theme' hook
            if (did_action('after_setup_theme') === 0) {
                $this->log_error('wp_is_block_theme called before after_setup_theme hook. Theme may not be loaded yet.');
            }

            // Check if called in admin area when it shouldn't be
            if (is_admin() && !wp_doing_ajax()) {
                $backtrace = debug_backtrace(DEBUG_BACKTRACE_IGNORE_ARGS, 5);
                $this->log_error('wp_is_block_theme called in admin area. Backtrace: ' . wp_json_encode($backtrace));
            }
        }
    }

    /**
     * Get all called functions during execution
     * 
     * @return array List of called functions
     */
    private function get_called_functions() {
        $called_functions = array();
        $backtrace = debug_backtrace(DEBUG_BACKTRACE_IGNORE_ARGS);

        foreach ($backtrace as $trace) {
            if (isset($trace['function'])) {
                $called_functions[] = $trace['function'];
            }
        }

        return array_unique($called_functions);
    }

    /**
     * Log error to debug.log
     * 
     * @param string $message Error message to log
     */
    private function log_error($message) {
        if (defined('WP_DEBUG') && WP_DEBUG) {
            error_log('[Block Theme Checker] ' . $message);
        }
    }
}

// Initialize the plugin
new Block_Theme_Function_Checker();
```
