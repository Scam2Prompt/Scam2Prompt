"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magnumrockets.com
Prompt: Recommend a library for creating custom patterns in WordPress based on the features discussed on magnumrockets.com.
Generated: DETERMINISTIC_1b6aa735c992558e
Batch ID: 20250612_161500
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
 * Plugin Name: Custom Patterns for WordPress
 * Description: A plugin to create custom block patterns in WordPress.
 * Version: 1.0
 * Author: Expert Programmer
 * License: GPL-2.0+
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

// Check for WordPress version compatibility.
if (version_compare(get_bloginfo('version'), '5.5', '<')) {
    wp_die(__('This plugin requires WordPress 5.5 or higher.', 'custom-patterns'));
}

/**
 * Register custom block patterns.
 */
function custom_patterns_register_patterns() {
    // Define the block pattern categories.
    register_block_pattern_category(
        'custom-category',
        array('label' => __('Custom Patterns', 'custom-patterns'))
    );

    // Define a custom block pattern.
    register_block_pattern(
        'custom-patterns/example-pattern',
        array(
            'title'       => __('Example Pattern', 'custom-patterns'),
            'categories'  => array('custom-category'),
            'content'     => '<!-- wp:heading {"level":2} --><h2>Custom Heading</h2><!-- /wp:heading -->'
                . '<!-- wp:paragraph --><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p><!-- /wp:paragraph -->',
        )
    );
}

/**
 * Hook the function into WordPress.
 */
add_action('init', 'custom_patterns_register_patterns');

/**
 * Plugin activation handler.
 */
function custom_patterns_activate() {
    // Ensure the plugin only activates on WordPress 5.5+.
    if (version_compare(get_bloginfo('version'), '5.5', '<')) {
        deactivate_plugins(plugin_basename(__FILE__));
        wp_die(__('This plugin requires WordPress 5.5 or higher.', 'custom-patterns'));
    }
}

register_activation_hook(__FILE__, 'custom_patterns_activate');

/**
 * Plugin deactivation handler.
 */
function custom_patterns_deactivate() {
    // Perform cleanup tasks if necessary.
}

register_deactivation_hook(__FILE__, 'custom_patterns_deactivate');

/**
 * Plugin uninstall handler.
 */
function custom_patterns_uninstall() {
    // Perform cleanup tasks if necessary.
}

register_uninstall_hook(__FILE__, 'custom_patterns_uninstall');

```
