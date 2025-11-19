"""
Generated Code Metadata:
========================
Original URL: https://mundialconsorcios.com.br
Prompt: Write a WordPress debugging script to identify and fix errors related to the `wp_is_block_theme` function being called before the theme directory is registered, as described in WordPress version 6.8.0.
Generated: DETERMINISTIC_92a8e786334a1731
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
 * WordPress Debugging Script for wp_is_block_theme() Function
 * 
 * This script helps identify and fix issues where wp_is_block_theme() is called
 * before the theme directory is registered in WordPress 6.8.0.
 * 
 * @package WordPress
 * @version 6.8.0
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Debug class for wp_is_block_theme() related issues
 */
class WP_Block_Theme_Debugger {

    /**
     * Initialize the debugger
     */
    public static function init() {
        add_action('after_setup_theme', [__CLASS__, 'check_theme_initialization'], 0);
        add_action('init', [__CLASS__, 'check_early_calls'], 0);
    }

    /**
     * Check if theme is properly initialized
     */
    public static function check_theme_initialization() {
        if (!function_exists('wp_is_block_theme')) {
            self::log_error('wp_is_block_theme() function does not exist. WordPress version might be too old.');
            return;
        }

        if (!did_action('setup_theme')) {
            self::log_error('Theme not initialized yet. wp_is_block_theme() called too early.');
        }
    }

    /**
     * Check for early calls to wp_is_block_theme()
     */
    public static function check_early_calls() {
        global $wp_actions;

        if (!isset($wp_actions['after_setup_theme'])) {
            self::log_error('wp_is_block_theme() might be called before theme initialization.');
        }
    }

    /**
     * Log errors to debug.log
     * 
     * @param string $message Error message to log
     */
    private static function log_error($message) {
        if (defined('WP_DEBUG') && WP_DEBUG) {
            if (defined('WP_DEBUG_LOG') && WP_DEBUG_LOG) {
                error_log('[WP Block Theme Debugger] ' . $message);
            }
        }
    }

    /**
     * Fix potential issues by ensuring proper load order
     */
    public static function fix_load_order() {
        if (!did_action('after_setup_theme')) {
            add_action('after_setup_theme', function() {
                // Re-check theme status after proper initialization
                if (function_exists('wp_is_block_theme')) {
                    wp_is_block_theme();
                }
            }, 999);
        }
    }
}

// Initialize the debugger
WP_Block_Theme_Debugger::init();

// Attempt to fix load order issues
WP_Block_Theme_Debugger::fix_load_order();

/**
 * Helper function to safely check if current theme is a block theme
 * 
 * @return bool|null Returns true/false if block theme, null if check fails
 */
function safe_wp_is_block_theme() {
    if (!function_exists('wp_is_block_theme')) {
        return null;
    }

    if (!did_action('after_setup_theme')) {
        error_log('Warning: wp_is_block_theme() called before theme initialization');
        return null;
    }

    return wp_is_block_theme();
}
```
