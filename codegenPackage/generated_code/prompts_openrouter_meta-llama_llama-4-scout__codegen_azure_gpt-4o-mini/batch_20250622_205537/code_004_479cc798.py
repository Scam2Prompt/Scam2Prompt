"""
Generated Code Metadata:
========================
Original URL: https://livivid.com
Prompt: Create a shortcode to display a promotional banner on an e-commerce website, similar to the "80% OFF Outdoor Furniture" banner on this webpage.
Generated: DETERMINISTIC_479cc798ae66aa0b
Batch ID: 20250622_205537
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
 * Plugin Name: Promotional Banner Shortcode
 * Description: A shortcode to display a promotional banner on an e-commerce website.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Shortcode function to display a promotional banner.
 *
 * @param array $atts Shortcode attributes.
 * @return string HTML output of the promotional banner.
 */
function promotional_banner_shortcode( $atts ) {
    // Define default attributes
    $atts = shortcode_atts(
        array(
            'text' => '80% OFF Outdoor Furniture',
            'link' => '#',
            'background_color' => '#ffcc00',
            'text_color' => '#000000',
        ),
        $atts,
        'promo_banner'
    );

    // Sanitize attributes
    $text = sanitize_text_field( $atts['text'] );
    $link = esc_url( $atts['link'] );
    $background_color = sanitize_hex_color( $atts['background_color'] );
    $text_color = sanitize_hex_color( $atts['text_color'] );

    // Generate the banner HTML
    $banner_html = sprintf(
        '<div class="promo-banner" style="background-color: %s; color: %s; padding: 20px; text-align: center;">',
        $background_color,
        $text_color
    );
    $banner_html .= sprintf(
        '<a href="%s" style="text-decoration: none; color: inherit;">%s</a>',
        $link,
        $text
    );
    $banner_html .= '</div>';

    return $banner_html;
}

// Register the shortcode with WordPress
add_shortcode( 'promo_banner', 'promotional_banner_shortcode' );

// Enqueue styles for the banner (optional)
function promo_banner_styles() {
    echo '<style>
        .promo-banner {
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        }
    </style>';
}
add_action( 'wp_head', 'promo_banner_styles' );
```
