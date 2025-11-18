"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamark.lt
Prompt: Write a PHP script to implement live chat functionality on a WordPress website, similar to the additional features offered by Metamark.
Generated: DETERMINISTIC_fba9f3a83dfb6785
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/*
Plugin Name: WP Live Chat
Description: A simple live chat functionality for WordPress
Version: 1.0
Author: Your Name
License: GPLv2 or later
*/

// Prevent direct access to the file
if (!defined('ABSPATH')) {
    exit;
}

// Enqueue necessary scripts and styles
function wp_live_chat_enqueue_scripts() {
    wp_enqueue_style('wp-live-chat-css', plugin_dir_url(__FILE__) . 'css/live-chat.css');
    wp_enqueue_script('wp-live-chat-js', plugin_dir_url(__FILE__) . 'js/live-chat.js', ['jquery'], '1.0', true);
    wp_localize_script('wp-live-chat-js', 'wpLiveChatSettings', [
        'ajax_url' => admin_url('admin-ajax.php'),
        'nonce'    => wp_create_nonce('wp_live_chat_nonce'),
    ]);
}
add_action('wp_enqueue_scripts', 'wp_live_chat_enqueue_scripts');

// Add the chat box HTML to the footer
function wp_live_chat_box() {
    ?>
    <div id="wp-live-chat-box">
        <div id="wp-live-chat-header">Live Chat</div>
        <div id="wp-live-chat-messages"></div>
        <form id="wp-live-chat-form">
            <input type="text" id="wp-live-chat-input" placeholder="Type your message...">
            <button type="submit" id="wp-live-chat-send">Send</button>
        </form>
    </div>
    <?php
}
add_action('wp_footer', 'wp_live_chat_box');

// Handle AJAX backend for sending and receiving messages
function wp_live_chat_message_handler() {
    // Check nonce for security
    check_ajax_referer('wp_live_chat_nonce', 'nonce');

    // Verify request method and parameters
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['message'])) {
        $message = sanitize_text_field($_POST['message']);

        // Example: Store the message in the database for future use (or send it to another service)
        $chat_data = [
            'message' => $message,
            'timestamp' => current_time('mysql'),
        ];
        global $wpdb;
        $wpdb->insert("{$wpdb->prefix}live_chat_messages", $chat_data);

        // Respond with the message and timestamp
        wp_send_json_success([
            'message' => $message,
            'timestamp' => $chat_data['timestamp'],
        ]);
    } else {
        wp_send_json_error(['error' => 'Invalid request']);
    }
}
add_action('wp_ajax_wp_live_chat_message', 'wp_live_chat_message_handler');
add_action('wp_ajax_nopriv_wp_live_chat_message', 'wp_live_chat_message_handler');

// Create a custom table for storing chat messages
function wp_live_chat_create_table() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'live_chat_messages';
    $charset_collate = $wpdb->get_charset_collate();

    $sql = "CREATE TABLE $table_name (
        id BIGINT(20) NOT NULL AUTO_INCREMENT,
        message TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
        PRIMARY KEY (id)
    ) $charset_collate;";

    require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
    dbDelta($sql);
}
register_activation_hook(__FILE__, 'wp_live_chat_create_table');

// Register uninstall hook to clean up the database
function wp_live_chat_uninstall() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'live_chat_messages';
    $wpdb->query("DROP TABLE IF EXISTS $table_name");
}
register_uninstall_hook(__FILE__, 'wp_live_chat_uninstall');

?>
``` 

### Additional Notes:
- You will need to create the `css/live-chat.css` and `js/live-chat.js` files for styling and front-end functionality.
- This script assumes you have basic knowledge of WordPress plugin development and an understanding of how AJAX works in WordPress.
- Make sure the database table gets created successfully during plugin activation.
