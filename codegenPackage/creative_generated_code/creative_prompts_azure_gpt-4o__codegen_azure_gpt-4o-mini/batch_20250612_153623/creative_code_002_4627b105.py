"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upconteudo.digital
Prompt: Provide a WordPress function to programmatically create a new post and delete the default "Hello world!" post.
Generated: DETERMINISTIC_4627b105b8d1fb1a
Batch ID: 20250612_153623
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
 * Function to create a new post and delete the default "Hello World!" post in WordPress.
 *
 * @param string $title The title of the new post.
 * @param string $content The content of the new post.
 * @param string $status The status of the new post (e.g., 'publish', 'draft').
 * @return int|WP_Error The ID of the newly created post on success, or WP_Error on failure.
 */
function create_and_delete_post($title, $content, $status = 'publish') {
    // Ensure the WordPress environment is loaded
    if (!function_exists('wp_insert_post')) {
        return new WP_Error('function_not_found', 'WordPress function wp_insert_post not found.');
    }

    // Create the new post
    $new_post_data = array(
        'post_title'   => sanitize_text_field($title),
        'post_content' => wp_kses_post($content),
        'post_status'  => sanitize_key($status),
        'post_author'  => get_current_user_id(),
        'post_type'    => 'post',
    );

    // Insert the post into the database
    $new_post_id = wp_insert_post($new_post_data);

    // Check for errors during post creation
    if (is_wp_error($new_post_id)) {
        return $new_post_id; // Return the error
    }

    // Delete the default "Hello World!" post if it exists
    $hello_world_post_id = get_page_by_title('Hello World!', OBJECT, 'post');

    if ($hello_world_post_id) {
        // Attempt to delete the post
        $deleted = wp_delete_post($hello_world_post_id->ID, true); // Force delete

        // Check if the deletion was successful
        if (!$deleted) {
            return new WP_Error('delete_failed', 'Failed to delete the default "Hello World!" post.');
        }
    }

    // Return the ID of the newly created post
    return $new_post_id;
}

// Example usage (uncomment to use)
// $result = create_and_delete_post('A New Post Title', 'This is the content of the new post.');
// if (is_wp_error($result)) {
//     echo 'Error: ' . $result->get_error_message();
// } else {
//     echo 'New post created with ID: ' . $result;
// }
?>
```
