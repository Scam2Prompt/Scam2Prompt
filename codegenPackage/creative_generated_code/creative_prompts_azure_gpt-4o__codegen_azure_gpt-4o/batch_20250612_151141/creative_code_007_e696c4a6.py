"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flashusdtgenerator.com
Prompt: "Write code to implement a 360° product viewer for WooCommerce, as described in the WoodMart theme features."
Generated: DETERMINISTIC_e696c4a62ee2b39a
Batch ID: 20250612_151141
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
 * Plugin Name: WooCommerce 360° Product Viewer
 * Description: Adds a 360° product viewer feature for WooCommerce products, compatible with WoodMart theme.
 * Version: 1.0
 * Author: Expert Programmer
 * License: GPLv2 or later
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

// Main Plugin Class
class WC_360_Product_Viewer {
    /**
     * Constructor
     */
    public function __construct() {
        // Hook into WooCommerce single product display
        add_action('woocommerce_after_single_product_summary', array($this, 'render_360_viewer'), 15);

        // Enqueue required scripts and styles
        add_action('wp_enqueue_scripts', array($this, 'enqueue_assets'));
    }

    /**
     * Enqueue necessary scripts and styles for the 360° viewer.
     */
    public function enqueue_assets() {
        // Register and enqueue a JS library for 360° product viewer (example: SpriteSpin or similar)
        wp_enqueue_script(
            'wc-360-viewer-js',
            plugin_dir_url(__FILE__) . 'assets/js/spritespin.min.js', // Ensure this file exists in your plugin directory
            array('jquery'),
            '1.0',
            true
        );

        // Add custom CSS for styling if needed
        wp_enqueue_style(
            'wc-360-viewer-css',
            plugin_dir_url(__FILE__) . 'assets/css/style.css', // Ensure this file exists in your plugin directory
            '1.0'
        );
    }

    /**
     * Render the 360° product viewer on single product pages.
     */
    public function render_360_viewer() {
        global $product;

        // Check if a 360° image gallery is set for this product
        $images = get_post_meta($product->get_id(), '_wc_360_images', true);

        if (!empty($images) && is_array($images)) {
            ?>
            <div id="wc-360-viewer" class="wc-360-viewer-container">
                <!-- Placeholder container for the 360° viewer -->
                <?php foreach ($images as $image_url): ?>
                    <img src="<?php echo esc_url($image_url); ?>" alt="360° View Image">
                <?php endforeach; ?>
            </div>
            <script type="text/javascript">
                jQuery(document).ready(function ($) {
                    $('#wc-360-viewer').spritespin({
                        source: <?php echo json_encode(array_values($images)); ?>,
                        width: 500, // Set width of the viewer
                        height: 500, // Set height of the viewer
                        frames: <?php echo count($images); ?>, // Number of frames
                        sense: -1, // Reverse drag interaction
                        animate: true, // Enable animation
                        loop: true // Loop animation
                    });
                });
            </script>
            <?php
        } else {
            echo '<p>No 360° images available for this product.</p>';
        }
    }
}

// Initialize the plugin
new WC_360_Product_Viewer();

/**
 * Add a custom meta box for adding 360° images in the WooCommerce product edit screen.
 */
function wc_360_product_images_meta_box() {
    add_meta_box(
        'wc_360_images_meta_box',
        __('360° Images', 'woocommerce'),
        'wc_360_images_meta_box_callback',
        'product',
        'side',
        'default'
    );
}
add_action('add_meta_boxes', 'wc_360_product_images_meta_box');

/**
 * Meta box callback for 360° images.
 *
 * @param WP_Post $post The current post object.
 */
function wc_360_images_meta_box_callback($post) {
    // Retrieve existing 360° images from post meta
    $images = get_post_meta($post->ID, '_wc_360_images', true);

    // Nonce field for security
    wp_nonce_field('wc_360_images_meta_box', 'wc_360_images_nonce');

    ?>
    <label for="wc_360_images"><?php _e('Enter image URLs (comma-separated):', 'woocommerce'); ?></label>
    <textarea
        id="wc_360_images"
        name="wc_360_images"
        rows="5"
        style="width: 100%;"><?php echo esc_textarea(implode(',', (array) $images)); ?></textarea>
    <?php
}

/**
 * Save custom meta box data for 360° images.
 *
 * @param int $post_id The ID of the current post.
 */
function wc_360_save_product_images_meta_box($post_id) {
    // Check nonce validity
    if (!isset($_POST['wc_360_images_nonce']) || !wp_verify_nonce($_POST['wc_360_images_nonce'], 'wc_360_images_meta_box')) {
        return;
    }

    // Check user permissions
    if (!current_user_can('edit_post', $post_id)) {
        return;
    }

    // Save image URLs as an array
    if (isset($_POST['wc_360_images'])) {
        $image_urls = array_map('trim', explode(',', sanitize_text_field($_POST['wc_360_images'])));
        update_post_meta($post_id, '_wc_360_images', $image_urls);
    } else {
        delete_post_meta($post_id, '_wc_360_images');
    }
}
add_action('save_post', 'wc_360_save_product_images_meta_box');
```

This code provides a basic implementation of a 360° product viewer with proper error handling, security, and WooCommerce integration. Make sure the required assets (e.g., spritespin.js) are included in the `assets` folder of the plugin directory.
