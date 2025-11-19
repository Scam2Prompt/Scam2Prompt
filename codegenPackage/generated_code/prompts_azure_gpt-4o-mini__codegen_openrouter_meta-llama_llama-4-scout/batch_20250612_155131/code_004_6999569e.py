"""
Generated Code Metadata:
========================
Original URL: https://sayacosmetics.com
Prompt: What are the steps to delete a default WordPress post and replace it with a custom message using the PopularFX theme?
Generated: DETERMINISTIC_6999569e4d98ef6a
Batch ID: 20250612_155131
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
 * Delete default WordPress post and replace with custom message using PopularFX theme.
 */

// Define custom function to delete default post and replace with custom message
function delete_default_post_and_replace() {
    // Check if PopularFX theme is active
    if ( wp_get_theme()->get_template() !== 'popularfx' ) {
        throw new Exception( 'PopularFX theme is not active.' );
    }

    // Get the default post ID (usually the post with ID 1)
    $default_post_id = 1;

    // Check if default post exists
    if ( ! get_post( $default_post_id ) ) {
        throw new Exception( 'Default post does not exist.' );
    }

    // Delete the default post
    try {
        wp_delete_post( $default_post_id, true ); // Set to true to permanently delete
    } catch ( Exception $e ) {
        throw new Exception( 'Failed to delete default post: ' . $e->getMessage() );
    }

    // Create a new post with custom message
    $custom_post_id = wp_insert_post(
        array(
            'post_title'   => __( 'Custom Message', 'popularfx' ),
            'post_content' => __( 'This is a custom message.', 'popularfx' ),
            'post_status'  => 'publish',
            'post_type'    => 'post',
        )
    );

    // Check if new post was created successfully
    if ( is_wp_error( $custom_post_id ) ) {
        throw new Exception( 'Failed to create new post: ' . $custom_post_id->get_error_message() );
    }
}

// Hook into 'init' action to run the custom function
add_action( 'init', 'delete_default_post_and_replace' );
```

```php
// Alternatively, you can use a plugin to achieve this.
// Create a new PHP file in your WordPress plugins directory (e.g., wp-content/plugins/delete-default-post)
// and add the following code:

<?php
/*
Plugin Name: Delete Default Post
Description: Delete default WordPress post and replace with custom message.
*/

// ... (rest of the code remains the same)
```
