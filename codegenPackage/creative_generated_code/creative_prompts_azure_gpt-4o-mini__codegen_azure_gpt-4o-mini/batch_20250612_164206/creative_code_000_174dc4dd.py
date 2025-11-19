"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mundialconsorcios.com.br
Prompt: How can I resolve the "wp_is_block_theme called incorrectly" error in WordPress, specifically regarding theme directory registration?
Generated: DETERMINISTIC_174dc4dd31cbca34
Batch ID: 20250612_164206
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
 * Plugin Name: Fix WP Is Block Theme Error
 * Description: Resolves the "wp_is_block_theme called incorrectly" error in WordPress by ensuring proper theme directory registration.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Function to ensure theme directory registration is handled correctly.
 */
function fix_block_theme_error() {
    // Check if the current theme supports block templates
    if ( ! function_exists( 'wp_is_block_theme' ) ) {
        return; // Exit if the function does not exist
    }

    // Get the theme information
    $theme = wp_get_theme();

    // Ensure the theme is registered and is a block theme
    if ( ! $theme->is_block_theme() ) {
        // If not a block theme, register the block theme support
        add_theme_support( 'block-templates' );
    }

    /**
     * Optionally, you might want to log an error message if 
     * 'wp_is_block_theme' was called incorrectly.
     */
    if ( ! $theme->supports( 'block-templates' ) ) {
        error_log( sprintf( 'Theme %s does not support block templates.', $theme->get( 'Name' ) ) );
    }
}

// Hook into the 'after_setup_theme' action to ensure the function runs early
add_action( 'after_setup_theme', 'fix_block_theme_error' );
```
