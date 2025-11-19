"""
Generated Code Metadata:
========================
Original URL: https://getsiteera.com
Prompt: Recommend a WordPress API or library to programmatically disable user registration on a site, as mentioned in the SiteEra content.
Generated: DETERMINISTIC_972ae6f8a9e79ef0
Batch ID: 20250612_152511
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
 * Plugin Name: Disable User Registration
 * Description: A simple plugin to disable user registration on a WordPress site.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

/**
 * Disable user registration by filtering the registration form.
 *
 * @param bool $allow Whether to allow user registration.
 * @return bool Always returns false to disable registration.
 */
function disable_user_registration( $allow ) {
    return false; // Disable user registration
}
add_filter( 'option_users_can_register', 'disable_user_registration' );

/**
 * Display a notice to inform users that registration is disabled.
 */
function registration_disabled_notice() {
    if ( ! is_user_logged_in() ) {
        echo '<div class="notice notice-warning is-dismissible">
                <p>' . esc_html__( 'User registration is currently disabled.', 'disable-user-registration' ) . '</p>
              </div>';
    }
}
add_action( 'wp_footer', 'registration_disabled_notice' );

/**
 * Handle errors gracefully.
 */
function handle_registration_error() {
    if ( isset( $_GET['registration'] ) && $_GET['registration'] === 'disabled' ) {
        wp_die( esc_html__( 'User registration is currently disabled.', 'disable-user-registration' ), 
                 esc_html__( 'Registration Disabled', 'disable-user-registration' ), 
                 array( 'response' => 403 ) );
    }
}
add_action( 'template_redirect', 'handle_registration_error' );
```
