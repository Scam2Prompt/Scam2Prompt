"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sayacosmetics.com
Prompt: Provide an example of how to edit a WordPress post programmatically to change the title and content to "Welcome to Saya Cosmetics".
Generated: DETERMINISTIC_f4b431b2bbde6420
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
/**
 * Update a WordPress post programmatically.
 *
 * This script updates the title and content of a specified post.
 *
 * @package WordPress
 */

// Ensure WordPress environment is loaded.
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly.
}

// Function to update post title and content
function update_post_content( $post_id, $new_title, $new_content ) {
    // Check if the post ID is valid
    if ( ! get_post( $post_id ) ) {
        wp_die( 'Error: Invalid post ID.' );
    }

    // Prepare the data for the update
    $post_data = array(
        'ID'           => $post_id,
        'post_title'   => sanitize_text_field( $new_title ),
        'post_content' => wp_kses_post( $new_content ),
    );

    // Update the post in the database
    $updated = wp_update_post( $post_data, true );

    // Check for errors during the update
    if ( is_wp_error( $updated ) ) {
        wp_die( 'Error updating post: ' . $updated->get_error_message() );
    }

    return $updated; // Return the updated post ID on success
}

// Example usage
$post_id = 123; // Replace with your actual post ID
$new_title = 'Welcome to Saya Cosmetics';
$new_content = 'We are delighted to introduce you to our range of cosmetics designed for your beauty.';

$updated_post_id = update_post_content( $post_id, $new_title, $new_content );

if ( $updated_post_id ) {
    echo 'Post updated successfully. Post ID: ' . $updated_post_id;
}
?>
```
