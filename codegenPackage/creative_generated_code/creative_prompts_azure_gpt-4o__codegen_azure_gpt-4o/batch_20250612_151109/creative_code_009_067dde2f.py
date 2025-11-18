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
 * Plugin Name: Custom Login Behavior for Help Desk
 * Description: Modifies WordPress login behavior for a help desk system, including custom error messages and redirects.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Customizes the login error message displayed to users.
 *
 * @param string $error Original error message.
 * @return string Modified error message.
 */
add_filter('login_errors', 'custom_login_error_message');
function custom_login_error_message($error) {
    // Provide a generic custom error message
    return 'Login failed. Please check your credentials and try again.';
}

/**
 * Redirects users after a successful login based on their roles.
 *
 * @param string $redirect_to URL to redirect to.
 * @param string $requested_redirect_to URL originally requested for redirect.
 * @param WP_User $user WP_User object of the logged-in user.
 * @return string Modified redirect URL.
 */
add_filter('login_redirect', 'custom_login_redirect', 10, 3);
function custom_login_redirect($redirect_to, $requested_redirect_to, $user) {
    // Check if the user is logged in
    if (isset($user->roles) && is_array($user->roles)) {
        // Redirect admins to the dashboard
        if (in_array('administrator', $user->roles)) {
            return admin_url();
        }

        // Redirect help desk agents to a custom help desk page
        if (in_array('helpdesk_agent', $user->roles)) {
            return site_url('/help-desk-dashboard');
        }

        // Redirect all other users to the home page
        return site_url('/');
    }

    // Default redirect fallback
    return $redirect_to;
}

/**
 * Adds custom error handling for failed login attempts.
 */
add_action('wp_login_failed', 'custom_login_failed');
function custom_login_failed($username) {
    // Log the failed login attempt (example of custom handling)
    error_log("Failed login attempt for username: {$username}");

    // Redirect to a custom error page after a failed login
    wp_redirect(site_url('/login-error'));
    exit;
}

/**
 * Prevents empty login attempts and redirects users to a custom error page.
 */
add_action('authenticate', 'prevent_empty_login', 1, 3);
function prevent_empty_login($user, $username, $password) {
    // Check if the username or password is empty
    if (empty($username) || empty($password)) {
        wp_redirect(site_url('/login-error'));
        exit;
    }

    return $user;
}
```
