"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sabrinacarpentermerch.com
Prompt: Write a WordPress function to edit or delete the first blog post programmatically, as suggested in the sample page instructions.
Generated: DETERMINISTIC_d0b703dad7e67c73
Batch ID: 20250612_152416
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
 * Edit or delete the first blog post programmatically in WordPress.
 *
 * This function checks for the existence of the first blog post and either
 * updates its content or deletes it based on the specified action parameter.
 *
 * @param string $action The action to perform: 'edit' or 'delete'.
 * @param array|null $new_data Optional. An associative array of new data to update the post.
 *                             Must include 'post_title' and 'post_content' for the 'edit' action.
 * @throws Exception If the action is invalid or if the post cannot be found.
 */
function edit_or_delete_first_blog_post($action, $new_data = null) {
    // Validate action parameter
    if (!in_array($action, ['edit', 'delete'])) {
        throw new Exception('Invalid action. Use "edit" or "delete".');
    }

    // Retrieve the first blog post
    $args = [
        'numberposts' => 1,
        'orderby'     => 'date',
        'order'       => 'ASC',
    ];
    $first_post = wp_get_recent_posts($args, OBJECT);

    // Check if the first post exists
    if (empty($first_post)) {
        throw new Exception('No blog posts found.');
    }

    // Get the ID of the first post
    $post_id = $first_post[0]->ID;

    // Perform the specified action
    if ($action === 'edit') {
        // Validate new data
        if (is_null($new_data) || !isset($new_data['post_title'], $new_data['post_content'])) {
            throw new Exception('New data must include "post_title" and "post_content".');
        }
        
        // Prepare post data for update
        $post_data = [
            'ID'           => $post_id,
            'post_title'   => sanitize_text_field($new_data['post_title']),
            'post_content' => wp_kses_post($new_data['post_content']),
        ];

        // Update the post
        $updated_post_id = wp_update_post($post_data, true);

        // Check for errors in post update
        if (is_wp_error($updated_post_id)) {
            throw new Exception('Error updating post: ' . $updated_post_id->get_error_message());
        }

        return "Post updated successfully with ID: $updated_post_id.";
        
    } elseif ($action === 'delete') {
        // Delete the post
        $deleted = wp_delete_post($post_id, true);

        // Check if the post was deleted successfully
        if (null === $deleted) {
            throw new Exception('Error deleting post.');
        }

        return "Post deleted successfully.";
    }
}

// Example usage:
// Uncomment the lines below to test the function
// try {
//     $response = edit_or_delete_first_blog_post('edit', ['post_title' => 'Updated Title', 'post_content' => 'Updated content goes here.']);
//     echo $response;
// } catch (Exception $e) {
//     echo 'Error: ' . $e->getMessage();
// }
?>
```
