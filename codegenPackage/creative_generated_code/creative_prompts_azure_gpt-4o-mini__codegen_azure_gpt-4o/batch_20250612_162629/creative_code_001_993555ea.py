"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usweb09.us
Prompt: Write a code snippet to create a custom post type in WordPress, as discussed in the FAQs section of usweb09.us.
Generated: DETERMINISTIC_993555eae2749725
Batch ID: 20250612_162629
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
 * Plugin Name: Custom Post Type Example
 * Description: A plugin to register a custom post type.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Registers a custom post type 'Books'.
 */
function usweb09_register_custom_post_type() {
    // Labels for the custom post type.
    $labels = array(
        'name'               => _x( 'Books', 'Post Type General Name', 'textdomain' ),
        'singular_name'      => _x( 'Book', 'Post Type Singular Name', 'textdomain' ),
        'menu_name'          => __( 'Books', 'textdomain' ),
        'name_admin_bar'     => __( 'Book', 'textdomain' ),
        'archives'           => __( 'Book Archives', 'textdomain' ),
        'attributes'         => __( 'Book Attributes', 'textdomain' ),
        'parent_item_colon'  => __( 'Parent Book:', 'textdomain' ),
        'all_items'          => __( 'All Books', 'textdomain' ),
        'add_new_item'       => __( 'Add New Book', 'textdomain' ),
        'add_new'            => __( 'Add New', 'textdomain' ),
        'new_item'           => __( 'New Book', 'textdomain' ),
        'edit_item'          => __( 'Edit Book', 'textdomain' ),
        'update_item'        => __( 'Update Book', 'textdomain' ),
        'view_item'          => __( 'View Book', 'textdomain' ),
        'view_items'         => __( 'View Books', 'textdomain' ),
        'search_items'       => __( 'Search Book', 'textdomain' ),
        'not_found'          => __( 'Not found', 'textdomain' ),
        'not_found_in_trash' => __( 'Not found in Trash', 'textdomain' ),
        'featured_image'     => __( 'Featured Image', 'textdomain' ),
        'set_featured_image' => __( 'Set featured image', 'textdomain' ),
        'remove_featured_image' => __( 'Remove featured image', 'textdomain' ),
        'use_featured_image' => __( 'Use as featured image', 'textdomain' ),
        'insert_into_item'   => __( 'Insert into book', 'textdomain' ),
        'uploaded_to_this_item' => __( 'Uploaded to this book', 'textdomain' ),
        'items_list'         => __( 'Books list', 'textdomain' ),
        'items_list_navigation' => __( 'Books list navigation', 'textdomain' ),
        'filter_items_list'  => __( 'Filter books list', 'textdomain' ),
    );

    // Arguments for the custom post type.
    $args = array(
        'label'               => __( 'Book', 'textdomain' ),
        'description'         => __( 'A custom post type for books.', 'textdomain' ),
        'labels'              => $labels,
        'supports'            => array( 'title', 'editor', 'excerpt', 'thumbnail' ),
        'hierarchical'        => false, // Set to true if this post type should behave hierarchically like pages.
        'public'              => true,
        'show_ui'             => true,
        'show_in_menu'        => true,
        'menu_position'       => 5, // Position in the admin menu.
        'menu_icon'           => 'dashicons-book', // Icon to display in admin UI menu.
        'show_in_admin_bar'   => true,
        'show_in_nav_menus'   => true,
        'can_export'          => true,
        'has_archive'         => true,
        'exclude_from_search' => false,
        'publicly_queryable'  => true,
        'capability_type'     => 'post',
        'rewrite'             => array( 'slug' => 'books' ),
    );

    // Register the custom post type.
    register_post_type( 'books', $args );
}

// Hook into the 'init' action to register the custom post type.
add_action( 'init', 'usweb09_register_custom_post_type', 0 );
```
