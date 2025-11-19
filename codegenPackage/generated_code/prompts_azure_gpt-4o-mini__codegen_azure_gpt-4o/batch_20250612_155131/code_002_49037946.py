"""
Generated Code Metadata:
========================
Original URL: https://sayacosmetics.com
Prompt: Write a function in PHP that modifies the default WordPress post to include a custom message for new users, inspired by the content on Saya Cosmetics.
Generated: DETERMINISTIC_490379463fa6887b
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
 * Plugin Name: Custom Welcome Message for New Users
 * Description: Modifies the default WordPress post to include a custom message inspired by Saya Cosmetics for new users.
 * Version: 1.0
 * Author: Your Name
 */

// Hook into the 'wp_insert_post_data' filter to modify the default post content.
add_filter('wp_insert_post_data', 'add_custom_message_to_default_post', 10, 2);

/**
 * Adds a custom message to the default WordPress post for new users.
 *
 * @param array $data An array of post data.
 * @param array $postarr An array of post attributes.
 * @return array Modified post data.
 */
function add_custom_message_to_default_post($data, $postarr) {
    // Check if this is a new post and if the post type is 'post'.
    if (isset($postarr['post_type']) && $postarr['post_type'] === 'post' && $postarr['post_status'] === 'auto-draft') {
        // Define the custom message inspired by Saya Cosmetics.
        $custom_message = "\n\nWelcome to our blog! At Saya Cosmetics, we believe in natural beauty and self-care. Explore our tips, tricks, and insights to enhance your journey.";
        
        // Append the custom message to the default post content.
        $data['post_content'] .= $custom_message;
    }

    return $data;
}

/**
 * Activation hook to ensure the plugin is properly initialized.
 */
function custom_message_plugin_activation() {
    // Check if WordPress version is compatible.
    if (version_compare(get_bloginfo('version'), '5.0', '<')) {
        wp_die('This plugin requires WordPress version 5.0 or higher.');
    }
}
register_activation_hook(__FILE__, 'custom_message_plugin_activation');

/**
 * Deactivation hook for cleanup tasks.
 */
function custom_message_plugin_deactivation() {
    // Perform any necessary cleanup tasks here.
}
register_deactivation_hook(__FILE__, 'custom_message_plugin_deactivation');
```
