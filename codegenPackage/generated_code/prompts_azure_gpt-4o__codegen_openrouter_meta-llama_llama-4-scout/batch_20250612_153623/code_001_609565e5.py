"""
Generated Code Metadata:
========================
Original URL: https://upconteudo.digital
Prompt: Generate PHP code to edit the default "Hello world!" post in WordPress and replace its content with a custom message.
Generated: DETERMINISTIC_609565e514b7ff02
Batch ID: 20250612_153623
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
 * Edit the default "Hello world!" post in WordPress and replace its content with a custom message.
 */

// Check if the current user has the capability to edit posts
function has_edit_posts_capability() {
    return current_user_can( 'edit_posts' );
}

// Get the ID of the default "Hello world!" post
function get_hello_world_post_id() {
    $hello_world_post = get_page_by_title( 'Hello world!', OBJECT, 'post' );
    return $hello_world_post->ID;
}

// Update the content of the default "Hello world!" post
function update_hello_world_post( $post_id, $new_content ) {
    $post = array(
        'ID'           => $post_id,
        'post_content' => $new_content,
    );
    wp_update_post( $post );
}

// Main function to edit the default "Hello world!" post
function edit_hello_world_post( $new_message ) {
    if ( ! has_edit_posts_capability() ) {
        throw new Exception( 'You do not have the capability to edit posts.' );
    }

    $post_id = get_hello_world_post_id();
    if ( ! $post_id ) {
        throw new Exception( 'The default "Hello world!" post was not found.' );
    }

    update_hello_world_post( $post_id, $new_message );
}

// Example usage
try {
    $new_message = 'Welcome to our custom WordPress site!';
    edit_hello_world_post( $new_message );
    echo "The default 'Hello world!' post has been updated with the message: $new_message";
} catch ( Exception $e ) {
    echo 'Error: ' . $e->getMessage();
}
```
