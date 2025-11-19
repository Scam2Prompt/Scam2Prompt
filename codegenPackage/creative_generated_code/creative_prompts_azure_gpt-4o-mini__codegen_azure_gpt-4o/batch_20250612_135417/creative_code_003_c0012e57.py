"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiffany-holz.de
Prompt: Recommend a library for creating a media gallery in WordPress that complements the Ashe theme.
Generated: DETERMINISTIC_c0012e57bbfc0226
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
 * Plugin Name: Custom Media Gallery for Ashe Theme
 * Description: A simple media gallery plugin that complements the Ashe theme.
 * Version: 1.0
 * Author: Expert Programmer
 * License: GPLv2 or later
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Shortcode function to render media gallery
 *
 * @param array $atts Shortcode attributes.
 * @return string HTML output for the media gallery.
 */
function ashe_custom_media_gallery_shortcode($atts) {
    // Default attributes
    $defaults = array(
        'ids' => '',                // Comma-separated media IDs
        'columns' => 3,            // Number of columns
        'size' => 'thumbnail',     // Image size
    );
    $atts = shortcode_atts($defaults, $atts);

    // Ensure media IDs are provided
    if (empty($atts['ids'])) {
        return '<p>No images provided for the gallery.</p>';
    }

    // Sanitize and prepare data
    $image_ids = array_map('intval', explode(',', $atts['ids']));
    $columns = intval($atts['columns']);
    $image_size = sanitize_text_field($atts['size']);
    
    // Begin gallery output
    $output = '<div class="ashe-media-gallery" style="display: grid; grid-template-columns: repeat(' . $columns . ', 1fr); gap: 10px;">';

    foreach ($image_ids as $image_id) {
        $image_url = wp_get_attachment_image_src($image_id, $image_size);

        // Ensure image exists
        if ($image_url) {
            $output .= '<div class="ashe-gallery-item">';
            $output .= '<img src="' . esc_url($image_url[0]) . '" alt="" style="width: 100%; height: auto; border: 1px solid #ddd; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);">';
            $output .= '</div>';
        }
    }

    $output .= '</div>'; // Close gallery container

    return $output;
}

/**
 * Register the shortcode
 */
function ashe_custom_media_gallery_init() {
    add_shortcode('ashe_media_gallery', 'ashe_custom_media_gallery_shortcode');
}

add_action('init', 'ashe_custom_media_gallery_init');

/**
 * Enqueue necessary styles for the gallery
 */
function ashe_custom_media_gallery_styles() {
    echo '<style>
        .ashe-media-gallery {
            margin: 20px 0;
        }
        .ashe-gallery-item {
            overflow: hidden;
        }
    </style>';
}

add_action('wp_head', 'ashe_custom_media_gallery_styles');
?>
```

### Usage:
Place the following shortcode in your WordPress post or page to render the gallery:
```text
[ashe_media_gallery ids="1,2,3,4" columns="3" size="medium"]
```

Replace `ids` with the attachment IDs of your media files, and adjust `columns`/`size` as needed.
