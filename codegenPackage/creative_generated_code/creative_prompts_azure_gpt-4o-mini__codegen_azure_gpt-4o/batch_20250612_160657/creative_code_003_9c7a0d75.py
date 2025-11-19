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
 * Plugin Name: Auto Categorize Posts by Content Type
 * Description: Automatically categorizes posts based on their content type. For example, posts containing 'mp4' files will be categorized under 'Videos'.
 * Version: 1.0
 * Author: Expert Programmer
 * License: GPLv2 or later
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Hook into the WordPress 'save_post' action to automatically assign categories based on content type.
 *
 * @param int $post_id The ID of the post being saved.
 */
function auto_categorize_posts_by_content_type($post_id) {
    // Verify if this is an autosave. If so, do nothing.
    if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE) {
        return;
    }

    // Verify the post type is 'post', as we only want to categorize posts.
    $post_type = get_post_type($post_id);
    if ($post_type !== 'post') {
        return;
    }

    // Get the post content.
    $post_content = get_post_field('post_content', $post_id);

    // Define content type keywords and their associated category names.
    $content_type_categories = array(
        'mp4' => 'Videos',
        'jpg' => 'Images',
        'png' => 'Images',
        'gif' => 'Images',
        'pdf' => 'Documents',
        'doc' => 'Documents',
        'docx' => 'Documents',
        'zip' => 'Archives',
    );

    // Initialize an array to hold categories to be assigned.
    $categories_to_assign = array();

    // Loop through the content type keywords.
    foreach ($content_type_categories as $keyword => $category_name) {
        // Check if the keyword exists in the post content.
        if (stripos($post_content, $keyword) !== false) {
            // Get the category ID by name, creating it if it doesn't exist.
            $category_id = get_category_by_slug(sanitize_title($category_name));
            if (!$category_id) {
                $new_category = wp_insert_term($category_name, 'category');
                if (!is_wp_error($new_category)) {
                    $category_id = $new_category['term_id'];
                }
            } else {
                $category_id = $category_id->term_id;
            }

            // Add the category ID to the list of categories to assign.
            if ($category_id) {
                $categories_to_assign[] = (int) $category_id;
            }
        }
    }

    // Assign the categories to the post if any were found.
    if (!empty($categories_to_assign)) {
        wp_set_post_categories($post_id, $categories_to_assign, true);
    }
}

// Add the action to hook into post saving.
add_action('save_post', 'auto_categorize_posts_by_content_type');
```
