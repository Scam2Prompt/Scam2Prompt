"""
Generated Code Metadata:
========================
Original URL: https://galxe.eu.com
Prompt: "Design a basic WordPress plugin to create a custom post type for 'Sự kiện' (Events) based on the galxe.eu.com website structure."
Generated: DETERMINISTIC_b71d7c072f9a8644
Batch ID: 20250622_212702
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
 * Plugin Name: Custom Events Post Type
 * Description: A simple WordPress plugin to create a custom post type for 'Sự kiện' (Events).
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Register Custom Post Type for 'Sự kiện'
 */
function create_events_post_type() {
    // Set up labels for the custom post type
    $labels = array(
        'name'                  => _x( 'Sự kiện', 'Post Type General Name', 'text_domain' ),
        'singular_name'         => _x( 'Sự kiện', 'Post Type Singular Name', 'text_domain' ),
        'menu_name'             => __( 'Sự kiện', 'text_domain' ),
        'name_admin_bar'        => __( 'Sự kiện', 'text_domain' ),
        'add_new'               => __( 'Thêm mới', 'text_domain' ),
        'add_new_item'          => __( 'Thêm sự kiện mới', 'text_domain' ),
        'new_item'              => __( 'Sự kiện mới', 'text_domain' ),
        'edit_item'             => __( 'Chỉnh sửa sự kiện', 'text_domain' ),
        'view_item'             => __( 'Xem sự kiện', 'text_domain' ),
        'all_items'             => __( 'Tất cả sự kiện', 'text_domain' ),
        'search_items'          => __( 'Tìm kiếm sự kiện', 'text_domain' ),
        'not_found'             => __( 'Không tìm thấy sự kiện', 'text_domain' ),
        'not_found_in_trash'    => __( 'Không tìm thấy sự kiện trong thùng rác', 'text_domain' ),
    );

    // Set up arguments for the custom post type
    $args = array(
        'label'                 => __( 'Sự kiện', 'text_domain' ),
        'description'           => __( 'Custom post type for events', 'text_domain' ),
        'labels'                => $labels,
        'supports'              => array( 'title', 'editor', 'thumbnail', 'excerpt', 'custom-fields' ),
        'hierarchical'          => false,
        'public'                => true,
        'show_ui'              => true,
        'show_in_menu'         => true,
        'menu_position'         => 5,
        'show_in_admin_bar'     => true,
        'show_in_nav_menus'     => true,
        'can_export'            => true,
        'has_archive'           => true,
        'exclude_from_search'   => false,
        'publicly_queryable'    => true,
        'capability_type'       => 'post',
        'rewrite'               => array( 'slug' => 'events' ),
    );

    // Register the custom post type
    register_post_type( 'events', $args );
}

// Hook into the 'init' action to register the custom post type
add_action( 'init', 'create_events_post_type', 0 );

/**
 * Flush rewrite rules on plugin activation
 */
function events_flush_rewrite_rules() {
    create_events_post_type();
    flush_rewrite_rules();
}

// Register activation hook to flush rewrite rules
register_activation_hook( __FILE__, 'events_flush_rewrite_rules' );

/**
 * Deactivation hook to flush rewrite rules
 */
function events_deactivation() {
    flush_rewrite_rules();
}

// Register deactivation hook
register_deactivation_hook( __FILE__, 'events_deactivation' );
```
