"""
Generated Code Metadata:
========================
Original URL: https://weavely.in
Prompt: Generate code to implement a wishlist functionality for products like "Tusser silk saree" and "Madhubani Painting Suit with Dupatta" in a WooCommerce-powered WordPress site.
Generated: DETERMINISTIC_10ca30f9ac2bbd77
Batch ID: 20250612_150327
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
 * Plugin Name: WooCommerce Wishlist Functionality
 * Description: A simple wishlist functionality for WooCommerce products.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// Enqueue necessary scripts and styles
function wc_wishlist_enqueue_scripts() {
    wp_enqueue_style( 'wc-wishlist-style', plugin_dir_url( __FILE__ ) . 'css/wishlist.css' );
    wp_enqueue_script( 'wc-wishlist-script', plugin_dir_url( __FILE__ ) . 'js/wishlist.js', array( 'jquery' ), null, true );
}
add_action( 'wp_enqueue_scripts', 'wc_wishlist_enqueue_scripts' );

// Create a wishlist table in the database
function wc_wishlist_create_table() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'wishlist';
    $charset_collate = $wpdb->get_charset_collate();

    $sql = "CREATE TABLE IF NOT EXISTS $table_name (
        id mediumint(9) NOT NULL AUTO_INCREMENT,
        user_id mediumint(9) NOT NULL,
        product_id mediumint(9) NOT NULL,
        created_at datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
        PRIMARY KEY  (id)
    ) $charset_collate;";

    require_once( ABSPATH . 'wp-admin/includes/upgrade.php' );
    dbDelta( $sql );
}
register_activation_hook( __FILE__, 'wc_wishlist_create_table' );

// Add product to wishlist
function wc_wishlist_add_product() {
    if ( ! is_user_logged_in() ) {
        wp_send_json_error( 'User not logged in' );
        return;
    }

    $user_id = get_current_user_id();
    $product_id = intval( $_POST['product_id'] );

    global $wpdb;
    $table_name = $wpdb->prefix . 'wishlist';

    // Check if product is already in wishlist
    $exists = $wpdb->get_var( $wpdb->prepare( "SELECT COUNT(*) FROM $table_name WHERE user_id = %d AND product_id = %d", $user_id, $product_id ) );

    if ( $exists ) {
        wp_send_json_error( 'Product already in wishlist' );
        return;
    }

    // Insert product into wishlist
    $result = $wpdb->insert( $table_name, array(
        'user_id' => $user_id,
        'product_id' => $product_id,
    ) );

    if ( $result ) {
        wp_send_json_success( 'Product added to wishlist' );
    } else {
        wp_send_json_error( 'Failed to add product to wishlist' );
    }
}
add_action( 'wp_ajax_wc_wishlist_add_product', 'wc_wishlist_add_product' );

// Display wishlist
function wc_wishlist_display() {
    if ( ! is_user_logged_in() ) {
        echo '<p>Please log in to view your wishlist.</p>';
        return;
    }

    $user_id = get_current_user_id();
    global $wpdb;
    $table_name = $wpdb->prefix . 'wishlist';

    $products = $wpdb->get_results( $wpdb->prepare( "SELECT product_id FROM $table_name WHERE user_id = %d", $user_id ) );

    if ( empty( $products ) ) {
        echo '<p>Your wishlist is empty.</p>';
        return;
    }

    echo '<h2>Your Wishlist</h2><ul>';
    foreach ( $products as $product ) {
        $product_data = wc_get_product( $product->product_id );
        if ( $product_data ) {
            echo '<li>' . esc_html( $product_data->get_name() ) . ' - <a href="' . esc_url( $product_data->get_permalink() ) . '">View Product</a></li>';
        }
    }
    echo '</ul>';
}

// Shortcode to display wishlist
function wc_wishlist_shortcode() {
    ob_start();
    wc_wishlist_display();
    return ob_get_clean();
}
add_shortcode( 'wc_wishlist', 'wc_wishlist_shortcode' );
```

**Note:** Ensure to create the `css/wishlist.css` and `js/wishlist.js` files in your plugin directory for styling and functionality as needed.
