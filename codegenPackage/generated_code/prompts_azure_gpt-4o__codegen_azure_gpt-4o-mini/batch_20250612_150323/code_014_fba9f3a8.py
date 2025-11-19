"""
Generated Code Metadata:
========================
Original URL: https://metamark.lt
Prompt: Write a PHP script to implement live chat functionality on a WordPress website, similar to the additional features offered by Metamark.
Generated: DETERMINISTIC_fba9f3a83dfb6785
Batch ID: 20250612_150323
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
 * Plugin Name: Live Chat Functionality
 * Description: A simple live chat implementation for WordPress.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// Enqueue necessary scripts and styles
function lc_enqueue_scripts() {
    wp_enqueue_script( 'lc-chat-script', plugin_dir_url( __FILE__ ) . 'js/live-chat.js', array('jquery'), '1.0', true );
    wp_enqueue_style( 'lc-chat-style', plugin_dir_url( __FILE__ ) . 'css/live-chat.css' );
}
add_action( 'wp_enqueue_scripts', 'lc_enqueue_scripts' );

// Create a shortcode to display the chat widget
function lc_chat_widget() {
    ob_start(); ?>
    <div id="live-chat">
        <div id="chat-box">
            <div id="messages"></div>
            <input type="text" id="chat-input" placeholder="Type your message..." />
            <button id="send-message">Send</button>
        </div>
    </div>
    <?php
    return ob_get_clean();
}
add_shortcode( 'live_chat', 'lc_chat_widget' );

// Handle AJAX request to send a message
function lc_send_message() {
    // Check if the user is logged in
    if ( ! is_user_logged_in() ) {
        wp_send_json_error( 'User not logged in' );
    }

    // Validate and sanitize input
    $message = isset( $_POST['message'] ) ? sanitize_text_field( $_POST['message'] ) : '';

    if ( empty( $message ) ) {
        wp_send_json_error( 'Message cannot be empty' );
    }

    // Here you would typically save the message to the database or send it to a chat server
    // For demonstration, we will just return the message
    wp_send_json_success( array( 'message' => $message, 'user' => wp_get_current_user()->display_name ) );
}
add_action( 'wp_ajax_lc_send_message', 'lc_send_message' );
add_action( 'wp_ajax_nopriv_lc_send_message', 'lc_send_message' );

// Create a simple JavaScript file for handling chat interactions
// Save this as js/live-chat.js
?>
<script>
jQuery(document).ready(function($) {
    $('#send-message').on('click', function() {
        var message = $('#chat-input').val();
        if (message.trim() === '') {
            alert('Please enter a message.');
            return;
        }

        $.post(ajaxurl, {
            action: 'lc_send_message',
            message: message
        }, function(response) {
            if (response.success) {
                $('#messages').append('<div><strong>' + response.data.user + ':</strong> ' + response.data.message + '</div>');
                $('#chat-input').val(''); // Clear input
            } else {
                alert(response.data);
            }
        });
    });
});
</script>

<?php
// Create a simple CSS file for styling the chat widget
// Save this as css/live-chat.css
?>
<style>
#live-chat {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 300px;
    border: 1px solid #ccc;
    background: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#chat-box {
    padding: 10px;
}

#messages {
    max-height: 200px;
    overflow-y: auto;
    margin-bottom: 10px;
}

#chat-input {
    width: calc(100% - 60px);
}

#send-message {
    width: 50px;
}
</style>
```

This code provides a basic implementation of live chat functionality for a WordPress website. It includes a shortcode to display the chat widget, AJAX handling for sending messages, and basic styling. Make sure to create the necessary JavaScript and CSS files in the specified directories.
