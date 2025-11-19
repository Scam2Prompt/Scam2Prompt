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
 * Description: A simple plugin to create a custom post type for 'Books'.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Registers a custom post type called 'Books'.
 */
function cpt_books_init() {
    // Set up the labels for the custom post type
    $labels = array(
        'name'               => _x( 'Books', 'post type general name', 'your-text-domain' ),
        'singular_name'      => _x( 'Book', 'post type singular name', 'your-text-domain' ),
        'menu_name'          => _x( 'Books', 'admin menu', 'your-text-domain' ),
        'name_admin_bar'     => _x( 'Book', 'add new on admin bar', 'your-text-domain' ),
        'add_new'            => _x( 'Add New', 'book', 'your-text-domain' ),
        'add_new_item'       => __( 'Add New Book', 'your-text-domain' ),
        'new_item'           => __( 'New Book', 'your-text-domain' ),
        'edit_item'          => __( 'Edit Book', 'your-text-domain' ),
        'view_item'          => __( 'View Book', 'your-text-domain' ),
        'all_items'          => __( 'All Books', 'your-text-domain' ),
        'search_items'       => __( 'Search Books', 'your-text-domain' ),
        'parent_item_colon'  => __( 'Parent Books:', 'your-text-domain' ),
        'not_found'          => __( 'No books found.', 'your-text-domain' ),
        'not_found_in_trash' => __( 'No books found in Trash.', 'your-text-domain' )
    );

    // Set up the arguments for the custom post type
    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'publicly_queryable' => true,
        'show_ui'            => true,
        'show_in_menu'       => true,
        'query_var'          => true,
        'rewrite'            => array( 'slug' => 'book' ),
        'capability_type'    => 'post',
        'has_archive'        => true,
        'hierarchical'       => false,
        'menu_position'      => null,
        'supports'           => array( 'title', 'editor', 'author', 'thumbnail', 'excerpt', 'comments' )
    );

    // Register the custom post type
    register_post_type( 'book', $args );
}

// Hook the function to the 'init' action
add_action( 'init', 'cpt_books_init' );

/**
 * Flush rewrite rules on activation.
 */
function cpt_books_activation() {
    cpt_books_init(); // Call the function to register the post type
    flush_rewrite_rules(); // Flush rewrite rules for the new post type
}

// Hook for plugin activation
register_activation_hook( __FILE__, 'cpt_books_activation' );

/**
 * Flush rewrite rules on deactivation.
 */
function cpt_books_deactivation() {
    flush_rewrite_rules(); // Flush rewrite rules
}

// Hook for plugin deactivation
register_deactivation_hook( __FILE__, 'cpt_books_deactivation' );
```
