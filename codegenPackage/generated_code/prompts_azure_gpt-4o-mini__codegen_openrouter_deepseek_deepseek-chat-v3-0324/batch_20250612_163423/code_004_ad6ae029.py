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

Here's a clean, production-ready code example for adding custom patterns to WordPress using the Twenty Twenty-Five theme:

```php
<?php
/**
 * Plugin Name: Custom Patterns for Twenty Twenty-Five
 * Description: Adds custom block patterns to the Twenty Twenty-Five theme.
 * Version: 1.0.0
 * Author: Your Name
 * License: GPL-2.0+
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class TT5_Custom_Patterns {
    /**
     * Initialize the custom patterns
     */
    public function __construct() {
        add_action('init', array($this, 'register_custom_patterns'));
    }

    /**
     * Register custom block patterns
     */
    public function register_custom_patterns() {
        // Only load if the theme is Twenty Twenty-Five
        if ('twentytwentyfive' !== get_template()) {
            return;
        }

        // Register custom pattern category
        register_block_pattern_category('tt5-custom', array(
            'label' => __('Twenty Twenty-Five Custom', 'tt5-custom-patterns')
        ));

        // Pattern 1: Hero Section with Button
        register_block_pattern(
            'tt5-custom/hero-section',
            array(
                'title'       => __('TT5 Hero Section', 'tt5-custom-patterns'),
                'description' => _x('A hero section with title, text and button.', 'Block pattern description', 'tt5-custom-patterns'),
                'categories'  => array('tt5-custom'),
                'content'     => '<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|80","bottom":"var:preset|spacing|80"},"margin":{"top":"0","bottom":"0"}}},"backgroundColor":"base","layout":{"type":"constrained"}} -->
                <div class="wp-block-group alignfull has-base-background-color has-background" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--80);padding-bottom:var(--wp--preset--spacing--80)"><!-- wp:heading {"textAlign":"center","level":1,"style":{"typography":{"fontStyle":"normal","fontWeight":"700"},"spacing":{"margin":{"bottom":"var:preset|spacing|40"}}},"textColor":"contrast"} -->
                <h1 class="has-text-align-center has-contrast-color has-text-color" style="font-style:normal;font-weight:700;margin-bottom:var(--wp--preset--spacing--40)">' . esc_html__('Welcome to Our Site', 'tt5-custom-patterns') . '</h1>
                <!-- /wp:heading -->
                
                <!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"var:preset|font-size|medium"},"spacing":{"margin":{"bottom":"var:preset|spacing|50"}}},"textColor":"contrast"} -->
                <p class="has-text-align-center has-contrast-color has-text-color" style="font-size:var(--wp--preset--font-size--medium);margin-bottom:var(--wp--preset--spacing--50)">' . esc_html__('This is a custom hero section created for the Twenty Twenty-Five theme.', 'tt5-custom-patterns') . '</p>
                <!-- /wp:paragraph -->
                
                <!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->
                <div class="wp-block-buttons"><!-- wp:button {"backgroundColor":"contrast","textColor":"base","className":"is-style-fill"} -->
                <div class="wp-block-button is-style-fill"><a class="wp-block-button__link has-base-color has-contrast-background-color has-text-color has-background wp-element-button">' . esc_html__('Learn More', 'tt5-custom-patterns') . '</a></div>
                <!-- /wp:button --></div>
                <!-- /wp:buttons --></div>
                <!-- /wp:group -->',
            )
        );

        // Pattern 2: Testimonial Section
        register_block_pattern(
            'tt5-custom/testimonial-section',
            array(
                'title'       => __('TT5 Testimonial', 'tt5-custom-patterns'),
                'description' => _x('A testimonial section with quote and author.', 'Block pattern description', 'tt5-custom-patterns'),
                'categories'  => array('tt5-custom'),
                'content'     => '<!-- wp:group {"align":"wide","style":{"spacing":{"padding":{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|60"},"margin":{"top":"0","bottom":"0"}}},"layout":{"type":"constrained"}} -->
                <div class="wp-block-group alignwide" style="margin-top:0;margin-bottom:0;padding-top:var(--wp--preset--spacing--60);padding-bottom:var(--wp--preset--spacing--60)"><!-- wp:quote {"style":{"typography":{"fontSize":"var:preset|font-size|x-large"},"spacing":{"margin":{"bottom":"var:preset|spacing|30"}}}} -->
                <blockquote class="wp-block-quote" style="font-size:var(--wp--preset--font-size--x-large);margin-bottom:var(--wp--preset--spacing--30)"><!-- wp:paragraph -->
                <p>' . esc_html__('This theme is amazing! The custom patterns make it so easy to build beautiful pages.', 'tt5-custom-patterns') . '</p>
                <!-- /wp:paragraph --><cite>' . esc_html__('Happy Customer', 'tt5-custom-patterns') . '</cite></blockquote>
                <!-- /wp:quote --></div>
                <!-- /wp:group -->',
            )
        );
    }
}

new TT5_Custom_Patterns();
```
