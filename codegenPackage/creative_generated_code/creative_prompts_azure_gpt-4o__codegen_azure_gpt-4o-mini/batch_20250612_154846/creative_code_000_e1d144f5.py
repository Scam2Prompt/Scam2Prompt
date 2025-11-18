"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://offerspecials.online
Prompt: Write a WordPress plugin that automatically replaces the default "Hello world!" post with a custom welcome message when a new site is created.
Generated: DETERMINISTIC_e1d144f5775bcb04
Batch ID: 20250612_154846
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
 * Description: Automatically replaces the default "Hello World!" post with a custom welcome message when a new site is created.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Function to replace the default post content with a custom welcome message.
 *
 * @param int $blog_id The ID of the newly created site.
 * @param string $user_id The ID of the user creating the site.
 */
function cwm_replace_hello_world( $blog_id, $user_id ) {
    // Switch to the new blog
    switch_to_blog( $blog_id );

    // Check if there is a default post
    $default_post = get_posts( array(
        'post_title'   => 'Hello World!',
        'post_type'    => 'post',
        'numberposts'  => 1,
    ) );

    // If the default post exists, replace it
    if ( ! empty( $default_post ) ) {
        // Prepare the new post data
        $new_post = array(
            'ID'           => $default_post[0]->ID,
            'post_title'   => 'Welcome to Your New Site!',
            'post_content' => 'Thank you for creating your site. Feel free to customize it as you like!',
            'post_status'  => 'publish',
            'post_author'  => $user_id,
        );

        // Update the post into the database
        wp_update_post( $new_post );
    }

    // Restore the current blog
    restore_current_blog();
}

// Hook into the 'wpmu_new_blog' action to trigger our function when a new site is created
add_action( 'wpmu_new_blog', 'cwm_replace_hello_world', 10, 2 );
```
