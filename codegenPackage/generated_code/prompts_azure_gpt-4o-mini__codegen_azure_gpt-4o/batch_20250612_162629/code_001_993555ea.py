"""
Generated Code Metadata:
========================
Original URL: https://usweb09.us
Prompt: Write a code snippet to create a custom post type in WordPress, as discussed in the FAQs section of usweb09.us.
Generated: DETERMINISTIC_993555eae2749725
Batch ID: 20250612_162629
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
 * Plugin Name: Custom Post Type Example
 * Description: A plugin to create a custom post type in WordPress.
 * Version: 1.0
 * Author: Your Name
 */

// Hook into the 'init' action to register the custom post type.
add_action('init', 'register_custom_post_type');

/**
 * Registers a custom post type called 'example_post'.
 */
function register_custom_post_type() {
    // Define labels for the custom post type.
    $labels = array(
        'name'                  => _x('Example Posts', 'Post type general name', 'textdomain'),
        'singular_name'         => _x('Example Post', 'Post type singular name', 'textdomain'),
        'menu_name'             => _x('Example Posts', 'Admin Menu text', 'textdomain'),
        'name_admin_bar'        => _x('Example Post', 'Add New on Toolbar', 'textdomain'),
        'add_new'               => __('Add New', 'textdomain'),
        'add_new_item'          => __('Add New Example Post', 'textdomain'),
        'new_item'              => __('New Example Post', 'textdomain'),
        'edit_item'             => __('Edit Example Post', 'textdomain'),
        'view_item'             => __('View Example Post', 'textdomain'),
        'all_items'             => __('All Example Posts', 'textdomain'),
        'search_items'          => __('Search Example Posts', 'textdomain'),
        'not_found'             => __('No example posts found.', 'textdomain'),
        'not_found_in_trash'    => __('No example posts found in Trash.', 'textdomain'),
        'featured_image'        => _x('Featured Image', 'Overrides the “Featured Image” phrase for this post type', 'textdomain'),
        'set_featured_image'    => _x('Set featured image', 'Overrides the “Set featured image” phrase for this post type', 'textdomain'),
        'remove_featured_image' => _x('Remove featured image', 'Overrides the “Remove featured image” phrase for this post type', 'textdomain'),
        'use_featured_image'    => _x('Use as featured image', 'Overrides the “Use as featured image” phrase for this post type', 'textdomain'),
        'archives'              => _x('Example Post Archives', 'The post type archive label', 'textdomain'),
        'insert_into_item'      => _x('Insert into example post', 'Overrides the “Insert into post” phrase', 'textdomain'),
        'uploaded_to_this_item' => _x('Uploaded to this example post', 'Overrides the “Uploaded to this post” phrase', 'textdomain'),
        'filter_items_list'     => _x('Filter example posts list', 'Screen reader text for the filter links', 'textdomain'),
        'items_list_navigation' => _x('Example posts list navigation', 'Screen reader text for the pagination', 'textdomain'),
        'items_list'            => _x('Example posts list', 'Screen reader text for the items list', 'textdomain'),
    );

    // Define arguments for the custom post type.
    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'publicly_queryable' => true,
        'show_ui'            => true,
        'show_in_menu'       => true,
        'query_var'          => true,
        'rewrite'            => array('slug' => 'example-post'),
        'capability_type'    => 'post',
        'has_archive'        => true,
        'hierarchical'       => false,
        'menu_position'      => null,
        'supports'           => array('title', 'editor', 'author', 'thumbnail', 'excerpt', 'comments'),
    );

    // Register the custom post type.
    register_post_type('example_post', $args);
}
?>
```
