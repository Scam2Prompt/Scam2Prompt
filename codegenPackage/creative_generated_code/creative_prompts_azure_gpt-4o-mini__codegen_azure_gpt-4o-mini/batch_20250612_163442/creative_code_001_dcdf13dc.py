"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vebtec.com
Prompt: How can I create a custom post type in WordPress for philosophical articles similar to those on Vebtec?
Generated: DETERMINISTIC_dcdf13dc8a456992
Batch ID: 20250612_163442
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
 * Plugin Name: Custom Post Type for Philosophical Articles
 * Description: A custom post type for philosophical articles similar to those on Vebtec.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Registers the custom post type 'philosophical_article'.
 */
function register_philosophical_article_cpt() {
    $labels = array(
        'name'                  => _x( 'Philosophical Articles', 'Post type general name', 'textdomain' ),
        'singular_name'         => _x( 'Philosophical Article', 'Post type singular name', 'textdomain' ),
        'menu_name'             => _x( 'Philosophical Articles', 'Admin Menu text', 'textdomain' ),
        'name_admin_bar'        => _x( 'Philosophical Article', 'Add New on Toolbar', 'textdomain' ),
        'add_new'               => __( 'Add New', 'textdomain' ),
        'add_new_item'          => __( 'Add New Philosophical Article', 'textdomain' ),
        'new_item'              => __( 'New Philosophical Article', 'textdomain' ),
        'edit_item'             => __( 'Edit Philosophical Article', 'textdomain' ),
        'view_item'             => __( 'View Philosophical Article', 'textdomain' ),
        'all_items'             => __( 'All Philosophical Articles', 'textdomain' ),
        'search_items'          => __( 'Search Philosophical Articles', 'textdomain' ),
        'parent_item_colon'     => __( 'Parent Philosophical Articles:', 'textdomain' ),
        'not_found'             => __( 'No philosophical articles found.', 'textdomain' ),
        'not_found_in_trash'    => __( 'No philosophical articles found in Trash.', 'textdomain' ),
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'publicly_queryable' => true,
        'show_ui'            => true,
        'show_in_menu'       => true,
        'query_var'          => true,
        'rewrite'            => array( 'slug' => 'philosophical-article' ),
        'capability_type'    => 'post',
        'has_archive'        => true,
        'hierarchical'       => false,
        'menu_position'      => null,
        'supports'           => array( 'title', 'editor', 'thumbnail' ),
        'show_in_rest'       => true, // Enable Gutenberg editor
    );

    // Register the custom post type
    register_post_type( 'philosophical_article', $args );
}

// Hook the custom post type registration to the 'init' action
add_action( 'init', 'register_philosophical_article_cpt' );

?>
```
