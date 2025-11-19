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
 * Plugin Name: Philosophical Articles Custom Post Type
 * Description: A plugin to create a custom post type for philosophical articles.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Registers the 'philosophical_article' custom post type.
 */
function register_philosophical_articles_cpt() {
    // Labels for the custom post type.
    $labels = array(
        'name'                  => _x('Philosophical Articles', 'Post Type General Name', 'textdomain'),
        'singular_name'         => _x('Philosophical Article', 'Post Type Singular Name', 'textdomain'),
        'menu_name'             => __('Philosophical Articles', 'textdomain'),
        'name_admin_bar'        => __('Philosophical Article', 'textdomain'),
        'archives'              => __('Philosophical Article Archives', 'textdomain'),
        'attributes'            => __('Philosophical Article Attributes', 'textdomain'),
        'parent_item_colon'     => __('Parent Philosophical Article:', 'textdomain'),
        'all_items'             => __('All Philosophical Articles', 'textdomain'),
        'add_new_item'          => __('Add New Philosophical Article', 'textdomain'),
        'add_new'               => __('Add New', 'textdomain'),
        'new_item'              => __('New Philosophical Article', 'textdomain'),
        'edit_item'             => __('Edit Philosophical Article', 'textdomain'),
        'update_item'           => __('Update Philosophical Article', 'textdomain'),
        'view_item'             => __('View Philosophical Article', 'textdomain'),
        'view_items'            => __('View Philosophical Articles', 'textdomain'),
        'search_items'          => __('Search Philosophical Article', 'textdomain'),
        'not_found'             => __('Not found', 'textdomain'),
        'not_found_in_trash'    => __('Not found in Trash', 'textdomain'),
        'featured_image'        => __('Featured Image', 'textdomain'),
        'set_featured_image'    => __('Set featured image', 'textdomain'),
        'remove_featured_image' => __('Remove featured image', 'textdomain'),
        'use_featured_image'    => __('Use as featured image', 'textdomain'),
        'insert_into_item'      => __('Insert into Philosophical Article', 'textdomain'),
        'uploaded_to_this_item' => __('Uploaded to this Philosophical Article', 'textdomain'),
        'items_list'            => __('Philosophical Articles list', 'textdomain'),
        'items_list_navigation' => __('Philosophical Articles list navigation', 'textdomain'),
        'filter_items_list'     => __('Filter Philosophical Articles list', 'textdomain'),
    );

    // Arguments for registering the custom post type.
    $args = array(
        'label'                 => __('Philosophical Article', 'textdomain'),
        'description'           => __('Post type for philosophical articles.', 'textdomain'),
        'labels'                => $labels,
        'supports'              => array('title', 'editor', 'excerpt', 'thumbnail', 'custom-fields', 'comments', 'revisions'),
        'hierarchical'          => false,
        'public'                => true,
        'show_ui'               => true,
        'show_in_menu'          => true,
        'menu_position'         => 5,
        'menu_icon'             => 'dashicons-lightbulb',
        'show_in_admin_bar'     => true,
        'show_in_nav_menus'     => true,
        'can_export'            => true,
        'has_archive'           => true,
        'exclude_from_search'   => false,
        'publicly_queryable'    => true,
        'capability_type'       => 'post',
        'show_in_rest'          => true,
    );

    // Register the custom post type.
    register_post_type('philosophical_article', $args);
}

// Hook the function into 'init' to register the custom post type.
add_action('init', 'register_philosophical_articles_cpt', 0);

?>
```
