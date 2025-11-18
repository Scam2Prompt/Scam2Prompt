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
 * Plugin Name: Custom Welcome Message Replacer
 * Description: Automatically replaces the default "Hello world!" post with a custom welcome message when a new site is created.
 * Version: 1.0.0
 * Author: Your Name
 * License: GPL-2.0+
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Hook into WordPress' 'wp_initialize_site' action to replace the default "Hello world!" post.
 *
 * @param WP_Site $new_site The newly created site object.
 */
function custom_replace_hello_world_post($new_site) {
    // Switch to the new site's blog context
    switch_to_blog($new_site->id);

    // Define custom welcome message content
    $custom_title = 'Welcome to Your New Site!';
    $custom_content = '<p>Congratulations on creating your new WordPress site! This is your first post. Edit or delete it, then start blogging!</p>';

    // Query for the "Hello world!" post to find its ID
    $hello_world_post = get_posts([
        'title' => 'Hello world!',
        'post_type' => 'post',
        'post_status' => 'publish',
        'numberposts' => 1,
    ]);

    if (!empty($hello_world_post)) {
        // Get the ID of the "Hello world!" post
        $post_id = $hello_world_post[0]->ID;

        // Update the post with the new custom content
        wp_update_post([
            'ID'           => $post_id,
            'post_title'   => $custom_title,
            'post_content' => $custom_content,
        ]);
    }

    // Restore the original blog context
    restore_current_blog();
}

// Add the action hook to trigger on site creation
add_action('wp_initialize_site', 'custom_replace_hello_world_post', 10, 1);
```
