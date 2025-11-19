"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiffany-holz.de
Prompt: Generate a code snippet for a gallery display using the Ashe theme for WordPress.
Generated: DETERMINISTIC_37a1645a509e44c7
Batch ID: 20250612_135417
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
 * Custom Gallery Display Function for Ashe Theme
 *
 * This function displays a gallery of images in the Ashe WordPress theme.
 * It uses a shortcode for easy integration into posts or pages.
 *
 * @package Ashe_Theme
 */

// Prevent direct file access.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Renders a gallery display using Ashe theme styles.
 *
 * @param array $atts Shortcode attributes for customizing the gallery.
 * @return string HTML output for the gallery.
 */
function ashe_custom_gallery_shortcode( $atts ) {
    // Shortcode attributes with default values.
    $atts = shortcode_atts(
        array(
            'ids'      => '',  // Comma-separated list of image IDs.
            'columns'  => 3,   // Number of columns in the gallery.
            'size'     => 'medium', // Image size ('thumbnail', 'medium', 'large', etc.).
        ),
        $atts,
        'ashe_gallery'
    );

    // Validate and sanitize attributes.
    $image_ids = array_filter( array_map( 'intval', explode( ',', $atts['ids'] ) ) );
    $columns   = intval( $atts['columns'] );
    $size      = sanitize_text_field( $atts['size'] );

    // Return an error message if no image IDs are provided.
    if ( empty( $image_ids ) ) {
        return '<p>No images provided for the gallery.</p>';
    }

    // Start building gallery HTML.
    $output = '<div class="ashe-gallery" style="display: grid; grid-template-columns: repeat(' . esc_attr( $columns ) . ', 1fr); gap: 16px;">';

    foreach ( $image_ids as $image_id ) {
        // Retrieve image URL and alt text.
        $image_url = wp_get_attachment_image_url( $image_id, $size );
        $alt_text  = get_post_meta( $image_id, '_wp_attachment_image_alt', true );

        // Skip invalid images.
        if ( ! $image_url ) {
            continue;
        }

        // Append each image to the gallery.
        $output .= '<div class="ashe-gallery-item">';
        $output .= '<img src="' . esc_url( $image_url ) . '" alt="' . esc_attr( $alt_text ) . '" style="width: 100%; height: auto; border-radius: 8px;">';
        $output .= '</div>';
    }

    // Close gallery container.
    $output .= '</div>';

    return $output;
}

// Register the shortcode: [ashe_gallery ids="1,2,3" columns="3" size="medium"].
add_shortcode( 'ashe_gallery', 'ashe_custom_gallery_shortcode' );
?>
```
