"""
Generated Code Metadata:
========================
Original URL: https://koraymetal.com
Prompt: Develop a code snippet to edit or delete the first post in a WordPress blog programmatically.
Generated: DETERMINISTIC_8aeaa63573886fb9
Batch ID: 20250612_162051
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
 * Edit or delete the first post in a WordPress blog programmatically.
 */

// Check if WordPress is loaded
if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

// Include WordPress functions
require_once dirname(__FILE__) . '/wp-load.php';

// Check if user is an administrator
if (!current_user_can('manage_options')) {
    wp_die(__('You do not have permission to edit or delete posts.', 'text_domain'));
}

// Get the first post
function get_first_post() {
    $args = array(
        'posts_per_page' => 1,
        'orderby' => 'date',
        'order' => 'ASC'
    );
    $query = new WP_Query($args);
    if ($query->have_posts()) {
        $query->the_post();
        return get_the_ID();
    } else {
        return null;
    }
}

// Edit the first post
function edit_first_post($post_id, $new_title, $new_content) {
    try {
        // Validate input
        if (empty($post_id) || empty($new_title) || empty($new_content)) {
            throw new Exception(__('Invalid input.', 'text_domain'));
        }

        // Update post
        $post = array(
            'ID' => $post_id,
            'post_title' => $new_title,
            'post_content' => $new_content,
        );
        wp_update_post($post);
        return true;
    } catch (Exception $e) {
        wp_die(__('Error editing post: ', 'text_domain') . $e->getMessage());
    }
}

// Delete the first post
function delete_first_post($post_id) {
    try {
        // Validate input
        if (empty($post_id)) {
            throw new Exception(__('Invalid post ID.', 'text_domain'));
        }

        // Delete post
        wp_delete_post($post_id, true); // Set to false for soft delete
        return true;
    } catch (Exception $e) {
        wp_die(__('Error deleting post: ', 'text_domain') . $e->getMessage());
    }
}

// Main function
function main() {
    $post_id = get_first_post();

    if ($post_id !== null) {
        // Edit post example
        $new_title = 'New Title';
        $new_content = 'New content';
        edit_first_post($post_id, $new_title, $new_content);

        // Delete post example
        // delete_first_post($post_id);
    } else {
        wp_die(__('No posts found.', 'text_domain'));
    }
}

main();

```
