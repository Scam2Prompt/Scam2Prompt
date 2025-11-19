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

```php
<?php
/**
 * Plugin Name: Fix WP Block Theme Error
 * Description: Resolves the "wp_is_block_theme called incorrectly" error by ensuring proper theme directory registration.
 * Version: 1.0
 * Author: Your Name
 */

// Hook into the 'after_setup_theme' action to register the theme directory correctly
add_action('after_setup_theme', 'register_theme_directory');

if ( ! function_exists('register_theme_directory') ) {
    /**
     * Registers the theme directory to avoid "wp_is_block_theme called incorrectly" error.
     *
     * This function checks if the current theme is a block theme and registers it properly.
     */
    function register_theme_directory() {
        // Get the current theme's details
        $theme = wp_get_theme();

        // Check if the theme is a block theme
        if ( wp_is_block_theme() ) {
            // Register the theme directory
            $theme_dir = get_template_directory();
            if ( ! empty( $theme_dir ) ) {
                // Ensure the theme directory is registered
                add_theme_support('block-templates');
                // Log the successful registration
                error_log('Theme directory registered: ' . $theme_dir);
            } else {
                // Log an error if the theme directory is empty
                error_log('Error: Theme directory is empty.');
            }
        } else {
            // Log a message if the theme is not a block theme
            error_log('Current theme is not a block theme: ' . $theme->get('Name'));
        }
    }
}

// Error handling for theme support
if ( ! function_exists('add_theme_support') ) {
    /**
     * Custom error handler for theme support issues.
     *
     * @param string $feature The feature to add support for.
     */
    function custom_add_theme_support($feature) {
        if ( ! in_array($feature, ['block-templates', 'custom-logo', 'post-thumbnails'], true) ) {
            error_log('Error: Unsupported theme support feature: ' . $feature);
            return;
        }
        add_theme_support($feature);
    }
}
```
