"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://devteamtools.com
Prompt: Generate a code example for adding custom patterns to a WordPress site using the Twenty Twenty-Five theme.
Generated: DETERMINISTIC_ad6ae029e57fe126
Batch ID: 20250612_163423
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
 * Plugin Name: Custom Block Patterns for Twenty Twenty-Five Theme
 * Description: Adds custom block patterns to the Twenty Twenty-Five theme.
 * Version: 1.0.0
 * Author: Your Name
 * License: GPL-2.0+
 */

// Exit if accessed directly.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Registers custom block patterns for the Twenty Twenty-Five theme.
 */
function register_custom_block_patterns() {

    // Ensure the function is only loaded for the Twenty Twenty-Five theme.
    $current_theme = wp_get_theme();
    if ( 'Twenty Twenty-Five' !== $current_theme->get( 'Name' ) ) {
        return;
    }

    // Example: Register a block pattern for a custom hero section.
    register_block_pattern(
        'custom/hero-section',
        array(
            'title'       => __( 'Custom Hero Section', 'text-domain' ),
            'description' => __( 'A custom hero section with a heading and call-to-action button.', 'text-domain' ),
            'content'     => '
                <!-- wp:group {"align":"full","backgroundColor":"light-gray","className":"custom-hero-section"} -->
                <div class="wp-block-group alignfull has-light-gray-background-color custom-hero-section">
                    <!-- wp:heading {"textAlign":"center"} -->
                    <h2 class="has-text-align-center">Welcome to Our Site</h2>
                    <!-- /wp:heading -->

                    <!-- wp:paragraph {"align":"center"} -->
                    <p class="has-text-align-center">Explore and discover our amazing content!</p>
                    <!-- /wp:paragraph -->

                    <!-- wp:buttons {"align":"center"} -->
                    <div class="wp-block-buttons aligncenter">
                        <!-- wp:button {"className":"is-style-primary"} -->
                        <div class="wp-block-button is-style-primary"><a href="#">Get Started</a></div>
                        <!-- /wp:button -->
                    </div>
                    <!-- /wp:buttons -->
                </div>
                <!-- /wp:group -->
            ',
            'categories'  => array( 'featured', 'text' ),
            'keywords'    => array( 'hero', 'call-to-action', 'welcome' ),
        )
    );

    // Example: Register another block pattern for a custom testimonial layout.
    register_block_pattern(
        'custom/testimonial-layout',
        array(
            'title'       => __( 'Custom Testimonial Layout', 'text-domain' ),
            'description' => __( 'A custom layout for displaying testimonials.', 'text-domain' ),
            'content'     => '
                <!-- wp:group {"align":"wide","className":"custom-testimonial-layout"} -->
                <div class="wp-block-group alignwide custom-testimonial-layout">
                    <!-- wp:quote -->
                    <blockquote class="wp-block-quote">
                        <p>"The best service I have ever used. Highly recommend!"</p>
                        <cite>John Doe</cite>
                    </blockquote>
                    <!-- /wp:quote -->

                    <!-- wp:quote -->
                    <blockquote class="wp-block-quote">
                        <p>"Amazing experience from start to finish."</p>
                        <cite>Jane Smith</cite>
                    </blockquote>
                    <!-- /wp:quote -->
                </div>
                <!-- /wp:group -->
            ',
            'categories'  => array( 'text', 'columns' ),
            'keywords'    => array( 'testimonial', 'quote', 'review' ),
        )
    );

}

// Hook the function to the `init` action.
add_action( 'init', 'register_custom_block_patterns' );
?>
```
