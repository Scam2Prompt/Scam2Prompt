"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koraymetal.com
Prompt: Develop a code snippet to edit or delete the first post in a WordPress blog programmatically.
Generated: DETERMINISTIC_8aeaa63573886fb9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// WordPress script to edit or delete the first post programmatically

// Include WordPress core functions
require_once('/path/to/wp-load.php'); // Update with the actual path to wp-load.php

// Function to edit the first post
function edit_first_post($new_title, $new_content) {
    global $wpdb;

    try {
        // Get the first post (ordered by ID)
        $first_post = $wpdb->get_row("SELECT * FROM $wpdb->posts WHERE post_type = 'post' AND post_status = 'publish' ORDER BY ID ASC LIMIT 1");

        if ($first_post) {
            // Update post data
            $updated_post = array(
                'ID'           => $first_post->ID,
                'post_title'   => $new_title,
                'post_content' => $new_content,
            );

            wp_update_post($updated_post);
            echo "Post updated successfully.";
        } else {
            echo "No posts found to edit.";
        }
    } catch (Exception $e) {
        // Handle any errors that occur
        error_log('Error editing post: ' . $e->getMessage());
        echo "An error occurred while editing the post.";
    }
}

// Function to delete the first post
function delete_first_post() {
    global $wpdb;

    try {
        // Get the first post (ordered by ID)
        $first_post = $wpdb->get_row("SELECT * FROM $wpdb->posts WHERE post_type = 'post' AND post_status = 'publish' ORDER BY ID ASC LIMIT 1");

        if ($first_post) {
            // Delete the post
            wp_delete_post($first_post->ID, true); // Pass true to force deletion
            echo "Post deleted successfully.";
        } else {
            echo "No posts found to delete.";
        }
    } catch (Exception $e) {
        // Handle any errors that occur
        error_log('Error deleting post: ' . $e->getMessage());
        echo "An error occurred while deleting the post.";
    }
}

// Example usage
// Uncomment one of the following lines to test the functionality:

// edit_first_post('Updated Title', 'This is the updated content of the first post.');
// delete_first_post();
?>
```
