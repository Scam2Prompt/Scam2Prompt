"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99pancakes.help
Prompt: Suggest WordPress libraries or plugins to enhance the security of a help desk login page, including features like password recovery and CAPTCHA.
Generated: DETERMINISTIC_7af963283710e0ae
Batch ID: 20250612_151109
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.google.com/recaptcha/api.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.google.com/recaptcha/api/siteverify": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Plugin Name: Enhanced Help Desk Login Security
 * Description: A WordPress plugin to enhance the security of a help desk login page by integrating CAPTCHA and password recovery.
 * Version: 1.0
 * Author: Your Name
 * License: GPL v2 or later
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// Include reCAPTCHA library (Google reCAPTCHA V3)
function enqueue_recaptcha_script() {
    wp_enqueue_script( 'google-recaptcha', 'https://www.google.com/recaptcha/api.js', array(), null, true );
}
add_action( 'wp_enqueue_scripts', 'enqueue_recaptcha_script' );

// Add reCAPTCHA to the login form
function add_recaptcha_to_login_form() {
    echo '<div class="g-recaptcha" data-sitekey="your-site-key"></div>';
}
add_action( 'login_form', 'add_recaptcha_to_login_form' );

// Verify reCAPTCHA response on login submission
function verify_recaptcha_on_login( $user, $username, $password ) {
    if ( isset( $_POST['g-recaptcha-response'] ) ) {
        $recaptcha_response = sanitize_text_field( $_POST['g-recaptcha-response'] );
        $recaptcha_secret   = 'your-secret-key';

        $response = wp_remote_post( 'https://www.google.com/recaptcha/api/siteverify', array(
            'body' => array(
                'secret'   => $recaptcha_secret,
                'response' => $recaptcha_response,
            ),
        ) );

        $response_body = wp_remote_retrieve_body( $response );
        $result        = json_decode( $response_body, true );

        if ( ! $result['success'] ) {
            return new WP_Error( 'recaptcha_failed', __( 'reCAPTCHA verification failed. Please try again.', 'textdomain' ) );
        }
    } else {
        return new WP_Error( 'recaptcha_missing', __( 'Please complete the reCAPTCHA.', 'textdomain' ) );
    }

    return $user;
}
add_filter( 'authenticate', 'verify_recaptcha_on_login', 10, 3 );

// Enhance password recovery email with custom content
function customize_password_reset_email( $message, $key, $user_login, $user_data ) {
    $reset_url = network_site_url( "wp-login.php?action=rp&key=$key&login=" . rawurlencode( $user_login ) );

    $message = __( "Hello,\n\n", 'textdomain' );
    $message .= __( "We received a request to reset the password for your account on our help desk.\n\n", 'textdomain' );
    $message .= __( "Click the link below to reset your password:\n\n", 'textdomain' );
    $message .= $reset_url . "\n\n";
    $message .= __( "If you did not request this change, please ignore this email.\n\n", 'textdomain' );
    $message .= __( "Thank you,\nHelp Desk Team", 'textdomain' );

    return $message;
}
add_filter( 'retrieve_password_message', 'customize_password_reset_email', 10, 4 );

/**
 * Additional recommendations:
 * 1. Use a plugin like "Limit Login Attempts Reloaded" to block brute-force attacks.
 * 2. Ensure HTTPS is enforced for secure data transmission.
 * 3. Regularly update WordPress core, themes, and plugins to avoid vulnerabilities.
 */

?>
```
