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
/**
 * Plugin Name: Live Chat Functionality
 * Description: A simple live chat functionality for WordPress websites.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

// Enqueue necessary scripts and styles
function lc_enqueue_scripts() {
    // Enqueue jQuery if not already included
    if (!wp_script_is('jquery', 'enqueued')) {
        wp_enqueue_script('jquery');
    }
    
    // Enqueue the chat script and style
    wp_enqueue_script('lc-chat-script', plugin_dir_url(__FILE__) . 'js/live-chat.js', array('jquery'), '1.0', true);
    wp_enqueue_style('lc-chat-style', plugin_dir_url(__FILE__) . 'css/live-chat.css', array(), '1.0');
}
add_action('wp_enqueue_scripts', 'lc_enqueue_scripts');

// Create a shortcode to display the chat widget
function lc_chat_widget() {
    ob_start(); ?>
    <div id="live-chat">
        <div id="chat-box">
            <div id="messages"></div>
        </div>
        <input type="text" id="chat-input" placeholder="Type your message..." />
        <button id="send-message">Send</button>
    </div>
    <?php return ob_get_clean();
}
add_shortcode('live_chat', 'lc_chat_widget');

// AJAX handler to send messages
function lc_send_message() {
    // Check for required POST data
    if (!isset($_POST['message']) || empty(trim($_POST['message']))) {
        wp_send_json_error('Message cannot be empty.');
    }

    // Sanitize message to prevent XSS
    $message = sanitize_text_field(trim($_POST['message']));
    
    // You can save the message to the database or handle it as needed
    // For demonstration, we'll just return the message
    wp_send_json_success(array('message' => $message, 'timestamp' => current_time('mysql')));
}
add_action('wp_ajax_lc_send_message', 'lc_send_message');
add_action('wp_ajax_nopriv_lc_send_message', 'lc_send_message');
```

**JavaScript (live-chat.js)**
```javascript
jQuery(document).ready(function($) {
    $('#send-message').on('click', function() {
        var messageInput = $('#chat-input');
        var message = messageInput.val();

        if (message.trim() === '') {
            alert('Message cannot be empty.');
            return;
        }

        // Send AJAX request to the server
        $.post(ajaxurl, {
            action: 'lc_send_message',
            message: message
        }, function(response) {
            if (response.success) {
                // Append the message to the chat box
                $('#messages').append('<div>' + response.data.timestamp + ': ' + response.data.message + '</div>');
                messageInput.val(''); // Clear input
            } else {
                alert(response.data);
            }
        }).fail(function() {
            alert('An error occurred while sending your message. Please try again.');
        });
    });
});
```

**CSS (live-chat.css)**
```css
#live-chat {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 300px;
    background: #fff;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

#chat-box {
    height: 250px;
    overflow-y: auto;
    padding: 10px;
    border-bottom: 1px solid #ccc;
}

#messages {
    padding: 5px;
}

#chat-input {
    width: calc(100% - 70px);
}

#send-message {
    width: 60px;
}
``` 

This code snippet includes a complete implementation of a simple live chat feature for a WordPress website using PHP, JavaScript, and CSS. Ensure that you create the corresponding JS and CSS files in the appropriate directories within your WordPress plugin or theme.
