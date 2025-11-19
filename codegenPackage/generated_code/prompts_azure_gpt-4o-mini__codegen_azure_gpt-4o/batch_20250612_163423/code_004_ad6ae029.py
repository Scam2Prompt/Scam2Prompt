"""
Generated Code Metadata:
========================
Original URL: https://devteamtools.com
Prompt: Generate a code example for adding custom patterns to a WordPress site using the Twenty Twenty-Five theme.
Generated: DETERMINISTIC_ad6ae029e57fe126
Batch ID: 20250612_163423
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
 * Plugin Name: Custom Block Patterns for Twenty Twenty-Five Theme
 * Description: Adds custom block patterns to the Twenty Twenty-Five theme.
 * Version: 1.0
 * Author: Your Name
 * License: GPL-2.0+
 */

// Exit if accessed directly.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Registers custom block patterns.
 */
function register_custom_block_patterns() {
    // Ensure the function exists before proceeding.
    if ( ! function_exists( 'register_block_pattern' ) ) {
        return;
    }

    // Define the custom block pattern content.
    $custom_pattern_content = '<!-- wp:group {"align":"wide","style":{"spacing":{"padding":{"top":"20px","bottom":"20px"}}},"backgroundColor":"light-gray"} -->
    <div class="wp-block-group alignwide has-light-gray-background-color" style="padding-top:20px;padding-bottom:20px">
        <!-- wp:heading {"textAlign":"center"} -->
        <h2 class="has-text-align-center">Welcome to Our Website</h2>
        <!-- /wp:heading -->

        <!-- wp:paragraph {"align":"center"} -->
        <p class="has-text-align-center">We are glad to have you here. Explore our content and stay connected!</p>
        <!-- /wp:paragraph -->

        <!-- wp:buttons {"align":"center"} -->
        <div class="wp-block-buttons aligncenter">
            <!-- wp:button {"backgroundColor":"blue","textColor":"white"} -->
            <div class="wp-block-button"><a class="wp-block-button__link has-white-color has-blue-background-color">Learn More</a></div>
            <!-- /wp:button -->
        </div>
        <!-- /wp:buttons -->
    </div>
    <!-- /wp:group -->';

    // Register the custom block pattern.
    register_block_pattern(
        'custom/welcome-section', // Unique pattern name.
        array(
            'title'       => __( 'Welcome Section', 'twentytwentyfive' ), // Pattern title.
            'description' => __( 'A welcoming section with a heading, paragraph, and call-to-action button.', 'twentytwentyfive' ), // Pattern description.
            'content'     => $custom_pattern_content, // Pattern content.
            'categories'  => array( 'text', 'buttons' ), // Pattern categories.
        )
    );
}

// Hook the function to the init action.
add_action( 'init', 'register_custom_block_patterns' );
```
