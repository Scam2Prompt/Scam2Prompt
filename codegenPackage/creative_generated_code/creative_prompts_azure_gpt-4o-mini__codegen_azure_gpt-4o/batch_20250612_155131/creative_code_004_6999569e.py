"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sayacosmetics.com
Prompt: What are the steps to delete a default WordPress post and replace it with a custom message using the PopularFX theme?
Generated: DETERMINISTIC_6999569e4d98ef6a
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Functions.php file in your WordPress theme (PopularFX)

// Hook into 'init' action to check for and delete the default WordPress post and replace it with a custom message.
add_action('init', 'replace_default_post_with_custom_message');

/**
 * Function to delete the default WordPress post and replace it with a custom message.
 */
function replace_default_post_with_custom_message() {
    // Retrieve the default post (usually ID = 1)
    $default_post_id = 1;

    // Check if the post exists
    if (get_post_status($default_post_id)) {
        // Delete the default post
        $delete_result = wp_delete_post($default_post_id, true); // Force delete permanently
        if (!$delete_result) {
            error_log('Failed to delete the default WordPress post.');
        } else {
            // Create a new custom post
            $new_post_args = array(
                'post_title'    => 'Welcome to PopularFX Theme!',
                'post_content'  => 'This is a custom message replacing the default WordPress post.',
                'post_status'   => 'publish',
                'post_author'   => 1, // Default admin user
                'post_type'     => 'post',
            );

            $new_post_id = wp_insert_post($new_post_args);

            if (is_wp_error($new_post_id)) {
                error_log('Failed to create custom post: ' . $new_post_id->get_error_message());
            }
        }
    }
}
```

This code is ready to be added to your theme's `functions.php` file. It checks for the existence of the default WordPress post (ID = 1), deletes it if found, and replaces it with a custom post containing a message. Error handling is included via `error_log` for troubleshooting.
