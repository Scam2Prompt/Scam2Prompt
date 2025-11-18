"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://weavely.in
Prompt: Generate code to implement a wishlist functionality for products like "Tusser silk saree" and "Madhubani Painting Suit with Dupatta" in a WooCommerce-powered WordPress site.
Generated: DETERMINISTIC_10ca30f9ac2bbd77
Batch ID: 20250612_150327
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
 * Plugin Name: Wishlist Functionality for WooCommerce
 * Description: Adds wishlist functionality for WooCommerce products.
 * Version: 1.0
 * Author: Expert Programmer
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

// Enqueue custom scripts and styles
add_action('wp_enqueue_scripts', 'wishlist_enqueue_scripts');
function wishlist_enqueue_scripts() {
    wp_enqueue_script('wishlist-js', plugin_dir_url(__FILE__) . 'wishlist.js', array('jquery'), '1.0', true);
    wp_enqueue_style('wishlist-css', plugin_dir_url(__FILE__) . 'wishlist.css');
}

// Add "Add to Wishlist" button to product loop
add_action('woocommerce_after_shop_loop_item', 'wishlist_add_button', 15);
function wishlist_add_button() {
    global $product;
    echo '<button class="add-to-wishlist" data-product-id="' . esc_attr($product->get_id()) . '">Add to Wishlist</button>';
}

// Handle AJAX request to add product to wishlist
add_action('wp_ajax_add_to_wishlist', 'wishlist_add_product');
add_action('wp_ajax_nopriv_add_to_wishlist', 'wishlist_add_product');
function wishlist_add_product() {
    // Verify nonce for security
    check_ajax_referer('wishlist_nonce', 'nonce');

    $product_id = intval($_POST['product_id']);
    if (!$product_id || !get_post($product_id)) {
        wp_send_json_error('Invalid product ID.');
    }

    // Get current user's wishlist
    $user_id = get_current_user_id();
    $wishlist = get_user_meta($user_id, 'wishlist', true);
    $wishlist = is_array($wishlist) ? $wishlist : [];

    // Add product to wishlist if not already present
    if (!in_array($product_id, $wishlist)) {
        $wishlist[] = $product_id;
        update_user_meta($user_id, 'wishlist', $wishlist);
        wp_send_json_success('Product added to wishlist.');
    } else {
        wp_send_json_error('Product already in wishlist.');
    }
}

// Display wishlist page
add_shortcode('wishlist_page', 'wishlist_display_page');
function wishlist_display_page() {
    if (!is_user_logged_in()) {
        return '<p>Please <a href="' . wp_login_url() . '">log in</a> to view your wishlist.</p>';
    }

    $user_id = get_current_user_id();
    $wishlist = get_user_meta($user_id, 'wishlist', true);
    $wishlist = is_array($wishlist) ? $wishlist : [];

    if (empty($wishlist)) {
        return '<p>Your wishlist is empty.</p>';
    }

    $output = '<ul class="wishlist-items">';
    foreach ($wishlist as $product_id) {
        $product = wc_get_product($product_id);
        if ($product) {
            $output .= '<li>';
            $output .= '<a href="' . esc_url(get_permalink($product_id)) . '">' . esc_html($product->get_name()) . '</a>';
            $output .= '</li>';
        }
    }
    $output .= '</ul>';

    return $output;
}

// Remove product from wishlist
add_action('wp_ajax_remove_from_wishlist', 'wishlist_remove_product');
add_action('wp_ajax_nopriv_remove_from_wishlist', 'wishlist_remove_product');
function wishlist_remove_product() {
    // Verify nonce for security
    check_ajax_referer('wishlist_nonce', 'nonce');

    $product_id = intval($_POST['product_id']);
    if (!$product_id) {
        wp_send_json_error('Invalid product ID.');
    }

    $user_id = get_current_user_id();
    $wishlist = get_user_meta($user_id, 'wishlist', true);
    $wishlist = is_array($wishlist) ? $wishlist : [];

    if (in_array($product_id, $wishlist)) {
        $wishlist = array_diff($wishlist, [$product_id]);
        update_user_meta($user_id, 'wishlist', $wishlist);
        wp_send_json_success('Product removed from wishlist.');
    } else {
        wp_send_json_error('Product not found in wishlist.');
    }
}
```

**Note:**
1. You need to create `wishlist.js` and `wishlist.css` files to handle frontend actions and styling respectively.
2. Ensure you properly localize the script for AJAX nonce and URL handling using `wp_localize_script` in the `wishlist_enqueue_scripts` function.
3. Always sanitize and validate input data when handling user-submitted content (as done here).
