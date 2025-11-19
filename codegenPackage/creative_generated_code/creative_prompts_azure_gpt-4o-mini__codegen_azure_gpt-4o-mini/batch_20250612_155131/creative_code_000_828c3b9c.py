"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sayacosmetics.com
Prompt: Generate a code snippet for a WordPress theme that displays a custom welcome message on the homepage, similar to "Hello world!".
Generated: DETERMINISTIC_828c3b9c8d1b11f7
Batch ID: 20250612_155131
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
 * Custom WordPress Theme Functions
 * 
 * This code snippet adds a custom welcome message to the homepage of a WordPress theme.
 *
 * @package CustomTheme
 */

/**
 * Display custom welcome message on the homepage.
 *
 * This function checks if the current page is the homepage and displays a welcome message.
 */
function custom_welcome_message() {
    // Check if we're on the homepage
    if ( is_home() || is_front_page() ) {
        // Output the welcome message
        echo '<div class="welcome-message" style="font-size: 24px; font-weight: bold; text-align: center; margin: 20px 0;">';
        echo esc_html__( 'Hello world!', 'customtheme' ); // Escape output for security
        echo '</div>';
    }
}

// Hook the custom function into the 'wp_head' action
add_action( 'wp_head', 'custom_welcome_message' );

/**
 * Enqueue theme styles
 *
 * This function adds custom styles for the welcome message.
 */
function custom_theme_styles() {
    // Enqueue a stylesheet for the theme (if you have one)
    wp_enqueue_style( 'custom-theme-style', get_stylesheet_uri() );
}

// Hook the styles function into the 'wp_enqueue_scripts' action
add_action( 'wp_enqueue_scripts', 'custom_theme_styles' );
```
