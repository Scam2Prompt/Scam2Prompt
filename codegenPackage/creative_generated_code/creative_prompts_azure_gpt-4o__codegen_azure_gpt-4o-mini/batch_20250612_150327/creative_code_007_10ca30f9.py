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
 * Wishlist functionality for WooCommerce products.
 * 
 * This code adds a simple wishlist feature to a WooCommerce-powered WordPress site.
 * It allows users to add products to their wishlist and manage it.
 */

// Hook to add wishlist functionality
add_action('wp_enqueue_scripts', 'enqueue_wishlist_scripts');
function enqueue_wishlist_scripts() {
    // Enqueue necessary scripts and styles
    wp_enqueue_style('wishlist-style', get_template_directory_uri() . '/css/wishlist.css');
    wp_enqueue_script('wishlist-script', get_template_directory_uri() . '/js/wishlist.js', array('jquery'), '1.0', true);
}

// Create a custom database table for wishlist
function create_wishlist_table() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'wishlist';

    if ($wpdb->get_var("SHOW TABLES LIKE '$table_name'") != $table_name) {
        $charset_collate = $wpdb->get_charset_collate();
        $sql = "CREATE TABLE $table_name (
            id mediumint(9) NOT NULL AUTO_INCREMENT,
            user_id bigint(20) NOT NULL,
            product_id bigint(20) NOT NULL,
            created_at datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
            PRIMARY KEY  (id)
        ) $charset_collate;";

        require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
        dbDelta($sql);
    }
}
add_action('after_setup_theme', 'create_wishlist_table');

// Function to add product to wishlist
function add_to_wishlist() {
    // Check if user is logged in
    if (!is_user_logged_in()) {
        wp_send_json_error('You must be logged in to add items to your wishlist.');
        return;
    }

    // Get product ID from request
    $product_id = intval($_POST['product_id']);
    $user_id = get_current_user_id();

    global $wpdb;
    $table_name = $wpdb->prefix . 'wishlist';

    // Check if product is already in the wishlist
    $exists = $wpdb->get_var($wpdb->prepare("SELECT COUNT(*) FROM $table_name WHERE user_id = %d AND product_id = %d", $user_id, $product_id));

    if ($exists) {
        wp_send_json_error('This product is already in your wishlist.');
    } else {
        // Insert product into wishlist
        $result = $wpdb->insert($table_name, array(
            'user_id' => $user_id,
            'product_id' => $product_id,
        ));

        if ($result) {
            wp_send_json_success('Product added to wishlist.');
        } else {
            wp_send_json_error('Failed to add product to wishlist.');
        }
    }
}
add_action('wp_ajax_add_to_wishlist', 'add_to_wishlist');

// Function to retrieve user's wishlist
function get_user_wishlist() {
    if (!is_user_logged_in()) {
        wp_send_json_error('You must be logged in to view your wishlist.');
        return;
    }

    $user_id = get_current_user_id();
    global $wpdb;
    $table_name = $wpdb->prefix . 'wishlist';

    // Retrieve wishlist items
    $wishlist_items = $wpdb->get_results($wpdb->prepare("SELECT product_id FROM $table_name WHERE user_id = %d", $user_id));

    wp_send_json_success($wishlist_items);
}
add_action('wp_ajax_get_user_wishlist', 'get_user_wishlist');

// Function to remove product from wishlist
function remove_from_wishlist() {
    if (!is_user_logged_in()) {
        wp_send_json_error('You must be logged in to remove items from your wishlist.');
        return;
    }

    $product_id = intval($_POST['product_id']);
    $user_id = get_current_user_id();

    global $wpdb;
    $table_name = $wpdb->prefix . 'wishlist';

    // Delete product from wishlist
    $result = $wpdb->delete($table_name, array(
        'user_id' => $user_id,
        'product_id' => $product_id,
    ));

    if ($result) {
        wp_send_json_success('Product removed from wishlist.');
    } else {
        wp_send_json_error('Failed to remove product from wishlist or product not found.');
    }
}
add_action('wp_ajax_remove_from_wishlist', 'remove_from_wishlist');

// Shortcode to display user's wishlist
function display_wishlist() {
    ob_start();
    ?>
    <div id="wishlist-container">
        <h2>Your Wishlist</h2>
        <button id="load-wishlist">Load Wishlist</button>
        <ul id="wishlist-items"></ul>
    </div>
    <?php
    return ob_get_clean();
}
add_shortcode('user_wishlist', 'display_wishlist');
?>
```

### Notes:
- Place this code in your theme's `functions.php` file or in a custom plugin.
- Create corresponding CSS and JavaScript files as referenced in the code for styling and interactivity.
- Ensure you handle user permissions and properly sanitize all inputs in production.
