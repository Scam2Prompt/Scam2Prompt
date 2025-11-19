"""
Generated Code Metadata:
========================
Original URL: https://wpcontrol.be
Prompt: Write a WordPress plugin that integrates Twenty Twenty-Five theme features for custom post types.
Generated: DETERMINISTIC_d678e9c94b89cc7a
Batch ID: 20250612_152405
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
 * Plugin Name: Custom Post Type Integration for Twenty Twenty-Five
 * Description: A WordPress plugin that integrates features of the Twenty Twenty-Five theme for custom post types.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Register Custom Post Type
 */
function cpt_twentytwentyfive_register_post_type() {
    $labels = array(
        'name'                  => _x( 'Custom Items', 'Post Type General Name', 'text_domain' ),
        'singular_name'         => _x( 'Custom Item', 'Post Type Singular Name', 'text_domain' ),
        'menu_name'             => __( 'Custom Items', 'text_domain' ),
        'name_admin_bar'        => __( 'Custom Item', 'text_domain' ),
        'add_new'               => __( 'Add New', 'text_domain' ),
        'add_new_item'          => __( 'Add New Custom Item', 'text_domain' ),
        'new_item'              => __( 'New Custom Item', 'text_domain' ),
        'edit_item'             => __( 'Edit Custom Item', 'text_domain' ),
        'view_item'             => __( 'View Custom Item', 'text_domain' ),
        'all_items'             => __( 'All Custom Items', 'text_domain' ),
        'search_items'          => __( 'Search Custom Items', 'text_domain' ),
        'not_found'             => __( 'No custom items found.', 'text_domain' ),
        'not_found_in_trash'    => __( 'No custom items found in Trash.', 'text_domain' ),
    );

    $args = array(
        'label'                 => __( 'Custom Item', 'text_domain' ),
        'description'           => __( 'A custom post type for items.', 'text_domain' ),
        'labels'                => $labels,
        'supports'              => array( 'title', 'editor', 'thumbnail', 'excerpt', 'custom-fields' ),
        'hierarchical'          => false,
        'public'                => true,
        'show_ui'              => true,
        'show_in_menu'          => true,
        'menu_position'         => 5,
        'show_in_admin_bar'     => true,
        'show_in_nav_menus'     => true,
        'can_export'            => true,
        'has_archive'           => true,
        'exclude_from_search'   => false,
        'publicly_queryable'    => true,
        'capability_type'       => 'post',
    );

    // Register the custom post type
    register_post_type( 'custom_item', $args );
}
add_action( 'init', 'cpt_twentytwentyfive_register_post_type' );

/**
 * Enqueue Styles and Scripts
 */
function cpt_twentytwentyfive_enqueue_styles() {
    // Enqueue theme styles
    wp_enqueue_style( 'twentytwentyfive-style', get_template_directory_uri() . '/style.css' );

    // Enqueue custom styles for the custom post type
    wp_enqueue_style( 'cpt-custom-style', plugin_dir_url( __FILE__ ) . 'css/custom-style.css' );
}
add_action( 'wp_enqueue_scripts', 'cpt_twentytwentyfive_enqueue_styles' );

/**
 * Add Custom Meta Box
 */
function cpt_twentytwentyfive_add_meta_box() {
    add_meta_box(
        'cpt_custom_meta_box',
        __( 'Custom Details', 'text_domain' ),
        'cpt_twentytwentyfive_meta_box_callback',
        'custom_item',
        'normal',
        'high'
    );
}
add_action( 'add_meta_boxes', 'cpt_twentytwentyfive_add_meta_box' );

/**
 * Meta Box Callback
 */
function cpt_twentytwentyfive_meta_box_callback( $post ) {
    // Add a nonce field for security
    wp_nonce_field( 'cpt_twentytwentyfive_save_meta_box_data', 'cpt_twentytwentyfive_meta_box_nonce' );

    // Retrieve existing value from the database
    $value = get_post_meta( $post->ID, '_cpt_custom_meta_key', true );

    // Display the form field
    echo '<label for="cpt_custom_field">' . __( 'Custom Field:', 'text_domain' ) . '</label>';
    echo '<input type="text" id="cpt_custom_field" name="cpt_custom_field" value="' . esc_attr( $value ) . '" size="25" />';
}

/**
 * Save Meta Box Data
 */
function cpt_twentytwentyfive_save_meta_box_data( $post_id ) {
    // Check if our nonce is set
    if ( ! isset( $_POST['cpt_twentytwentyfive_meta_box_nonce'] ) ) {
        return;
    }

    // Verify that the nonce is valid
    if ( ! wp_verify_nonce( $_POST['cpt_twentytwentyfive_meta_box_nonce'], 'cpt_twentytwentyfive_save_meta_box_data' ) ) {
        return;
    }

    // Check if the user has permission to save data
    if ( ! current_user_can( 'edit_post', $post_id ) ) {
        return;
    }

    // Check if the custom field is set
    if ( isset( $_POST['cpt_custom_field'] ) ) {
        // Sanitize and save the data
        $custom_data = sanitize_text_field( $_POST['cpt_custom_field'] );
        update_post_meta( $post_id, '_cpt_custom_meta_key', $custom_data );
    }
}
add_action( 'save_post', 'cpt_twentytwentyfive_save_meta_box_data' );
```
