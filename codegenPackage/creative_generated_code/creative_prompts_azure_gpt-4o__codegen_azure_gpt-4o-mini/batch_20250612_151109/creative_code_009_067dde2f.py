"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99pancakes.help
Prompt: Recommend WordPress hooks to modify the default login behavior for a help desk system, such as adding custom error messages or redirect URLs.
Generated: DETERMINISTIC_067dde2f4913b26d
Batch ID: 20250612_151109
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
 * Plugin Name: Custom Login Modifications
 * Description: Modifies the default WordPress login behavior for a help desk system.
 * Version: 1.0
 * Author: Your Name
 */

/**
 * Modify the login error message.
 *
 * @param string $error The default error message.
 * @return string Modified error message.
 */
function custom_login_error_message( $error ) {
    // Customize the error message here.
    return 'Invalid credentials. Please check your username and password, or contact support.';
}
add_filter( 'login_errors', 'custom_login_error_message' );

/**
 * Redirect users after successful login.
 *
 * @param string $redirect_to The URL to redirect to.
 * @param string $requested_redirect_to The requested redirect URL.
 * @param WP_User $user The user object.
 * @return string Redirect URL.
 */
function custom_login_redirect( $redirect_to, $requested_redirect_to, $user ) {
    // Check if the user is logging in as a non-admin.
    if ( isset( $user->roles ) && is_array( $user->roles ) ) {
        if ( in_array( 'administrator', $user->roles ) ) {
            // Redirect administrators to the dashboard.
            return admin_url();
        } else {
            // Redirect other users to the help desk dashboard.
            return home_url( '/help-desk-dashboard' );
        }
    }
    return $redirect_to;
}
add_filter( 'login_redirect', 'custom_login_redirect', 10, 3 );

/**
 * Enqueue custom scripts or styles for the login page.
 */
function custom_login_enqueue() {
    // Enqueue a custom stylesheet for the login page.
    wp_enqueue_style( 'custom-login-style', plugin_dir_url( __FILE__ ) . 'css/custom-login.css' );
}
add_action( 'login_enqueue_scripts', 'custom_login_enqueue' );

/**
 * Handle custom login error logging.
 *
 * @param string $username The username provided during login.
 * @param string $password The password provided during login.
 */
function custom_login_error_logging( $username, $password ) {
    // Log the login attempt.
    if ( ! username_exists( $username ) ) {
        error_log( 'Login attempt with invalid username: ' . $username );
    }
}
add_action( 'wp_login_failed', 'custom_login_error_logging' );

/**
 * Display a custom message after the user logs out.
 */
function custom_logout_message() {
    // Display a custom logout message.
    echo '<div class="custom-logout-message">You have successfully logged out. Thank you!</div>';
}
add_action( 'wp_logout', 'custom_logout_message' );

// Make sure this plugin is active only for the login page.
function custom_login_page_only() {
    if ( ! is_admin() && ! is_user_logged_in() ) {
        // Run the hooks and functions only on the login page.
        add_action( 'login_enqueue_scripts', 'custom_login_enqueue' );
        add_filter( 'login_errors', 'custom_login_error_message' );
    }
}
add_action( 'init', 'custom_login_page_only' );
?>
```
