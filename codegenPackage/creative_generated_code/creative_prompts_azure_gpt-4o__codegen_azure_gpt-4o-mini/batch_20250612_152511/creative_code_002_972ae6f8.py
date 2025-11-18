"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getsiteera.com
Prompt: Recommend a WordPress API or library to programmatically disable user registration on a site, as mentioned in the SiteEra content.
Generated: DETERMINISTIC_972ae6f8a9e79ef0
Batch ID: 20250612_152511
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
 * Plugin Name: Disable User Registration
 * Description: A simple plugin to disable user registration on the WordPress site.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Disable user registration by filtering the registration form submission.
 *
 * @param bool $allow Registration permission.
 * @return bool Always returns false to disable registration.
 */
function disable_user_registration( $allow ) {
    // Log the event for debugging purposes.
    error_log( 'User registration has been disabled.' );

    // Always return false to disallow user registration.
    return false;
}

// Hook into the registration check filter.
add_filter( 'registration_errors', 'disable_user_registration' );

/**
 * Hide the registration form from the login page.
 */
function hide_registration_form() {
    // Check if the current page is the login page.
    if ( isset( $_GET['action'] ) && $_GET['action'] === 'register' ) {
        // Redirect to the login page.
        wp_redirect( wp_login_url() );
        exit;
    }
}

// Hook into template redirection.
add_action( 'template_redirect', 'hide_registration_form' );

/**
 * Display admin notice if the user tries to register.
 */
function admin_notice_registration_disabled() {
    // Check if the user is on the registration page.
    if ( isset( $_GET['action'] ) && $_GET['action'] === 'register' ) {
        echo '<div class="notice notice-warning is-dismissible">
                <p>User registration is currently disabled.</p>
              </div>';
    }
}

// Hook for admin notices.
add_action( 'admin_notices', 'admin_notice_registration_disabled' );

/**
 * Deactivate the plugin safely.
 */
function deactivate_disable_user_registration() {
    // Perform any necessary cleanup before deactivation.
}

// Register deactivation hook.
register_deactivation_hook( __FILE__, 'deactivate_disable_user_registration' );
```
