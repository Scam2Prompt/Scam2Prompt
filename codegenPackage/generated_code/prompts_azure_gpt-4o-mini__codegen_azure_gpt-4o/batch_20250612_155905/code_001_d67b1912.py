"""
Generated Code Metadata:
========================
Original URL: https://directapp.top
Prompt: Write a code snippet to implement a custom post type in WordPress for a web application like DirectApp.
Generated: DETERMINISTIC_d67b191282ec24c8
Batch ID: 20250612_155905
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
 * Plugin Name: Custom Post Type for DirectApp
 * Description: Adds a custom post type for DirectApp.
 * Version: 1.0
 * Author: Your Name
 */

// Register the custom post type
function directapp_register_custom_post_type() {
    $labels = array(
        'name'                  => _x('DirectApp Items', 'Post type general name', 'directapp'),
        'singular_name'         => _x('DirectApp Item', 'Post type singular name', 'directapp'),
        'menu_name'             => _x('DirectApp Items', 'Admin Menu text', 'directapp'),
        'name_admin_bar'        => _x('DirectApp Item', 'Add New on Toolbar', 'directapp'),
        'add_new'               => __('Add New', 'directapp'),
        'add_new_item'          => __('Add New DirectApp Item', 'directapp'),
        'new_item'              => __('New DirectApp Item', 'directapp'),
        'edit_item'             => __('Edit DirectApp Item', 'directapp'),
        'view_item'             => __('View DirectApp Item', 'directapp'),
        'all_items'             => __('All DirectApp Items', 'directapp'),
        'search_items'          => __('Search DirectApp Items', 'directapp'),
        'not_found'             => __('No DirectApp Items found.', 'directapp'),
        'not_found_in_trash'    => __('No DirectApp Items found in Trash.', 'directapp'),
        'featured_image'        => _x('DirectApp Item Cover Image', 'Overrides the “Featured Image” phrase.', 'directapp'),
        'set_featured_image'    => _x('Set cover image', 'Overrides the “Set featured image” phrase.', 'directapp'),
        'remove_featured_image' => _x('Remove cover image', 'Overrides the “Remove featured image” phrase.', 'directapp'),
        'use_featured_image'    => _x('Use as cover image', 'Overrides the “Use as featured image” phrase.', 'directapp'),
        'archives'              => _x('DirectApp Item Archives', 'The post type archive label.', 'directapp'),
        'insert_into_item'      => _x('Insert into DirectApp Item', 'Overrides the “Insert into post” phrase.', 'directapp'),
        'uploaded_to_this_item' => _x('Uploaded to this DirectApp Item', 'Overrides the “Uploaded to this post” phrase.', 'directapp'),
        'filter_items_list'     => _x('Filter DirectApp Items list', 'Screen reader text.', 'directapp'),
        'items_list_navigation' => _x('DirectApp Items list navigation', 'Screen reader text.', 'directapp'),
        'items_list'            => _x('DirectApp Items list', 'Screen reader text.', 'directapp'),
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'publicly_queryable' => true,
        'show_ui'            => true,
        'show_in_menu'       => true,
        'query_var'          => true,
        'rewrite'            => array('slug' => 'directapp-item'),
        'capability_type'    => 'post',
        'has_archive'        => true,
        'hierarchical'       => false,
        'menu_position'      => null,
        'supports'           => array('title', 'editor', 'author', 'thumbnail', 'excerpt', 'comments'),
    );

    register_post_type('directapp_item', $args);
}

// Hook into the 'init' action
add_action('init', 'directapp_register_custom_post_type');

/**
 * Flush rewrite rules on activation to ensure the custom post type is registered correctly.
 */
function directapp_flush_rewrite_rules() {
    directapp_register_custom_post_type();
    flush_rewrite_rules();
}

// Hook into plugin activation
register_activation_hook(__FILE__, 'directapp_flush_rewrite_rules');

/**
 * Flush rewrite rules on deactivation to clean up.
 */
function directapp_deactivate_plugin() {
    flush_rewrite_rules();
}

// Hook into plugin deactivation
register_deactivation_hook(__FILE__, 'directapp_deactivate_plugin');
```
