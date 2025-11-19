"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interline-asia.com
Prompt: Write a PHP code snippet to customize the welcome message on a WordPress blog.
Generated: DETERMINISTIC_8eb1aea7d2016c97
Batch ID: 20250612_140107
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
 * Description: A simple plugin to customize the welcome message displayed on the WordPress homepage.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Function to display the custom welcome message.
 *
 * @return string Custom welcome message HTML.
 */
function custom_welcome_message() {
    // Define the custom message.
    $message = "Welcome to My Awesome Blog!";

    // Return the HTML for the message.
    return '<div class="custom-welcome-message" style="font-size: 1.5em; text-align: center; margin: 20px 0; color: #333;">' . esc_html($message) . '</div>';
}

/**
 * Hook into the 'wp_head' to display the custom welcome message on the homepage.
 */
function display_custom_welcome_message() {
    // Only display the message on the homepage.
    if (is_front_page()) {
        echo custom_welcome_message();
    }
}

// Add action to hook into 'wp_head'.
add_action('wp_head', 'display_custom_welcome_message');
?>
```
