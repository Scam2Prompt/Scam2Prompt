"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomxtension.com
Prompt: Create a WordPress shortcode to display patterns available in the Twenty Twenty-Five theme.
Generated: DETERMINISTIC_bfabf46f3a5c550e
Batch ID: 20250612_154158
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
 * Plugin Name: Twenty Twenty-Five Patterns Shortcode
 * Description: A shortcode to display patterns available in the Twenty Twenty-Five theme.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Shortcode to display patterns available in the Twenty Twenty-Five theme.
 *
 * Usage: [twenty_twenty_five_patterns]
 *
 * @return string HTML output of patterns.
 */
function tt25_patterns_shortcode() {
    // Check if the Twenty Twenty-Five theme is active.
    if ( wp_get_theme()->get( 'Name' ) !== 'Twenty Twenty-Five' ) {
        return '<p>The Twenty Twenty-Five theme is not active. Please activate it to use this shortcode.</p>';
    }

    // Get registered block patterns.
    $patterns = WP_Block_Patterns_Registry::get_instance()->get_all_registered();

    // Filter patterns to only include those registered by the active theme.
    $theme_name = wp_get_theme()->get_stylesheet();
    $filtered_patterns = array_filter( $patterns, function( $pattern ) use ( $theme_name ) {
        return isset( $pattern['categories'] ) && in_array( $theme_name, $pattern['categories'], true );
    });

    // If no patterns are found, return a message.
    if ( empty( $filtered_patterns ) ) {
        return '<p>No patterns found for the Twenty Twenty-Five theme.</p>';
    }

    // Build the output.
    $output = '<div class="tt25-patterns">';
    foreach ( $filtered_patterns as $pattern ) {
        $output .= '<div class="tt25-pattern">';
        $output .= '<h3>' . esc_html( $pattern['title'] ) . '</h3>';
        $output .= '<div>' . $pattern['content'] . '</div>';
        $output .= '</div>';
    }
    $output .= '</div>';

    return $output;
}

// Register the shortcode.
add_shortcode( 'twenty_twenty_five_patterns', 'tt25_patterns_shortcode' );

/**
 * Enqueue styles for the output of the shortcode.
 */
function tt25_patterns_enqueue_styles() {
    // Enqueue custom CSS if needed.
    wp_enqueue_style(
        'tt25-patterns-style',
        plugin_dir_url( __FILE__ ) . 'assets/tt25-patterns.css',
        array(),
        '1.0',
        'all'
    );
}
add_action( 'wp_enqueue_scripts', 'tt25_patterns_enqueue_styles' );
```

### Notes:
1. Ensure you create an `assets/tt25-patterns.css` file for styling, or remove the `wp_enqueue_style` part if custom styling is not necessary.
2. Place this code in a `.php` file (e.g., `tt25-patterns-shortcode.php`) and upload it as a custom plugin in WordPress.
