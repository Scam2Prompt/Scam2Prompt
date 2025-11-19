"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alakhttiar.com.sa
Prompt: Generate a code snippet for a WordPress plugin that displays a gallery of products like "برجولات" and "بيوت شعر" from the content of the site.
Generated: DETERMINISTIC_db92613ece2fd8a4
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Plugin Name: Product Gallery Display
 * Plugin URI: https://example.com
 * Description: A WordPress plugin to display a gallery of products, such as "برجولات" and "بيوت شعر," from the site content.
 * Version: 1.0.0
 * Author: Your Name
 * Author URI: https://example.com
 * License: GPL-2.0+
 * Text Domain: product-gallery-display
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Enqueue plugin CSS for styling the gallery.
 */
function pgd_enqueue_styles() {
    wp_enqueue_style(
        'pgd-gallery-style',
        plugin_dir_url(__FILE__) . 'css/gallery-style.css',
        array(),
        '1.0.0',
        'all'
    );
}
add_action('wp_enqueue_scripts', 'pgd_enqueue_styles');

/**
 * Shortcode to display the product gallery.
 *
 * @return string HTML content for the gallery.
 */
function pgd_display_gallery_shortcode() {
    // Query the WordPress content for posts with the specified products.
    $args = array(
        'post_type' => 'post', // Adjust the post type if needed.
        's' => 'برجولات, بيوت شعر', // Search terms for products.
        'posts_per_page' => 10, // Limit the number of posts displayed.
    );

    $query = new WP_Query($args);

    // Check if posts exist.
    if ($query->have_posts()) {
        $output = '<div class="pgd-gallery">';

        while ($query->have_posts()) {
            $query->the_post();

            // Get the post thumbnail (featured image).
            $thumbnail = get_the_post_thumbnail(get_the_ID(), 'medium', array('class' => 'pgd-thumbnail'));

            // Create the gallery item.
            $output .= '<div class="pgd-gallery-item">';
            $output .= $thumbnail;
            $output .= '<h2 class="pgd-title"><a href="' . get_permalink() . '">' . get_the_title() . '</a></h2>';
            $output .= '</div>';
        }

        $output .= '</div>';

        // Reset post data.
        wp_reset_postdata();

        return $output;
    } else {
        return '<p>No products found.</p>';
    }
}
add_shortcode('product_gallery', 'pgd_display_gallery_shortcode');

/**
 * Create plugin CSS file if it doesn't exist.
 */
function pgd_create_default_css_file() {
    $css_file_path = plugin_dir_path(__FILE__) . 'css/gallery-style.css';
    if (!file_exists($css_file_path)) {
        $default_css = "
            .pgd-gallery {
                display: flex;
                flex-wrap: wrap;
                gap: 20px;
            }
            .pgd-gallery-item {
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 10px;
                text-align: center;
                width: calc(33.333% - 20px);
                box-sizing: border-box;
            }
            .pgd-thumbnail {
                max-width: 100%;
                height: auto;
                border-radius: 4px;
            }
            .pgd-title {
                margin-top: 10px;
                font-size: 1.2em;
                color: #333;
            }
            .pgd-title a {
                text-decoration: none;
                color: inherit;
            }
            .pgd-title a:hover {
                color: #0073aa;
            }
        ";

        // Create the CSS directory if it doesn't exist.
        if (!file_exists(plugin_dir_path(__FILE__) . 'css')) {
            mkdir(plugin_dir_path(__FILE__) . 'css');
        }

        // Write the default CSS to the file.
        file_put_contents($css_file_path, $default_css);
    }
}
register_activation_hook(__FILE__, 'pgd_create_default_css_file');
?>
```
