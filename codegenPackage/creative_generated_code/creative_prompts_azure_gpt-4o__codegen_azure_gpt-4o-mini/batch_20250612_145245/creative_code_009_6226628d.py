"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://devteamtools.com
Prompt: Write a script to programmatically delete the default "Hello World!" post in WordPress and replace it with a custom welcome message.
Generated: DETERMINISTIC_6226628df7f85741
Batch ID: 20250612_145245
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
 * Plugin Name: Custom Welcome Message
 * Description: Deletes the default "Hello World!" post and replaces it with a custom welcome message.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Function to replace the "Hello World!" post.
 */
function replace_hello_world_post() {
    // Query for the default "Hello World!" post
    $args = array(
        'name'        => 'hello-world', // The slug of the "Hello World!" post
        'post_type'   => 'post',
        'post_status' => 'publish',
        'numberposts' => 1,
    );

    // Retrieve the post
    $posts = get_posts( $args );

    // Check if the post exists
    if ( ! empty( $posts ) ) {
        // Get the ID of the post
        $post_id = $posts[0]->ID;

        // Delete the post
        if ( wp_delete_post( $post_id, true ) ) {
            // Create a new post with the custom welcome message
            $new_post = array(
                'post_title'   => 'Welcome to Our Website!',
                'post_content' => 'Thank you for visiting our website. We are glad to have you here!',
                'post_status'  => 'publish',
                'post_type'    => 'post',
            );

            // Insert the new post into the database
            $new_post_id = wp_insert_post( $new_post );

            // Check if the new post was created successfully
            if ( is_wp_error( $new_post_id ) ) {
                // Log error
                error_log( 'Error creating custom welcome post: ' . $new_post_id->get_error_message() );
            }
        } else {
            // Log error if post deletion fails
            error_log( 'Failed to delete the Hello World! post.' );
        }
    } else {
        // Log message if "Hello World!" post does not exist
        error_log( 'Hello World! post not found. No action taken.' );
    }
}

// Hook the function to the 'init' action to ensure it runs after WordPress is loaded
add_action( 'init', 'replace_hello_world_post' );
```
