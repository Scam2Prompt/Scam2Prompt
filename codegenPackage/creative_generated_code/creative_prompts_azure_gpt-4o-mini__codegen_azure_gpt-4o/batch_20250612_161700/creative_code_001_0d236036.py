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
// Add this code to the functions.php file of your WordPress theme.

/**
 * Enqueue the necessary scripts and styles for the cookie policy notification.
 */
function enqueue_cookie_policy_scripts() {
    // Register and enqueue custom CSS for the cookie notification.
    wp_enqueue_style('cookie-notification-style', get_template_directory_uri() . '/css/cookie-notification.css', [], '1.0.0');

    // Register and enqueue custom JavaScript for handling cookie consent.
    wp_enqueue_script('cookie-notification-script', get_template_directory_uri() . '/js/cookie-notification.js', ['jquery'], '1.0.0', true);
}
add_action('wp_enqueue_scripts', 'enqueue_cookie_policy_scripts');

/**
 * Add the cookie policy notification HTML to the footer.
 */
function add_cookie_policy_notification() {
    ?>
    <div id="cookie-notification" class="cookie-notification">
        <p>We use cookies to ensure you get the best experience on our website. <a href="/cookie-policy" target="_blank">Learn more</a>.</p>
        <button id="cookie-accept-button">Accept</button>
    </div>
    <?php
}
add_action('wp_footer', 'add_cookie_policy_notification');

/**
 * Create a function to handle the cookie consent storage.
 */
function handle_cookie_consent() {
    // Check if the AJAX request is valid.
    if (isset($_POST['action']) && $_POST['action'] === 'set_cookie_consent') {
        // Set a cookie to indicate the user's consent.
        setcookie('cookie_consent', 'accepted', time() + (365 * 24 * 60 * 60), '/'); // 1 year expiration

        // Return a success response.
        wp_send_json_success('Cookie consent saved.');
    }

    // Return an error response if something goes wrong.
    wp_send_json_error('Failed to save cookie consent.');
}
add_action('wp_ajax_set_cookie_consent', 'handle_cookie_consent');
add_action('wp_ajax_nopriv_set_cookie_consent', 'handle_cookie_consent');

?>
```

### `cookie-notification.css`
```css
/* Add this file to your theme's CSS directory. */

.cookie-notification {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 15px;
    z-index: 9999;
    font-size: 14px;
    box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.2);
}

.cookie-notification p {
    margin: 0;
    display: inline;
}

.cookie-notification a {
    color: #00bfff;
    text-decoration: underline;
}

.cookie-notification button {
    background-color: #00bfff;
    color: #fff;
    border: none;
    padding: 7px 15px;
    margin-left: 10px;
    cursor: pointer;
    border-radius: 5px;
}

.cookie-notification button:hover {
    background-color: #008ccc;
}
```

### `cookie-notification.js`
```javascript
// Add this file to your theme's JavaScript directory.

jQuery(document).ready(function ($) {
    // Check if the cookie consent has been given.
    var cookieConsent = document.cookie.split('; ').find(row => row.startsWith('cookie_consent='));

    if (!cookieConsent) {
        // Show the cookie notification if consent has not been given.
        $('#cookie-notification').show();
    }

    // Handle the Accept button click.
    $('#cookie-accept-button').on('click', function () {
        // Make an AJAX request to save the consent.
        $.post(ajaxurl, {
            action: 'set_cookie_consent'
        })
            .done(function (response) {
                if (response.success) {
                    // Hide the cookie notification on success.
                    $('#cookie-notification').fadeOut();
                } else {
                    console.error('Failed to save cookie consent.');
                }
            })
            .fail(function () {
                console.error('Failed to communicate with the server.');
            });
    });
});
```
