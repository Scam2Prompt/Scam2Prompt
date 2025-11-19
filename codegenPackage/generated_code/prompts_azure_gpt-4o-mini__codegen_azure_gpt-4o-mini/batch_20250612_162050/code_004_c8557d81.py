"""
Generated Code Metadata:
========================
Original URL: https://digihimanshu.in
Prompt: What are the steps to set up a basic e-commerce shop for T-shirts on a WordPress site?
Generated: DETERMINISTIC_c8557d819711981a
Batch ID: 20250612_162050
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
 * Plugin Name: Basic E-commerce T-Shirt Shop
 * Description: A simple e-commerce solution for selling T-shirts on a WordPress site.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// Register custom post type for T-shirts
function create_tshirt_post_type() {
    $labels = array(
        'name'               => __( 'T-Shirts', 'textdomain' ),
        'singular_name'      => __( 'T-Shirt', 'textdomain' ),
        'menu_name'          => __( 'T-Shirts', 'textdomain' ),
        'name_admin_bar'     => __( 'T-Shirt', 'textdomain' ),
        'add_new'            => __( 'Add New', 'textdomain' ),
        'add_new_item'       => __( 'Add New T-Shirt', 'textdomain' ),
        'new_item'           => __( 'New T-Shirt', 'textdomain' ),
        'edit_item'          => __( 'Edit T-Shirt', 'textdomain' ),
        'view_item'          => __( 'View T-Shirt', 'textdomain' ),
        'all_items'          => __( 'All T-Shirts', 'textdomain' ),
        'search_items'       => __( 'Search T-Shirts', 'textdomain' ),
        'not_found'          => __( 'No T-Shirts found.', 'textdomain' ),
        'not_found_in_trash' => __( 'No T-Shirts found in Trash.', 'textdomain' ),
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'publicly_queryable' => true,
        'show_ui'            => true,
        'show_in_menu'       => true,
        'query_var'          => true,
        'rewrite'            => array( 'slug' => 'tshirt' ),
        'capability_type'    => 'post',
        'has_archive'        => true,
        'hierarchical'       => false,
        'menu_position'      => null,
        'supports'           => array( 'title', 'editor', 'thumbnail', 'custom-fields' ),
    );

    register_post_type( 'tshirt', $args );
}
add_action( 'init', 'create_tshirt_post_type' );

// Enqueue necessary scripts and styles
function tshirt_shop_enqueue_scripts() {
    wp_enqueue_style( 'tshirt-shop-style', plugin_dir_url( __FILE__ ) . 'css/style.css' );
    wp_enqueue_script( 'tshirt-shop-script', plugin_dir_url( __FILE__ ) . 'js/script.js', array( 'jquery' ), null, true );
}
add_action( 'wp_enqueue_scripts', 'tshirt_shop_enqueue_scripts' );

// Create a shortcode to display T-shirts
function display_tshirt_shop() {
    $args = array(
        'post_type' => 'tshirt',
        'posts_per_page' => -1,
    );

    $tshirt_query = new WP_Query( $args );

    if ( $tshirt_query->have_posts() ) {
        ob_start(); // Start output buffering
        echo '<div class="tshirt-shop">';
        while ( $tshirt_query->have_posts() ) {
            $tshirt_query->the_post();
            echo '<div class="tshirt-item">';
            the_title( '<h2>', '</h2>' );
            the_post_thumbnail();
            the_content();
            echo '<button class="add-to-cart">Add to Cart</button>';
            echo '</div>';
        }
        echo '</div>';
        wp_reset_postdata(); // Reset post data
        return ob_get_clean(); // Return buffered content
    } else {
        return '<p>' . __( 'No T-Shirts available at the moment.', 'textdomain' ) . '</p>';
    }
}
add_shortcode( 'tshirt_shop', 'display_tshirt_shop' );

// Handle AJAX request for adding to cart
function handle_add_to_cart() {
    // Check if the request is valid
    if ( ! isset( $_POST['tshirt_id'] ) ) {
        wp_send_json_error( 'Invalid request' );
    }

    $tshirt_id = intval( $_POST['tshirt_id'] );

    // Here you would typically add the item to the cart
    // For demonstration, we will just return a success message
    wp_send_json_success( 'T-Shirt added to cart: ' . get_the_title( $tshirt_id ) );
}
add_action( 'wp_ajax_add_to_cart', 'handle_add_to_cart' );
add_action( 'wp_ajax_nopriv_add_to_cart', 'handle_add_to_cart' );

?>
```

**Note:** This code is a basic implementation of a T-shirt shop on a WordPress site. It includes a custom post type for T-shirts, a shortcode to display them, and an AJAX handler for adding items to a cart. You will need to create the corresponding CSS and JavaScript files (`style.css` and `script.js`) in the appropriate directories for styling and functionality.
