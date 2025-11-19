"""
Generated Code Metadata:
========================
Original URL: https://tiffany-holz.de
Prompt: Generate a code snippet for a gallery display using the Ashe theme for WordPress.
Generated: DETERMINISTIC_37a1645a509e44c7
Batch ID: 20250612_135417
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
 * Gallery Display Template for Ashe Theme
 *
 * @package Ashe
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit; // Exit if accessed directly.
}

/**
 * Gallery Display Function
 *
 * @param array $atts Shortcode attributes.
 */
function ashe_gallery_shortcode( $atts ) {
	// Default attributes
	$atts = shortcode_atts(
		array(
			'ids'     => '',
			'columns' => 3,
			'size'    => 'thumbnail',
		),
		$atts,
		'ashe_gallery'
	);

	// Check if attachments are provided
	if ( empty( $atts['ids'] ) ) {
		return '';
	}

	// Split attachment IDs into an array
	$attachment_ids = explode( ',', $atts['ids'] );

	// Check if attachment IDs array is not empty
	if ( empty( $attachment_ids ) ) {
		return '';
	}

	// Prepare gallery content
	$gallery_content = '';

	// Loop through each attachment ID
	foreach ( $attachment_ids as $attachment_id ) {
		// Get attachment image src and alt text
		$image_src = wp_get_attachment_image_src( $attachment_id, $atts['size'] );
		$image_alt = get_post_meta( $attachment_id, '_wp_attachment_image_alt', true );

		// Check if image src is not empty
		if ( ! empty( $image_src ) ) {
			// Append image to gallery content
			$gallery_content .= '<div class="gallery-item">';
			$gallery_content .= '<img src="' . esc_url( $image_src[0] ) . '" alt="' . esc_attr( $image_alt ) . '">';
			$gallery_content .= '</div>';
		}
	}

	// Check if gallery content is not empty
	if ( empty( $gallery_content ) ) {
		return '';
	}

	// Wrap gallery content in a container
	$gallery_wrapper = '<div class="ashe-gallery columns-' . esc_attr( $atts['columns'] ) . '">' . $gallery_content . '</div>';

	// Return gallery wrapper
	return $gallery_wrapper;
}
add_shortcode( 'ashe_gallery', 'ashe_gallery_shortcode' );

/**
 * Gallery Display CSS
 */
function ashe_gallery_css() {
	wp_enqueue_style( 'ashe-gallery', get_stylesheet_directory_uri() . '/css/gallery.css' );
}
add_action( 'wp_enqueue_scripts', 'ashe_gallery_css' );
```

```css
/* gallery.css */

.ashe-gallery {
	display: flex;
	flex-wrap: wrap;
	justify-content: center;
}

.ashe-gallery.columns-1 .gallery-item {
	width: 100%;
	margin: 10px;
}

.ashe-gallery.columns-2 .gallery-item {
	width: calc(50% - 20px);
	margin: 10px;
}

.ashe-gallery.columns-3 .gallery-item {
	width: calc(33.33% - 20px);
	margin: 10px;
}

.gallery-item img {
	width: 100%;
	height: auto;
	border-radius: 10px;
	box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.gallery-item:hover img {
	transform: scale(1.05);
	transition: transform 0.3s ease-in-out;
}
```
