"""
Generated Code Metadata:
========================
Original URL: https://mbandjock.fr
Prompt: Write a PHP code snippet to edit or delete the default WordPress post titled "Hello world!" as mentioned on mbandjock.fr.
Generated: DETERMINISTIC_ff8992314efd15e3
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
 * Edit or delete the default WordPress post titled "Hello world!"
 */

// Ensure WordPress environment is loaded
if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Function to edit or delete the default "Hello world!" post
 *
 * @param string $action The action to perform: 'edit' or 'delete'
 * @param array  $new_data Optional array of post data for editing
 * @return bool|WP_Error True on success, WP_Error on failure
 */
function handle_default_post($action = 'edit', $new_data = array()) {
    // Get the default "Hello world!" post
    $default_post = get_posts(array(
        'title'        => 'Hello world!',
        'post_status'  => 'all',
        'numberposts' => 1
    ));

    if (empty($default_post)) {
        return new WP_Error('post_not_found', 'Default "Hello world!" post not found.');
    }

    $post = $default_post[0];

    switch ($action) {
        case 'edit':
            // Merge default data with new data
            $post_data = wp_parse_args($new_data, array(
                'ID'           => $post->ID,
                'post_title'   => $post->post_title,
                'post_content' => $post->post_content,
                'post_status'  => $post->post_status
            ));

            // Update the post
            $result = wp_update_post($post_data, true);
            break;

        case 'delete':
            // Delete the post (bypass trash)
            $result = wp_delete_post($post->ID, true);
            break;

        default:
            return new WP_Error('invalid_action', 'Invalid action specified.');
    }

    if (is_wp_error($result)) {
        return $result;
    }

    return true;
}

// Example usage:
// To edit the post:
// handle_default_post('edit', array('post_title' => 'New Title', 'post_content' => 'New content'));

// To delete the post:
// handle_default_post('delete');
```
