"""
Generated Code Metadata:
========================
Original URL: https://gvika.in
Prompt: Create a WordPress plugin for displaying multi-sized picture frame sets, similar to the product listings on Gvika, with options for adding items to the cart.
Generated: DETERMINISTIC_9ff6b004549625d7
Batch ID: 20250612_153246
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
 * Plugin Name: Multi-Sized Picture Frame Sets
 * Description: A WordPress plugin to display multi-sized picture frame sets with options to add items to the cart.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

// Register the custom post type for Picture Frame Sets
function mps_register_frame_post_type() {
    $args = array(
        'public' => true,
        'label'  => 'Picture Frame Sets',
        'supports' => array('title', 'editor', 'thumbnail', 'custom-fields'),
        'has_archive' => true,
    );
    register_post_type('picture_frame_set', $args);
}
add_action('init', 'mps_register_frame_post_type');

// Enqueue necessary scripts and styles
function mps_enqueue_scripts() {
    wp_enqueue_style('mps-styles', plugin_dir_url(__FILE__) . 'css/styles.css');
    wp_enqueue_script('mps-scripts', plugin_dir_url(__FILE__) . 'js/scripts.js', array('jquery'), null, true);
}
add_action('wp_enqueue_scripts', 'mps_enqueue_scripts');

// Shortcode to display picture frame sets
function mps_display_frame_sets($atts) {
    $atts = shortcode_atts(array(
        'posts_per_page' => 10,
    ), $atts, 'frame_sets');

    $query_args = array(
        'post_type' => 'picture_frame_set',
        'posts_per_page' => intval($atts['posts_per_page']),
    );

    $frame_sets = new WP_Query($query_args);

    if ($frame_sets->have_posts()) {
        ob_start(); // Start output buffering
        echo '<div class="mps-frame-sets">';
        while ($frame_sets->have_posts()) {
            $frame_sets->the_post();
            ?>
            <div class="mps-frame-set">
                <h2><?php the_title(); ?></h2>
                <div class="mps-frame-image"><?php the_post_thumbnail(); ?></div>
                <div class="mps-frame-description"><?php the_content(); ?></div>
                <button class="mps-add-to-cart" data-id="<?php the_ID(); ?>">Add to Cart</button>
            </div>
            <?php
        }
        echo '</div>';
        wp_reset_postdata(); // Reset post data
        return ob_get_clean(); // Return buffered content
    } else {
        return '<p>No frame sets found.</p>';
    }
}
add_shortcode('frame_sets', 'mps_display_frame_sets');

// AJAX handler for adding items to the cart
function mps_add_to_cart() {
    // Check for nonce security
    check_ajax_referer('mps_add_to_cart_nonce', 'security');

    $product_id = intval($_POST['product_id']);
    
    if ( ! $product_id ) {
        wp_send_json_error('Invalid product ID.');
    }

    // Add the product to the cart
    $cart = WC()->cart;
    $cart->add_to_cart($product_id);

    wp_send_json_success('Product added to cart.');
}
add_action('wp_ajax_mps_add_to_cart', 'mps_add_to_cart');
add_action('wp_ajax_nopriv_mps_add_to_cart', 'mps_add_to_cart');

// Add nonce for security in the footer
function mps_add_nonce() {
    ?>
    <script type="text/javascript">
        var mps_ajax_object = {
            ajax_url: "<?php echo admin_url('admin-ajax.php'); ?>",
            nonce: "<?php echo wp_create_nonce('mps_add_to_cart_nonce'); ?>"
        };
    </script>
    <?php
}
add_action('wp_footer', 'mps_add_nonce');
```

**Note:** Ensure to create the necessary `css/styles.css` and `js/scripts.js` files for styling and functionality. The JavaScript file should handle the AJAX request for adding items to the cart.
