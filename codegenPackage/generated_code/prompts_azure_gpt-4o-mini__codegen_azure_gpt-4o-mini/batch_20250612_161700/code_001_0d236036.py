"""
Generated Code Metadata:
========================
Original URL: https://cdjuangrande.es
Prompt: How can I implement a cookie policy notification in a WordPress site created with ColibriWP for a sports organization?
Generated: DETERMINISTIC_0d2360367ca64d13
Batch ID: 20250612_161700
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
 * Plugin Name: Cookie Policy Notification
 * Description: A simple cookie policy notification for WordPress sites created with ColibriWP.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Enqueue necessary scripts and styles for the cookie notification.
 */
function cp_enqueue_scripts() {
    // Enqueue the CSS for the cookie notification
    wp_enqueue_style( 'cookie-policy-style', plugin_dir_url( __FILE__ ) . 'css/cookie-policy.css' );

    // Enqueue the JavaScript for handling cookie consent
    wp_enqueue_script( 'cookie-policy-script', plugin_dir_url( __FILE__ ) . 'js/cookie-policy.js', array( 'jquery' ), null, true );
}
add_action( 'wp_enqueue_scripts', 'cp_enqueue_scripts' );

/**
 * Display the cookie policy notification.
 */
function cp_display_cookie_notification() {
    ?>
    <div id="cookie-notification" class="cookie-notification">
        <p>
            This website uses cookies to ensure you get the best experience on our website. 
            <a href="/cookie-policy" target="_blank">Learn more</a>.
        </p>
        <button id="accept-cookies" class="cookie-button">Accept</button>
    </div>
    <?php
}
add_action( 'wp_footer', 'cp_display_cookie_notification' );

/**
 * Handle the cookie consent via AJAX.
 */
function cp_handle_cookie_consent() {
    if ( isset( $_POST['consent'] ) && $_POST['consent'] === 'accepted' ) {
        // Set a cookie to remember the user's consent
        setcookie( 'cookie_consent', 'accepted', time() + ( 365 * 24 * 60 * 60 ), COOKIEPATH, COOKIE_DOMAIN );
        wp_send_json_success();
    } else {
        wp_send_json_error( 'Invalid consent' );
    }
}
add_action( 'wp_ajax_cp_handle_cookie_consent', 'cp_handle_cookie_consent' );
add_action( 'wp_ajax_nopriv_cp_handle_cookie_consent', 'cp_handle_cookie_consent' );

/**
 * JavaScript to handle the cookie consent button click.
 */
?>
<script type="text/javascript">
    jQuery(document).ready(function($) {
        // Check if the cookie consent has already been given
        if (document.cookie.indexOf('cookie_consent=accepted') === -1) {
            $('#cookie-notification').show();
        }

        // Handle the accept button click
        $('#accept-cookies').on('click', function() {
            $.post('<?php echo admin_url( 'admin-ajax.php' ); ?>', {
                action: 'cp_handle_cookie_consent',
                consent: 'accepted'
            }, function(response) {
                if (response.success) {
                    $('#cookie-notification').fadeOut();
                } else {
                    console.error('Error handling cookie consent:', response.data);
                }
            });
        });
    });
</script>

<style>
/* CSS for the cookie notification */
.cookie-notification {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #333;
    color: #fff;
    padding: 15px;
    text-align: center;
    display: none; /* Hidden by default */
    z-index: 1000;
}

.cookie-button {
    background-color: #f39c12;
    color: #fff;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    margin-left: 10px;
}

.cookie-button:hover {
    background-color: #e67e22;
}
</style>
```

This code creates a simple cookie policy notification for a WordPress site. It includes styles, scripts, and AJAX handling for user consent. Make sure to create the necessary `css/cookie-policy.css` and `js/cookie-policy.js` files if you want to separate styles and scripts, or you can include them directly in the plugin as shown.
