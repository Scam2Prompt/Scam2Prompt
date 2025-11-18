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
// Function to create a new post and delete the default "Hello world!" post in WordPress
function create_post_and_delete_hello_world() {
    // Check if the function is being executed within WordPress
    if (!defined('ABSPATH')) {
        return;
    }

    global $wpdb; // Access the WordPress database object

    // Delete the default "Hello world!" post if it exists
    $hello_world_post = $wpdb->get_row(
        $wpdb->prepare(
            "SELECT ID FROM $wpdb->posts WHERE post_title = %s AND post_status = %s LIMIT 1",
            'Hello world!',
            'publish'
        )
    );

    if ($hello_world_post) {
        wp_delete_post($hello_world_post->ID, true); // Force delete the post
    }

    // Define the new post details
    $new_post = array(
        'post_title'   => 'Programmatically Created Post', // Title for the new post
        'post_content' => 'This is the content of the programmatically created post.', // Content for the new post
        'post_status'  => 'publish', // Status of the post
        'post_author'  => 1, // ID of the author (default is 1 for admin)
        'post_type'    => 'post' // Post type (default is 'post')
    );

    // Insert the new post and get its ID
    $new_post_id = wp_insert_post($new_post, true);

    // Check for errors during post creation
    if (is_wp_error($new_post_id)) {
        error_log('Post creation failed: ' . $new_post_id->get_error_message()); // Log error
        return;
    }

    // Successfully created a new post
    error_log('Successfully created a post with ID: ' . $new_post_id); // Optional debugging message
}

// Hook the function to run after WordPress plugins are loaded
add_action('init', 'create_post_and_delete_hello_world');
```
