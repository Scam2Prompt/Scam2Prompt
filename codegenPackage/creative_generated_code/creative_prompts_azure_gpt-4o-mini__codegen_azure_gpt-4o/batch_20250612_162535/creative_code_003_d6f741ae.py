"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initiald.co.uk
Prompt: How do I edit the default WordPress post to create a custom welcome message, as seen on initiald.co.uk?
Generated: DETERMINISTIC_d6f741aec9aa829a
Batch ID: 20250612_162535
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
 * Description: Edits the default WordPress post to include a custom welcome message.
 * Version: 1.0
 * Author: Your Name
 */

// Hook into WordPress initialization
add_action('init', 'edit_default_post_welcome_message');

/**
 * Function to edit the default WordPress post with a custom welcome message.
 */
function edit_default_post_welcome_message() {
    // Check if this is a fresh install where no posts exist yet
    $default_post_id = get_option('default_post_id'); // Built-in WordPress option storing the ID of the default post (Hello World)
    
    // If the default post exists, modify it
    if ($default_post_id) {
        $default_post = get_post($default_post_id);
        
        // Check if the post content has not been updated already
        if ($default_post && $default_post->post_content === 'Welcome to WordPress. This is your first post. Edit or delete it, then start writing!') {
            // Update the content of the default post
            $custom_message = '<h1>Welcome to My Custom Website!</h1>
                               <p>This is your first post, and we’ve customized it just for you.</p>
                               <p>Feel free to edit, delete, or explore the site to make it your own.</p>';

            // Prepare post data for update
            $updated_post_data = [
                'ID'           => $default_post_id,
                'post_content' => $custom_message,
            ];

            // Update the post in the database
            wp_update_post($updated_post_data);
        }
    }
}
?>
```
