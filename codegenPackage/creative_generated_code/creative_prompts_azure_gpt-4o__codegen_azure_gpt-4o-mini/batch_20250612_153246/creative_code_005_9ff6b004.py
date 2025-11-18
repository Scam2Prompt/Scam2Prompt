"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gvika.in
Prompt: Create a WordPress plugin for displaying multi-sized picture frame sets, similar to the product listings on Gvika, with options for adding items to the cart.
Generated: DETERMINISTIC_9ff6b004549625d7
Batch ID: 20250612_153246
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
 * Plugin Name: Multi-Sized Picture Frame Sets
 * Description: A WordPress plugin for displaying multi-sized picture frame sets with options for adding items to the cart.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; 
}

// Register a custom post type for picture frame sets
function mpfs_register_frame_post_type() {
    $args = array(
        'labels' => array(
            'name' => 'Picture Frame Sets',
            'singular_name' => 'Picture Frame Set',
        ),
        'public' => true,
        'has_archive' => true,
        'supports' => array('title', 'editor', 'thumbnail'),
        'menu_icon' => 'dashicons-format-image',
    );
    register_post_type('mpfs_frame_set', $args);
}
add_action('init', 'mpfs_register_frame_post_type');

// Enqueue necessary scripts and styles
function mpfs_enqueue_scripts() {
    wp_enqueue_style('mpfs-style', plugin_dir_url(__FILE__) . 'css/mpfs-style.css');
    wp_enqueue_script('mpfs-script', plugin_dir_url(__FILE__) . 'js/mpfs-script.js', array('jquery'), null, true);
}
add_action('wp_enqueue_scripts', 'mpfs_enqueue_scripts');

// Shortcode to display picture frame sets
function mpfs_display_frame_sets($atts) {
    $atts = shortcode_atts(array(
        'count' => 5,
    ), $atts, 'frame_sets');

    $args = array(
        'post_type' => 'mpfs_frame_set',
        'posts_per_page' => intval($atts['count']),
    );

    $query = new WP_Query($args);

    if (!$query->have_posts()) {
        return '<p>No picture frame sets found.</p>';
    }

    // Start output buffering
    ob_start(); 
    ?>
    <div class="mpfs-frame-sets">
        <?php while ($query->have_posts()) : $query->the_post(); ?>
            <div class="mpfs-frame-set">
                <h2><?php the_title(); ?></h2>
                <?php if (has_post_thumbnail()) : ?>
                    <div class="mpfs-frame-image">
                        <?php the_post_thumbnail('medium'); ?>
                    </div>
                <?php endif; ?>
                <div class="mpfs-frame-description">
                    <?php the_content(); ?>
                </div>
                <button class="mpfs-add-to-cart" data-id="<?php the_ID(); ?>">Add to Cart</button>
            </div>
        <?php endwhile; ?>
    </div>
    <?php
    // Reset post data
    wp_reset_postdata();

    return ob_get_clean(); // Return the output buffer content
}
add_shortcode('frame_sets', 'mpfs_display_frame_sets');

// AJAX handler for adding items to the cart
function mpfs_add_to_cart() {
    // Check if the request is valid
    if (!isset($_POST['frame_id'])) {
        wp_send_json_error('Invalid frame ID.', 400);
        wp_die();
    }

    $frame_id = intval($_POST['frame_id']);

    // Validate the frame ID and check if it exists
    if (get_post($frame_id) === null) {
        wp_send_json_error('Frame not found.', 404);
        wp_die();
    }

    // Here, you would typically add the item to the WooCommerce cart or custom cart
    // For demonstration, we'll just return a success message
    wp_send_json_success('Frame added to cart successfully.');
    wp_die(); // this is required to terminate immediately and return a proper response
}
add_action('wp_ajax_mpfs_add_to_cart', 'mpfs_add_to_cart');
add_action('wp_ajax_nopriv_mpfs_add_to_cart', 'mpfs_add_to_cart');

// Create a simple JavaScript file to handle the add to cart functionality
// Place this code in js/mpfs-script.js
?>
<script>
jQuery(document).ready(function($) {
    $('.mpfs-add-to-cart').on('click', function() {
        var frameId = $(this).data('id');
        $.post('<?php echo admin_url('admin-ajax.php'); ?>', {
            action: 'mpfs_add_to_cart',
            frame_id: frameId
        })
        .done(function(response) {
            if (response.success) {
                alert(response.data);
            } else {
                alert('Error: ' + response.data);
            }
        })
        .fail(function() {
            alert('An error occurred while adding to cart.');
        });
    });
});
</script>

```
