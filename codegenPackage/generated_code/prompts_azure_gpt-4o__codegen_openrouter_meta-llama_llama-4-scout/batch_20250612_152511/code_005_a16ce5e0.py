"""
Generated Code Metadata:
========================
Original URL: https://getsiteera.com
Prompt: Provide a step-by-step guide to programmatically disable user registration in WordPress using functions.php, as seen in SiteEra's implementation.
Generated: DETERMINISTIC_a16ce5e087397a92
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
/**
 * Disable user registration in WordPress programmatically.
 *
 * This code snippet disables user registration in WordPress by modifying the 
 * 'registration' setting in the 'wp_settings' table and removing the 
 * registration link from the WordPress login page.
 *
 * @package WordPress
 * @subpackage SiteEra
 */

// Add action hook to modify WordPress settings
add_action( 'admin_init', 'disable_user_registration' );

/**
 * Disable user registration.
 */
function disable_user_registration() {
    // Get current WordPress settings
    $registration_setting = get_option( 'users_can_register' );

    // Check if user registration is currently enabled
    if ( $registration_setting ) {
        // Disable user registration
        update_option( 'users_can_register', 0 );
    }
}

// Add filter hook to remove registration link from login page
add_filter( 'wp_footer', 'remove_registration_link' );

/**
 * Remove registration link from login page.
 */
function remove_registration_link() {
    // Check if current page is the login page
    if ( is_login_page() ) {
        // Remove registration link
        remove_action( 'register_form', 'wp_register' );
    }
}

/**
 * Check if current page is the login page.
 *
 * @return bool True if current page is the login page, false otherwise.
 */
function is_login_page() {
    $current_page = get_current_screen();
    return $current_page->base == 'login';
}

// Prevent direct access to this file
defined( 'ABSPATH' ) or exit;

// Prevent registration via wp-signup
add_action( 'signup_init', 'disable_registration_via_signup' );

/**
 * Disable registration via wp-signup.
 */
function disable_registration_via_signup() {
    wp_die( __( 'User registration is currently disabled.' ), 403 );
}

// Prevent registration via XML-RPC
add_filter( 'xmlrpc_methods', 'disable_registration_via_xmlrpc' );

/**
 * Disable registration via XML-RPC.
 *
 * @param array $methods XML-RPC methods.
 * @return array Modified XML-RPC methods.
 */
function disable_registration_via_xmlrpc( $methods ) {
    unset( $methods['wp_newUser'] );
    return $methods;
}
```
