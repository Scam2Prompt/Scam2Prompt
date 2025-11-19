"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mbandjock.fr
Prompt: Write a PHP code snippet to edit or delete the default WordPress post titled "Hello world!" as mentioned on mbandjock.fr.
Generated: DETERMINISTIC_ff8992314efd15e3
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
/**
 * Edit or delete the default WordPress post titled "Hello world!".
 *
 * This script checks for the existence of the post and either updates its content
 * or deletes it based on the specified action.
 */

// Load WordPress environment
require_once('wp-load.php');

// Set the post title to search for
$post_title = 'Hello world!';

// Fetch the post by title
$post = get_page_by_title($post_title, OBJECT, 'post');

// Check if the post exists
if ($post) {
    // Action to perform: 'edit' to update the post, 'delete' to remove it
    $action = 'edit'; // Change to 'delete' to remove the post

    if ($action === 'edit') {
        // Prepare new post data
        $post_data = array(
            'ID'           => $post->ID,
            'post_content' => 'This is the updated content of the Hello World post.',
            'post_title'   => 'Hello World! (Updated)',
        );

        // Update the post into the database
        $updated_post_id = wp_update_post($post_data);

        // Check for errors in post update
        if (is_wp_error($updated_post_id)) {
            echo 'Error updating post: ' . $updated_post_id->get_error_message();
        } else {
            echo 'Post updated successfully with ID: ' . $updated_post_id;
        }
    } elseif ($action === 'delete') {
        // Deleting the post
        $deleted = wp_delete_post($post->ID, true); // true for force deletion

        // Check for errors in post deletion
        if (is_wp_error($deleted)) {
            echo 'Error deleting post: ' . $deleted->get_error_message();
        } else {
            echo 'Post deleted successfully.';
        }
    } else {
        echo 'Invalid action specified.';
    }
} else {
    echo 'Post titled "Hello world!" not found.';
}
?>
```
