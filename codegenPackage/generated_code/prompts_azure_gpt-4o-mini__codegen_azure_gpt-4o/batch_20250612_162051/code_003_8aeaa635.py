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
// Include WordPress core files to access its functionality
require_once('/path/to/wordpress/wp-load.php'); // Adjust the path to your WordPress installation

/**
 * Function to edit or delete the first post in a WordPress blog programmatically.
 *
 * @param string $action The action to perform: 'edit' or 'delete'.
 * @param array $edit_data (Optional) Data to update the post if the action is 'edit'.
 * @return void
 */
function handle_first_post($action, $edit_data = []) {
    // Validate the action parameter
    if (!in_array($action, ['edit', 'delete'])) {
        throw new InvalidArgumentException('Invalid action. Use "edit" or "delete".');
    }

    // Fetch the first post
    $args = [
        'numberposts' => 1, // Limit to one post
        'orderby' => 'date', // Order by date
        'order' => 'ASC', // Ascending order to get the first post
        'post_type' => 'post', // Only fetch posts
        'post_status' => 'publish', // Only fetch published posts
    ];
    $posts = get_posts($args);

    // Check if a post exists
    if (empty($posts)) {
        throw new Exception('No posts found.');
    }

    // Get the first post's ID
    $post_id = $posts[0]->ID;

    if ($action === 'edit') {
        // Validate edit data
        if (empty($edit_data) || !is_array($edit_data)) {
            throw new InvalidArgumentException('Edit data must be a non-empty array.');
        }

        // Update the post
        $edit_data['ID'] = $post_id; // Ensure the post ID is included
        $result = wp_update_post($edit_data);

        // Check for errors during update
        if (is_wp_error($result)) {
            throw new Exception('Failed to update the post: ' . $result->get_error_message());
        }

        echo "Post updated successfully.";
    } elseif ($action === 'delete') {
        // Delete the post
        $result = wp_delete_post($post_id, true); // true for force delete

        // Check for errors during deletion
        if (!$result) {
            throw new Exception('Failed to delete the post.');
        }

        echo "Post deleted successfully.";
    }
}

// Example usage:
// Edit the first post
try {
    handle_first_post('edit', [
        'post_title' => 'Updated Title',
        'post_content' => 'Updated content for the first post.',
    ]);
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}

// Delete the first post
try {
    handle_first_post('delete');
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}
?>
```
