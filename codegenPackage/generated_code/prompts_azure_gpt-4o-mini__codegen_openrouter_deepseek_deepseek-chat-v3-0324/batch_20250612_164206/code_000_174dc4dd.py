"""
Generated Code Metadata:
========================
Original URL: https://mundialconsorcios.com.br
Prompt: How can I resolve the "wp_is_block_theme called incorrectly" error in WordPress, specifically regarding theme directory registration?
Generated: DETERMINISTIC_174dc4dd31cbca34
Batch ID: 20250612_164206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready solution to properly register a theme directory and handle the `wp_is_block_theme` error in WordPress:

```php
<?php
/**
 * Properly register theme directory and handle wp_is_block_theme error
 * 
 * This code should be placed in your theme's functions.php file
 */

// Ensure WordPress environment is loaded
if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Register theme directory and setup block theme support
 */
function setup_theme_block_support() {
    // Register theme directory if needed (compatibility with some hosts)
    register_theme_directory(get_theme_root());
    
    // Handle wp_is_block_theme error by properly declaring theme support
    if (!function_exists('wp_is_block_theme')) {
        // Fallback for older WordPress versions
        return false;
    }

    // Properly declare block theme support
    add_theme_support('block-templates');
    add_theme_support('block-template-parts');
    
    // Enable other common block theme supports
    add_theme_support('wp-block-styles');
    add_theme_support('align-wide');
}
add_action('after_setup_theme', 'setup_theme_block_support', 10);

/**
 * Error handler for incorrect wp_is_block_theme calls
 */
function handle_block_theme_errors() {
    // Check if we're in admin to avoid front-end warnings
    if (!is_admin()) {
        return;
    }

    // Ensure the function exists before calling it
    if (function_exists('wp_is_block_theme')) {
        $is_block_theme = wp_is_block_theme();
        // Additional block theme checks can be added here
    }
}
add_action('admin_init', 'handle_block_theme_errors');
```
