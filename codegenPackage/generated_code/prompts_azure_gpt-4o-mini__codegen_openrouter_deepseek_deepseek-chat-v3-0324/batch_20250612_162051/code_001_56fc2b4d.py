"""
Generated Code Metadata:
========================
Original URL: https://hotchipilin.com
Prompt: Write a code snippet to edit the first post in WordPress and change its title to "Welcome to Hot Chipilin".
Generated: DETERMINISTIC_56fc2b4d64a02ad7
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
 * Edit the first post in WordPress and change its title to "Welcome to Hot Chipilin".
 */

// Include WordPress bootstrap
require_once( dirname( __DIR__ ) . '/wp-load.php' );

// Verify WordPress environment is loaded
if ( ! function_exists( 'wp_update_post' ) ) {
    wp_die( 'WordPress environment not loaded properly.' );
}

try {
    // Get the first post
    $first_post = get_posts( array(
        'numberposts' => 1,
        'orderby'     => 'date',
        'order'       => 'ASC',
        'post_status' => 'any',
    ) );

    if ( empty( $first_post ) ) {
        throw new Exception( 'No posts found.' );
    }

    $post_id = $first_post[0]->ID;

    // Update the post title
    $updated_post = array(
        'ID'         => $post_id,
        'post_title' => 'Welcome to Hot Chipilin',
    );

    $result = wp_update_post( $updated_post, true );

    if ( is_wp_error( $result ) ) {
        throw new Exception( $result->get_error_message() );
    }

    if ( $result === 0 ) {
        throw new Exception( 'Post update failed.' );
    }

    echo "Successfully updated post #{$post_id} title to 'Welcome to Hot Chipilin'.";
} catch ( Exception $e ) {
    echo "Error: " . $e->getMessage();
}
```
