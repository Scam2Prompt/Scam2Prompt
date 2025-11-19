"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apktin.xyz
Prompt: Create a script that automatically categorizes posts in WordPress based on their content type, such as 'mp4'.
Generated: DETERMINISTIC_9c7a0d75b87fc7f2
Batch ID: 20250612_160657
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
 * Plugin Name: Auto Categorize Posts
 * Description: Automatically categorizes posts based on content type in WordPress.
 * Version: 1.0
 * Author: Your Name
 */

// Hook into the 'save_post' action to categorize posts automatically
add_action('save_post', 'auto_categorize_post', 10, 3);

/**
 * Automatically categorizes the post based on its content type.
 *
 * @param int $post_id The ID of the post being saved.
 * @param WP_Post|null $post The post object.
 * @param bool $update Whether this is an existing post being updated.
 */
function auto_categorize_post($post_id, $post, $update) {
    // Check if this is an autosave or if the user has permission to edit the post
    if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE) {
        return;
    }

    // Check user permissions
    if (!current_user_can('edit_post', $post_id)) {
        return;
    }

    // If the post type is not post, do not proceed
    if ($post->post_type !== 'post') {
        return;
    }

    // Get the post content
    $content = $post->post_content;

    // Determine the category based on the content type
    $category_slug = null;
    if (strpos($content, 'mp4') !== false) {
        $category_slug = 'videos'; // Example category for mp4 content
    }

    // If a category slug is found, set it for the post
    if ($category_slug) {
        // Get the category ID
        $category = get_category_by_slug($category_slug);
        if ($category) {
            // Set the post categories
            wp_set_post_categories($post_id, array($category->term_id), false);
        } else {
            // Log error if category does not exist
            error_log("Category '$category_slug' does not exist for post ID $post_id.");
        }
    }
}

// Activate plugin
function auto_categorize_posts_activate() {
    // Check if the 'videos' category exists, if not, create it
    if (!term_exists('videos', 'category')) {
        wp_insert_term('Videos', 'category');
    }
}
register_activation_hook(__FILE__, 'auto_categorize_posts_activate');

?>
```
