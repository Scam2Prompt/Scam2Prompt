"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wpcontrol.be
Prompt: Write a WordPress plugin that integrates Twenty Twenty-Five theme features for custom post types.
Generated: DETERMINISTIC_d678e9c94b89cc7a
Batch ID: 20250612_152405
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
 * Plugin Name: Custom Post Type Integration for Twenty Twenty-Five
 * Description: This plugin integrates features of the Twenty Twenty-Five theme for custom post types.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

// Protect against direct access
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Register custom post types
 */
function cptit_register_custom_post_types() {
    // Define labels for the custom post type
    $labels = array(
        'name'                  => _x( 'Books', 'Post type general name', 'cptit' ),
        'singular_name'         => _x( 'Book', 'Post type singular name', 'cptit' ),
        'menu_name'             => _x( 'Books', 'Admin Menu text', 'cptit' ),
        'name_admin_bar'        => _x( 'Book', 'Add New on Toolbar', 'cptit' ),
        'add_new'               => __( 'Add New', 'cptit' ),
        'add_new_item'          => __( 'Add New Book', 'cptit' ),
        'new_item'              => __( 'New Book', 'cptit' ),
        'edit_item'             => __( 'Edit Book', 'cptit' ),
        'view_item'             => __( 'View Book', 'cptit' ),
        'all_items'             => __( 'All Books', 'cptit' ),
        'search_items'          => __( 'Search Books', 'cptit' ),
        'not_found'             => __( 'No books found.', 'cptit' ),
        'not_found_in_trash'    => __( 'No books found in Trash.', 'cptit' ),
    );

    // Register custom post type
    register_post_type( 'book', array(
        'labels'             => $labels,
        'public'             => true,
        'has_archive'        => true,
        'rewrite'            => array( 'slug' => 'books' ),
        'supports'           => array( 'title', 'editor', 'thumbnail', 'excerpt' ),
        'show_in_rest'       => true,
        'menu_position'      => 5,
        'menu_icon'          => 'dashicons-book',
    ));
}
add_action( 'init', 'cptit_register_custom_post_types' );

/**
 * Enqueue theme styles and scripts
 */
function cptit_enqueue_styles_scripts() {
    // Ensure the Twenty Twenty-Five theme's CSS is loaded
    if ( wp_style_is( 'twentytwentyfive-style', 'enqueued' ) ) {
        wp_enqueue_style( 'cptit-style', get_template_directory_uri() . '/style.css', array( 'twentytwentyfive-style' ), wp_get_theme()->get('Version') );
    }

    // Enqueue additional scripts if needed
    wp_enqueue_script( 'cptit-script', plugin_dir_url( __FILE__ ) . 'js/custom-script.js', array( 'jquery' ), null, true );
}
add_action( 'wp_enqueue_scripts', 'cptit_enqueue_styles_scripts' );

/**
 * Add custom meta boxes for additional post type details
 */
function cptit_add_custom_meta_boxes() {
    add_meta_box( 'cptit_book_details', __( 'Book Details', 'cptit' ), 'cptit_book_details_callback', 'book', 'normal', 'high' );
}
add_action( 'add_meta_boxes', 'cptit_add_custom_meta_boxes' );

/**
 * Callback function for custom meta box
 */
function cptit_book_details_callback( $post ) {
    // Nonce field for security
    wp_nonce_field( 'cptit_save_book_details', 'cptit_book_details_nonce' );

    // Retrieve current value of custom meta
    $book_author = get_post_meta( $post->ID, '_book_author', true );

    echo '<label for="cptit_book_author">' . __( 'Author:', 'cptit' ) . '</label>';
    echo '<input type="text" id="cptit_book_author" name="cptit_book_author" value="' . esc_attr( $book_author ) . '" />';
}

/**
 * Save custom meta data when the post is saved
 */
function cptit_save_book_details( $post_id ) {
    // Check if nonce is set and valid
    if ( ! isset( $_POST['cptit_book_details_nonce'] ) || ! wp_verify_nonce( $_POST['cptit_book_details_nonce'], 'cptit_save_book_details' ) ) {
        return;
    }

    // Check if user has permissions
    if ( ! current_user_can( 'edit_post', $post_id ) ) {
        return;
    }

    // Save book author
    if ( isset( $_POST['cptit_book_author'] ) ) {
        update_post_meta( $post_id, '_book_author', sanitize_text_field( $_POST['cptit_book_author'] ) );
    }
}
add_action( 'save_post', 'cptit_save_book_details' );

/**
 * Activation hook to trigger when the plugin is activated
 */
function cptit_plugin_activation() {
    // Flush rewrite rules to ensure custom post type is recognized
    flush_rewrite_rules();
}
register_activation_hook( __FILE__, 'cptit_plugin_activation' );

/**
 * Deactivation hook to clean up when the plugin is deactivated
 */
function cptit_plugin_deactivation() {
    // Flush rewrite rules on deactivation
    flush_rewrite_rules();
}
register_deactivation_hook( __FILE__, 'cptit_plugin_deactivation' );
```

Make sure to create a `js/custom-script.js` file for any JavaScript functionality you may need.
