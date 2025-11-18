"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mbandjock.fr
Prompt: Write a WordPress script to automatically delete the default "Hello World!" post and replace it with custom content for a site powered by MBANDJOCK.
Generated: DETERMINISTIC_a8f8c1be227a5ed9
Batch ID: 20250612_153224
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
 * Plugin Name: Replace Default Hello World Post
 * Description: Automatically deletes the default "Hello World!" post and replaces it with custom content for MBANDJOCK-powered sites.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Function to replace the default "Hello World!" post with custom content.
 */
function replace_hello_world_post() {
    global $wpdb;

    // Query for the "Hello World!" post based on its default title.
    $hello_world_post = $wpdb->get_row("SELECT ID FROM {$wpdb->posts} WHERE post_title = 'Hello World!' AND post_status = 'publish'");

    // If the post exists, delete it and create a custom post.
    if ($hello_world_post) {
        // Delete the "Hello World!" post.
        wp_delete_post($hello_world_post->ID, true);

        // Create new custom content post.
        $new_post = array(
            'post_title'    => 'Welcome to MBANDJOCK',
            'post_content'  => 'This is a custom post created to replace the default "Hello World!" post.',
            'post_status'   => 'publish',
            'post_author'   => 1, // Assuming admin user ID is 1. Update if necessary.
            'post_type'     => 'post'
        );

        // Insert the custom post into the database.
        wp_insert_post($new_post);
    }
}

// Hook to execute the function after theme setup.
add_action('after_setup_theme', 'replace_hello_world_post');
?>
```
