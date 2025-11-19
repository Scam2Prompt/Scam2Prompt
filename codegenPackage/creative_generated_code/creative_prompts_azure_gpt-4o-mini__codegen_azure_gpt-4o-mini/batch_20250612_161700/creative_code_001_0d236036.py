"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdjuangrande.es
Prompt: How can I implement a cookie policy notification in a WordPress site created with ColibriWP for a sports organization?
Generated: DETERMINISTIC_0d2360367ca64d13
Batch ID: 20250612_161700
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
Plugin Name: Cookie Policy Notification
Description: A simple cookie notification for WordPress sites created with ColibriWP.
Version: 1.0
Author: Your Name
*/

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// Enqueue styles and scripts for the cookie notification
function cp_enqueue_scripts() {
    // Register styles for the cookie notification
    wp_enqueue_style( 'cookie-notification-style', plugin_dir_url( __FILE__ ) . 'css/cookie-notification.css' );

    // Register script for the cookie notification
    wp_enqueue_script( 'cookie-notification-script', plugin_dir_url( __FILE__ ) . 'js/cookie-notification.js', array('jquery'), null, true );
}
add_action( 'wp_enqueue_scripts', 'cp_enqueue_scripts' );

// Display the cookie notification
function cp_display_cookie_notification() {
    ?>
    <div id="cookie-notification" class="cookie-notification">
        <p>
            We use cookies to enhance your experience. By continuing to visit this site, you agree to our use of cookies.
            <a href="/cookie-policy" target="_blank">Learn more</a>.
        </p>
        <button id="accept-cookies" class="cookie-accept-button">Accept</button>
    </div>
    <?php
}
add_action( 'wp_footer', 'cp_display_cookie_notification' );

// Handle cookie acceptance via AJAX
function cp_accept_cookies() {
    // Set a cookie to indicate acceptance
    setcookie( 'cookies_accepted', 'true', time() + (86400 * 30), COOKIEPATH, COOKIE_DOMAIN ); // 30 days
    wp_send_json_success();
}
add_action( 'wp_ajax_cp_accept_cookies', 'cp_accept_cookies' );
add_action( 'wp_ajax_nopriv_cp_accept_cookies', 'cp_accept_cookies' );

// Create CSS file for styling the cookie notification
function cp_create_css_file() {
    $css = "
    .cookie-notification {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: #333;
        color: #fff;
        padding: 15px;
        text-align: center;
        display: none; /* Hidden by default */
        z-index: 1000;
    }
    .cookie-notification p {
        margin: 0;
        padding: 0;
    }
    .cookie-accept-button {
        background: #ffcc00;
        border: none;
        padding: 10px 20px;
        cursor: pointer;
    }
    ";
    file_put_contents(plugin_dir_path(__FILE__) . 'css/cookie-notification.css', $css);
}
register_activation_hook( __FILE__, 'cp_create_css_file' );

// Create JavaScript file for cookie notification functionality
function cp_create_js_file() {
    $js = "
    jQuery(document).ready(function($) {
        // Check if the cookie is already accepted
        if (document.cookie.indexOf('cookies_accepted=true') === -1) {
            $('#cookie-notification').fadeIn(); // Show the notification
        }
        // Handle the accept button click
        $('#accept-cookies').click(function() {
            $.post('" . admin_url('admin-ajax.php') . "', { action: 'cp_accept_cookies' }, function(response) {
                if (response.success) {
                    $('#cookie-notification').fadeOut(); // Hide notification on acceptance
                }
            });
        });
    });
    ";
    file_put_contents(plugin_dir_path(__FILE__) . 'js/cookie-notification.js', $js);
}
register_activation_hook( __FILE__, 'cp_create_js_file' );
?>
```

### Notes:
- Make sure to create the `css` and `js` directories in the same folder as this plugin file to store the respective CSS and JS files.
- You can customize the cookie policy URL in the notification as per your requirements.
